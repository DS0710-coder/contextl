"""
Repository Intelligence Engine
Step 2: Import Parser

Reads each scanned file and extracts import relationships.
Handles:
  - Relative imports:  import X from "./foo"  or  "../../lib/bar"
  - Alias imports:     import X from "@/components/Button"
  - Type imports:      import type { X } from "@/types"
  - Named imports:     import { X, Y } from "./utils"

Returns only imports that resolve to other files in the repository.
External packages (react, next, etc.) are ignored.
"""

import re
from pathlib import Path
from dataclasses import dataclass, field

from scanner import ScannedFile, ScanResult


# Matches any ES6 import statement and captures the module path
IMPORT_PATTERN = re.compile(
    r"""(?:import|export)\s+(?:type\s+)?          # import or import type or export
        (?:
            \{[^}]*\}                  # named imports: { Foo, Bar }
            |[\w*]+                    # default or namespace: Foo or *
            |[\w*]+\s*,\s*\{[^}]*\}   # mixed: Foo, { Bar }
        )?
        \s*(?:from\s+)?                # optional "from"
        ['"](.*?)['"]                  # the module path in quotes
    """,
    re.VERBOSE,
)

# Also catch: import("./foo")  — dynamic imports
DYNAMIC_IMPORT_PATTERN = re.compile(r"""import\s*\(\s*['"](.*?)['"]\s*\)""")

# Python
PYTHON_FROM_IMPORT_PATTERN = re.compile(r"^[ \t]*from\s+([.\w]+)\s+import\s+(?:\(([^)]+)\)|([^#\n]+))", re.MULTILINE)
PYTHON_IMPORT_PATTERN = re.compile(r"^[ \t]*import\s+([.\w]+)", re.MULTILINE)

# Java
JAVA_IMPORT_PATTERN = re.compile(r"^import\s+(?:static\s+)?([\w.*]+);", re.MULTILINE)
JAVA_PACKAGE_PATTERN = re.compile(r"^package\s+([\w.]+);", re.MULTILINE)


@dataclass
class ImportRelationship:
    """A resolved import from one file to another."""
    source: str       # Relative path of the file doing the importing
    target: str       # Relative path of the file being imported
    raw_import: str   # The original import string (e.g. "@/components/Button")


@dataclass
class ParseResult:
    """All import relationships discovered across the repository."""
    relationships: list[ImportRelationship] = field(default_factory=list)
    unresolved: list[tuple[str, str]] = field(default_factory=list)
    # unresolved = [(source_file, raw_import), ...] — external packages or not found

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


def _extract_raw_imports(source_code: str, extension: str) -> list[str]:
    """Pull all import paths out of a source file based on its extension."""
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


def _is_external(import_path: str, extension: str, alias_map: dict[str, str] = None) -> bool:
    """Return True if this is an external package rather than a local file."""
    if extension in {".py", ".java"}:
        # For Python and Java, it's hard to tell without resolving, 
        # so assume it's local and let the resolver fail if it's external.
        return False

    # Node.js: Local files start with . (relative) or match an alias
    if import_path.startswith("./") or import_path.startswith("../"):
        return False
    
    if alias_map:
        for alias in alias_map:
            if import_path.startswith(alias):
                return False

    if import_path.startswith("@/"):
        return False
        
    return True  # Everything else is an external package


def _resolve_alias(import_path: str, alias_map: dict[str, str]) -> str | None:
    """
    Convert an aliased import path to a repo-relative path.
    Example: "@/components/Button" → "frontend/components/Button"
    """
    for alias, real_prefix in alias_map.items():
        if import_path.startswith(alias):
            suffix = import_path[len(alias):].lstrip("/")
            prefix = real_prefix.rstrip("/")
            if prefix:
                return prefix + "/" + suffix
            else:
                # alias maps directly to the repo root — no leading slash
                return suffix
    return None


def _resolve_relative(import_path: str, source_file: str) -> str:
    """
    Resolve a relative import path against the source file's directory.
    Returns a repo-relative path string (NOT absolute).

    Example: source="apps/web/src/routes.tsx", import="./App.tsx"
             → "apps/web/src/App.tsx"
    """
    # Use pure PurePosixPath arithmetic — never call .resolve() which
    # anchors to the OS cwd and produces a wrong absolute path.
    from pathlib import PurePosixPath
    source_dir = PurePosixPath(source_file).parent
    # Normalise away any .. and . components without touching the filesystem
    resolved = (source_dir / import_path)
    # PurePosixPath doesn't have .resolve(), so manually normalise ".."
    parts = []
    for part in resolved.parts:
        if part == "..":
            if parts:
                parts.pop()
        elif part != ".":
            parts.append(part)
    return str(PurePosixPath(*parts)) if parts else "."


