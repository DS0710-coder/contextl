# Benchmark Report

## Iteration 1 - 2026-06-28T12:29:36.410894

**Summary:** Total=12, PASS=6, FAIL=2, CRASH=4

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| python | query_invariants | query_repo | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 31, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 45, in test_query<br>    res1 = query(repo_path, "monster", max_results=10)<br>TypeError: query() got an unexpected keyword argument 'max_results'<br>` |
| python | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 31, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 80, in test_standalone<br>    dead_files = [f.path for f in find_standalone_files(repo_graph, scan)]<br>                                  ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^<br>TypeError: find_standalone_files() takes 1 positional argument but 2 were given<br>` |
| python | skeleton_complex | get_skeleton | ❌ FAIL | `Decorator missing` |
| typescript | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 31, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 113, in test_standalone<br>    dead_files = [f.path for f in find_standalone_files(repo_graph, scan)]<br>                                  ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^<br>TypeError: find_standalone_files() takes 1 positional argument but 2 were given<br>` |
| javascript | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| java | relative_circular_barrel | analyze_impact | ❌ FAIL | `Main.java missing` |
| rust | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| go | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| cpp | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| all | adversarial | query_repo | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 31, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 168, in test_empty_query<br>    mcp_server._query(str(FIXTURES_DIR / "python"), "")<br>    ^^^^^^^^^^^^^^^^^<br>AttributeError: module 'mcp_server' has no attribute '_query'<br>` |

---

## Iteration 2 - 2026-06-28T12:30:30.660456

**Summary:** Total=12, PASS=8, FAIL=2, CRASH=2

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| python | query_invariants | query_repo | ✅ PASS | - |
| python | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 31, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 80, in test_standalone<br>    dead_files = [f.path for f in find_standalone_files(repo_graph)]<br>                  ^^^^^^<br>AttributeError: 'str' object has no attribute 'path'<br>` |
| python | skeleton_complex | get_skeleton | ❌ FAIL | `Decorator missing` |
| typescript | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 31, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 113, in test_standalone<br>    dead_files = [f.path for f in find_standalone_files(repo_graph)]<br>                  ^^^^^^<br>AttributeError: 'str' object has no attribute 'path'<br>` |
| javascript | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| java | relative_circular_barrel | analyze_impact | ❌ FAIL | `Main.java missing` |
| rust | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| go | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| cpp | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| all | adversarial | query_repo | ✅ PASS | - |

---

## Iteration 3 - 2026-06-28T12:30:52.017267

**Summary:** Total=12, PASS=10, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| python | query_invariants | query_repo | ✅ PASS | - |
| python | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ❌ FAIL | `Decorator missing` |
| typescript | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| java | relative_circular_barrel | analyze_impact | ❌ FAIL | `Main.java missing` |
| rust | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| go | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| cpp | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| all | adversarial | query_repo | ✅ PASS | - |

---

## Iteration 4 - 2026-06-28T12:33:44.181188

**Summary:** Total=12, PASS=11, FAIL=1, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| python | query_invariants | query_repo | ✅ PASS | - |
| python | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ❌ FAIL | `Nested doc missing` |
| typescript | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| java | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| rust | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| go | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| cpp | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| all | adversarial | query_repo | ✅ PASS | - |

---

## Iteration 5 - 2026-06-28T12:34:22.886957

**Summary:** Total=12, PASS=12, FAIL=0, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| python | query_invariants | query_repo | ✅ PASS | - |
| python | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| java | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| rust | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| go | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| cpp | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| all | adversarial | query_repo | ✅ PASS | - |

---

## Iteration 6 - 2026-06-28T12:34:31.197354

**Summary:** Total=12, PASS=12, FAIL=0, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| python | query_invariants | query_repo | ✅ PASS | - |
| python | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| java | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| rust | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| go | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| cpp | relative_circular_barrel | analyze_impact | ✅ PASS | - |
| all | adversarial | query_repo | ✅ PASS | - |

---

## Iteration 7 - 2026-06-28T12:35:10.618763

