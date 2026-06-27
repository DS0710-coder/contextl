"""
Repository Intelligence Engine
Step 2: Import Parser

Reads each scanned file and extracts import relationships using tree-sitter
for accurate, AST-level parsing across Python, TypeScript, JavaScript, Java,
Rust, Go, and C++.

Falls back to the previous regex engine if tree-sitter is not installed
(zero regression for existing users).

Public API (unchanged):
  parse_imports(scan_result: ScanResult) -> ParseResult
  extract_skeleton(file_path: str) -> dict   [NEW — Skeleton Mode]
"""

import re
import sys
from pathlib import Path, PurePosixPath
from dataclasses import dataclass, field

PYTHON_STDLIB_AND_COMMON_PACKAGES = {
    "os", "sys", "re", "math", "json", "datetime", "typing", "collections",
    "itertools", "functools", "pathlib", "logging", "argparse", "subprocess",
    "unittest", "pytest", "numpy", "pandas", "requests", "urllib", "asyncio",
    "time", "random", "hashlib", "base64", "csv", "xml", "html", "http",
    "concurrent", "multiprocessing", "threading", "sqlite3", "flask", "django",
    "fastapi", "sqlalchemy", "pydantic", "dataclasses", "uuid", "socket",
    "struct", "tempfile", "shutil", "glob", "copy", "warnings", "traceback",
    "contextlib", "io", "sysconfig", "importlib", "pkgutil", "runpy",
    "celery", "redis", "psycopg2", "boto3", "jinja2", "pytest_mock",
}

from scanner import ScannedFile, ScanResult


# ---------------------------------------------------------------------------
# tree-sitter availability check — graceful fallback to regex if not installed
# ---------------------------------------------------------------------------
try:
    from tree_sitter import Language, Parser as TSParser, Node
    import tree_sitter_python     as _tspy
    import tree_sitter_javascript as _tsjs
    import tree_sitter_typescript as _tsts
    import tree_sitter_java       as _tsjava
    import tree_sitter_rust       as _tsrs
    import tree_sitter_go         as _tsgo
    import tree_sitter_cpp        as _tscpp

    _TS_AVAILABLE = True
except ImportError:
    _TS_AVAILABLE = False


# ---------------------------------------------------------------------------
# Module-level caches (Parser + Language objects are expensive to create)
# ---------------------------------------------------------------------------
_PARSERS:   dict[str, "TSParser"]  = {}   # ext -> Parser
_LANGUAGES: dict[str, "Language"]  = {}   # ext -> Language


def _get_language(ext: str):
    """Return the tree-sitter Language for a file extension, or None."""
    if not _TS_AVAILABLE:
        return None
    if ext in _LANGUAGES:
        return _LANGUAGES[ext]

    lang = None
    if ext == ".py":
        lang = Language(_tspy.language())
    elif ext in (".js", ".mjs", ".cjs", ".jsx"):
        lang = Language(_tsjs.language())
    elif ext == ".tsx":
        lang = Language(_tsts.language_tsx())
    elif ext in (".ts",):
        lang = Language(_tsts.language_typescript())
    elif ext == ".java":
        lang = Language(_tsjava.language())
    elif ext == ".rs":
        lang = Language(_tsrs.language())
    elif ext == ".go":
        lang = Language(_tsgo.language())
    elif ext in (".cpp", ".cc", ".cxx", ".h", ".hpp", ".c"):
        lang = Language(_tscpp.language())

    if lang is not None:
        _LANGUAGES[ext] = lang
    return lang


def _get_parser(ext: str):
    """Return a cached Parser for the given extension, or None."""
    if not _TS_AVAILABLE:
        return None, None
    if ext in _PARSERS:
        return _PARSERS[ext], _LANGUAGES[ext]

    lang = _get_language(ext)
    if lang is None:
        return None, None

    parser = TSParser(lang)
    _PARSERS[ext] = parser
    return parser, lang


# ---------------------------------------------------------------------------
# tree-sitter import extraction — per-language node walkers
# ---------------------------------------------------------------------------

def _ts_imports_python(root: "Node") -> list[str]:
    """Extract import module names from a Python AST root."""
    results: list[str] = []

    def visit(node: "Node"):
        if node.type == "import_statement":
            # import os, sys  →  dotted_name children
            for child in node.children:
                if child.type == "dotted_name":
                    results.append(child.text.decode("utf-8", errors="replace"))
                elif child.type == "aliased_import":
                    # import os as operating_system → first dotted_name
                    for sub in child.children:
                        if sub.type == "dotted_name":
                            results.append(sub.text.decode("utf-8", errors="replace"))
                            break

        elif node.type == "import_from_statement":
            # from pathlib import Path
            # from . import utils
            # from ..models import User
            rel_import = None
            for child in node.children:
                if child.type == "relative_import":
                    rel_import = child.text.decode("utf-8", errors="replace")
                    break

            if rel_import and rel_import.replace(".", "") == "":
                # Bare relative import like `.` or `..`
                seen_import = False
                for child in node.children:
                    if child.type == "import":
                        seen_import = True
                    elif seen_import:
                        if child.type == "dotted_name":
                            results.append(f"{rel_import}{child.text.decode('utf-8', errors='replace')}")
                        elif child.type == "aliased_import":
                            for sub in child.children:
                                if sub.type == "dotted_name":
                                    results.append(f"{rel_import}{sub.text.decode('utf-8', errors='replace')}")
                                    break
            else:
                for child in node.children:
                    if child.type in ("dotted_name", "relative_import"):
                        results.append(child.text.decode("utf-8", errors="replace"))
                        break  # only the module name, not the imported symbols

        for child in node.children:
            visit(child)

    visit(root)
    return results


