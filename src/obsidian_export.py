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
from import_parser import parse_imports
from graph_builder import build_graph, RepoGraph


PYTHON_DOCSTRING_PATTERN = re.compile(r'^\s*["\']{3}(.*?)["\']{3}', re.DOTALL)
JS_DOC_PATTERN = re.compile(r'^\s*/\*\*(.*?)\*/', re.DOTALL)

def _extract_explanation(file_path: str, extension: str, root_dir: str) -> str:
    """Reads the top-level docstring or JSDoc block from the file."""
    try:
        content = (Path(root_dir) / file_path).read_text(encoding="utf-8")
        if extension == ".py":
            match = PYTHON_DOCSTRING_PATTERN.search(content)
            if match:
                return match.group(1).strip()
        elif extension in {".ts", ".tsx", ".js", ".jsx", ".java"}:
            match = JS_DOC_PATTERN.search(content)
            if match:
                # Clean up leading asterisks from JSDoc lines
                lines = match.group(1).split('\n')
                cleaned = [line.strip().lstrip('*').strip() for line in lines]
                return "\n".join(cleaned).strip()
    except Exception:
        pass
    return "*No explanation provided in source code.*"


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
        
        explanation = _extract_explanation(path, node.extension, repo_graph.root)
        
        content = [
            f"# {path}",
            "",
            "## Explanation",
            explanation,
            "",
            "## Metrics",
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