**Summary:** Total=41, PASS=22, FAIL=11, CRASH=8

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: []` |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ❌ FAIL | `Failed to export` |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 30, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 90, in test_review<br>    assert len(ctx.get("direct_impacts", [])) > 0<br>               ^^^^^^^<br>AttributeError: 'ReviewContext' object has no attribute 'get'<br>` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ❌ FAIL | `Failed to export` |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 30, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 90, in test_review<br>    assert len(ctx.get("direct_impacts", [])) > 0<br>               ^^^^^^^<br>AttributeError: 'ReviewContext' object has no attribute 'get'<br>` |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ❌ FAIL | `Failed to export` |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 30, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 90, in test_review<br>    assert len(ctx.get("direct_impacts", [])) > 0<br>               ^^^^^^^<br>AttributeError: 'ReviewContext' object has no attribute 'get'<br>` |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ❌ FAIL | `Failed to export` |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 30, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 90, in test_review<br>    assert len(ctx.get("direct_impacts", [])) > 0<br>               ^^^^^^^<br>AttributeError: 'ReviewContext' object has no attribute 'get'<br>` |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ❌ FAIL | `Failed to export` |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 30, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 90, in test_review<br>    assert len(ctx.get("direct_impacts", [])) > 0<br>               ^^^^^^^<br>AttributeError: 'ReviewContext' object has no attribute 'get'<br>` |
| rust | dead_code_heuristics | find_standalone_files | ❌ FAIL | `entry point incorrectly flagged as dead: ['dead', 'fastest', 'main', 'monster', 'my file', 'mod', 'mod', 'x']` |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ❌ FAIL | `Failed to export` |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 30, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 90, in test_review<br>    assert len(ctx.get("direct_impacts", [])) > 0<br>               ^^^^^^^<br>AttributeError: 'ReviewContext' object has no attribute 'get'<br>` |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ❌ FAIL | `Failed to export` |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 30, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 90, in test_review<br>    assert len(ctx.get("direct_impacts", [])) > 0<br>               ^^^^^^^<br>AttributeError: 'ReviewContext' object has no attribute 'get'<br>` |
| go | dead_code_heuristics | find_standalone_files | ❌ FAIL | `entry point incorrectly flagged as dead: ['main', 'contest', 'dead', 'monster', 'my file', 'x']` |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ❌ FAIL | `Failed to export` |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 30, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 90, in test_review<br>    assert len(ctx.get("direct_impacts", [])) > 0<br>               ^^^^^^^<br>AttributeError: 'ReviewContext' object has no attribute 'get'<br>` |
| all | adversarial | query_repo | ✅ PASS | - |

---

## Iteration 8 - 2026-06-28T12:36:57.638039

**Summary:** Total=41, PASS=33, FAIL=0, CRASH=8

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 30, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 90, in test_review<br>    assert len(ctx.direct_impacts) > 0<br>               ^^^^^^^^^^^^^^^^^^<br>AttributeError: 'ReviewContext' object has no attribute 'direct_impacts'<br>` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 30, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 90, in test_review<br>    assert len(ctx.direct_impacts) > 0<br>               ^^^^^^^^^^^^^^^^^^<br>AttributeError: 'ReviewContext' object has no attribute 'direct_impacts'<br>` |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 30, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 90, in test_review<br>    assert len(ctx.direct_impacts) > 0<br>               ^^^^^^^^^^^^^^^^^^<br>AttributeError: 'ReviewContext' object has no attribute 'direct_impacts'<br>` |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 30, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 90, in test_review<br>    assert len(ctx.direct_impacts) > 0<br>               ^^^^^^^^^^^^^^^^^^<br>AttributeError: 'ReviewContext' object has no attribute 'direct_impacts'<br>` |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 30, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 90, in test_review<br>    assert len(ctx.direct_impacts) > 0<br>               ^^^^^^^^^^^^^^^^^^<br>AttributeError: 'ReviewContext' object has no attribute 'direct_impacts'<br>` |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 30, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 90, in test_review<br>    assert len(ctx.direct_impacts) > 0<br>               ^^^^^^^^^^^^^^^^^^<br>AttributeError: 'ReviewContext' object has no attribute 'direct_impacts'<br>` |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 30, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 90, in test_review<br>    assert len(ctx.direct_impacts) > 0<br>               ^^^^^^^^^^^^^^^^^^<br>AttributeError: 'ReviewContext' object has no attribute 'direct_impacts'<br>` |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | 💥 CRASH | `Traceback (most recent call last):<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 30, in run_test<br>    func(*args, **kwargs)<br>    ~~~~^^^^^^^^^^^^^^^^^<br>  File "/home/dev7shah/Desktop/contextl/tests/benchmark/runner.py", line 90, in test_review<br>    assert len(ctx.direct_impacts) > 0<br>               ^^^^^^^^^^^^^^^^^^<br>AttributeError: 'ReviewContext' object has no attribute 'direct_impacts'<br>` |
| all | adversarial | query_repo | ✅ PASS | - |

---

## Iteration 9 - 2026-06-28T12:37:23.162032

