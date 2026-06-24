import sys
import os
import shutil
from pathlib import Path

# Use the globally installed contextl engine as requested
sys.path.insert(0, '/home/dev7shah/.nvm/versions/node/v24.15.0/lib/node_modules/contextl/python')

from scanner import scan_repo
from import_parser import parse_imports
from graph_builder import build_graph
from query_engine import query as search_codebase
from impact_analysis import analyze_impact
from dead_code import find_dead_files
from obsidian_export import export_obsidian_vault

repos = {
    "Java (LibrePlan)": "/home/dev7shah/Desktop/testfiles/libreplan-main./libreplan-main",
    "Python (Meshtastic)": "/home/dev7shah/Desktop/testfiles/python-master./python-master",
    "TypeScript (Web)": "/home/dev7shah/Desktop/testfiles/web-main./web-main",
    "Mixed P4A": "/home/dev7shah/Desktop/testfiles/python-for-android-develop./python-for-android-develop"
}

test_queries = {
    "Java (LibrePlan)": ("login auth", "libreplan-webapp/src/main/java/org/libreplan/web/users/UserCRUDController.java"),
    "Python (Meshtastic)": ("node config", "meshtastic/node.py"),
    "TypeScript (Web)": ("connection status", "apps/web/src/pages/Connections/index.tsx"),
    "Mixed P4A": ("build recipe", "pythonforandroid/toolchain.py")
}

print("Starting Comprehensive Engine Validation...\n")

for lang, path in repos.items():
    print(f"=========================================")
    print(f"Testing {lang}")
    print(f"=========================================")
    
    try:
        # 1. Scan
        scan = scan_repo(path)
        print(f"  ✅ Scan: Found {len(scan.files)} files")
        
        # 2. Parse & Build
        parse = parse_imports(scan)
        rg = build_graph(scan, parse)
        print(f"  ✅ Graph: Built with {len(parse.relationships)} relationships")
        
        # 3. Search
        search_query, impact_target = test_queries[lang]
        results = search_codebase(search_query, rg)
        print(f"  ✅ Search: '{search_query}' returned {len(results)} matches (Top: {results[0].path if results else 'None'})")
        
        # 4. Impact Analysis
        impact_report = analyze_impact(impact_target, rg)
        print(f"  ✅ Impact Analysis: '{os.path.basename(impact_target)}' affects {impact_report.total_affected} downstream files")
        
        # 5. Dead Code
        dead = find_dead_files(rg)
        print(f"  ✅ Dead Code: Found {len(dead)} potentially unused files")
        
        # 6. Obsidian
        vault_path = f"/tmp/obsidian_{lang.replace(' ', '_').replace('(', '').replace(')', '')}"
        if os.path.exists(vault_path):
            shutil.rmtree(vault_path)
        export_obsidian_vault(rg, vault_path)
        print(f"  ✅ Obsidian Export: Successfully generated vault at {vault_path}")
        
    except Exception as e:
        print(f"  ❌ FAILED: {str(e)}")
        
    print("\n")