def _ts_imports_js_ts(root: "Node") -> list[str]:
    """Extract import paths from a JS/TS/JSX/TSX AST root."""
    results: list[str] = []

    def _string_value(node: "Node") -> str | None:
        """Extract the inner string from a string node (strips quotes)."""
        if node.type == "string":
            for child in node.children:
                if child.type == "string_fragment":
                    return child.text.decode("utf-8", errors="replace")
            # Fallback: strip quotes manually
            raw = node.text.decode("utf-8", errors="replace")
            return raw.strip('"\'`')
        return None

    def visit(node: "Node"):
        # import X from 'module'  /  import { X } from 'module'  / import type ...
        if node.type == "import_statement":
            for child in node.children:
                if child.type == "string":
                    val = _string_value(child)
                    if val:
                        results.append(val)

        # export { X } from 'module'  /  export * from 'module'
        elif node.type == "export_statement":
            for child in node.children:
                if child.type == "string":
                    val = _string_value(child)
                    if val:
                        results.append(val)

        # require('./foo')  /  import('./lazy')
        elif node.type == "call_expression":
            func = None
            args_node = None
            for child in node.children:
                if child.type in ("identifier", "import"):
                    func = child.text.decode("utf-8", errors="replace")
                elif child.type == "arguments":
                    args_node = child

            if func in ("require", "import") and args_node:
                for arg in args_node.children:
                    if arg.type == "string":
                        val = _string_value(arg)
                        if val:
                            results.append(val)

        for child in node.children:
            visit(child)

    visit(root)
    return results


def _ts_imports_java(root: "Node") -> list[str]:
    """Extract import class names from a Java AST root."""
    results: list[str] = []

    def visit(node: "Node"):
        if node.type == "import_declaration":
            # Find the top-level scoped_identifier or identifier
            for child in node.children:
                if child.type in ("scoped_identifier", "identifier", "asterisk"):
                    results.append(child.text.decode("utf-8", errors="replace").replace("::", "."))
                    break
        for child in node.children:
            visit(child)

    visit(root)
    return results


def _ts_imports_rust(root: "Node") -> list[str]:
    """Extract use paths from a Rust AST root."""
    results: list[str] = []

    def visit(node: "Node"):
        if node.type == "use_declaration":
            # Grab the first meaningful child (scoped_identifier, scoped_use_list, identifier)
            for child in node.children:
                if child.type not in ("use", ";"):
                    raw = child.text.decode("utf-8", errors="replace")
                    import re
                    match = re.match(r'^(.*?)::\{([^}]+)\}$', raw)
                    if match:
                        base = match.group(1)
                        for item in match.group(2).split(','):
                            results.append(f"{base}::{item.strip()}")
                    else:
                        results.append(raw)
                    break
        elif node.type == "extern_crate_declaration":
            for child in node.children:
                if child.type == "identifier":
                    results.append(child.text.decode("utf-8", errors="replace"))
                    break
        for child in node.children:
            visit(child)

    visit(root)
    return results


def _ts_imports_go(root: "Node") -> list[str]:
    """Extract import paths from a Go AST root."""
    results: list[str] = []

    def visit(node: "Node"):
        if node.type == "import_spec":
            for child in node.children:
                if child.type == "interpreted_string_literal":
                    raw = child.text.decode("utf-8", errors="replace")
                    results.append(raw.strip('"'))
                    break
        for child in node.children:
            visit(child)

    visit(root)
    return results


def _ts_imports_cpp(root: "Node") -> list[str]:
    """Extract #include paths from a C/C++ AST root."""
    results: list[str] = []

    def visit(node: "Node"):
        if node.type == "preproc_include":
            for child in node.children:
                if child.type in ("string_literal", "system_lib_string"):
                    raw = child.text.decode("utf-8", errors="replace")
                    results.append(raw.strip('"<>'))
                    break
        for child in node.children:
            visit(child)

    visit(root)
    return results


# Map extension → walker function
_TS_WALKERS = {
    ".py":  _ts_imports_python,
    ".js":  _ts_imports_js_ts,
    ".mjs": _ts_imports_js_ts,
    ".cjs": _ts_imports_js_ts,
    ".jsx": _ts_imports_js_ts,
    ".ts":  _ts_imports_js_ts,
    ".tsx": _ts_imports_js_ts,
    ".java": _ts_imports_java,
    ".rs":  _ts_imports_rust,
    ".go":  _ts_imports_go,
    ".cpp": _ts_imports_cpp,
    ".cc":  _ts_imports_cpp,
    ".cxx": _ts_imports_cpp,
    ".h":   _ts_imports_cpp,
    ".hpp": _ts_imports_cpp,
    ".c":   _ts_imports_cpp,
}


def _extract_raw_imports_ts(source_bytes: bytes, ext: str) -> list[str]:
    """
    Parse imports from source bytes using tree-sitter.
    Returns a deduplicated list of raw import strings.
    Never raises — returns [] on any error.
    """
    try:
        parser, lang = _get_parser(ext)
        if parser is None:
            return []

        tree = parser.parse(source_bytes)
        walker = _TS_WALKERS.get(ext)
        if walker is None:
            return []

        raw = walker(tree.root_node)
        # Deduplicate while preserving first-seen order
        seen: set[str] = set()
        result: list[str] = []
        for s in raw:
            s = s.strip()
            if s and s not in seen:
                seen.add(s)
                result.append(s)
        return result
    except Exception as e:
        print(f"[contextl] tree-sitter parse warning ({ext}): {e}", file=sys.stderr)
        return []


# ---------------------------------------------------------------------------
# Regex fallback (kept verbatim from original for non-tree-sitter envs)
# ---------------------------------------------------------------------------

IMPORT_PATTERN = re.compile(
    r"""(?:import|export)\s+(?:type\s+)?          # import or import type or export
        (?:
            \{[^}]*\}                  # named imports: { Foo, Bar }
            |[\w*]+                    # default or namespace: Foo or *
            |[\w*]+\s*,\s*\{[^}]*\}   # mixed: Foo, { Bar }
        )?
        \s*(?:from\s+)?                # optional "from"
        ['\"](.*?)['\"]                  # the module path in quotes
    """,
    re.VERBOSE,
)
DYNAMIC_IMPORT_PATTERN = re.compile(r"""import\s*\(\s*['"](.*?)['"]\s*\)""")
PYTHON_FROM_IMPORT_PATTERN = re.compile(r"^[ \t]*from\s+([\.\w]+)\s+import\s+(?:\(([^)]+)\)|([^#\n]+))", re.MULTILINE)
PYTHON_IMPORT_PATTERN = re.compile(r"^[ \t]*import\s+([\.\w]+)", re.MULTILINE)
JAVA_IMPORT_PATTERN = re.compile(r"^import\s+(?:static\s+)?([\w.*]+);", re.MULTILINE)
JAVA_PACKAGE_PATTERN = re.compile(r"^package\s+([\w.]+);", re.MULTILINE)