def _find_file_in_repo(
    candidate: str,
    file_index: dict[str, str],
    root: str,
    extension: str = "",
) -> str | None:
    """
    Given a candidate path (without extension), find the matching file
    in the repository. Tries adding common extensions if missing.
    
    file_index maps absolute_path → relative_path.
    """
    root_path = Path(root)
    candidate_path = Path(candidate)

    # If candidate is absolute, make it relative to root
    if candidate_path.is_absolute():
        try:
            candidate_path = candidate_path.relative_to(root_path)
        except ValueError:
            return None

    candidate_str = str(candidate_path)

    # Try exact match first (already has extension)
    if candidate_str in file_index:
        return candidate_str

    if extension == ".java":
        # Java candidate is like 'com/example/Config'
        # We search for any file ending in this candidate + .java
        suffix = candidate_str + ".java"
        for path in file_index:
            if path.endswith(suffix):
                return path
        
        # Fallback for static method/field imports: import static com.example.MyClass.myMethod;
        # In this case, candidate_str is 'com/example/MyClass/myMethod'
        if "/" in candidate_str:
            parent_candidate = candidate_str.rsplit("/", 1)[0]
            parent_suffix = parent_candidate + ".java"
            for path in file_index:
                if path.endswith(parent_suffix):
                    return path
                    
        return None

    if extension == ".py":
        # Python: try exact candidate + .py
        py_ext = candidate_str + ".py"
        if py_ext in file_index:
            return py_ext
        # Try python package index
        py_idx = candidate_str + "/__init__.py"
        if py_idx in file_index:
            return py_idx
        # Fallback: search for any file ending in candidate + .py (handles src/ prefix omit)
        suffix = "/" + py_ext
        for path in file_index:
            if path.endswith(suffix) or path == py_ext:
                return path
        return None

    # Node.js: Try adding each supported extension
    for ext in [".tsx", ".ts", ".jsx", ".js"]:
        with_ext = candidate_str + ext
        if with_ext in file_index:
            return with_ext

    # Node.js / Deno: Try as a directory index/mod file
    for ext in [".tsx", ".ts", ".jsx", ".js"]:
        index_path = candidate_str + "/index" + ext
        if index_path in file_index:
            return index_path
        mod_path = candidate_str + "/mod" + ext
        if mod_path in file_index:
            return mod_path

    # Fuzzy fallback for dynamic paths (like P4A recipes)
    if extension == ".py":
        candidate_suffix = "/" + candidate_str + ".py"
        matches = [p for p in file_index if p.endswith(candidate_suffix)]
        if len(matches) == 1:
            return matches[0]

    return None


def _load_tsconfig_paths(tsconfig_path: Path) -> dict:
    """
    Load compilerOptions.paths from a tsconfig.json, following `extends` chains.
    Returns merged paths dict (child overrides parent).
    """
    import json
    visited = set()
    merged_paths = {}

    def _load(path: Path):
        if path in visited:
            return
        visited.add(path)
        try:
            text = path.read_text(encoding="utf-8")
            pattern = r'(".*?(?<!\\)")|(/\*.*?\*/|//[^\r\n]*)'
            text = re.sub(pattern, lambda m: m.group(1) if m.group(1) else '', text, flags=re.S)
            data = json.loads(text)
        except Exception:
            return

        # Follow extends first (parent paths are base, child overrides)
        extends = data.get("extends")
        if extends:
            parent = (path.parent / extends).resolve()
            # handle both with and without .json
            if not parent.suffix:
                parent = parent.with_suffix(".json")
            _load(parent)

        # Then apply this tsconfig's own paths (child wins)
        paths = data.get("compilerOptions", {}).get("paths", {})
        for alias, targets in paths.items():
            if targets:
                merged_paths[alias] = targets[0]

    _load(tsconfig_path)
    return merged_paths


