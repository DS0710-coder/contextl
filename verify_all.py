import sys
import os

sys.path.insert(0, '/home/dev7shah/.nvm/versions/node/v24.15.0/lib/node_modules/contextl/python')
from scanner import scan_repo
from import_parser import parse_imports
from graph_builder import build_graph
from query_engine import query as search_codebase
from impact_analysis import analyze_impact
from dead_code import find_dead_files

repos = {
    "Python (Meshtastic)": ("/home/dev7shah/Desktop/testfiles/python-master./python-master", "node config", "meshtastic/node.py"),
    "TypeScript (Web)": ("/home/dev7shah/Desktop/testfiles/web-main./web-main", "connection status", "apps/web/src/pages/Connections/index.tsx"),
    "Mixed P4A": ("/home/dev7shah/Desktop/testfiles/python-for-android-develop./python-for-android-develop", "build recipe", "pythonforandroid/toolchain.py")
}

for name, (path, query, impact_target) in repos.items():
    print(f"\n======================================")
    print(f"VERIFYING: {name}")
    print(f"======================================")
    
    scan = scan_repo(path)
    print(f"--- 1. SCAN ---")
    print(f"Scanned files: {len(scan.files)}")

    parse = parse_imports(scan)
    rg = build_graph(scan, parse)
    print(f"\n--- 2. PARSE & GRAPH ---")
    print(f"Relationships: {len(parse.relationships)}")
    print(f"Unresolved imports: {len(parse.unresolved)}")

    print(f"\n--- 3. SEARCH ---")
    results = search_codebase(query, rg)
    print(f"Top 3 results for '{query}':")
    for r in results[:3]:
        print(f"  - {r.path} (score: {r.total_score:.3f})")

    print(f"\n--- 4. IMPACT ANALYSIS ---")
    impact = analyze_impact(impact_target, rg)
    print(f"Impact of {os.path.basename(impact_target)}:")
    print(f"  - Directly affected: {len(impact.directly_affected)}")
    print(f"  - Transitively affected: {len(impact.transitively_affected)}")
    print(f"  - Total: {impact.total_affected}")
    print("  Sample of directly affected files:")
    for f in impact.directly_affected[:3]:
        print(f"    - {f.path}")

    print(f"\n--- 5. DEAD CODE ---")
    dead = find_dead_files(rg)
    print(f"Total dead files: {len(dead)}")
    print(f"Sample of dead files:")
    for d in list(dead)[:5]:
        print(f"  - {d}")
