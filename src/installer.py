import os
import json
import platform
import sys
import tempfile
import shutil
from pathlib import Path

def install_mcp():
    home = Path.home()
    system = platform.system()
    
    # Define common MCP configuration paths
    targets = []
    
    # Default to pip/direct invocation if not explicitly set by the npm wrapper
    is_npm = os.environ.get("CONTEXTL_ECOSYSTEM") == "npm"
    
    # 1. Antigravity
    targets.append(home / ".gemini" / "config" / "mcp_config.json")
    
    # 2. Claude Desktop
    if system == "Darwin":
        targets.append(home / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json")
    elif system == "Windows":
        appdata = os.environ.get("APPDATA", "")
        if appdata:
            targets.append(Path(appdata) / "Claude" / "claude_desktop_config.json")
    else:
        # Linux
        targets.append(home / ".config" / "Claude" / "claude_desktop_config.json")
        
    # 3. Cline / Roo (VSCode)
    targets.append(home / "Documents" / "Cline" / "cline_mcp_settings.json")
    if system == "Darwin":
        targets.append(home / "Library" / "Application Support" / "Code" / "User" / "globalStorage" / "rooveterinaryinc.roo-cline" / "settings" / "cline_mcp_settings.json")
    elif system == "Windows":
        appdata = os.environ.get("APPDATA", "")
        if appdata:
            targets.append(Path(appdata) / "Code" / "User" / "globalStorage" / "rooveterinaryinc.roo-cline" / "settings" / "cline_mcp_settings.json")
    else:
        targets.append(home / ".config" / "Code" / "User" / "globalStorage" / "rooveterinaryinc.roo-cline" / "settings" / "cline_mcp_settings.json")
        
    # 4. Cursor
    targets.append(home / ".cursor" / "mcp.json")
    
    # 5. Claude Code
    targets.append(home / ".claude.json")
    
    # 6. Windsurf
    targets.append(home / ".codeium" / "windsurf" / "mcp_config.json")
    
    # 7. VS Code (Workspace level)
    targets.append(Path.cwd() / ".vscode" / "mcp.json")
    
    success_count = 0
    
    for path in targets:
        if path.exists():
            try:
                # Read config
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if not content.strip():
                        config = {}
                    else:
                        config = json.loads(content)
                
                # Ensure mcpServers key exists
                if "mcpServers" not in config:
                    config["mcpServers"] = {}
                
                # Inject contextl
                if is_npm:
                    config["mcpServers"]["contextl"] = {
                        "command": "npx",
                        "args": ["-y", "contextl"]
                    }
                else:
                    config["mcpServers"]["contextl"] = {
                        "command": "contextl",
                        "args": []
                    }
                
                # Backup existing config
                shutil.copy(path, path.with_suffix(path.suffix + ".bak"))
                
                # Write config atomically
                fd, tmp_path = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
                with os.fdopen(fd, "w", encoding="utf-8") as f:
                    json.dump(config, f, indent=2)
                os.replace(tmp_path, path)
                    
                print(f"[SUCCESS] Successfully injected ContextL MCP Server into: {path}")
                success_count += 1
            except Exception as e:
                print(f"[ERROR] Failed to parse or write to {path}: {e}")
                
    if success_count > 0:
        print("\nInstallation successful! Please restart your IDE or AI Client (e.g. reload the window) for the changes to take effect.")
    else:
        print("No supported MCP configuration files were found automatically.")
        print("You may need to manually add the following JSON to your MCP configuration:")
        if is_npm:
            print(json.dumps({
                "mcpServers": {
                    "contextl": {
                        "command": "npx",
                        "args": ["-y", "contextl"]
                    }
                }
            }, indent=2))
        else:
            print(json.dumps({
                "mcpServers": {
                    "contextl": {
                        "command": "contextl",
                        "args": []
                    }
                }
            }, indent=2))
