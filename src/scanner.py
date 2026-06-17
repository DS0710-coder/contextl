"""
Repository Intelligence Engine
Step 1: Repository Scanner

Walks a repository and discovers all relevant source files.
Filters by supported extensions for the MVP (Next.js / React / TypeScript).
"""

import os
from pathlib import Path
from dataclasses import dataclass, field


SUPPORTED_EXTENSIONS = {".tsx", ".ts", ".jsx", ".js"}

IGNORED_DIRS = {
    "node_modules",
    ".git",
    ".next",
    "dist",
    "build",
    ".cache",
    "__pycache__",
    ".turbo",
    "coverage",
}


@dataclass
class ScannedFile:
    """Represents a single discovered file in the repository."""
    path: str           # Relative path from repo root
    absolute_path: str  # Full path on disk
    extension: str      # File extension
    size_bytes: int     # File size


@dataclass
class ScanResult:
    """Result of scanning an entire repository."""
    root: str
    files: list[ScannedFile] = field(default_factory=list)

    @property
    def total_files(self) -> int:
        return len(self.files)

    def summary(self) -> str:
        ext_counts: dict[str, int] = {}
        for f in self.files:
            ext_counts[f.extension] = ext_counts.get(f.extension, 0) + 1

        lines = [
            f"Repository: {self.root}",
            f"Total files: {self.total_files}",
            "",
            "By extension:",
        ]
        for ext, count in sorted(ext_counts.items()):
            lines.append(f"  {ext:8s}  {count} file{'s' if count != 1 else ''}")

        return "\n".join(lines)


def scan_repo(repo_path: str) -> ScanResult:
    """
    Walk the repository at repo_path and return a ScanResult
    containing all discovered source files.

    Args:
        repo_path: Path to the repository root (absolute or relative).

    Returns:
        ScanResult with all discovered files.

    Raises:
        ValueError: If repo_path does not exist or is not a directory.
    """
    root = Path(repo_path).resolve()

    if not root.exists():
        raise ValueError(f"Path does not exist: {root}")
    if not root.is_dir():
        raise ValueError(f"Path is not a directory: {root}")

    result = ScanResult(root=str(root))

    for dirpath, dirnames, filenames in os.walk(root):
        # Prune ignored directories in-place so os.walk skips them
        dirnames[:] = [d for d in dirnames if d not in IGNORED_DIRS]

        for filename in filenames:
            filepath = Path(dirpath) / filename
            ext = filepath.suffix.lower()

            if ext not in SUPPORTED_EXTENSIONS:
                continue

            relative = filepath.relative_to(root)
            result.files.append(
                ScannedFile(
                    path=str(relative),
                    absolute_path=str(filepath),
                    extension=ext,
                    size_bytes=filepath.stat().st_size,
                )
            )

    # Sort by path for deterministic output
    result.files.sort(key=lambda f: f.path)

    return result


if __name__ == "__main__":
    import sys

    target = sys.argv[1] if len(sys.argv) > 1 else "."
    result = scan_repo(target)

    print(result.summary())
    print()
    print("Discovered files:")
    for f in result.files:
        print(f"  {f.path}  ({f.size_bytes} bytes)")
