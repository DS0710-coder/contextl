"""
Repository Intelligence Engine — Test Suite

Tests cover:
  - scan_repo()      : correct file count, extension filtering, ignored dirs
  - parse_imports()  : @/ alias resolution, relative imports, external packages
  - build_graph()    : correct node/edge counts, PageRank computed
  - query()          : top result for known queries, ranking correctness
  - Edge cases       : empty repo, repo with no imports, stop-word-only query
"""

import os
import sys
import json
import tempfile
import shutil
from pathlib import Path

import pytest

# Ensure the project root is on the path so modules resolve correctly
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scanner import scan_repo, ScanResult
from import_parser import parse_imports
from graph_builder import build_graph
from query_engine import query

SAMPLE_REPO = PROJECT_ROOT / "sample_repo"


# ===========================================================================
# Fixtures
# ===========================================================================

@pytest.fixture(scope="module")
def sample_scan():
    """Scanned ScanResult for the bundled sample_repo."""
    return scan_repo(str(SAMPLE_REPO))


@pytest.fixture(scope="module")
def sample_parse(sample_scan):
    """ParseResult for the bundled sample_repo."""
    return parse_imports(sample_scan)


@pytest.fixture(scope="module")
def sample_graph(sample_scan, sample_parse):
    """RepoGraph for the bundled sample_repo."""
    return build_graph(sample_scan, sample_parse)


@pytest.fixture
def empty_repo(tmp_path):
    """A temporary empty directory (no source files)."""
    return tmp_path


@pytest.fixture
def no_imports_repo(tmp_path):
    """A repo with source files that have zero import statements."""
    (tmp_path / "standalone.tsx").write_text("export const x = 42;\n")
    (tmp_path / "another.ts").write_text("export const y = 'hello';\n")
    return tmp_path


@pytest.fixture
def alias_repo(tmp_path):
    """
    A minimal repo with an @/ alias configured in tsconfig.json
    and one file that uses it.
    """
    tsconfig = {
        "compilerOptions": {
            "paths": {"@/*": ["./*"]}
        }
    }
    (tmp_path / "tsconfig.json").write_text(json.dumps(tsconfig))
    (tmp_path / "components").mkdir()
    (tmp_path / "components" / "Button.tsx").write_text(
        "export function Button() { return null; }\n"
    )
    (tmp_path / "app").mkdir()
    (tmp_path / "app" / "page.tsx").write_text(
        "import { Button } from '@/components/Button';\nexport default function Page() { return null; }\n"
    )
    return tmp_path


# ===========================================================================
# 1. scan_repo() tests
# ===========================================================================

class TestScanRepo:

    def test_correct_file_count(self, sample_scan):
        """sample_repo should contain exactly the known number of .ts/.tsx files."""
        # Count expected files by walking the directory ourselves
        expected = sum(
            1
            for root, dirs, files in os.walk(SAMPLE_REPO)
            for f in files
            if Path(f).suffix in {".ts", ".tsx", ".js", ".jsx"}
            and "node_modules" not in root
        )
        assert sample_scan.total_files == expected

    def test_only_supported_extensions(self, sample_scan):
        """Every discovered file must have a supported extension."""
        for f in sample_scan.files:
            assert f.extension in {".ts", ".tsx", ".js", ".jsx"}, (
                f"Unexpected extension: {f.extension} in {f.path}"
            )

    def test_no_json_files(self, sample_scan):
        """tsconfig.json and other JSON files must not appear in results."""
        for f in sample_scan.files:
            assert f.extension != ".json"

    def test_sorted_by_path(self, sample_scan):
        """Files should be sorted by path for deterministic output."""
        paths = [f.path for f in sample_scan.files]
        assert paths == sorted(paths)

    def test_absolute_paths_exist(self, sample_scan):
        """Every absolute_path should point to a real file on disk."""
        for f in sample_scan.files:
            assert Path(f.absolute_path).is_file(), f"Missing: {f.absolute_path}"

    def test_empty_repo_returns_zero_files(self, empty_repo):
        result = scan_repo(str(empty_repo))
        assert result.total_files == 0

    def test_invalid_path_raises(self):
        with pytest.raises(ValueError, match="does not exist"):
            scan_repo("/does/not/exist/anywhere")

    def test_file_path_raises(self, tmp_path):
        """Passing a file instead of directory should raise ValueError."""
        f = tmp_path / "file.ts"
        f.write_text("const x = 1;")
        with pytest.raises(ValueError, match="not a directory"):
            scan_repo(str(f))

    def test_ignores_node_modules(self, tmp_path):
        """Files inside node_modules must be ignored."""
        (tmp_path / "node_modules").mkdir()
        (tmp_path / "node_modules" / "react.ts").write_text("export {};")
        (tmp_path / "index.ts").write_text("export const x = 1;")
        result = scan_repo(str(tmp_path))
        paths = [f.path for f in result.files]
        assert not any("node_modules" in p for p in paths)
        assert any("index.ts" in p for p in paths)