def _extract_raw_imports_regex(source_code: str, extension: str) -> list[str]:
    """Legacy regex-based import extractor (fallback when tree-sitter is unavailable)."""
    paths = []
    if extension in {".ts", ".tsx", ".js", ".jsx"}:
        for match in IMPORT_PATTERN.finditer(source_code):
            paths.append(match.group(1))
        for match in DYNAMIC_IMPORT_PATTERN.finditer(source_code):
            paths.append(match.group(1))
    elif extension == ".py":
        for match in PYTHON_FROM_IMPORT_PATTERN.finditer(source_code):
            base = match.group(1)
            paths.append(base)
            symbols_str = match.group(2) or match.group(3)
            if symbols_str:
                symbols_str = symbols_str.replace('(', '').replace(')', '').replace('\\', '').strip()
                for sym in symbols_str.split(','):
                    sym = sym.split(' as ')[0].strip()
                    if sym and sym != '*':
                        paths.append(f"{base}.{sym}")
        for match in PYTHON_IMPORT_PATTERN.finditer(source_code):
            paths.append(match.group(1))
    elif extension == ".java":
        for match in JAVA_IMPORT_PATTERN.finditer(source_code):
            paths.append(match.group(1))
    return list(set(paths))


def _extract_raw_imports(source_bytes: bytes, source_code: str, extension: str) -> list[str]:
    """
    Route to tree-sitter (preferred) or regex (fallback).
    Returns deduplicated raw import strings.
    """
    if _TS_AVAILABLE and extension in _TS_WALKERS:
        return _extract_raw_imports_ts(source_bytes, extension)
    return _extract_raw_imports_regex(source_code, extension)


# ---------------------------------------------------------------------------
# Resolution helpers (unchanged from original — already correct)
# ---------------------------------------------------------------------------

def _is_external(import_path: str, extension: str, alias_map: dict[str, str] = None) -> bool:
    """Return True if this is an external package rather than a local file."""
    if extension in {".py", ".java", ".rs", ".go", ".cpp", ".cc", ".cxx", ".h", ".hpp", ".c"}:
        return False
    if import_path.startswith("./") or import_path.startswith("../"):
        return False
    if alias_map:
        for alias in alias_map:
            if import_path.startswith(alias):
                return False
    if import_path.startswith("@/"):
        return False
    return True


def _resolve_alias(import_path: str, alias_map: dict[str, str]) -> str | None:
    for alias, real_prefix in alias_map.items():
        if import_path.startswith(alias):
            suffix = import_path[len(alias):].lstrip("/")
            prefix = real_prefix.rstrip("/")
            if prefix:
                return prefix + "/" + suffix
            else:
                return suffix
    return None


def _resolve_relative(import_path: str, source_file: str) -> str:
    source_dir = PurePosixPath(source_file).parent
    resolved = source_dir / import_path
    parts = []
    for part in resolved.parts:
        if part == "..":
            if parts:
                parts.pop()
        elif part != ".":
            parts.append(part)
    return str(PurePosixPath(*parts)) if parts else "."


def _path_distance(source: str, target: str) -> int:
    s_parts = source.split('/')[:-1]
    t_parts = target.split('/')[:-1]
    common = 0
    for s, t in zip(s_parts, t_parts):
        if s == t:
            common += 1
        else:
            break
    return (len(s_parts) - common) + (len(t_parts) - common)


def _find_file_in_repo(
    candidate: str,
    file_index: dict,
    root: str,
    extension: str = "",
    source_file: str = "",
) -> str | None:
    root_path = Path(root)
    candidate_path = Path(candidate)

    if candidate_path.is_absolute():
        try:
            candidate_path = candidate_path.relative_to(root_path)
        except ValueError:
            return None

    candidate_str = str(candidate_path)

    if candidate_str in file_index:
        return candidate_str

    if extension == ".java":
        suffix = candidate_str + ".java"
        for path in file_index:
            if path.endswith(suffix):
                return path
        if "/" in candidate_str:
            parent_candidate = candidate_str.rsplit("/", 1)[0]
            parent_suffix = parent_candidate + ".java"
            for path in file_index:
                if path.endswith(parent_suffix):
                    return path
        return None

    if extension in (".cpp", ".cc", ".cxx", ".h", ".hpp", ".c"):
        suffix = "/" + candidate_str
        matches = []
        for path in file_index:
            if path.endswith(suffix) or path == candidate_str:
                matches.append(path)
        if not matches and "/" in candidate_str:
            base_name = "/" + candidate_str.split("/")[-1]
            for path in file_index:
                if path.endswith(base_name) or path == base_name.lstrip("/"):
                    matches.append(path)
        if matches:
            if source_file:
                matches.sort(key=lambda p: _path_distance(source_file, p))
            return matches[0]
        return None

    if extension == ".rs":
        if candidate_str.startswith("crate/"):
            match_str = candidate_str[6:]
        else:
            match_str = candidate_str
        
        rs_suffix = "/" + match_str + ".rs"
        mod_suffix = "/" + match_str + "/mod.rs"
        matches = []
        for path in file_index:
            if path.endswith(rs_suffix) or path == match_str + ".rs":
                matches.append(path)
            if path.endswith(mod_suffix) or path == match_str + "/mod.rs":
                matches.append(path)
        
        if not matches and "/" in match_str:
            parts = match_str.split("/")
            for i in range(len(parts) - 1, 0, -1):
                sub_path = "/" + "/".join(parts[:i])
                b_rs = sub_path + ".rs"
                b_mod = sub_path + "/mod.rs"
                for path in file_index:
                    if path.endswith(b_rs) or path.endswith(b_mod) or path == b_rs.lstrip("/") or path == b_mod.lstrip("/"):
                        matches.append(path)
                if matches:
                    break
        
        if matches:
            if source_file:
                matches.sort(key=lambda p: _path_distance(source_file, p))
            return matches[0]
        return None

    if extension == ".go":
        matches = []
        for path in file_index:
            parent_dir = path.rsplit("/", 1)[0] if "/" in path else ""
            if parent_dir and candidate_str.endswith(parent_dir):
                matches.append(path)
            elif candidate_str.endswith(path.replace(".go", "")):
                matches.append(path)
        
        if not matches:
            last_part = candidate_str.split("/")[-1]
            fallback_suffix = "/" + last_part + "/"
            for path in file_index:
                if fallback_suffix in path or path.startswith(last_part + "/"):
                    matches.append(path)
        
        if matches:
            matches.sort()
            last_part = candidate_str.split("/")[-1]
            preferred = "/" + last_part + ".go"
            for m in matches:
                if m.endswith(preferred) or m == preferred.lstrip("/"):
                    return m
            for m in matches:
                if m.endswith("/mod.go") or m == "mod.go":
                    return m
            return matches[0]
        return None

    if extension == ".py":
        def _resolve_python(cand: str) -> str | None:
            py_ext = cand + ".py"
            if py_ext in file_index:
                return py_ext
            py_idx = cand + "/__init__.py"
            if py_idx in file_index:
                return py_idx
            suffix = "/" + py_ext
            for path in file_index:
                if path.endswith(suffix) or path == py_ext:
                    return path
                    
            # Fallback for Python cross-language imports (e.g. from tests to .ts/.js core logic)
            for ext in [".ts", ".tsx", ".js", ".jsx", ".java", ".go", ".rs", ".cpp", ".cc", ".cxx", ".h", ".hpp", ".c"]:
                alt_suffix = "/" + cand + ext
                alt_matches = [p for p in file_index if p.endswith(alt_suffix) or p == alt_suffix.lstrip("/")]
                if len(alt_matches) == 1:
                    return alt_matches[0]
            return None
            
        res = _resolve_python(candidate_str)
        if res is not None:
            return res
            
        # Try stripping the last component (in case it's a symbol-level import like `from a.b import C`)
        if "/" in candidate_str:
            stripped = candidate_str.rsplit("/", 1)[0]
            return _resolve_python(stripped)
            
        return None
    for ext in [".tsx", ".ts", ".jsx", ".js"]:
        with_ext = candidate_str + ext
        if with_ext in file_index:
            return with_ext

    for ext in [".tsx", ".ts", ".jsx", ".js"]:
        index_path = candidate_str + "/index" + ext
        if index_path in file_index:
            return index_path
        mod_path = candidate_str + "/mod" + ext
        if mod_path in file_index:
            return mod_path




