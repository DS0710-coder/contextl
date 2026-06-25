"""
Tests for tree-sitter import parser and Skeleton Mode.

All fixtures are inline strings — no external files needed.
"""

import sys
import os
import time
import tempfile
import json
from pathlib import Path

import pytest

# Make sure the engine modules are importable
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from import_parser import (
    _extract_raw_imports_ts,
    _TS_AVAILABLE,
    extract_skeleton,
    parse_imports,
    ImportRelationship,
    ParseResult,
)
from scanner import ScanResult, ScannedFile


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def write_fixture(tmp_path: Path, name: str, content: str) -> Path:
    """Write content to a named file in tmp_path, returns the path."""
    p = tmp_path / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return p


def make_scan(root: str, files: list[Path]) -> ScanResult:
    """Construct a minimal ScanResult from a list of absolute paths."""
    root_p = Path(root)
    scanned = []
    for f in files:
        rel = str(f.relative_to(root_p))
        scanned.append(ScannedFile(
            path=rel,
            absolute_path=str(f),
            extension=f.suffix.lower(),
            size_bytes=f.stat().st_size,
        ))
    return ScanResult(root=root, files=sorted(scanned, key=lambda s: s.path))


# ---------------------------------------------------------------------------
# Skip guard
# ---------------------------------------------------------------------------
ts_required = pytest.mark.skipif(
    not _TS_AVAILABLE,
    reason="tree-sitter not installed",
)


# ---------------------------------------------------------------------------
# PART 1: Import extraction tests
# ---------------------------------------------------------------------------

@ts_required
def test_python_imports():
    src = b"""
import os
import sys
from pathlib import Path
from . import utils
from ..models import User
from scanner import ScannedFile, ScanResult
"""
    result = _extract_raw_imports_ts(src, ".py")
    assert "os" in result
    assert "sys" in result
    assert "pathlib" in result
    assert "scanner" in result
    # Relative imports captured
    assert any(r.startswith(".") for r in result), "Expected relative import like '.' or '..models'"


@ts_required
def test_typescript_imports():
    src = b"""
import React from 'react';
import { useState, useEffect } from 'react';
import type { FC } from 'react';
import styles from './App.module.css';
import { Button } from '@/components/Button';
"""
    result = _extract_raw_imports_ts(src, ".ts")
    assert "react" in result
    assert "./App.module.css" in result
    assert "@/components/Button" in result


@ts_required
def test_typescript_require():
    src = b"""
const foo = require('./utils');
const bar = require('lodash');
"""
    result = _extract_raw_imports_ts(src, ".ts")
    assert "./utils" in result
    assert "lodash" in result


@ts_required
def test_tsx_imports():
    src = b"""
import React from 'react';
import { useState } from 'react';
import './styles.css';
export { something } from './other';
"""
    result = _extract_raw_imports_ts(src, ".tsx")
    assert "react" in result
    assert "./other" in result


@ts_required
def test_java_imports():
    src = b"""
package com.example.app;
import java.util.List;
import java.util.HashMap;
import static com.example.Util.method;
"""
    result = _extract_raw_imports_ts(src, ".java")
    assert any("java.util.List" in r for r in result)
    assert any("java.util.HashMap" in r for r in result)


@ts_required
def test_rust_imports():
    src = b"""
use std::collections::HashMap;
use crate::models::{User, Config};
extern crate serde;
"""
    result = _extract_raw_imports_ts(src, ".rs")
    assert any("std" in r for r in result)
    assert "serde" in result


@ts_required
def test_go_imports():
    src = b"""
import (
    "fmt"
    "os"
    alias "github.com/foo/bar"
)
"""
    result = _extract_raw_imports_ts(src, ".go")
    assert "fmt" in result
    assert "os" in result
    assert "github.com/foo/bar" in result


@ts_required
def test_cpp_includes():
    src = b"""
#include <vector>
#include <string>
#include "myheader.h"
#include "utils/helper.h"
"""
    result = _extract_raw_imports_ts(src, ".cpp")
    assert "vector" in result
    assert "string" in result
    assert "myheader.h" in result
    assert "utils/helper.h" in result


def test_unknown_extension():
    """Unknown extensions must return [] without crashing."""
    for ext in (".md", ".json", ".yaml", ".txt", ".toml"):
        result = _extract_raw_imports_ts(b"# nothing here", ext)
        assert result == [], f"Expected [] for {ext}, got {result}"