def _detect_alias_map(scan_result: ScanResult) -> dict[str, str]:
    """
    Auto-detect TypeScript path aliases by reading every tsconfig.json in the repo.
    Each tsconfig's aliases are scoped relative to its own directory so that
    multiple packages with conflicting @/* aliases don't clobber each other.

    Returns a flat map:  alias_prefix -> resolved_repo_relative_prefix
    e.g. {
        '@/'            : 'packages/ui/src/',
        '@components/'  : 'apps/web/src/components/',
        '@core/'        : 'apps/web/src/core/',
    }
    """
    root = Path(scan_result.root)
    alias_map: dict[str, str] = {}

    # Walk all tsconfig.json files (skip node_modules / build dirs)
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
            # Normalise: strip trailing /* or *
            clean_alias = alias.rstrip("/*").rstrip("*")
            clean_target = target.rstrip("/*").rstrip("*").lstrip("./")

            # Resolve target relative to the tsconfig's own directory
            resolved = (tsconfig_dir / clean_target).resolve()
            try:
                repo_rel = str(resolved.relative_to(root))
            except ValueError:
                continue  # outside repo — skip

            alias_key = clean_alias + "/"
            target_val = repo_rel.replace("\\", "/") + "/"

            # Only add if not already defined (first match / most specific wins)
            if alias_key not in alias_map:
                alias_map[alias_key] = target_val

    # Detect NPM Workspaces (monorepos)
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
                        continue # Skip root package.json
                    # For absolute imports like "@meshtastic/sdk-react"
                    alias_map[name] = repo_rel
                    # For sub-path imports like "@meshtastic/sdk-react/src/foo"
                    alias_map[name + "/"] = repo_rel + "/"
                except ValueError:
                    pass
        except Exception:
            pass

    if not alias_map:
        # Heuristic fallback: single top-level source dir
        top_dirs = {Path(f.path).parts[0] for f in scan_result.files if Path(f.path).parts}
        if len(top_dirs) == 1:
            top = list(top_dirs)[0]
            alias_map["@/"] = top + "/"
        else:
            alias_map["@/"] = ""

    return alias_map


def parse_imports(scan_result: ScanResult) -> ParseResult:
    """
    Parse all import statements from scanned files and resolve them
    to concrete file paths within the repository.

    Args:
        scan_result: Output from scan_repo().

    Returns:
        ParseResult containing all resolved ImportRelationships.
    """
    result = ParseResult()

    # Build lookup: relative_path → ScannedFile
    file_index: dict[str, ScannedFile] = {f.path: f for f in scan_result.files}

    # Auto-detect alias map (e.g. @/ → frontend/)
    alias_map = _detect_alias_map(scan_result)

    # Pre-pass for Java: build package map and implicit same-package relationships
    java_packages = {}
    for scanned_file in scan_result.files:
        if scanned_file.extension == ".java":
            try:
                source_code = Path(scanned_file.absolute_path).read_text(encoding="utf-8")
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
                        ImportRelationship(source=source_file, target=target_file, raw_import=f"implicit_package:{pkg}")
                    )

    for scanned_file in scan_result.files:
        try:
            source_code = Path(scanned_file.absolute_path).read_text(encoding="utf-8")
        except Exception:
            continue

        raw_imports = _extract_raw_imports(source_code, scanned_file.extension)

        for raw in raw_imports:
            if _is_external(raw, scanned_file.extension, alias_map):
                result.unresolved.append((scanned_file.path, raw))
                continue

            # Resolve to a candidate path string
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
                    # Relative python import: from .utils import foo
                    # Count leading dots
                    dots = len(raw) - len(raw.lstrip("."))
                    base_dir = Path(scanned_file.path).parent
                    # For every dot beyond the first, go up one directory
                    for _ in range(dots - 1):
                        base_dir = base_dir.parent
                    mod_path = raw.lstrip(".").replace(".", "/")
                    candidate = str(base_dir / mod_path) if mod_path else str(base_dir)
                else:
                    # Absolute python import from root
                    candidate = raw.replace(".", "/")
            else:
                # Node.js
                resolved_alias = _resolve_alias(raw, alias_map)
                if resolved_alias is not None:
                    candidate = resolved_alias
                else:
                    candidate = _resolve_relative(raw, scanned_file.path)

            # Find the actual file in the repo
            matched = _find_file_in_repo(candidate, file_index, scan_result.root, scanned_file.extension)

            if matched:
                result.relationships.append(
                    ImportRelationship(
                        source=scanned_file.path,
                        target=matched,
                        raw_import=raw,
                    )
                )
            else:
                result.unresolved.append((scanned_file.path, raw))

    return result


if __name__ == "__main__":
    import sys
    from scanner import scan_repo

    target = sys.argv[1] if len(sys.argv) > 1 else "."
    scan = scan_repo(target)
    parse = parse_imports(scan)

    print(parse.summary())
