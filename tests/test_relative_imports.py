from impact_analysis import analyze_impact
from standalone import find_standalone_files
from graph_builder import build_graph
from scanner import scan_repo
from import_parser import parse_imports

import sys
import os
sys.path.insert(0, os.path.abspath('src'))

def test():
    root = "tests/fixtures/bare_relative_py"
    scan = scan_repo(root)
    imports = parse_imports(scan)
    graph = build_graph(scan, imports)

    def check_impact(target, expected_dependent):
        impact = analyze_impact(target, graph)
        direct = [f.path for f in impact.directly_affected]
        assert expected_dependent in direct, f"Failed: {target} did not impact {expected_dependent}, got {direct}"
        print(f"PASS: {target} correctly impacts {expected_dependent}")

    # check impact
    # pkg/a.py imports ..a (which resolves to pkg/a.py?) Wait, does it? Let's check impact of pkg/a.py.
    # Actually wait, `..a` from `pkg/a.py` would be `tests/fixtures/bare_relative_py/a.py` or something.
    
    check_impact("pkg/sub/sibling.py", "pkg/sub/x.py")
    check_impact("pkg/helper.py", "pkg/sub/y.py")
    check_impact("pkg/sub/a.py", "pkg/sub/z.py")
    check_impact("pkg/sub/b.py", "pkg/sub/z.py")
    check_impact("pkg/sub/sibling.py", "pkg/sub/w.py")

    # check standalone
    dead = find_standalone_files(graph)
    for target in [
        "pkg/sub/sibling.py",
        "pkg/helper.py",
        "pkg/sub/a.py",
        "pkg/sub/b.py",
    ]:
        assert target not in dead, f"Failed: {target} falsely marked as dead code"
        print(f"PASS: {target} is correctly not dead code")

    print("ALL REGRESSION TESTS PASSED")

if __name__ == "__main__":
    test()
