import os
import json
from pathlib import Path
from import_parser import extract_skeleton

def test_ts_skeleton():
    src = """
    enum Status {
      Active,
      Inactive,
    }

    enum HttpCode {
      OK = 200,
      NotFound = 404,
    }

    export enum Direction {
      Up = "UP",
      Down = "DOWN",
    }
    
    export enum MyEnum { A = 1, B = 2 }
    export async function* myGenerator() { yield 1; }
    export const MyComponent = () => {};
    export const PI = 3.14;
    """
    
    test_file = Path("test_skeleton_fixture.ts")
    test_file.write_text(src)
    
    try:
        res = extract_skeleton(str(test_file))
        
        # Verify classes
        classes = res.get("classes", [])
        assert len(classes) == 4, f"Expected 4 classes/enums, got {len(classes)}"
        
        status = next((c for c in classes if c["name"] == "Status"), None)
        assert status is not None
        assert len(status["properties"]) == 2
        assert status["properties"][0]["name"] == "Active"
        assert status["properties"][0]["type"] == ""
        
        http_code = next((c for c in classes if c["name"] == "HttpCode"), None)
        assert http_code is not None
        assert len(http_code["properties"]) == 2
        assert http_code["properties"][0]["name"] == "OK"
        assert http_code["properties"][0]["type"] == "200"
        
        direction = next((c for c in classes if c["name"] == "Direction"), None)
        assert direction is not None
        assert len(direction["properties"]) == 2
        assert direction["properties"][0]["name"] == "Up"
        assert direction["properties"][0]["type"] == '"UP"'
        
        # Verify functions
        functions = res.get("functions", [])
        assert len(functions) == 2, f"Expected 2 functions, got {len(functions)}"
        assert functions[0]["name"] == "myGenerator"
        assert functions[0]["is_async"] is True
        assert functions[1]["name"] == "MyComponent"
        
        # Verify exports
        exports = res.get("exports", [])
        assert "Direction" in exports
        assert "MyEnum" in exports
        assert "myGenerator" in exports
        assert "MyComponent" in exports
        assert "PI" in exports
        assert len(exports) == 5, f"Expected 5 exports, got {len(exports)}"
        
        print("All TypeScript skeleton tests passed successfully.")
        
    finally:
        if test_file.exists():
            test_file.unlink()

if __name__ == "__main__":
    # Ensure src is in PYTHONPATH when running directly
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    test_ts_skeleton()
