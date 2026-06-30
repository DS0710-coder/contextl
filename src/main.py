"""CLI entry point for the repository intelligence engine."""

import argparse
import json
import sys
import time
from pathlib import Path

from scanner import scan_repo
from import_parser import parse_imports
from graph_builder import build_graph
from query_engine import query, RankedFile


# ---------------------------------------------------------------------------
# Confidence thresholds
# ---------------------------------------------------------------------------
def _confidence(score: float) -> str:
    """Derive a confidence label from the total relevance score."""
    if score > 0.7:
        return "high"
    elif score >= 0.4:
        return "medium"
    else:
        return "low"


# ---------------------------------------------------------------------------
# Reasoning generator
# ---------------------------------------------------------------------------
def _reasoning(ranked: RankedFile, repo_graph) -> str:
    """
    Produce a one-line human-readable explanation of why this file ranked here.
    Uses the score breakdown from RankedFile plus graph context.
    """
    parts = []

    # Filename / path signal
    if ranked.keyword_score >= 0.8:
        parts.append("Filename strongly matches query terms")
    elif ranked.keyword_score >= 0.4:
        parts.append("Filename partially matches query terms")

    # Content signal
    if ranked.content_score >= 0.8:
        parts.append("file contents heavily reference query terms")
    elif ranked.content_score >= 0.4:
        parts.append("file contents mention query terms")

    # Graph context
    if ranked.neighbor_bonus > 0.05:
        try:
            dependents = repo_graph.get_dependents(ranked.path)
            if dependents:
                short_names = [Path(d).name for d in dependents[:2]]
                parts.append(f"imported by {', '.join(short_names)}")
        except Exception:
            pass

    # Centrality signal
    if ranked.centrality > 0.05:
        parts.append("highly connected file in the dependency graph")

    # Terms matched
    if ranked.matched_terms:
        term_str = ", ".join(f'"{t}"' for t in sorted(ranked.matched_terms)[:4])
        parts.append(f"matched terms: {term_str}")

    if not parts:
        return "Low-signal match based on graph proximity"

    return "; ".join(parts).capitalize() + "."


# ---------------------------------------------------------------------------
# Output formatters
# ---------------------------------------------------------------------------
def _format_json(query_str: str, repo_path: str, results: list[RankedFile], repo_graph) -> str:
    """Render results as a clean JSON string."""
    output = {
        "query": query_str,
        "repo": str(Path(repo_path).resolve()),
        "results": [
            {
                "rank": i + 1,
                "path": r.path,
                "score": round(r.total_score, 4),
                "confidence": _confidence(r.total_score),
                "matched_terms": sorted(r.matched_terms),
                "reasoning": _reasoning(r, repo_graph),
            }
            for i, r in enumerate(results)
        ],
    }
    return json.dumps(output, indent=2)


