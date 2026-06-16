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
    r"""import\s+(?:type\s+)?          # import or import type
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


def _extract_raw_imports(source_code: str) -> list[str]:
    """Pull all import paths out of a TypeScript/JSX file."""
    paths = []
    for match in IMPORT_PATTERN.finditer(source_code):
        paths.append(match.group(1))
    for match in DYNAMIC_IMPORT_PATTERN.finditer(source_code):
        paths.append(match.group(1))
    return paths


def _is_external(import_path: str) -> bool:
    """Return True if this is an npm package rather than a local file."""
    # Local files start with . (relative) or @ followed by / (alias like @/)
    # but NOT @scope/package style from npm — those don't contain our alias prefix
    if import_path.startswith("./") or import_path.startswith("../"):
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
    Example: source="frontend/app/page.tsx", import="../lib/api" → "frontend/lib/api"
    """
    source_dir = Path(source_file).parent
    resolved = (source_dir / import_path).resolve()
    # Make it relative again (we'll strip the absolute prefix below)
    return str(resolved)


def _find_file_in_repo(
    candidate: str,
    file_index: dict[str, str],
    root: str,
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

    # Try adding each supported extension
    for ext in [".tsx", ".ts", ".jsx", ".js"]:
        with_ext = candidate_str + ext
        if with_ext in file_index:
            return with_ext

    # Try as a directory index file (e.g. components/Button/index.tsx)
    for ext in [".tsx", ".ts", ".jsx", ".js"]:
        index_path = candidate_str + "/index" + ext
        if index_path in file_index:
            return index_path

    return None


def _detect_alias_map(scan_result: ScanResult) -> dict[str, str]:
    """
    Auto-detect the @/ alias by finding tsconfig.json or next.config files
    and inferring the project root. Falls back to a heuristic.
    
    Returns a map like {"@/": "frontend/"} or {"@/": ""}
    """
    root = Path(scan_result.root)

    # Look for tsconfig.json to find paths config
    for tsconfig in root.rglob("tsconfig.json"):
        try:
            import json
            data = json.loads(tsconfig.read_text())
            paths = data.get("compilerOptions", {}).get("paths", {})
            base_url = data.get("compilerOptions", {}).get("baseUrl", ".")

            alias_map = {}
            for alias, targets in paths.items():
                if not targets:
                    continue
                # "@/*": ["./src/*"] → strip trailing /* from both
                clean_alias = alias.rstrip("/*").rstrip("*")
                clean_target = targets[0].rstrip("/*").rstrip("*").lstrip("./")

                tsconfig_dir = tsconfig.parent.relative_to(root)
                prefix = str(tsconfig_dir / clean_target).lstrip("./")
                alias_map[clean_alias + "/"] = prefix + "/" if prefix else ""

            if alias_map:
                return alias_map
        except Exception:
            continue

    # Heuristic fallback: if all files share a common top-level dir, use that
    top_dirs = {Path(f.path).parts[0] for f in scan_result.files if Path(f.path).parts}
    if len(top_dirs) == 1:
        top = list(top_dirs)[0]
        return {"@/": top + "/"}

    return {"@/": ""}


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

    for scanned_file in scan_result.files:
        try:
            source_code = Path(scanned_file.absolute_path).read_text(encoding="utf-8")
        except Exception:
            continue

        raw_imports = _extract_raw_imports(source_code)

        for raw in raw_imports:
            if _is_external(raw):
                result.unresolved.append((scanned_file.path, raw))
                continue

            # Resolve to a candidate path string
            if raw.startswith("@/"):
                resolved_alias = _resolve_alias(raw, alias_map)
                if resolved_alias is None:
                    result.unresolved.append((scanned_file.path, raw))
                    continue
                candidate = resolved_alias
            else:
                # Relative import
                candidate = _resolve_relative(raw, scanned_file.path)

            # Find the actual file in the repo
            matched = _find_file_in_repo(candidate, file_index, scan_result.root)

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