def _load_tsconfig_paths(tsconfig_path: Path) -> dict:
    import json
    visited: set = set()
    merged_paths: dict = {}

    def _load(path: Path):
        if path in visited:
            return
        visited.add(path)
        try:
            text = path.read_text(encoding="utf-8")
            pattern = r'(".*?"(?<!\\)")|(\/\*.*?\*\/|\/\/[^\r\n]*)'
            text = re.sub(pattern, lambda m: m.group(1) if m.group(1) else '', text, flags=re.S)
            data = json.loads(text)
        except Exception:
            return
        extends = data.get("extends")
        if extends:
            parent = (path.parent / extends).resolve()
            if not parent.suffix:
                parent = parent.with_suffix(".json")
            _load(parent)
        paths = data.get("compilerOptions", {}).get("paths", {})
        for alias, targets in paths.items():
            if targets:
                merged_paths[alias] = targets[0]

    _load(tsconfig_path)
    return merged_paths


def _detect_alias_map(scan_result: ScanResult) -> dict[str, str]:
    root = Path(scan_result.root)
    alias_map: dict[str, str] = {}
    ignore = {"node_modules", "dist", "build", ".next", "coverage", "out"}

    tsconfigs = []
    for tc in root.rglob("tsconfig.json"):
        if any(p in ignore for p in tc.parts):
            continue
        tsconfigs.append(tc)

    for tsconfig in tsconfigs:
        tsconfig_dir = tsconfig.parent
        paths = _load_tsconfig_paths(tsconfig)
        for alias, target in paths.items():
            clean_alias = alias.rstrip("/*").rstrip("*")
            clean_target = target.rstrip("/*").rstrip("*").lstrip("./")
            resolved = (tsconfig_dir / clean_target).resolve()
            try:
                repo_rel = str(resolved.relative_to(root))
            except ValueError:
                continue
            alias_key = clean_alias + "/"
            target_val = repo_rel.replace("\\", "/") + "/"
            if alias_key not in alias_map:
                alias_map[alias_key] = target_val

    for pkg in root.rglob("package.json"):
        if any(p in ignore for p in pkg.parts):
            continue
        try:
            import json
            data = json.loads(pkg.read_text(encoding="utf-8"))
            name = data.get("name")
            if name and isinstance(name, str):
                pkg_dir = pkg.parent
                try:
                    repo_rel = str(pkg_dir.relative_to(root)).replace("\\", "/")
                    if repo_rel == ".":
                        continue
                    alias_map[name] = repo_rel
                    alias_map[name + "/"] = repo_rel + "/"
                except ValueError:
                    pass
        except Exception:
            pass

    for gomod in root.rglob("go.mod"):
        if any(p in ignore for p in gomod.parts):
            continue
        try:
            text = gomod.read_text(encoding="utf-8")
            for line in text.splitlines():
                if line.startswith("module "):
                    mod_name = line.split(" ")[1].strip()
                    try:
                        repo_rel = str(gomod.parent.relative_to(root)).replace("\\", "/")
                        if repo_rel == ".":
                            alias_map[mod_name] = ""
                            alias_map[mod_name + "/"] = ""
                        else:
                            alias_map[mod_name] = repo_rel
                            alias_map[mod_name + "/"] = repo_rel + "/"
                    except ValueError:
                        pass
                    break
        except Exception:
            pass

    if not alias_map:
        top_dirs = {Path(f.path).parts[0] for f in scan_result.files if Path(f.path).parts}
        if len(top_dirs) == 1:
            top = list(top_dirs)[0]
            alias_map["@/"] = top + "/"
        else:
            alias_map["@/"] = ""

    return alias_map


# ---------------------------------------------------------------------------
# Data structures (unchanged)
# ---------------------------------------------------------------------------

@dataclass
class ImportRelationship:
    """A resolved import from one file to another."""
    source: str
    target: str
    raw_import: str


@dataclass
class ParseResult:
    """All import relationships discovered across the repository."""
    relationships: list[ImportRelationship] = field(default_factory=list)
    unresolved: list[tuple[str, str]] = field(default_factory=list)

    def summary(self) -> str:
        lines = [
            f"Import relationships found: {len(self.relationships)}",
            f"Unresolved (external/missing): {len(self.unresolved)}",
            "",
            "Resolved imports:",
        ]
        for rel in self.relationships:
            lines.append(f"  {rel.source}")
            lines.append(f"    → {rel.target}  (from '{rel.raw_import}')")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main entry point (public API — signature unchanged)
