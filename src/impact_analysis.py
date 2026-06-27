"""
Repository Intelligence Engine
Step 6: Change Impact Analysis

Answers: "If I modify this file, what else is affected?"

Walks the dependency graph upstream (predecessors) from a given file to find
every file that directly or transitively depends on it. Also flags likely
test files so the impact report highlights what needs re-testing.

Pure graph traversal — no LLM, no embeddings. Uses the same RepoGraph
built in graph_builder.py.
"""

from dataclasses import dataclass, field

from scanner import scan_repo
from import_parser import parse_imports
from graph_builder import build_graph, RepoGraph


import re

# Heuristics for detecting test files by path/name
TEST_MARKERS = ("test", "spec", "__tests__", "__mocks__")
_TEST_PATTERN = re.compile(r'\b(?:' + '|'.join(re.escape(m) for m in TEST_MARKERS) + r')\b', re.IGNORECASE)


@dataclass
class ImpactedFile:
    """A single file affected by a change, with its distance from the source."""
    path: str
    distance: int          # 1 = directly imports the changed file, 2 = imports something that does, etc.
    is_test_file: bool
    via: str                # the immediate file that pulled this one in (for tracing the chain)


@dataclass
class ImpactReport:
    """Full result of an impact analysis for one target file."""
    target: str
    directly_affected: list[ImpactedFile] = field(default_factory=list)
    transitively_affected: list[ImpactedFile] = field(default_factory=list)
    test_files: list[str] = field(default_factory=list)
    total_affected: int = 0
    cycle_detected: bool = False
    cycle_members: list[str] = field(default_factory=list)
    risk_score: float = 0.0

    def summary(self) -> str:
        lines = [
            f"Impact analysis for: {self.target}",
            f"Total affected files: {self.total_affected}",
            f"Risk score: {self.risk_score:.1f}",
            "",
        ]

        if self.cycle_detected:
            lines.append("⚠️ WARNING: Circular dependency detected ⚠️")
            lines.append(f"This file is part of a cycle containing {len(self.cycle_members)} files.")
            lines.append("Members: " + ", ".join(self.cycle_members))
            lines.append("")

        if self.directly_affected:
            lines.append("Directly affected (import this file):")
            for f in self.directly_affected:
                marker = "  [test]" if f.is_test_file else ""
                lines.append(f"  {f.path}{marker}")
            lines.append("")

        if self.transitively_affected:
            lines.append("Transitively affected (depend on a direct dependent):")
            for f in self.transitively_affected:
                marker = "  [test]" if f.is_test_file else ""
                lines.append(f"  {f.path}  (via {f.via}, distance {f.distance}){marker}")
            lines.append("")

        if self.test_files:
            lines.append("Suggested tests to run:")
            for t in self.test_files:
                lines.append(f"  {t}")
        else:
            lines.append("No test files found in the impact radius.")

        return "\n".join(lines)

    def to_tree_string(self) -> str:
        """Render as an ASCII dependency tree, similar to `tree` output."""
        lines = [self.target]
        direct = self.directly_affected
        for i, f in enumerate(direct):
            is_last_direct = (i == len(direct) - 1)
            connector = "└──" if is_last_direct else "├──"
            marker = " [test]" if f.is_test_file else ""
            lines.append(f"{connector} {f.path}{marker}")

            # Find transitive files that came via this direct file
            children = [t for t in self.transitively_affected if t.via == f.path]
            for j, child in enumerate(children):
                is_last_child = (j == len(children) - 1)
                prefix = "    " if is_last_direct else "│   "
                child_connector = "└──" if is_last_child else "├──"
                child_marker = " [test]" if child.is_test_file else ""
                lines.append(f"{prefix}{child_connector} {child.path}{child_marker}")

        return "\n".join(lines)


def _is_test_file(path: str) -> bool:
    return bool(_TEST_PATTERN.search(path))


def analyze_impact(
    target_file: str,
    repo_graph: RepoGraph,
    max_depth: int = 5,
) -> ImpactReport:
    """
    Find every file affected by a change to target_file.

    Args:
        target_file: Relative path of the file being changed (must exist in repo_graph.nodes).
        repo_graph:  Built graph from build_graph().
        max_depth:   Maximum number of hops to traverse upstream (default 5).

    Returns:
        ImpactReport listing direct and transitive dependents.

    Raises:
        ValueError: If target_file is not found in the graph.
    """
    if not target_file:
        raise ValueError("target_file cannot be empty")

    if target_file not in repo_graph.nodes:
        raise ValueError(
            f"File not found in repository graph: {target_file}. "
            f"Make sure the path is relative to the repo root."
        )

    report = ImpactReport(target=target_file)

    visited: set[str] = {target_file}
    direct_dependents = repo_graph.get_dependents(target_file)

    # --- Distance 1: direct dependents ---
    frontier: list[tuple[str, str]] = []  # (path, via)
    for dep in direct_dependents:
        if dep in visited:
            continue
        visited.add(dep)
        is_test = _is_test_file(dep)
        report.directly_affected.append(
            ImpactedFile(path=dep, distance=1, is_test_file=is_test, via=target_file)
        )
        if is_test:
            report.test_files.append(dep)
        frontier.append((dep, dep))

    # --- Distance 2+: transitive dependents (BFS upstream) ---
    distance = 2
    while frontier and distance <= max_depth:
        next_frontier: list[tuple[str, str]] = []

        for current_path, origin_direct_file in frontier:
            for dep in repo_graph.get_dependents(current_path):
                if dep in visited:
                    continue
                visited.add(dep)
                is_test = _is_test_file(dep)
                report.transitively_affected.append(
                    ImpactedFile(
                        path=dep,
                        distance=distance,
                        is_test_file=is_test,
                        via=origin_direct_file,  # trace back to the original direct dependent
                    )
                )
                if is_test:
                    report.test_files.append(dep)
                next_frontier.append((dep, origin_direct_file))

        frontier = next_frontier
        distance += 1

    report.total_affected = len(report.directly_affected) + len(report.transitively_affected)

    import networkx as nx
    sccs = [scc for scc in nx.strongly_connected_components(repo_graph.graph) if len(scc) > 1]
    for scc in sccs:
        if target_file in scc:
            report.cycle_detected = True
            report.cycle_members = list(scc)
            break
            
    target_node = repo_graph.nodes.get(target_file)
    in_degree = target_node.in_degree if target_node else 0
    report.risk_score = (in_degree * 0.5) + (len(report.transitively_affected) * 0.2)
    if report.cycle_detected:
        report.risk_score += len(report.cycle_members) * 0.8

    return report


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python impact_analysis.py <repo_path> <target_file>")
        print("Example: python impact_analysis.py ../sample_repo types/files.ts")
        sys.exit(1)

    repo_path = sys.argv[1]
    target = sys.argv[2]

    scan = scan_repo(repo_path)
    parse = parse_imports(scan)
    repo_graph = build_graph(scan, parse)

    report = analyze_impact(target, repo_graph)

    print(report.summary())
    print()
    print("Dependency tree:")
    print(report.to_tree_string())