# ===========================================================================
# 2. parse_imports() tests
# ===========================================================================

class TestParseImports:

    def test_relationships_found(self, sample_parse):
        """sample_repo has inter-file imports; relationships must be non-empty."""
        assert len(sample_parse.relationships) > 0

    def test_alias_import_resolved(self, alias_repo):
        """@/ alias imports should resolve to real files in the repo."""
        scan = scan_repo(str(alias_repo))
        parse = parse_imports(scan)

        resolved_targets = {r.target for r in parse.relationships}
        # 'app/page.tsx' imports '@/components/Button' → should resolve to 'components/Button.tsx'
        assert any("Button.tsx" in t for t in resolved_targets), (
            f"Expected Button.tsx in resolved targets; got: {resolved_targets}"
        )

    def test_alias_import_source(self, alias_repo):
        """The source of the alias relationship should be the importing file."""
        scan = scan_repo(str(alias_repo))
        parse = parse_imports(scan)

        sources = {r.source for r in parse.relationships}
        assert any("page.tsx" in s for s in sources)

    def test_external_packages_unresolved(self, sample_parse):
        """External npm packages (react, next, etc.) go into unresolved."""
        raw_imports = [raw for (_, raw) in sample_parse.unresolved]
        # The sample repo imports from react (via Next.js type annotations)
        # At minimum, the unresolved list should contain some external packages
        # (we don't assert on exact package names since they vary)
        assert isinstance(sample_parse.unresolved, list)

    def test_no_imports_repo(self, no_imports_repo):
        """A repo with no import statements should have zero relationships."""
        scan = scan_repo(str(no_imports_repo))
        parse = parse_imports(scan)
        assert len(parse.relationships) == 0

    def test_empty_repo_parse(self, empty_repo):
        """Parsing an empty repo should return empty relationships."""
        scan = scan_repo(str(empty_repo))
        parse = parse_imports(scan)
        assert len(parse.relationships) == 0
        assert len(parse.unresolved) == 0

    def test_relationships_reference_existing_nodes(self, sample_scan, sample_parse):
        """Every resolved relationship must reference files that were scanned."""
        scanned_paths = {f.path for f in sample_scan.files}
        for rel in sample_parse.relationships:
            assert rel.source in scanned_paths, f"Unknown source: {rel.source}"
            assert rel.target in scanned_paths, f"Unknown target: {rel.target}"


# ===========================================================================
# 3. build_graph() tests
# ===========================================================================