# ---------------------------------------------------------------------------

def parse_imports(scan_result: ScanResult) -> ParseResult:
    """
    Parse all import statements from scanned files and resolve them
    to concrete file paths within the repository.

    Uses tree-sitter for accurate AST-level parsing when available,
    falling back to the original regex engine transparently.

    Args:
        scan_result: Output from scan_repo().

    Returns:
        ParseResult containing all resolved ImportRelationships.
    """
    result = ParseResult()
    file_index: dict[str, ScannedFile] = {f.path: f for f in scan_result.files}
    alias_map = _detect_alias_map(scan_result)

    # Java pre-pass: build package map + implicit same-package edges
    java_packages: dict[str, list[str]] = {}
    for scanned_file in scan_result.files:
        if scanned_file.extension == ".java":
            try:
                source_bytes = Path(scanned_file.absolute_path).read_bytes()
                source_code = source_bytes.decode("utf-8", errors="replace")
                pkg_match = JAVA_PACKAGE_PATTERN.search(source_code)
                if pkg_match:
                    pkg = pkg_match.group(1)
                    java_packages.setdefault(pkg, []).append(scanned_file.path)
            except Exception:
                pass

    for pkg, files in java_packages.items():
        for source_file in files:
            for target_file in files:
                if source_file != target_file:
                    result.relationships.append(
                        ImportRelationship(
                            source=source_file,
                            target=target_file,
                            raw_import=f"implicit_package:{pkg}",
                        )
                    )

    # Main pass: parse each file
    for scanned_file in scan_result.files:
        try:
            source_bytes = Path(scanned_file.absolute_path).read_bytes()
            source_code = source_bytes.decode("utf-8", errors="replace")
        except Exception:
            continue

        raw_imports = _extract_raw_imports(source_bytes, source_code, scanned_file.extension)

        # For Python: also add base.Symbol candidates (for fine-grained resolution)
        if scanned_file.extension == ".py" and not _TS_AVAILABLE:
            pass  # regex already handles this above
        elif scanned_file.extension == ".py" and _TS_AVAILABLE:
            # tree-sitter gives us just the module name; add symbol-level candidates
            # to match the legacy behaviour that resolves "scanner.ScannedFile" → scanner.py
            extra: list[str] = []
            for match in PYTHON_FROM_IMPORT_PATTERN.finditer(source_code):
                base = match.group(1)
                symbols_str = match.group(2) or match.group(3)
                if symbols_str:
                    symbols_str = symbols_str.replace('(', '').replace(')', '').replace('\\', '').strip()
                    for sym in symbols_str.split(','):
                        sym = sym.split(' as ')[0].strip()
                        if sym and sym != '*':
                            extra.append(f"{base}.{sym}")
            # Merge without duplicates
            seen = set(raw_imports)
            for e in extra:
                if e not in seen:
                    raw_imports.append(e)
                    seen.add(e)

        for raw in raw_imports:
            if _is_external(raw, scanned_file.extension, alias_map):
                result.unresolved.append((scanned_file.path, raw))
                continue

            # Resolve to candidate path
            if scanned_file.extension == ".java":
                if raw.endswith(".*"):
                    pkg = raw[:-2]
                    for target_file in java_packages.get(pkg, []):
                        if target_file != scanned_file.path:
                            result.relationships.append(
                                ImportRelationship(source=scanned_file.path, target=target_file, raw_import=raw)
                            )
                    continue
                candidate = raw.replace(".", "/")

            elif scanned_file.extension == ".py":
                if raw.startswith("."):
                    dots = len(raw) - len(raw.lstrip("."))
                    base_dir = Path(scanned_file.path).parent
                    for _ in range(dots - 1):
                        base_dir = base_dir.parent
                    mod_path = raw.lstrip(".").replace(".", "/")
                    candidate = str(base_dir / mod_path) if mod_path else str(base_dir)
                else:
                    candidate = raw.replace(".", "/")

            elif scanned_file.extension in (".cpp", ".cc", ".cxx", ".h", ".hpp", ".c"):
                candidate = raw
            elif scanned_file.extension == ".rs":
                is_likely_external = not (raw.startswith("crate::") or raw.startswith("super::") or raw.startswith("self::"))
                candidate = raw.replace("::", "/")
            elif scanned_file.extension == ".go":
                resolved = _resolve_alias(raw, alias_map)
                if resolved is not None:
                    candidate = resolved
                else:
                    candidate = raw

            else:
                # Node.js / TypeScript
                resolved_alias = _resolve_alias(raw, alias_map)
                if resolved_alias is not None:
                    candidate = resolved_alias
                else:
                    candidate = _resolve_relative(raw, scanned_file.path)

            matched = _find_file_in_repo(candidate, file_index, scan_result.root, scanned_file.extension, scanned_file.path)

            if matched:
                result.relationships.append(
                    ImportRelationship(
                        source=scanned_file.path,
                        target=matched,
                        raw_import=raw,
                    )
                )
            else:
                if scanned_file.extension == ".rs" and locals().get("is_likely_external", False):
                    continue
                if scanned_file.extension == ".py":
                    base_pkg = raw.split(".")[0]
                    if base_pkg in PYTHON_STDLIB_AND_COMMON_PACKAGES:
                        continue
                result.unresolved.append((scanned_file.path, raw))

    return result


# ---------------------------------------------------------------------------
# SKELETON MODE — extract_skeleton(file_path: str) -> dict
# ---------------------------------------------------------------------------

def _node_text(node: "Node") -> str:
    return node.text.decode("utf-8", errors="replace") if node.text else ""


