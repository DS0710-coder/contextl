"""
Repository Intelligence Engine
Step 7: Obsidian Exporter

Exports the RepoGraph into a folder of interconnected Markdown files.
By opening the folder as an Obsidian Vault, users get an instant 3D interactive
visualization of their entire codebase.
"""

import os
import shutil
from pathlib import Path

from scanner import scan_repo
from import_parser import parse_imports
from graph_builder import build_graph, RepoGraph


def export_obsidian_vault(repo_graph: RepoGraph, output_dir: str) -> str:
    """
    Generates a markdown file for every node in the graph, with
    Obsidian wikilinks connecting them based on imports.
    """
    out_path = Path(output_dir).resolve()
    
    # Create the output directory (clean it if it exists)
    if out_path.exists():
        shutil.rmtree(out_path)
    out_path.mkdir(parents=True)

    for path, node in repo_graph.nodes.items():
        # We replace slashes with dashes to keep a flat folder structure
        # so Obsidian graph view looks clean, but keep original name as title
        safe_name = path.replace("/", "-").replace("\\", "-")
        md_file = out_path / f"{safe_name}.md"
        
        dependencies = repo_graph.get_dependencies(path)
        dependents = repo_graph.get_dependents(path)
        
        content = [
            f"# {path}",
            "",
            f"**Extension:** `{node.extension}`",
            f"**Size:** {node.size_bytes} bytes",
            f"**Centrality Score:** {node.centrality:.4f}",
            "",
            "## Imports (Dependencies)",
        ]
        
        if dependencies:
            for dep in sorted(dependencies):
                dep_safe = dep.replace("/", "-").replace("\\", "-")
                content.append(f"- [[{dep_safe}]]")
        else:
            content.append("*No internal imports*")
            
        content.extend([
            "",
            "## Imported By (Dependents)"
        ])
        
        if dependents:
            for dep in sorted(dependents):
                dep_safe = dep.replace("/", "-").replace("\\", "-")
                content.append(f"- [[{dep_safe}]]")
        else:
            content.append("*Not imported by any file*")
            
        md_file.write_text("\n".join(content), encoding="utf-8")
        
    return str(out_path)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python obsidian_export.py <repo_path> <output_dir>")
        sys.exit(1)

    repo_path = sys.argv[1]
    output_dir = sys.argv[2]

    scan = scan_repo(repo_path)
    parse = parse_imports(scan)
    repo_graph = build_graph(scan, parse)

    vault_path = export_obsidian_vault(repo_graph, output_dir)
    print(f"Obsidian Vault successfully generated at: {vault_path}")
    print("Open this folder in Obsidian to view your codebase graph!")
