"""
Repository Intelligence Engine
Feature #6: Git-Aware Context

Reads git diff to find what you've changed, then builds a full blast-radius
context package showing every file that depends on your changes — ready for
AI review.
"""

import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class FileReview:
    path: str
    status: str           # "staged", "unstaged", or "staged+unstaged"
    direct_dependents: list[str] = field(default_factory=list)
    transitive_dependents: list[str] = field(default_factory=list)
    test_files: list[str] = field(default_factory=list)


@dataclass
class ReviewContext:
    repo: str
    changed_files: list[FileReview]
    all_affected: list[str]        # union of all dependents, deduped, sorted
    suggested_tests: list[str]     # union of all test files, deduped, sorted
    staged_count: int
    unstaged_count: int


# ---------------------------------------------------------------------------
# Git helpers
# ---------------------------------------------------------------------------

def _run_git(args: list[str], cwd: str) -> list[str]:
    """Run a git command and return non-empty lines of stdout."""
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=15,
        )
        if result.returncode != 0:
            return []
        return [line.strip() for line in result.stdout.splitlines() if line.strip()]
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return []


def _is_git_repo(repo_path: str) -> bool:
    result = subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"],
        cwd=repo_path,
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def get_changed_files(
    repo_path: str,
    include_staged: bool = True,
    include_unstaged: bool = True,
) -> tuple[set[str], set[str]]:
    """
    Returns (staged_files, unstaged_files) as sets of relative paths.
    Only includes files that actually exist on disk (deleted files are excluded).
    """
    staged: set[str] = set()
    unstaged: set[str] = set()

    if include_staged:
        for f in _run_git(["diff", "--cached", "--name-only", "--diff-filter=ACMRT"], repo_path):
            full = Path(repo_path) / f
            if full.exists():
                staged.add(f)

    if include_unstaged:
        for f in _run_git(["diff", "--name-only", "--diff-filter=ACMRT"], repo_path):
            full = Path(repo_path) / f
            if full.exists():
                unstaged.add(f)

    return staged, unstaged


# ---------------------------------------------------------------------------
# Core review engine
# ---------------------------------------------------------------------------

def build_review_context(
    repo_path: str,
    staged: set[str],
    unstaged: set[str],
    repo_graph,
) -> ReviewContext:
    """
    For each changed file, run impact analysis and aggregate into a ReviewContext.
    """
    # Avoid circular import — import here
    from impact_analysis import analyze_impact

    resolved = str(Path(repo_path).resolve())
    all_changed = staged | unstaged

    all_affected: set[str] = set()
    suggested_tests: set[str] = set()
    file_reviews: list[FileReview] = []

    for rel_path in sorted(all_changed):
        # Determine status label
        in_staged = rel_path in staged
        in_unstaged = rel_path in unstaged
        if in_staged and in_unstaged:
            status = "staged+unstaged"
        elif in_staged:
            status = "staged"
        else:
            status = "unstaged"

        # Run impact analysis (may raise ValueError if file not in graph)
        direct: list[str] = []
        transitive: list[str] = []
        tests: list[str] = []
        try:
            report = analyze_impact(rel_path, repo_graph, max_depth=5)
            direct = [f.path for f in report.directly_affected]
            transitive = [f.path for f in report.transitively_affected]
            tests = report.test_files
        except (ValueError, KeyError):
            # File isn't tracked in graph (new file, binary, etc.) — still include it
            pass

        file_reviews.append(FileReview(
            path=rel_path,
            status=status,
            direct_dependents=direct,
            transitive_dependents=transitive,
            test_files=tests,
        ))

        all_affected.update(direct)
        all_affected.update(transitive)
        suggested_tests.update(tests)

    # Don't list changed files as "affected by themselves"
    all_affected -= all_changed
    suggested_tests -= all_changed

    return ReviewContext(
        repo=resolved,
        changed_files=file_reviews,
        all_affected=sorted(all_affected),
        suggested_tests=sorted(suggested_tests),
        staged_count=len(staged),
        unstaged_count=len(unstaged),
    )


# ---------------------------------------------------------------------------
# Output formatters
# ---------------------------------------------------------------------------

def format_review_human(ctx: ReviewContext) -> str:
    BOLD  = "\033[1m"
    DIM   = "\033[2m"
    GREEN = "\033[32m"
    YELLOW= "\033[33m"
    CYAN  = "\033[36m"
    RED   = "\033[31m"
    RESET = "\033[0m"

    total = ctx.staged_count + ctx.unstaged_count
    lines = [
        "",
        f"{BOLD}Repository Intelligence Engine — Git Review{RESET}",
        f"{DIM}{'─' * 60}{RESET}",
        f"  Repo    : {ctx.repo}",
        f"  Changed : {total} file(s)  "
        f"({ctx.staged_count} staged, {ctx.unstaged_count} unstaged)",
        f"{DIM}{'─' * 60}{RESET}",
        "",
    ]

    # Changed files section
    lines.append(f"  {BOLD}CHANGED FILES{RESET}  {DIM}(what you edited){RESET}")
    if not ctx.changed_files:
        lines.append(f"  {DIM}No changed files found.{RESET}")
    for fr in ctx.changed_files:
        label_color = GREEN if fr.status == "staged" else YELLOW if fr.status == "unstaged" else CYAN
        label = f"{label_color}[{fr.status}]{RESET}"
        lines.append(f"  {CYAN}{fr.path}{RESET}  {label}")
    lines.append("")

    # Blast radius section
    lines.append(f"  {BOLD}BLAST RADIUS{RESET}  {DIM}(files that depend on your changes){RESET}")
    if not ctx.all_affected:
        lines.append(f"  {DIM}No dependent files found.{RESET}")
    else:
        for path in ctx.all_affected:
            is_test = any(t in path for t in [".test.", ".spec.", "_test.", "test_"])
            test_badge = f"  {RED}[TEST]{RESET}" if is_test else ""
            lines.append(f"  {DIM}→{RESET} {path}{test_badge}")
    lines.append("")

    # Suggested tests
    lines.append(f"  {BOLD}SUGGESTED TESTS{RESET}  ({len(ctx.suggested_tests)} file(s) to re-run)")
    if not ctx.suggested_tests:
        lines.append(f"  {DIM}No test files identified.{RESET}")
    for t in ctx.suggested_tests:
        lines.append(f"  {RED}→{RESET} {t}")
    lines.append("")

    return "\n".join(lines)


def format_review_json(ctx: ReviewContext) -> str:
    import json
    return json.dumps({
        "repo": ctx.repo,
        "staged_count": ctx.staged_count,
        "unstaged_count": ctx.unstaged_count,
        "changed_files": [
            {
                "path": fr.path,
                "status": fr.status,
                "direct_dependents": fr.direct_dependents,
                "transitive_dependents": fr.transitive_dependents,
                "test_files": fr.test_files,
            }
            for fr in ctx.changed_files
        ],
        "all_affected": ctx.all_affected,
        "suggested_tests": ctx.suggested_tests,
    }, indent=2)
