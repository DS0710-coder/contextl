import os
import json
import platform
from pathlib import Path

def install_mcp():
    home = Path.home()
    system = platform.system()
    
    # Define common MCP configuration paths
    targets = []
    
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
                config["mcpServers"]["contextl"] = {
                    "command": "npx",
                    "args": ["-y", "contextl"]
                }
                
                # Write config
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(config, f, indent=2)
                    
                print(f"✅ Successfully injected ContextL MCP Server into: {path}")
                success_count += 1
            except Exception as e:
                print(f"❌ Failed to parse or write to {path}: {e}")
                
    if success_count > 0:
        print("\nInstallation successful! Please restart your IDE or AI Client (e.g. reload the window) for the changes to take effect.")
    else:
        print("No supported MCP configuration files were found automatically.")
        print("You may need to manually add the following JSON to your MCP configuration:")
        print(json.dumps({
            "mcpServers": {
                "contextl": {
                    "command": "npx",
                    "args": ["-y", "contextl"]
                }
            }
        }, indent=2))