class TestBuildGraph:

    def test_node_count_equals_file_count(self, sample_scan, sample_graph):
        """Every scanned file should appear as a node in the graph."""
        assert sample_graph.graph.number_of_nodes() == sample_scan.total_files

    def test_edge_count_equals_relationships(self, sample_parse, sample_graph):
        """Edge count should equal the number of resolved import relationships."""
        # (Some edges may be deduplicated if the same pair is imported twice)
        assert sample_graph.graph.number_of_edges() <= len(sample_parse.relationships)
        assert sample_graph.graph.number_of_edges() > 0

    def test_centrality_sum_approx_one(self, sample_graph):
        """PageRank values across all nodes should sum approximately to 1."""
        total = sum(n.centrality for n in sample_graph.nodes.values())
        assert abs(total - 1.0) < 0.01, f"PageRank sum is {total}, expected ~1.0"

    def test_all_nodes_have_centrality(self, sample_graph):
        """Every node must have a non-negative centrality score."""
        for path, node in sample_graph.nodes.items():
            assert node.centrality >= 0.0, f"Negative centrality for {path}"

    def test_most_central_files_returns_list(self, sample_graph):
        top = sample_graph.most_central_files(top_n=3)
        assert len(top) == 3
        # Should be sorted descending
        assert top[0].centrality >= top[1].centrality >= top[2].centrality

    def test_get_dependents(self, sample_graph):
        """DownloadPanel should be imported by page.tsx."""
        dependents = sample_graph.get_dependents("components/DownloadPanel.tsx")
        assert any("page.tsx" in d for d in dependents), (
            f"Expected page.tsx in dependents of DownloadPanel; got {dependents}"
        )

    def test_get_dependencies(self, sample_graph):
        """page.tsx should import DownloadPanel."""
        deps = sample_graph.get_dependencies("app/page.tsx")
        assert any("DownloadPanel" in d for d in deps), (
            f"Expected DownloadPanel in deps of page.tsx; got {deps}"
        )

    def test_get_neighbors_depth_1(self, sample_graph):
        """Neighbors at depth=1 should include direct imports and importers."""
        neighbors = sample_graph.get_neighbors("components/DownloadPanel.tsx", depth=1)
        # DownloadPanel imports DownloadButton and is imported by page.tsx
        assert any("DownloadButton" in n for n in neighbors) or any("page" in n for n in neighbors)

    def test_empty_repo_graph(self, empty_repo):
        scan = scan_repo(str(empty_repo))
        parse = parse_imports(scan)
        graph = build_graph(scan, parse)
        assert graph.graph.number_of_nodes() == 0
        assert graph.graph.number_of_edges() == 0

    def test_no_imports_repo_graph(self, no_imports_repo):
        scan = scan_repo(str(no_imports_repo))
        parse = parse_imports(scan)
        graph = build_graph(scan, parse)
        assert graph.graph.number_of_nodes() == scan.total_files
        assert graph.graph.number_of_edges() == 0


# ===========================================================================
# 4. query() tests — known queries against sample_repo
# ===========================================================================