def _skeleton_python(root: "Node", source_bytes: bytes) -> dict:
    """Extract Python skeleton: classes, functions, docstrings."""
    classes: list[dict] = []
    functions: list[dict] = []
    exports: list[str] = []
    docstrings: dict[str, str] = {}

    def _get_docstring(body_node: "Node") -> str | None:
        """Check if the first statement in a body is a string literal (docstring)."""
        for child in body_node.children:
            if child.type == "expression_statement":
                for sub in child.children:
                    if sub.type == "string":
                        raw = _node_text(sub).strip()
                        # Strip triple or single quotes
                        for q in ('"""', "'''", '"', "'"):
                            if raw.startswith(q) and raw.endswith(q) and len(raw) > 2 * len(q):
                                return raw[len(q):-len(q)].strip()
                        return raw
            break  # Only check first statement
        return None

    def _get_decorators(node: "Node") -> list[str]:
        """Collect decorator nodes that appear before a function/class definition."""
        decorators: list[str] = []
        if not node.parent:
            return decorators
        siblings = node.parent.children
        try:
            idx = list(siblings).index(node)
        except ValueError:
            return decorators
        for i in range(idx - 1, -1, -1):
            sib = siblings[i]
            if sib.type == "decorator":
                decorators.insert(0, _node_text(sib).strip())
            else:
                break
        return decorators

    def visit_class(node: "Node") -> dict:
        name = ""
        bases: list[str] = []
        methods: list[dict] = []
        props: list[dict] = []

        for child in node.children:
            if child.type == "identifier" and not name:
                name = _node_text(child)
            elif child.type == "argument_list":
                for arg in child.children:
                    if arg.type not in ("(", ")", ","):
                        bases.append(_node_text(arg).strip())
            elif child.type == "block":
                ds = _get_docstring(child)
                if ds:
                    docstrings[name] = ds
                for stmt in child.children:
                    if stmt.type in ("function_definition", "decorated_definition"):
                        fn_node = stmt
                        if stmt.type == "decorated_definition":
                            for sub in stmt.children:
                                if sub.type == "function_definition":
                                    fn_node = sub
                                    break
                        methods.append(visit_function(fn_node, is_method=True))

        entry: dict = {"name": name, "bases": bases, "methods": methods, "properties": props}
        return entry

    def visit_function(node: "Node", is_method: bool = False) -> dict:
        name = ""
        params = ""
        decorators = _get_decorators(node)
        is_async = False

        for child in node.children:
            if child.type == "async":
                is_async = True
            elif child.type == "identifier" and not name:
                name = _node_text(child)
            elif child.type == "parameters":
                params = _node_text(child)
            elif child.type == "block":
                ds = _get_docstring(child)
                if ds and name:
                    docstrings[name] = ds
                break  # Stop before body

        return {
            "name": name,
            "params": params,
            "is_async": is_async,
            "decorators": decorators,
        }

    def visit(node: "Node"):
        if node.type == "class_definition":
            classes.append(visit_class(node))
            return  # Don't recurse into classes (handled inside visit_class)
        if node.type == "function_definition":
            functions.append(visit_function(node))
            return
        if node.type == "decorated_definition":
            for child in node.children:
                if child.type == "class_definition":
                    classes.append(visit_class(child))
                    return
                if child.type == "function_definition":
                    functions.append(visit_function(child))
                    return
        for child in node.children:
            visit(child)

    visit(root)

    return {
        "classes": classes,
        "functions": functions,
        "exports": exports,
        "docstrings": docstrings,
    }


def _skeleton_ts_js(root: "Node") -> dict:
    """Extract TypeScript/JavaScript skeleton: classes, methods, functions, exports."""
    classes: list[dict] = []
    functions: list[dict] = []
    exports: list[str] = []
    docstrings: dict[str, str] = {}

    def _visibility(node: "Node") -> str:
        for child in node.children:
            if child.type == "accessibility_modifier":
                return _node_text(child)
        return "public"

    def _return_type(node: "Node") -> str:
        for child in node.children:
            if child.type == "type_annotation":
                raw = _node_text(child)
                return raw.lstrip(":").strip()
        return ""

    def _is_async(node: "Node") -> bool:
        for child in node.children:
            if child.type == "async":
                return True
        return False

    def _decorators_before(node: "Node") -> list[str]:
        decs: list[str] = []
        if not node.parent:
            return decs
        siblings = node.parent.children
        idx = siblings.index(node)
        for i in range(idx - 1, -1, -1):
            s = siblings[i]
            if s.type == "decorator":
                decs.insert(0, _node_text(s).strip())
            else:
                break
        return decs

    def visit_class(node: "Node") -> dict:
        name = ""
        extends_cls = ""
        implements_list: list[str] = []
        methods: list[dict] = []
        properties: list[dict] = []

        for child in node.children:
            if child.type == "type_identifier" and not name:
                name = _node_text(child)
            elif child.type == "class_heritage":
                for hc in child.children:
                    if hc.type == "extends_clause":
                        for sub in hc.children:
                            if sub.type in ("type_identifier", "identifier"):
                                extends_cls = _node_text(sub)
                                break
                    elif hc.type == "implements_clause":
                        for sub in hc.children:
                            if sub.type not in ("implements",):
                                implements_list.append(_node_text(sub).strip().rstrip(","))
            elif child.type == "class_body":
                for member in child.children:
                    if member.type in ("method_definition", "method_signature"):
                        methods.append(visit_method(member))
                    elif member.type in ("public_field_definition", "field_definition"):
                        vis = _visibility(member)
                        prop_name = ""
                        prop_type = ""
                        for sub in member.children:
                            if sub.type in ("property_identifier", "identifier") and not prop_name:
                                prop_name = _node_text(sub)
                            elif sub.type == "type_annotation":
                                prop_type = _node_text(sub).lstrip(":").strip()
                        if prop_name:
                            properties.append({
                                "name": prop_name,
                                "type": prop_type,
                                "visibility": vis,
                            })

        return {
            "name": name,
            "extends": extends_cls,
            "implements": implements_list,
            "methods": methods,
            "properties": properties,
        }

    def visit_method(node: "Node") -> dict:
        name = ""
        params = ""
        vis = _visibility(node)
        ret_type = _return_type(node)
        async_ = _is_async(node)
        decs = _decorators_before(node)

        for child in node.children:
            if child.type in ("property_identifier", "identifier") and not name:
                name = _node_text(child)
            elif child.type == "formal_parameters":
                params = _node_text(child)
            elif child.type == "statement_block":
                break  # Stop before body

        return {
            "name": name,
            "params": params,
            "return_type": ret_type,
            "visibility": vis,
            "is_async": async_,
            "decorators": decs,
        }

    def visit_function(node: "Node") -> dict:
        name = ""
        params = ""
        ret_type = _return_type(node)
        async_ = _is_async(node)
        is_exported = False

        for child in node.children:
            if child.type in ("identifier",) and not name:
                name = _node_text(child)
            elif child.type == "formal_parameters":
                params = _node_text(child)
            elif child.type == "statement_block":
                break

        return {
            "name": name,
            "params": params,
            "return_type": ret_type,
            "is_async": async_,
            "is_exported": is_exported,
        }

    def visit(node: "Node"):
        if node.type == "class_declaration":
            c = visit_class(node)
            classes.append(c)
            return
        if node.type in ("function_declaration", "function"):
            f = visit_function(node)
            if f["name"]:
                functions.append(f)
            return
        if node.type == "export_statement":
            # Track what is exported
            for child in node.children:
                if child.type == "class_declaration":
                    c = visit_class(child)
                    c_copy = dict(c)
                    classes.append(c_copy)
                    if c["name"]:
                        exports.append(c["name"])
                    return
                if child.type in ("function_declaration", "function"):
                    f = visit_function(child)
                    if f["name"]:
                        f["is_exported"] = True
                        functions.append(f)
                        exports.append(f["name"])
                    return
                if child.type == "export_clause":
                    for spec in child.children:
                        if spec.type == "export_specifier":
                            for sub in spec.children:
                                if sub.type == "identifier":
                                    exports.append(_node_text(sub))
                                    break
                if child.type in ("identifier", "type_identifier"):
                    exports.append(_node_text(child))
        for child in node.children:
            visit(child)

    visit(root)

    return {
        "classes": classes,
        "functions": functions,
        "exports": list(dict.fromkeys(exports)),  # dedupe, preserve order
        "docstrings": docstrings,
    }