**Summary:** Total=41, PASS=41, FAIL=0, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| all | adversarial | query_repo | ✅ PASS | - |

---

## Iteration 10 - 2026-06-28T12:37:32.189270

**Summary:** Total=41, PASS=41, FAIL=0, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| all | adversarial | query_repo | ✅ PASS | - |

---

## Iteration 11 - 2026-06-28T12:39:14.632515

**Summary:** Total=41, PASS=41, FAIL=0, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| all | adversarial | query_repo | ✅ PASS | - |

---

## Iteration 12 - 2026-06-28T12:39:24.454114

**Summary:** Total=41, PASS=41, FAIL=0, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| all | adversarial | query_repo | ✅ PASS | - |

---

## Iteration 13 - 2026-06-28T13:19:36.485340

**Summary:** Total=48, PASS=40, FAIL=8, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ❌ FAIL | `Duplicate term inflated score: 6.9641674469339625 != 8.62194966168321` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ❌ FAIL | `Duplicate term inflated score: 4.406140875910195 != 7.5031168982298215` |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ❌ FAIL | `Duplicate term inflated score: 5.451666276783747 != 9.590535215404316` |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ❌ FAIL | `Duplicate term inflated score: 6.503370720883376 != 10.461013748956228` |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ❌ FAIL | `Duplicate term inflated score: 4.322057974310681 != 7.451561703154505` |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ❌ FAIL | `Duplicate term inflated score: 4.674100740410421 != 8.427449855271199` |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ❌ FAIL | `Duplicate term inflated score: 4.3219228666151555 != 7.451478862250273` |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ❌ FAIL | `Duplicate term inflated score: 5.5026372056601724 != 8.175508935877568` |

---

## Iteration 14 - 2026-06-28T13:19:45.959358

**Summary:** Total=48, PASS=40, FAIL=8, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ❌ FAIL | `Empty query in MCP handler did not raise ValueError` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ❌ FAIL | `Empty query in MCP handler did not raise ValueError` |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ❌ FAIL | `Empty query in MCP handler did not raise ValueError` |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ❌ FAIL | `Empty query in MCP handler did not raise ValueError` |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ❌ FAIL | `Empty query in MCP handler did not raise ValueError` |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ❌ FAIL | `Empty query in MCP handler did not raise ValueError` |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ❌ FAIL | `Empty query in MCP handler did not raise ValueError` |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ❌ FAIL | `Empty query in MCP handler did not raise ValueError` |

---

## Iteration 15 - 2026-06-28T13:20:16.209144

**Summary:** Total=48, PASS=48, FAIL=0, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 16 - 2026-06-28T13:20:24.803791

**Summary:** Total=48, PASS=48, FAIL=0, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 17 - 2026-06-29T02:14:34.866210

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 18 - 2026-06-29T02:14:36.731887

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 19 - 2026-06-29T02:14:38.694802

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 20 - 2026-06-29T02:14:40.533154

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 21 - 2026-06-29T02:14:42.323663

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 22 - 2026-06-29T02:14:44.284003

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 23 - 2026-06-29T02:14:46.144756

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 24 - 2026-06-29T02:14:47.880072

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 25 - 2026-06-29T02:14:49.800466

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 26 - 2026-06-29T02:14:51.573379

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 27 - 2026-06-29T02:14:53.449730

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 28 - 2026-06-29T02:14:55.256645

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 29 - 2026-06-29T02:14:56.999413

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 30 - 2026-06-29T02:14:58.954796

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 31 - 2026-06-29T02:15:00.708550

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 32 - 2026-06-29T02:15:02.640243

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 33 - 2026-06-29T02:15:04.638083

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 34 - 2026-06-29T02:15:06.439766

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 35 - 2026-06-29T02:15:08.307337

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 36 - 2026-06-29T02:15:10.252880

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 37 - 2026-06-29T02:15:12.286853

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 38 - 2026-06-29T02:15:14.240306

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 39 - 2026-06-29T02:15:16.117044

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 40 - 2026-06-29T02:15:18.058280

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 41 - 2026-06-29T02:15:19.876990

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 42 - 2026-06-29T02:15:22.003144

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 43 - 2026-06-29T02:15:23.963438

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 44 - 2026-06-29T02:15:26.046758

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 45 - 2026-06-29T02:15:27.940664

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 46 - 2026-06-29T02:15:29.948646

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 47 - 2026-06-29T02:15:31.873575

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 48 - 2026-06-29T02:15:33.919774

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 49 - 2026-06-29T02:15:35.914812

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 50 - 2026-06-29T02:15:37.835281

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 51 - 2026-06-29T02:15:39.976759

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 52 - 2026-06-29T02:15:41.900246

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 53 - 2026-06-29T02:15:43.733784

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 54 - 2026-06-29T02:15:45.919855

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 55 - 2026-06-29T02:15:48.123333

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 56 - 2026-06-29T02:15:50.203178

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 57 - 2026-06-29T02:15:52.069191

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 58 - 2026-06-29T02:15:53.937617

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 59 - 2026-06-29T02:15:55.765249

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 60 - 2026-06-29T02:15:57.543874

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 61 - 2026-06-29T02:15:59.425310

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 62 - 2026-06-29T02:16:01.359164

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 63 - 2026-06-29T02:16:03.136444

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 64 - 2026-06-29T02:16:04.937374

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 65 - 2026-06-29T02:16:06.762586

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

