"""
Repository Intelligence Engine — Universal MCP Server

Exposes the engine as an MCP (Model Context Protocol) server over stdio.
Works with any MCP-compatible IDE: Cursor, Windsurf, Claude Code, VS Code, etc.

The IDE launches this script automatically when it needs it.
No manual server to keep running.

Usage (the IDE does this for you, but you can test manually):
    python mcp_server.py

Tools exposed:
    query_repo      — rank files by relevance to a natural-language query
    scan_repo       — list all source files the engine can see in a repo
    analyze_impact  — find every file affected by changing a target file
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path

import mcp.types as types
from mcp.server import Server
from mcp.server.stdio import stdio_server

# Make sure the engine modules are importable from the same directory
sys.path.insert(0, str(Path(__file__).parent))

from scanner import scan_repo
from import_parser import parse_imports
from graph_builder import build_graph
from query_engine import query as engine_query
from main import _confidence, _reasoning
from impact_analysis import analyze_impact
from dead_code import find_dead_files
from obsidian_export import export_obsidian_vault


# ---------------------------------------------------------------------------
# Server setup
# ---------------------------------------------------------------------------
server = Server("repo-intelligence")


# ---------------------------------------------------------------------------
# Tool definitions
# ---------------------------------------------------------------------------
@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="query_repo",
            description=(
                "Find the most relevant files in a code repository for a given "
                "change request or natural-language query. "
                "Returns a ranked list of files with relevance scores, confidence "
                "levels, matched terms, and a one-line reasoning string. "
                "Use this before editing code to identify exactly which files need "
                "to change — avoids reading irrelevant files."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "repo_path": {
                        "type": "string",
                        "description": "Absolute or relative path to the repository root.",
                    },
                    "query": {
                        "type": "string",
                        "description": (
                            "SYSTEM INSTRUCTION: The contextl search engine is highly optimized for both raw conversational queries AND exact keyword searches. "
                            "It uses dynamic structural multipliers to instantly rank classes for short/conversational queries, and switches to BM25 frequency math for longer keyword queries.\n\n"
                            "STRATEGY INSTRUCTION:\n"
                            "1. INITIAL SEARCHES: Pass the user's raw natural-language query directly. Do NOT convert it to keywords. The engine is smart enough to drop stop-words and find the primary class anchors. Example: 'where is the auth logic?' -> 'where is the auth logic?'\n"
                            "2. TARGETED DEBUG SEARCHES: If the initial search fails, or if you are deep into debugging and need to cross-reference very specific variables across the codebase, then convert the query into highly optimized, space-separated keywords. Example: 'auth failure bug' -> 'login jwt AuthController retry_count token'\n"
                            "Never append generic filler words to targeted searches."
                        ),
                    },
                    "top_n": {
                        "type": "integer",
                        "description": "Maximum number of files to return (default: 5, max: 20).",
                        "default": 5,
                        "minimum": 1,
                        "maximum": 20,
                    },
                },
                "required": ["repo_path", "query"],
            },
        ),
        types.Tool(
            name="scan_repo",
            description=(
                "Scan a repository and list all source files the engine can see. "
                "Useful for understanding the repository structure before querying. "
                "Returns file paths, extensions, and sizes."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "repo_path": {
                        "type": "string",
                        "description": "Absolute or relative path to the repository root.",
                    },
                },
                "required": ["repo_path"],
            },
        ),
        types.Tool(
            name="analyze_impact",
            description=(
                "Find every file affected by changing a specific file. "
                "Walks the dependency graph upstream to find direct and transitive "
                "dependents — files that import the target file, and files that import "
                "those files. Flags likely test files so you know what to re-test. "
                "Use this BEFORE modifying a shared file (types, utils, config) to "
                "understand the blast radius of the change."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "repo_path": {
                        "type": "string",
                        "description": "Absolute or relative path to the repository root.",
                    },
                    "target_file": {
                        "type": "string",
                        "description": (
                            "Path of the file being changed, relative to repo_path. "
                            "Example: 'src/types/index.ts' or 'lib/api.ts'. "
                            "Use scan_repo first if unsure of the exact path."
                        ),
                    },
                    "max_depth": {
                        "type": "integer",
                        "description": "Maximum hops to traverse upstream (default: 5).",
                        "default": 5,
                        "minimum": 1,
                        "maximum": 10,
                    },
                },
                "required": ["repo_path", "target_file"],
            },
        ),
        types.Tool(
            name="find_dead_files",
            description=(
                "Find files in the repository that are never imported by any other file "
                "(in-degree of 0 in the dependency graph). Automatically filters out "
                "standard entry points and test files. Use this to identify dead code "
                "and unused files that can potentially be deleted."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "repo_path": {
                        "type": "string",
                        "description": "Absolute or relative path to the repository root.",
                    },
                },
                "required": ["repo_path"],
            },
        ),
        types.Tool(
            name="export_obsidian_vault",
            description=(
                "Generates an Obsidian Vault from the repository graph. "
                "Creates a folder of interconnected Markdown files using wikilinks "
                "so the codebase can be visualized in Obsidian's 3D graph view."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "repo_path": {
                        "type": "string",
                        "description": "Absolute or relative path to the repository root.",
                    },
                    "output_dir": {
                        "type": "string",
                        "description": "Absolute path to a folder where the vault should be created.",
                    },
                },
                "required": ["repo_path", "output_dir"],
            },
        ),
    ]


# ---------------------------------------------------------------------------
# Tool handlers
# ---------------------------------------------------------------------------
@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[types.TextContent]:

    if name == "query_repo":
        return await _handle_query(arguments)

    if name == "scan_repo":
        return await _handle_scan(arguments)

    if name == "analyze_impact":
        return await _handle_impact(arguments)

    if name == "find_dead_files":
        return await _handle_dead_files(arguments)

    if name == "export_obsidian_vault":
        return await _handle_export_obsidian(arguments)

    return [types.TextContent(
        type="text",
        text=json.dumps({"error": f"Unknown tool: {name}"}),
    )]


async def _handle_query(args: dict) -> list[types.TextContent]:
    repo_path = args.get("repo_path", "")
    query_str = args.get("query", "")
    top_n = min(int(args.get("top_n", 5)), 20)

    # Run the engine (synchronous — wrap in thread to stay async-safe)
    loop = asyncio.get_event_loop()
    try:
        result = await loop.run_in_executor(None, _run_query, repo_path, query_str, top_n)
    except Exception as e:
        result = {"error": str(e), "query": query_str, "repo": repo_path, "results": []}

    return [types.TextContent(type="text", text=json.dumps(result, indent=2))]


def _run_query(repo_path: str, query_str: str, top_n: int) -> dict:
    """Synchronous pipeline — called from a thread executor."""
    scan = scan_repo(repo_path)
    parse = parse_imports(scan)
    repo_graph = build_graph(scan, parse)
    ranked = engine_query(query_str, repo_graph, top_n=top_n)

    return {
        "query": query_str,
        "repo": scan.root,
        "total_files_scanned": scan.total_files,
        "results": [
            {
                "rank": i + 1,
                "path": r.path,
                "score": round(r.total_score, 4),
                "confidence": _confidence(r.total_score),
                "matched_terms": sorted(r.matched_terms),
                "reasoning": _reasoning(r, repo_graph),
            }
            for i, r in enumerate(ranked)
        ],
    }


async def _handle_scan(args: dict) -> list[types.TextContent]:
    repo_path = args.get("repo_path", "")

    loop = asyncio.get_event_loop()
    try:
        result = await loop.run_in_executor(None, _run_scan, repo_path)
    except Exception as e:
        result = {"error": str(e), "repo": repo_path}

    return [types.TextContent(type="text", text=json.dumps(result, indent=2))]


def _run_scan(repo_path: str) -> dict:
    scan = scan_repo(repo_path)
    return {
        "repo": scan.root,
        "total_files": scan.total_files,
        "files": [
            {"path": f.path, "extension": f.extension, "size_bytes": f.size_bytes}
            for f in scan.files
        ],
    }


async def _handle_impact(args: dict) -> list[types.TextContent]:
    repo_path = args.get("repo_path", "")
    target_file = args.get("target_file", "")
    max_depth = min(int(args.get("max_depth", 5)), 10)

    loop = asyncio.get_event_loop()
    try:
        result = await loop.run_in_executor(None, _run_impact, repo_path, target_file, max_depth)
    except Exception as e:
        result = {"error": str(e), "repo": repo_path, "target_file": target_file}

    return [types.TextContent(type="text", text=json.dumps(result, indent=2))]


def _run_impact(repo_path: str, target_file: str, max_depth: int) -> dict:
    """Synchronous pipeline — called from a thread executor."""
    scan = scan_repo(repo_path)
    parse = parse_imports(scan)
    repo_graph = build_graph(scan, parse)
    report = analyze_impact(target_file, repo_graph, max_depth=max_depth)

    return {
        "target_file": report.target,
        "total_affected": report.total_affected,
        "directly_affected": [
            {"path": f.path, "is_test_file": f.is_test_file}
            for f in report.directly_affected
        ],
        "transitively_affected": [
            {
                "path": f.path,
                "distance": f.distance,
                "via": f.via,
                "is_test_file": f.is_test_file,
            }
            for f in report.transitively_affected
        ],
        "suggested_tests": report.test_files,
        "dependency_tree": report.to_tree_string(),
    }


async def _handle_dead_files(args: dict) -> list[types.TextContent]:
    repo_path = args.get("repo_path", "")

    loop = asyncio.get_event_loop()
    try:
        result = await loop.run_in_executor(None, _run_dead_files, repo_path)
    except Exception as e:
        result = {"error": str(e), "repo": repo_path}

    return [types.TextContent(type="text", text=json.dumps(result, indent=2))]


def _run_dead_files(repo_path: str) -> dict:
    """Synchronous pipeline — called from a thread executor."""
    scan = scan_repo(repo_path)
    parse = parse_imports(scan)
    repo_graph = build_graph(scan, parse)
    dead_files = find_dead_files(repo_graph)

    return {
        "repo": scan.root,
        "total_files_scanned": scan.total_files,
        "total_dead_files": len(dead_files),
        "dead_files": dead_files
    }


async def _handle_export_obsidian(args: dict) -> list[types.TextContent]:
    repo_path = args.get("repo_path", "")
    output_dir = args.get("output_dir", "")

    loop = asyncio.get_event_loop()
    try:
        result = await loop.run_in_executor(None, _run_export_obsidian, repo_path, output_dir)
    except Exception as e:
        result = {"error": str(e), "repo": repo_path, "output_dir": output_dir}

    return [types.TextContent(type="text", text=json.dumps(result, indent=2))]


def _run_export_obsidian(repo_path: str, output_dir: str) -> dict:
    """Synchronous pipeline — called from a thread executor."""
    scan = scan_repo(repo_path)
    parse = parse_imports(scan)
    repo_graph = build_graph(scan, parse)
    
    vault_path = export_obsidian_vault(repo_graph, output_dir)
    
    return {
        "repo": scan.root,
        "vault_path": vault_path,
        "total_files_exported": scan.total_files,
        "success": True
    }


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Fallback for CLI users: route all arguments to the main.py CLI engine
        from main import main as cli_main
        try:
            cli_main()
        except KeyboardInterrupt:
            sys.exit(0)
    else:
        asyncio.run(main())