def _skeleton_java(root: "Node") -> dict:
    """Extract Java skeleton: classes and methods."""
    classes: list[dict] = []
    functions: list[dict] = []
    exports: list[str] = []
    docstrings: dict[str, str] = {}

    def _modifiers(node: "Node") -> list[str]:
        mods = []
        for child in node.children:
            if child.type == "modifiers":
                for m in child.children:
                    mods.append(_node_text(m))
        return mods

    def visit_class(node: "Node") -> dict:
        name = ""
        superclass = ""
        interfaces: list[str] = []
        methods: list[dict] = []

        for child in node.children:
            if child.type == "identifier" and not name:
                name = _node_text(child)
            elif child.type == "superclass":
                for sub in child.children:
                    if sub.type in ("type_identifier", "identifier"):
                        superclass = _node_text(sub)
                        break
            elif child.type == "super_interfaces":
                for sub in child.children:
                    if sub.type not in ("implements",):
                        interfaces.append(_node_text(sub).strip().rstrip(","))
            elif child.type == "class_body":
                for member in child.children:
                    if member.type == "method_declaration":
                        methods.append(visit_method(member))
        return {
            "name": name,
            "extends": superclass,
            "implements": interfaces,
            "methods": methods,
            "properties": [],
        }

    def visit_method(node: "Node") -> dict:
        name = ""
        params = ""
        ret_type = ""
        mods = _modifiers(node)

        for child in node.children:
            if child.type == "identifier" and not name:
                name = _node_text(child)
            elif child.type == "formal_parameters":
                params = _node_text(child)
            elif child.type in ("type_identifier", "void_type", "generic_type", "array_type", "integral_type", "boolean_type", "floating_point_type"):
                if not ret_type:
                    ret_type = _node_text(child)
            elif child.type == "block":
                break

        return {
            "name": name,
            "params": params,
            "return_type": ret_type,
            "visibility": next((m for m in mods if m in ("public", "private", "protected")), "package"),
            "is_async": False,
            "decorators": [],
        }

    def visit(node: "Node"):
        if node.type == "class_declaration":
            classes.append(visit_class(node))
            return
        for child in node.children:
            visit(child)

    visit(root)
    return {"classes": classes, "functions": functions, "exports": exports, "docstrings": docstrings}


def _skeleton_rust(root: "Node") -> dict:
    """Extract Rust skeleton: structs, impl blocks, traits."""
    classes: list[dict] = []
    functions: list[dict] = []
    exports: list[str] = []
    docstrings: dict[str, str] = {}

    def visit_struct(node: "Node") -> dict:
        name = ""
        fields: list[dict] = []
        for child in node.children:
            if child.type == "type_identifier" and not name:
                name = _node_text(child)
            elif child.type == "field_declaration_list":
                for f in child.children:
                    if f.type == "field_declaration":
                        fname = ""
                        ftype = ""
                        for sub in f.children:
                            if sub.type == "field_identifier" and not fname:
                                fname = _node_text(sub)
                            elif sub.type in ("type_identifier", "generic_type", "reference_type", "primitive_type"):
                                if not ftype:
                                    ftype = _node_text(sub)
                        if fname:
                            fields.append({"name": fname, "type": ftype})
        return {"name": name, "fields": fields, "methods": [], "extends": "", "implements": [], "properties": []}

    def visit_fn(node: "Node") -> dict:
        name = ""
        params = ""
        ret_type = ""
        is_pub = False
        for child in node.children:
            if child.type == "visibility_modifier":
                is_pub = True
            elif child.type == "identifier" and not name:
                name = _node_text(child)
            elif child.type == "parameters":
                params = _node_text(child)
            elif child.type == "type_identifier" and not ret_type:
                ret_type = _node_text(child)
            elif child.type == "block":
                break
        return {"name": name, "params": params, "return_type": ret_type, "visibility": "pub" if is_pub else "private", "is_async": False, "decorators": []}

    def visit_impl(node: "Node") -> dict | None:
        impl_type = ""
        trait = ""
        methods: list[dict] = []
        for child in node.children:
            if child.type == "type_identifier":
                if not impl_type:
                    impl_type = _node_text(child)
                elif not trait:
                    trait = impl_type
                    impl_type = _node_text(child)
            elif child.type == "declaration_list":
                for fn_node in child.children:
                    if fn_node.type == "function_item":
                        methods.append(visit_fn(fn_node))
        return {"name": impl_type, "trait": trait, "methods": methods}

    def visit(node: "Node"):
        if node.type == "struct_item":
            classes.append(visit_struct(node))
        elif node.type == "impl_item":
            impl = visit_impl(node)
            if impl and impl["name"]:
                # Find or create the class entry
                existing = next((c for c in classes if c["name"] == impl["name"]), None)
                if existing:
                    existing["methods"].extend(impl["methods"])
                else:
                    classes.append({
                        "name": impl["name"],
                        "fields": [],
                        "methods": impl["methods"],
                        "extends": impl.get("trait", ""),
                        "implements": [],
                        "properties": [],
                    })
        elif node.type == "function_item":
            functions.append(visit_fn(node))
        for child in node.children:
            visit(child)

    visit(root)
    return {"classes": classes, "functions": functions, "exports": exports, "docstrings": docstrings}



