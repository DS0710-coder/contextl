"""
Repository Intelligence Engine — Universal MCP Server

Exposes the engine as an MCP (Model Context Protocol) server over stdio.
Works with any MCP-compatible IDE: Cursor, Windsurf, Claude Code, VS Code, etc.

The IDE launches this script automatically when it needs it.
No manual server to keep running.

Usage (the IDE does this for you, but you can test manually):
    python mcp_server.py

Tools exposed:
    query_repo   — rank files by relevance to a natural-language query
    scan_repo    — list all source files the engine can see in a repo
"""

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
                            "Natural-language description of the change you want to make. "
                            "Examples: 'fix the upload error handler', "
                            "'change the login page logo', 'add dark mode to footer'."
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
    asyncio.run(main())
