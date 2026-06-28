"""
Repository Intelligence Engine
Step 7: Standalone Files Analysis

Finds files in the dependency graph that have an in-degree of 0 
(meaning they are never imported by any other file), while filtering 
out standard entry points and test files.
"""

from graph_builder import RepoGraph
from impact_analysis import _is_test_file

# Common entry points that shouldn't be flagged as dead code
# even if nothing explicitly imports them
ENTRY_POINT_MARKERS = {
    "page.tsx", "page.ts", "page.js", "page.jsx",
    "layout.tsx", "layout.ts", "layout.js", "layout.jsx",
    "route.ts", "route.js",
    "globals.css", "global.css", "tailwind.css",
    "index.ts", "index.js", "index.tsx", "index.jsx",
    "main.ts", "main.js", "main.py", "main.go", "main.rs", "main.c", "main.cpp", "main.cc", "main.java",
    "app.ts", "app.js", "app.tsx", "app.jsx", "app.py",
    "mcp_server.py", "server.ts", "server.js", "server.py",
    "__main__.py", "__init__.py", "setup.py", "conftest.py",
    "next.config", "tailwind.config", "postcss.config", "vite.config", "webpack.config"
}

def _is_entry_point(path: str) -> bool:
    lowered = path.lower()
    if lowered.endswith(".d.ts"):
        return True
    for marker in ENTRY_POINT_MARKERS:
        if marker in lowered:
            return True
    return False

def find_standalone_files(repo_graph: RepoGraph) -> list[str]:
    """
    Find files with in-degree 0, excluding entry points and tests.
    """
    standalone_files = []
    
    for path, node in repo_graph.nodes.items():
        if node.in_degree == 0:
            if not _is_test_file(path) and not _is_entry_point(path):
                standalone_files.append(path)
                
    return sorted(standalone_files)

if __name__ == "__main__":
    import sys
    from scanner import scan_repo
    from import_parser import parse_imports
    from graph_builder import build_graph

    if len(sys.argv) < 2:
        print("Usage: python standalone.py <repo_path>")
        sys.exit(1)

    repo_path = sys.argv[1]
    scan = scan_repo(repo_path)
    parse = parse_imports(scan)
    repo_graph = build_graph(scan, parse)

    standalone = find_standalone_files(repo_graph)
    
    print(f"Found {len(standalone)} standalone files:")
    for f in standalone:
        print(f"  - {f}")
