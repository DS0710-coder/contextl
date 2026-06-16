"""
Repository Intelligence Engine
Step 3: Graph Builder

Takes the import relationships from the parser and builds a directed graph
where nodes are files and edges are import dependencies.

Adds useful metadata to each node:
  - in_degree:  how many files import this file (how "shared" it is)
  - out_degree: how many files this file imports (how many deps it has)
  - centrality: PageRank score (overall importance in the graph)

Also computes connected clusters so we can understand which files
belong to the same logical feature.
"""

import networkx as nx
from dataclasses import dataclass, field
from pathlib import Path

from scanner import scan_repo
from import_parser import parse_imports, ParseResult


@dataclass
class FileNode:
    """A file in the repository graph with computed metrics."""
    path: str
    extension: str
    size_bytes: int

    # Graph metrics (computed after graph is built)
    in_degree: int = 0        # files that import this
    out_degree: int = 0       # files this imports
    centrality: float = 0.0   # PageRank score


@dataclass
class RepoGraph:
    """
    The complete dependency graph of the repository.
    Wraps a NetworkX DiGraph with helper methods.
    """
    graph: nx.DiGraph
    nodes: dict[str, FileNode]   # path → FileNode
    root: str

    def get_dependents(self, file_path: str) -> list[str]:
        """Files that directly import this file (who uses me?)."""
        return list(self.graph.predecessors(file_path))

    def get_dependencies(self, file_path: str) -> list[str]:
        """Files this file directly imports (what do I use?)."""
        return list(self.graph.successors(file_path))

    def get_neighbors(self, file_path: str, depth: int = 1) -> set[str]:
        """
        All files within `depth` hops of file_path (both directions).
        depth=1 → direct imports + direct importers
        depth=2 → their imports/importers too
        """
        neighbors = set()
        frontier = {file_path}

        for _ in range(depth):
            next_frontier = set()
            for node in frontier:
                next_frontier.update(self.graph.predecessors(node))
                next_frontier.update(self.graph.successors(node))
            new_nodes = next_frontier - neighbors - {file_path}
            neighbors.update(new_nodes)
            frontier = new_nodes

        return neighbors

    def most_central_files(self, top_n: int = 5) -> list[FileNode]:
        """Return the top N files by PageRank centrality."""
        sorted_nodes = sorted(
            self.nodes.values(),
            key=lambda n: n.centrality,
            reverse=True,
        )
        return sorted_nodes[:top_n]

    def summary(self) -> str:
        lines = [
            f"Repository: {self.root}",
            f"Nodes (files):        {self.graph.number_of_nodes()}",
            f"Edges (imports):      {self.graph.number_of_edges()}",
            f"Connected components: {nx.number_weakly_connected_components(self.graph)}",
            "",
            "Most central files (PageRank):",
        ]
        for node in self.most_central_files():
            lines.append(
                f"  {node.centrality:.4f}  {node.path}"
                f"  (imported by {node.in_degree}, imports {node.out_degree})"
            )
        return "\n".join(lines)

    def print_adjacency(self) -> None:
        """Print a human-readable view of the full graph."""
        print("Full dependency graph:")
        for node_path in sorted(self.graph.nodes):
            deps = self.get_dependencies(node_path)
            used_by = self.get_dependents(node_path)
            print(f"\n  {node_path}")
            if deps:
                for d in deps:
                    print(f"    imports  → {d}")
            if used_by:
                for u in used_by:
                    print(f"    used by  ← {u}")


def build_graph(scan_result, parse_result: ParseResult) -> RepoGraph:
    """
    Build a directed dependency graph from scan + parse results.

    Args:
        scan_result:  Output from scan_repo()
        parse_result: Output from parse_imports()

    Returns:
        RepoGraph with computed metrics on every node.
    """
    G = nx.DiGraph()

    # Add all scanned files as nodes
    file_nodes: dict[str, FileNode] = {}
    for f in scan_result.files:
        node = FileNode(
            path=f.path,
            extension=f.extension,
            size_bytes=f.size_bytes,
        )
        file_nodes[f.path] = node
        G.add_node(f.path, **vars(node))

    # Add edges from import relationships
    for rel in parse_result.relationships:
        if rel.source in G and rel.target in G:
            G.add_edge(rel.source, rel.target, raw_import=rel.raw_import)

    # Compute PageRank (importance score)
    try:
        pagerank = nx.pagerank(G, alpha=0.85)
    except nx.PowerIterationFailedConvergence:
        pagerank = {n: 1.0 / len(G.nodes) for n in G.nodes}

    # Attach metrics to each node
    for path, node in file_nodes.items():
        node.in_degree = G.in_degree(path)
        node.out_degree = G.out_degree(path)
        node.centrality = pagerank.get(path, 0.0)

    return RepoGraph(graph=G, nodes=file_nodes, root=scan_result.root)


if __name__ == "__main__":
    import sys

    target = sys.argv[1] if len(sys.argv) > 1 else "."

    scan = scan_repo(target)
    parse = parse_imports(scan)
    repo_graph = build_graph(scan, parse)

    print(repo_graph.summary())
    print()
    repo_graph.print_adjacency()
