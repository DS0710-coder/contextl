"""
Repository Intelligence Engine
CLI Entry Point

Usage:
    python main.py <repo_path> "<query>" [--top N] [--json]

Examples:
    python main.py ./my-next-app "change the download button"
    python main.py ./my-next-app "fix file upload" --top 10
    python main.py ./my-next-app "update footer text" --json
"""

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
        prog="prune",
        description=(
            "Repository Intelligence Engine — find the most relevant files "
            "for a given change request without LLMs or embeddings."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("repo_path", help="Path to the repository root")
    parser.add_argument("query", help="Natural-language query (e.g. 'fix the upload error handler')")
    parser.add_argument(
        "--top", "-n",
        type=int,
        default=5,
        metavar="N",
        help="Number of results to return (default: 5)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        default=False,
        help="Output clean JSON instead of human-readable text",
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

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


if __name__ == "__main__":
    main()