def test_parse_error_resilience():
    """Malformed/binary content must return [] without raising."""
    garbage = b"\x00\x01\x02\x03" * 100 + b"\xff\xfe"
    for ext in (".py", ".ts", ".java"):
        result = _extract_raw_imports_ts(garbage, ext)
        assert isinstance(result, list), f"Expected list for {ext}"
        # May or may not be empty — but must not raise


# ---------------------------------------------------------------------------
# PART 2: Full pipeline integration tests (parse_imports)
# ---------------------------------------------------------------------------

def test_full_pipeline_python(tmp_path):
    """parse_imports correctly resolves Python relative imports."""
    (tmp_path / "src").mkdir()
    a = tmp_path / "src" / "main.py"
    b = tmp_path / "src" / "utils.py"
    a.write_text("from . import utils\nimport os\n")
    b.write_text("def helper(): pass\n")

    scan = make_scan(str(tmp_path), [a, b])
    result = parse_imports(scan)

    sources = {r.source for r in result.relationships}
    targets = {r.target for r in result.relationships}
    assert "src/utils.py" in targets, f"Expected src/utils.py in targets: {targets}"


def test_full_pipeline_typescript(tmp_path):
    """parse_imports correctly resolves TS relative imports."""
    (tmp_path / "src").mkdir()
    a = tmp_path / "src" / "app.ts"
    b = tmp_path / "src" / "utils.ts"
    a.write_text("import { helper } from './utils';\n")
    b.write_text("export function helper() {}\n")

    scan = make_scan(str(tmp_path), [a, b])
    result = parse_imports(scan)

    targets = {r.target for r in result.relationships}
    assert "src/utils.ts" in targets, f"Expected src/utils.ts in targets: {targets}"


def test_external_packages_unresolved(tmp_path):
    """External npm packages must end up in unresolved, not relationships."""
    (tmp_path / "src").mkdir()
    a = tmp_path / "src" / "app.ts"
    a.write_text("import React from 'react';\nimport axios from 'axios';\n")
    scan = make_scan(str(tmp_path), [a])
    result = parse_imports(scan)

    unresolved_raws = {raw for _, raw in result.unresolved}
    assert "react" in unresolved_raws
    assert "axios" in unresolved_raws


# ---------------------------------------------------------------------------
# PART 3: Skeleton Mode tests
# ---------------------------------------------------------------------------

@ts_required
def test_skeleton_typescript(tmp_path):
    content = """
export class ApiClient {
    private baseUrl: string;

    constructor(url: string) {
        this.baseUrl = url;
    }

    public async fetchUser(userId: string): Promise<User> {
        return fetch(this.baseUrl + '/users/' + userId);
    }

    private log(msg: string): void {
        console.log(msg);
    }
}

export function createClient(config: Config): ApiClient {
    return new ApiClient(config.url);
}
"""
    f = write_fixture(tmp_path, "api.ts", content)
    skel = extract_skeleton(str(f))

    assert skel.get("language") == "typescript"
    assert "error" not in skel

    cls_names = [c["name"] for c in skel["classes"]]
    assert "ApiClient" in cls_names, f"Expected ApiClient in {cls_names}"

    api_cls = next(c for c in skel["classes"] if c["name"] == "ApiClient")
    method_names = [m["name"] for m in api_cls["methods"]]
    assert "fetchUser" in method_names
    assert "log" in method_names

    # Return types
    fetch_method = next(m for m in api_cls["methods"] if m["name"] == "fetchUser")
    assert "Promise" in fetch_method.get("return_type", ""), f"Expected Promise return type, got: {fetch_method}"

    fn_names = [f["name"] for f in skel["functions"]]
    assert "createClient" in fn_names


@ts_required
def test_skeleton_python(tmp_path):
    content = '''
class DataProcessor:
    """Processes data from various sources."""

    def process(self, data: list) -> dict:
        """Process a list of data items."""
        return {}

    def _validate(self, item):
        return True

async def load_data(path: str) -> list:
    """Load data from a file."""
    return []
'''
    f = write_fixture(tmp_path, "processor.py", content)
    skel = extract_skeleton(str(f))

    assert skel.get("language") == "python"
    assert "error" not in skel

    cls_names = [c["name"] for c in skel["classes"]]
    assert "DataProcessor" in cls_names

    dp = next(c for c in skel["classes"] if c["name"] == "DataProcessor")
    method_names = [m["name"] for m in dp["methods"]]
    assert "process" in method_names

    # Docstrings
    assert "DataProcessor" in skel["docstrings"], f"Expected DataProcessor docstring, got: {skel['docstrings']}"
    assert "Processes data" in skel["docstrings"]["DataProcessor"]

    fn_names = [fn["name"] for fn in skel["functions"]]
    assert "load_data" in fn_names