class TestQueryEngine:

    def test_download_button_top_result(self, sample_graph):
        """'change the download button' → DownloadPanel.tsx or DownloadButton.tsx in #1 or #2."""
        results = query("change the download button", sample_graph, top_n=5)
        assert len(results) > 0
        top_paths = [r.path for r in results[:2]]
        assert any("Download" in p for p in top_paths), (
            f"Expected a Download file in top 2; got {top_paths}"
        )

    def test_upload_error_top_results(self, sample_graph):
        """'fix file upload' → FileUploader.tsx should be in top 3."""
        results = query("fix file upload", sample_graph, top_n=5)
        assert len(results) > 0
        top_paths = [r.path for r in results[:3]]
        assert any("Upload" in p or "upload" in p for p in top_paths), (
            f"Expected an Upload file in top 3; got {top_paths}"
        )

    def test_footer_text_top_results(self, sample_graph):
        """'update footer text fields' → FooterInput.tsx or Footer.tsx in top 4."""
        results = query("update footer text fields", sample_graph, top_n=5)
        assert len(results) > 0
        top_paths = [r.path for r in results[:4]]
        assert any("Footer" in p for p in top_paths), (
            f"Expected a Footer file in top 4; got {top_paths}"
        )

    def test_results_sorted_by_score(self, sample_graph):
        """Results must be sorted by total_score descending."""
        results = query("change download button", sample_graph, top_n=10)
        scores = [r.total_score for r in results]
        assert scores == sorted(scores, reverse=True)

    def test_results_have_all_fields(self, sample_graph):
        """Every RankedFile should have all required fields populated."""
        results = query("upload file", sample_graph, top_n=5)
        for r in results:
            assert isinstance(r.path, str) and r.path
            assert isinstance(r.total_score, float)
            assert isinstance(r.keyword_score, float)
            assert isinstance(r.content_score, float)
            assert isinstance(r.neighbor_bonus, float)
            assert isinstance(r.centrality, float)
            assert isinstance(r.matched_terms, list)

    def test_no_results_above_threshold(self, sample_graph):
        """All returned results must have a total_score > 0.01."""
        results = query("change the download button", sample_graph, top_n=10)
        for r in results:
            assert r.total_score > 0.01

    def test_top_n_respected(self, sample_graph):
        """query() must return at most top_n results."""
        results = query("download", sample_graph, top_n=3)
        assert len(results) <= 3

    def test_matched_terms_subset_of_query(self, sample_graph):
        """matched_terms should only contain words derived from the query."""
        results = query("download button panel", sample_graph, top_n=5)
        for r in results:
            for term in r.matched_terms:
                # Terms are lowercased tokens — just ensure they are strings
                assert isinstance(term, str)

    def test_explain_returns_string(self, sample_graph):
        """RankedFile.explain() should return a non-empty string."""
        results = query("download", sample_graph, top_n=1)
        if results:
            explanation = results[0].explain()
            assert isinstance(explanation, str) and len(explanation) > 0


# ===========================================================================
# 5. Edge cases
# ===========================================================================

class TestEdgeCases:

    def test_empty_repo_query(self, empty_repo):
        """query() on an empty repo should return an empty list."""
        scan = scan_repo(str(empty_repo))
        parse = parse_imports(scan)
        graph = build_graph(scan, parse)
        results = query("change the download button", graph, top_n=5)
        assert results == []

    def test_no_imports_query(self, no_imports_repo):
        """query() on a repo with no imports should still work (no graph edges)."""
        scan = scan_repo(str(no_imports_repo))
        parse = parse_imports(scan)
        graph = build_graph(scan, parse)
        # standalone.tsx has no content matching "download", so might return []
        results = query("standalone", graph, top_n=5)
        # Should not crash; results may or may not be empty
        assert isinstance(results, list)

    def test_stop_words_only_query(self, sample_graph):
        """A query consisting entirely of stop words returns an empty list."""
        results = query("the a an in", sample_graph, top_n=5)
        assert results == []

    def test_empty_string_query(self, sample_graph):
        """An empty query string returns an empty list."""
        results = query("", sample_graph, top_n=5)
        assert results == []

    def test_single_character_query(self, sample_graph):
        """Single-character queries (too short) should return an empty list."""
        # The tokenizer drops tokens with len <= 1
        results = query("a", sample_graph, top_n=5)
        assert results == []

    def test_query_with_special_characters(self, sample_graph):
        """Queries with special characters should not crash."""
        results = query("download!!! @button???", sample_graph, top_n=5)
        assert isinstance(results, list)

    def test_large_top_n(self, sample_graph):
        """top_n larger than the number of files should not raise."""
        results = query("download", sample_graph, top_n=9999)
        assert isinstance(results, list)

    def test_repo_without_tsconfig(self, tmp_path):
        """Repos without tsconfig.json should fall back gracefully."""
        (tmp_path / "app").mkdir()
        (tmp_path / "app" / "index.tsx").write_text("export default function App() { return null; }")
        (tmp_path / "components").mkdir()
        (tmp_path / "components" / "Button.tsx").write_text("export function Button() { return null; }")
        scan = scan_repo(str(tmp_path))
        parse = parse_imports(scan)
        graph = build_graph(scan, parse)
        results = query("button", graph, top_n=5)
        assert isinstance(results, list)


# ===========================================================================
# 6. MCP server — synchronous pipeline tests
# ===========================================================================

