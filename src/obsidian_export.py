"""
Repository Intelligence Engine
Step 7: Obsidian Exporter

Exports the RepoGraph into a folder of interconnected Markdown files.
By opening the folder as an Obsidian Vault, users get an instant 3D interactive
visualization of their entire codebase.
"""

import os
import shutil
import re
from pathlib import Path

from scanner import scan_repo
from import_parser import parse_imports, extract_skeleton
from graph_builder import build_graph, RepoGraph

def _extract_file_context(file_path: str, extension: str, root_dir: str) -> tuple[str, list[str], str]:
    """Returns (explanation, outline_symbols, snippet)."""
    explanation = "*No explanation provided in source code.*"
    outline = []
    snippet = ""
    abs_path = str(Path(root_dir) / file_path)
    
    try:
        content = Path(abs_path).read_text(encoding="utf-8")
        
        # 1. Snippet (first 20 lines)
        lines = content.splitlines()
        snippet = "\n".join(lines[:20])
        if len(lines) > 20:
            snippet += "\n..."
            
        # 2 & 3. Explanation and Outline from Tree-Sitter
        skeleton = extract_skeleton(abs_path)
        
        if "error" not in skeleton:
            # Grab the first docstring if it exists
            if skeleton["docstrings"]:
                explanation = list(skeleton["docstrings"].values())[0]
                
            # Collect classes and functions
            for cls in skeleton["classes"]:
                outline.append(cls["name"])
            for fn in skeleton["functions"]:
                outline.append(fn["name"])
                
    except Exception:
        pass
        
    return explanation, outline, snippet


def export_obsidian_vault(repo_path: str, output_dir: str) -> str:
    """
    Generates a markdown file for every node in the graph in a hierarchical folder structure, 
    with Obsidian wikilinks connecting them based on imports.
    """
    scan = scan_repo(repo_path)
    parse = parse_imports(scan)
    repo_graph = build_graph(scan, parse)

    out_path = Path(output_dir).resolve()
    
    if out_path.exists():
        shutil.rmtree(out_path)
    out_path.mkdir(parents=True)

    for path, node in repo_graph.nodes.items():
        md_file = out_path / f"{path}.md"
        md_file.parent.mkdir(parents=True, exist_ok=True)
        
        dependencies = repo_graph.get_dependencies(path)
        dependents = repo_graph.get_dependents(path)
        
        explanation, outline, snippet = _extract_file_context(path, node.extension, repo_graph.root)
        
        content = [
            f"# {Path(path).name}",
            "",
            "## Architecture Metrics",
            f"- **Path:** `{path}`",
            f"- **Extension:** `{node.extension}`",
            f"- **Size:** {node.size_bytes} bytes",
            f"- **Centrality Score:** {node.centrality:.4f}",
            f"- **In-Degree (Imported By):** {len(dependents)}",
            f"- **Out-Degree (Imports):** {len(dependencies)}",
            "",
            "## Explanation",
            explanation,
            "",
            "## Structural Outline",
        ]
        
        if outline:
            for symbol in outline:
                content.append(f"- `{symbol}`")
        else:
            content.append("*No major classes or functions detected.*")
            
        content.extend([
            "",
            "## Imports (Dependencies)"
        ])
        
        if dependencies:
            for dep in sorted(dependencies):
                # Use full relative path for accurate linking in hierarchical vaults
                content.append(f"- [[{dep}.md|{dep}]]")
        else:
            content.append("*No internal imports*")
            
        content.extend([
            "",
            "## Imported By (Dependents)"
        ])
        
        if dependents:
            for dep in sorted(dependents):
                content.append(f"- [[{dep}.md|{dep}]]")
        else:
            content.append("*Not imported by any file*")
            
        content.extend([
            "",
            "## Source Code Snippet",
            f"```{node.extension.lstrip('.')}",
            snippet,
            "```"
        ])
            
        md_file.write_text("\n".join(content), encoding="utf-8")
        
    return str(out_path)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python obsidian_export.py <repo_path> <output_dir>")
        sys.exit(1)

    repo_path = sys.argv[1]
    output_dir = sys.argv[2]

    vault_path = export_obsidian_vault(repo_path, output_dir)
    print(f"Obsidian Vault successfully generated at: {vault_path}")
    print("Open this folder in Obsidian to view your codebase graph!")