@ts_required
def test_skeleton_rust(tmp_path):
    content = """
pub struct UserRepo {
    db: Database,
    cache: Cache,
}

impl UserRepo {
    pub fn new(db: Database) -> Self {
        UserRepo { db, cache: Cache::default() }
    }

    pub fn find_by_id(&self, id: u64) -> Option<User> {
        self.db.query(id)
    }

    fn internal_helper(&self) {
        // private
    }
}
"""
    f = write_fixture(tmp_path, "repo.rs", content)
    skel = extract_skeleton(str(f))

    assert skel.get("language") == "rust"
    assert "error" not in skel, f"Unexpected error: {skel.get('error')}"

    cls_names = [c["name"] for c in skel["classes"]]
    assert "UserRepo" in cls_names, f"Expected UserRepo in {cls_names}"

    user_repo = next((c for c in skel["classes"] if c["name"] == "UserRepo"), None)
    assert user_repo is not None
    method_names = [m["name"] for m in user_repo.get("methods", [])]
    assert "new" in method_names or "find_by_id" in method_names


@ts_required
def test_skeleton_java(tmp_path):
    content = """
package com.example;

public class UserService {
    private UserRepository repo;

    public UserService(UserRepository repo) {
        this.repo = repo;
    }

    public User findById(Long id) {
        return repo.findById(id);
    }

    private void validate(User user) {
        // validation logic
    }
}
"""
    f = write_fixture(tmp_path, "UserService.java", content)
    skel = extract_skeleton(str(f))

    assert skel.get("language") == "java"
    assert "error" not in skel, f"Unexpected error: {skel.get('error')}"

    cls_names = [c["name"] for c in skel["classes"]]
    assert "UserService" in cls_names


def test_skeleton_unsupported_extension(tmp_path):
    """Unsupported extensions must return gracefully, not crash."""
    f = write_fixture(tmp_path, "readme.md", "# Hello")
    skel = extract_skeleton(str(f))
    assert "file" in skel
    # Should have error or empty structure — but never raise


def test_skeleton_nonexistent_file():
    """Missing file must return error dict, not raise."""
    skel = extract_skeleton("/nonexistent/path/to/file.ts")
    assert "error" in skel
    assert "file" in skel


def test_skeleton_output_is_json_serializable(tmp_path):
    """Skeleton output must be JSON serializable (no Node objects)."""
    content = "class Foo:\n    def bar(self): pass\n"
    f = write_fixture(tmp_path, "foo.py", content)
    skel = extract_skeleton(str(f))
    # Must not raise
    json.dumps(skel)


# ---------------------------------------------------------------------------
# PART 4: Performance test
# ---------------------------------------------------------------------------

@ts_required
def test_performance_typescript(tmp_path):
    """Parse 50 TS files: total import extraction must be under 500ms."""
    ts_content = b"""
import React from 'react';
import { useState, useEffect, useCallback } from 'react';
import { Button } from '@/components/Button';
import { useStore } from './store';
import type { Config } from '../types';

export class Component extends React.Component {
    render() { return null; }
}
"""
    files = []
    for i in range(50):
        p = tmp_path / f"component_{i}.ts"
        p.write_bytes(ts_content)
        files.append(p)

    start = time.perf_counter()
    for f in files:
        _extract_raw_imports_ts(f.read_bytes(), ".ts")
    elapsed_ms = (time.perf_counter() - start) * 1000

    print(f"\n50 TS files parsed in {elapsed_ms:.1f}ms")
    assert elapsed_ms < 500, f"Parsing 50 TS files took {elapsed_ms:.1f}ms — expected < 500ms"


@ts_required
def test_parser_cache_reuse():
    """Calling _get_parser twice for the same extension must return the same object."""
    from import_parser import _get_parser, _PARSERS
    parser1, _ = _get_parser(".ts")
    parser2, _ = _get_parser(".ts")
    assert parser1 is parser2, "Parser objects should be cached and reused"
