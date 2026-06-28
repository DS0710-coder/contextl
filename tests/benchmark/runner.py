import os
import sys
import json
import traceback
from pathlib import Path

sys.path.insert(0, str(Path("../../src").resolve()))
import mcp_server
from impact_analysis import analyze_impact
from standalone import find_standalone_files
from query_engine import query
from import_parser import extract_skeleton
from git_review import build_review_context
from obsidian_export import export_obsidian_vault

REPORT_FILE = Path(__file__).parent / "REPORT.md"
FIXTURES_DIR = Path(__file__).parent / "fixtures"

RESULTS = []

def record(lang: str, feature: str, tool: str, status: str, diff: str = "", severity: str = ""):
    RESULTS.append({
        "lang": lang, "feature": feature, "tool": tool, "status": status,
        "diff": diff, "severity": severity
    })
    print(f"[{status}] {lang} / {feature} / {tool}")

def run_test(lang, feature, tool, func, *args, **kwargs):
    try:
        func(*args, **kwargs)
        record(lang, feature, tool, "PASS")
    except AssertionError as e:
        record(lang, feature, tool, "FAIL", str(e), "Wrong-result")
    except Exception as e:
        record(lang, feature, tool, "CRASH", traceback.format_exc(), "Crash")

def test_language(lang: str, repo_path: str):
    try:
        scan, repo_graph = mcp_server._get_graph(repo_path)
    except Exception as e:
        record(lang, "setup", "graph_builder", "CRASH", str(e), "Crash")
        return

    # find_standalone_files
    def test_standalone():
        dead_files = find_standalone_files(repo_graph)
        dead_base = [Path(p).stem for p in dead_files]
        assert "dead" in dead_base or "Dead" in dead_base, f"dead code not flagged. found: {dead_base}"
        assert "main" not in dead_base and "index" not in dead_base and "Main" not in dead_base, f"entry point incorrectly flagged as dead: {dead_base}"
    run_test(lang, "dead_code_heuristics", "find_standalone_files", test_standalone)

    # get_skeleton
    def test_skeleton():
        monster_file = next((f for f in scan.files if "monster" in f.path.lower()), None)
        if not monster_file: return
        skel = extract_skeleton(os.path.join(repo_path, monster_file.path))
        skel_str = str(skel)
        lines = json.dumps(skel, indent=2).split('\n')
        for line in lines:
            assert len(line) < 200, f"Line too long (implementation leaked): {line[:50]}..."
    run_test(lang, "skeleton_complex", "get_skeleton", test_skeleton)

    # export_obsidian_vault
    def test_obsidian():
        import tempfile
        with tempfile.TemporaryDirectory() as out:
            res = export_obsidian_vault(repo_path, out)
            assert res == out or os.path.exists(res), f"Failed to export: {res}"
            md_files = list(Path(out).rglob("*.md"))
            assert len(md_files) > 0, "No markdown files generated"
    run_test(lang, "vault_generation", "export_obsidian_vault", test_obsidian)

    # analyze_impact
    def test_impact():
        target_a = next((f for f in scan.files if f.path.endswith("a.py") or f.path.endswith("a.ts") or f.path.endswith("a.js") or f.path.endswith("A.java") or f.path.endswith("a.rs") or f.path.endswith("a.go") or f.path.endswith("a.hpp") or f.path.endswith("a.h")), None)
        if target_a:
            impact_a = analyze_impact(target_a.path, repo_graph)
            direct_a = [Path(f.path).stem for f in impact_a.directly_affected]
            # Everyone who imports 'a' is a dependent. For most of these, 'b' or 'Main'/'index' imports 'a'
            assert any(x in direct_a for x in ["main", "index", "Main"]), f"Entry point not in dependents of a. Dependents: {direct_a}"
            assert any(x in direct_a for x in ["b", "B"]), f"Circular 'b' not in dependents of a. Dependents: {direct_a}"
    run_test(lang, "relative_circular", "analyze_impact", test_impact)

    # review_changes
    def test_review():
        target_a = next((f for f in scan.files if f.path.endswith("a.py") or f.path.endswith("a.ts") or f.path.endswith("a.js") or f.path.endswith("A.java") or f.path.endswith("a.rs") or f.path.endswith("a.go") or f.path.endswith("a.hpp") or f.path.endswith("a.h")), None)
        if target_a:
            ctx = build_review_context(repo_path, {target_a.path}, set(), repo_graph)
            # Expect transitive impacts
            assert len(ctx.all_affected) > 0
    run_test(lang, "git_impact", "review_changes", test_review)

def test_adversarial():
    def test_empty_query():
        try:
            mcp_server._run_query(str(FIXTURES_DIR / "python"), "", top_n=10)
        except ValueError:
            pass
    run_test("all", "adversarial", "query_repo", test_empty_query)

def main():
    if not FIXTURES_DIR.exists():
        return
    for lang_dir in FIXTURES_DIR.iterdir():
        if lang_dir.is_dir():
            test_language(lang_dir.name, str(lang_dir))
    
    test_adversarial()

    pass_cnt = sum(1 for r in RESULTS if r["status"] == "PASS")
    fail_cnt = sum(1 for r in RESULTS if r["status"] == "FAIL")
    crash_cnt = sum(1 for r in RESULTS if r["status"] == "CRASH")
    
    import datetime
    now = datetime.datetime.now().isoformat()
    
    existing = ""
    if REPORT_FILE.exists():
        existing = REPORT_FILE.read_text()
        iters = existing.count("## Iteration")
        iter_num = iters + 1
    else:
        iter_num = 1
        existing = "# Benchmark Report\n\n"

    new_report = f"## Iteration {iter_num} - {now}\n\n"
    new_report += f"**Summary:** Total={len(RESULTS)}, PASS={pass_cnt}, FAIL={fail_cnt}, CRASH={crash_cnt}\n\n"
    new_report += "| Language | Feature | Tool | Status | Details |\n"
    new_report += "|---|---|---|---|---|\n"
    
    for r in RESULTS:
        if r["status"] == "PASS":
            new_report += f"| {r['lang']} | {r['feature']} | {r['tool']} | ✅ PASS | - |\n"
        else:
            icon = "❌ FAIL" if r["status"] == "FAIL" else "💥 CRASH"
            diff = r['diff'].replace('\n', '<br>')
            new_report += f"| {r['lang']} | {r['feature']} | {r['tool']} | {icon} | `{diff}` |\n"
            
    REPORT_FILE.write_text(existing + new_report + "\n---\n\n")
    print(f"\nDone Iteration {iter_num}: {pass_cnt} PASS, {fail_cnt} FAIL, {crash_cnt} CRASH")

if __name__ == "__main__":
    main()