## Iteration 66 - 2026-06-29T02:16:08.632424

**Summary:** Total=54, PASS=52, FAIL=2, CRASH=0

| Language | Feature | Tool | Status | Details |
|---|---|---|---|---|
| java | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| java | skeleton_complex | get_skeleton | ✅ PASS | - |
| java | vault_generation | export_obsidian_vault | ✅ PASS | - |
| java | relative_circular | analyze_impact | ✅ PASS | - |
| java | git_impact | review_changes | ✅ PASS | - |
| java | search_quality | query_repo | ✅ PASS | - |
| git_test | dead_code_heuristics | find_standalone_files | ❌ FAIL | `dead code not flagged. found: ['file1', 'file2']` |
| git_test | skeleton_complex | get_skeleton | ✅ PASS | - |
| git_test | vault_generation | export_obsidian_vault | ✅ PASS | - |
| git_test | relative_circular | analyze_impact | ✅ PASS | - |
| git_test | git_impact | review_changes | ✅ PASS | - |
| git_test | search_quality | query_repo | ❌ FAIL | `monster file not found in results for 'monster'` |
| javascript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| javascript | skeleton_complex | get_skeleton | ✅ PASS | - |
| javascript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| javascript | relative_circular | analyze_impact | ✅ PASS | - |
| javascript | git_impact | review_changes | ✅ PASS | - |
| javascript | search_quality | query_repo | ✅ PASS | - |
| typescript | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| typescript | skeleton_complex | get_skeleton | ✅ PASS | - |
| typescript | vault_generation | export_obsidian_vault | ✅ PASS | - |
| typescript | relative_circular | analyze_impact | ✅ PASS | - |
| typescript | git_impact | review_changes | ✅ PASS | - |
| typescript | search_quality | query_repo | ✅ PASS | - |
| python | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| python | skeleton_complex | get_skeleton | ✅ PASS | - |
| python | vault_generation | export_obsidian_vault | ✅ PASS | - |
| python | relative_circular | analyze_impact | ✅ PASS | - |
| python | git_impact | review_changes | ✅ PASS | - |
| python | search_quality | query_repo | ✅ PASS | - |
| c | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| c | skeleton_complex | get_skeleton | ✅ PASS | - |
| c | vault_generation | export_obsidian_vault | ✅ PASS | - |
| c | relative_circular | analyze_impact | ✅ PASS | - |
| c | git_impact | review_changes | ✅ PASS | - |
| c | search_quality | query_repo | ✅ PASS | - |
| rust | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| rust | skeleton_complex | get_skeleton | ✅ PASS | - |
| rust | vault_generation | export_obsidian_vault | ✅ PASS | - |
| rust | relative_circular | analyze_impact | ✅ PASS | - |
| rust | git_impact | review_changes | ✅ PASS | - |
| rust | search_quality | query_repo | ✅ PASS | - |
| cpp | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| cpp | skeleton_complex | get_skeleton | ✅ PASS | - |
| cpp | vault_generation | export_obsidian_vault | ✅ PASS | - |
| cpp | relative_circular | analyze_impact | ✅ PASS | - |
| cpp | git_impact | review_changes | ✅ PASS | - |
| cpp | search_quality | query_repo | ✅ PASS | - |
| go | dead_code_heuristics | find_standalone_files | ✅ PASS | - |
| go | skeleton_complex | get_skeleton | ✅ PASS | - |
| go | vault_generation | export_obsidian_vault | ✅ PASS | - |
| go | relative_circular | analyze_impact | ✅ PASS | - |
| go | git_impact | review_changes | ✅ PASS | - |
| go | search_quality | query_repo | ✅ PASS | - |

---