def _format_human(query_str: str, repo_path: str, results: list[RankedFile], repo_graph, elapsed: float) -> str:
    """Render results as styled, human-readable console output."""
    BOLD  = "\033[1m"
    DIM   = "\033[2m"
    GREEN = "\033[32m"
    YELLOW= "\033[33m"
    RED   = "\033[31m"
    CYAN  = "\033[36m"
    RESET = "\033[0m"

    CONF_COLOR = {"high": GREEN, "medium": YELLOW, "low": RED}

    lines = [
        "",
        f"{BOLD}Repository Intelligence Engine{RESET}",
        f"{DIM}{'─' * 60}{RESET}",
        f"  Query : {BOLD}{query_str}{RESET}",
        f"  Repo  : {repo_path}",
        f"  Found : {len(results)} result(s)  {DIM}({elapsed:.2f}s){RESET}",
        f"{DIM}{'─' * 60}{RESET}",
        "",
    ]

    for i, r in enumerate(results, 1):
        conf = _confidence(r.total_score)
        color = CONF_COLOR.get(conf, RESET)
        badge = f"{color}[{conf.upper()}]{RESET}"

        terms = ", ".join(sorted(r.matched_terms)) if r.matched_terms else "—"
        reason = _reasoning(r, repo_graph)

        lines += [
            f"  {BOLD}#{i}{RESET}  {CYAN}{r.path}{RESET}  {badge}",
            f"      Score    : {r.total_score:.4f}  "
            f"(kw={r.keyword_score:.3f} "
            f"content={r.content_score:.3f} "
            f"neighbor={r.neighbor_bonus:.3f} "
            f"pr={r.centrality:.4f})",
            f"      Terms    : {terms}",
            f"      Reason   : {DIM}{reason}{RESET}",
            "",
        ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------
def run_engine(repo_path: str, query_str: str, top_n: int):
    """
    Execute the full pipeline and return (results, repo_graph, elapsed_seconds).
    Raises SystemExit on unrecoverable errors.
    """
    t0 = time.perf_counter()

    try:
        scan = scan_repo(repo_path)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if scan.total_files == 0:
        print("Warning: No source files found in the repository.", file=sys.stderr)

    parse = parse_imports(scan)
    repo_graph = build_graph(scan, parse)
    results = query(query_str, repo_graph, top_n=top_n)

    elapsed = time.perf_counter() - t0
    return results, repo_graph, elapsed


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="contextl",
        description="Repository Intelligence Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # 1. Search
    search_parser = subparsers.add_parser("search", help="Search the codebase using natural language")
    search_parser.add_argument("repo_path", help="Path to the repository root")
    search_parser.add_argument("query", help="Natural-language query (e.g. 'fix the upload error handler')")
    search_parser.add_argument("--top", "-n", type=int, default=5, help="Number of results to return (default: 5)")
    search_parser.add_argument("--json", action="store_true", help="Output clean JSON instead of human-readable text")

    # 2. Standalone Files
    standalone_parser = subparsers.add_parser("standalone", help="Find files with 0 in-degree dependencies (unimported)")
    standalone_parser.add_argument("repo_path", help="Path to the repository root")

    # 3. Impact Analysis
    impact_parser = subparsers.add_parser("impact", help="Analyze the impact of changing a file")
    impact_parser.add_argument("repo_path", help="Path to the repository root")
    impact_parser.add_argument("target_file", help="Relative path to the file being changed")

    # 4. Obsidian Export
    obsidian_parser = subparsers.add_parser("obsidian", help="Export the repository graph to an Obsidian Vault")
    obsidian_parser.add_argument("repo_path", help="Path to the repository root")
    obsidian_parser.add_argument("output_dir", help="Absolute path to save the Obsidian markdown files")

    # 5. Git Review
    review_parser = subparsers.add_parser("review", help="Build AI-ready context from your git changes")
    review_parser.add_argument("repo_path", help="Path to the repository root (must be a git repo)")
    review_parser.add_argument("--staged", action="store_true", help="Only include staged changes")
    review_parser.add_argument("--unstaged", action="store_true", help="Only include unstaged changes")
    review_parser.add_argument("--json", action="store_true", help="Output clean JSON instead of human-readable text")

    # 6. Install MCP Server
    install_parser = subparsers.add_parser("install", help="Automatically install the ContextL MCP server into your AI Client")

    return parser


def main():
    # To maintain backward compatibility with old `contextl <repo> <query>`
    # we manually inject "search" if the first argument isn't a known command.
    if len(sys.argv) >= 2 and sys.argv[1] not in ["search", "standalone", "impact", "obsidian", "review", "install", "-h", "--help"]:
        sys.argv.insert(1, "search")

    parser = build_parser()
    args = parser.parse_args()

    if args.command == "install":
        from installer import install_mcp
        install_mcp()
        sys.exit(0)

    if args.command == "search":
        results, repo_graph, elapsed = run_engine(args.repo_path, args.query, args.top)

        if not results:
            if args.json:
                print(json.dumps({
                    "query": args.query,
                    "repo": str(Path(args.repo_path).resolve()),
                    "results": [],
                }, indent=2))
            else:
                print(f"\nNo relevant files found for: '{args.query}'")
            sys.exit(0)

        if args.json:
            print(_format_json(args.query, args.repo_path, results, repo_graph))
        else:
            print(_format_human(args.query, args.repo_path, results, repo_graph, elapsed))

    elif args.command == "standalone":
        from standalone import find_standalone_files
        scan = scan_repo(args.repo_path)
        parse = parse_imports(scan)
        repo_graph = build_graph(scan, parse)
        standalone = find_standalone_files(repo_graph)
        print(f"Found {len(standalone)} standalone files:")
        for d in sorted(standalone):
            print(f"  {d}")

    elif args.command == "impact":
        from impact_analysis import analyze_impact
        scan = scan_repo(args.repo_path)
        parse = parse_imports(scan)
        repo_graph = build_graph(scan, parse)
        try:
            report = analyze_impact(args.target_file, repo_graph)
            print(report.summary())
            print("\nDependency tree:")
            print(report.to_tree_string())
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    elif args.command == "obsidian":
        from obsidian_export import export_obsidian_vault
        scan = scan_repo(args.repo_path)
        parse = parse_imports(scan)
        repo_graph = build_graph(scan, parse)
        vault_path = export_obsidian_vault(repo_graph, args.output_dir)
        print(f"Obsidian Vault successfully generated at: {vault_path}")
        print("Open this folder in Obsidian to view your codebase graph!")

    elif args.command == "review":
        from git_review import _is_git_repo, get_changed_files, build_review_context, format_review_human, format_review_json

        if not _is_git_repo(args.repo_path):
            print(f"Error: '{args.repo_path}' is not a git repository.", file=sys.stderr)
            sys.exit(1)

        # Default: both staged + unstaged unless a flag is explicitly set
        include_staged   = args.staged or (not args.staged and not args.unstaged)
        include_unstaged = args.unstaged or (not args.staged and not args.unstaged)

        staged, unstaged = get_changed_files(args.repo_path, include_staged, include_unstaged)

        if not staged and not unstaged:
            print("No changed files found. Make some edits and try again.")
            sys.exit(0)

        scan = scan_repo(args.repo_path)
        parse = parse_imports(scan)
        repo_graph = build_graph(scan, parse)
        ctx = build_review_context(args.repo_path, staged, unstaged, repo_graph)

        if args.json:
            print(format_review_json(ctx))
        else:
            print(format_review_human(ctx))


if __name__ == "__main__":
    main()