def _skeleton_go(root: "Node") -> dict:
    classes = []
    functions = []
    exports = []
    docstrings = {}

    def visit_fn(node: "Node") -> dict:
        name = ""
        params = ""
        ret_type = ""
        is_method = (node.type == "method_declaration")
        receiver = ""

        for child in node.children:
            if child.type == "identifier" or child.type == "field_identifier":
                if not name:
                    name = _node_text(child)
            elif child.type == "parameter_list":
                if is_method and not receiver:
                    receiver = _node_text(child)
                else:
                    params = _node_text(child)
            elif child.type == "type_identifier":
                ret_type = _node_text(child)

        return {"name": name, "params": params, "return_type": ret_type, "visibility": "pub" if name and name[0].isupper() else "private", "is_async": False, "decorators": [], "receiver": receiver}

    def visit(node: "Node"):
        if node.type in ("function_declaration", "method_declaration"):
            functions.append(visit_fn(node))
        elif node.type == "type_spec":
            name = ""
            for child in node.children:
                if child.type == "type_identifier":
                    name = _node_text(child)
                elif child.type == "struct_type" or child.type == "interface_type":
                    if name:
                        classes.append({"name": name, "fields": [], "methods": [], "extends": "", "implements": [], "properties": []})
        for child in node.children:
            visit(child)

    visit(root)
    return {"classes": classes, "functions": functions, "exports": exports, "docstrings": docstrings}

def _skeleton_cpp(root: "Node") -> dict:
    classes = []
    functions = []
    exports = []
    docstrings = {}

    def visit_fn(node: "Node") -> dict:
        name = ""
        params = ""
        for child in node.children:
            if child.type == "function_declarator":
                for sub in child.children:
                    if sub.type == "identifier" or sub.type == "field_identifier":
                        name = _node_text(sub)
                    elif sub.type == "parameter_list":
                        params = _node_text(sub)
        return {"name": name, "params": params, "return_type": "", "visibility": "pub", "is_async": False, "decorators": []}

    def visit(node: "Node"):
        if node.type == "function_definition":
            functions.append(visit_fn(node))
        elif node.type in ("class_specifier", "struct_specifier"):
            name = ""
            for child in node.children:
                if child.type == "type_identifier":
                    name = _node_text(child)
            if name:
                classes.append({"name": name, "fields": [], "methods": [], "extends": "", "implements": [], "properties": []})
        for child in node.children:
            visit(child)

    visit(root)
    return {"classes": classes, "functions": functions, "exports": exports, "docstrings": docstrings}

_SKELETON_HANDLERS = {
    ".py":  _skeleton_python,
    ".ts":  _skeleton_ts_js,
    ".tsx": _skeleton_ts_js,
    ".js":  _skeleton_ts_js,
    ".jsx": _skeleton_ts_js,
    ".java": _skeleton_java,
    ".rs":  _skeleton_rust,
    ".go": _skeleton_go,
    ".cpp": _skeleton_cpp,
    ".h": _skeleton_cpp,
    ".hpp": _skeleton_cpp,
    ".cc": _skeleton_cpp,
    ".c": _skeleton_cpp,
}


def extract_skeleton(file_path: str) -> dict:
    """
    Extract the structural skeleton (API surface) of a file.

    Uses tree-sitter to parse without executing or importing the code.
    Returns class names, method signatures, function signatures, and
    docstrings — without any implementation bodies.

    A 5,000-line file becomes a ~100-line reference header.

    Args:
        file_path: Absolute or relative path to the source file.

    Returns:
        dict with keys: file, language, classes, functions, exports, docstrings.
        Returns {"error": ...} on failure — never raises.
    """
    try:
        path = Path(file_path)
        ext = path.suffix.lower()
        
        lang_map = {
            ".py": "python", ".ts": "typescript", ".tsx": "tsx",
            ".js": "javascript", ".jsx": "jsx", ".java": "java",
            ".rs": "rust", ".go": "go", ".cpp": "cpp",
        }
        derived_language = lang_map.get(ext, ext.lstrip("."))

        if not _TS_AVAILABLE:
            return {
                "file": str(path),
                "language": derived_language,
                "error": "tree-sitter not installed — run: pip install tree-sitter tree-sitter-python tree-sitter-typescript ...",
                "classes": [],
                "functions": [],
                "exports": [],
                "docstrings": {},
            }

        parser, lang = _get_parser(ext)
        if parser is None:
            return {
                "file": str(path),
                "language": derived_language,
                "error": f"Unsupported file type: {ext}",
                "classes": [],
                "functions": [],
                "exports": [],
                "docstrings": {},
            }

        source_bytes = path.read_bytes()
        tree = parser.parse(source_bytes)

        handler = _SKELETON_HANDLERS.get(ext)
        if handler is None:
            return {
                "file": str(path),
                "language": derived_language,
                "error": f"No skeleton handler for {ext}",
                "classes": [],
                "functions": [],
                "exports": [],
                "docstrings": {},
            }

        if ext == ".py":
            body = handler(tree.root_node, source_bytes)
        else:
            body = handler(tree.root_node)

        return {
            "file": str(path),
            "language": derived_language,
            **body,
        }

    except Exception as e:
        # Fallback if path is not yet defined
        lang = "unknown"
        if 'derived_language' in locals():
            lang = derived_language
        elif 'file_path' in locals():
            ext = Path(file_path).suffix.lower()
            lang = lang_map.get(ext, ext.lstrip(".")) if 'lang_map' in locals() else ext.lstrip(".")

        return {
            "file": str(file_path),
            "language": lang,
            "error": str(e),
            "classes": [],
            "functions": [],
            "exports": [],
            "docstrings": {},
        }


# ---------------------------------------------------------------------------
# CLI entrypoint
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import sys
    from scanner import scan_repo

    target = sys.argv[1] if len(sys.argv) > 1 else "."
    scan = scan_repo(target)
    parse = parse_imports(scan)
    print(parse.summary())