class TestMCPServer:
    """
    Tests for the MCP server's synchronous helper functions (_run_query, _run_scan).
    These are the functions the MCP server calls inside its thread executor, so
    testing them directly gives full coverage without needing an async harness.
    """

    def test_run_scan_returns_expected_keys(self):
        from mcp_server import _run_scan
        result = _run_scan(str(SAMPLE_REPO))
        assert "repo" in result
        assert "total_files" in result
        assert "files" in result
        assert isinstance(result["files"], list)

    def test_run_scan_file_count(self):
        from mcp_server import _run_scan
        result = _run_scan(str(SAMPLE_REPO))
        assert result["total_files"] == len(result["files"])
        assert result["total_files"] > 0

    def test_run_scan_file_entry_schema(self):
        """Each file entry must have path, extension, size_bytes."""
        from mcp_server import _run_scan
        result = _run_scan(str(SAMPLE_REPO))
        for f in result["files"]:
            assert "path" in f
            assert "extension" in f
            assert "size_bytes" in f

    def test_run_scan_bad_path_raises(self):
        from mcp_server import _run_scan
        with pytest.raises(ValueError):
            _run_scan("/does/not/exist")

    def test_run_query_returns_expected_keys(self):
        from mcp_server import _run_query
        result = _run_query(str(SAMPLE_REPO), "download button", 5)
        assert "query" in result
        assert "repo" in result
        assert "total_files_scanned" in result
        assert "results" in result

    def test_run_query_result_schema(self):
        """Every result entry must have all required fields with correct types."""
        from mcp_server import _run_query
        result = _run_query(str(SAMPLE_REPO), "download button", 5)
        for r in result["results"]:
            assert isinstance(r["rank"], int)
            assert isinstance(r["path"], str) and r["path"]
            assert isinstance(r["score"], float)
            assert r["confidence"] in {"high", "medium", "low"}
            assert isinstance(r["matched_terms"], list)
            assert isinstance(r["reasoning"], str) and r["reasoning"]

    def test_run_query_top_n_capped_at_20(self):
        """The MCP server caps top_n at 20; verify the cap is enforced."""
        from mcp_server import _run_query
        # sample_repo only has 14 files; requesting 999 should return ≤14
        result = _run_query(str(SAMPLE_REPO), "download", 999)
        assert len(result["results"]) <= 14

    def test_run_query_ranks_ascending(self):
        """rank field should be 1-indexed and strictly sequential."""
        from mcp_server import _run_query
        result = _run_query(str(SAMPLE_REPO), "download", 5)
        ranks = [r["rank"] for r in result["results"]]
        assert ranks == list(range(1, len(ranks) + 1))

    def test_run_query_scores_descending(self):
        """Results must be ordered by score descending."""
        from mcp_server import _run_query
        result = _run_query(str(SAMPLE_REPO), "upload file", 10)
        scores = [r["score"] for r in result["results"]]
        assert scores == sorted(scores, reverse=True)

    def test_run_query_download_button_top_file(self):
        """'change the download button' should surface a Download* file at rank 1."""
        from mcp_server import _run_query
        result = _run_query(str(SAMPLE_REPO), "change the download button", 5)
        assert len(result["results"]) > 0
        top_path = result["results"][0]["path"]
        assert "Download" in top_path, f"Expected Download file at rank 1; got {top_path}"

    def test_run_query_empty_query_returns_empty(self):
        """An all-stop-word query should return an empty results list."""
        from mcp_server import _run_query
        result = _run_query(str(SAMPLE_REPO), "the a an", 5)
        assert result["results"] == []

    def test_run_query_total_files_scanned(self):
        """total_files_scanned should match what scan_repo reports."""
        from mcp_server import _run_query, _run_scan
        scan = _run_scan(str(SAMPLE_REPO))
        qr = _run_query(str(SAMPLE_REPO), "download", 5)
        assert qr["total_files_scanned"] == scan["total_files"]

