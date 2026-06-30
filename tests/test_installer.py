import os
import sys
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

# Adjust sys.path to import installer
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from installer import install_mcp

class TestInstaller(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.home = Path(self.temp_dir.name)
        
        # Create fake config directories
        (self.home / ".gemini" / "config").mkdir(parents=True, exist_ok=True)
        (self.home / ".config" / "Claude").mkdir(parents=True, exist_ok=True)
        (self.home / "Documents" / "Cline").mkdir(parents=True, exist_ok=True)
        (self.home / ".cursor").mkdir(parents=True, exist_ok=True)
        (self.home / ".codeium" / "windsurf").mkdir(parents=True, exist_ok=True)
        (self.home / ".vscode").mkdir(parents=True, exist_ok=True)
        
        # Initial config content with unrelated existing JSON keys
        self.initial_config = {
            "mcpServers": {
                "existing_server": {
                    "command": "foo",
                    "args": ["bar"]
                }
            },
            "unrelated_setting": True
        }
        
        self.config_paths = [
            self.home / ".gemini" / "config" / "mcp_config.json",
            self.home / ".config" / "Claude" / "claude_desktop_config.json",
            self.home / "Documents" / "Cline" / "cline_mcp_settings.json",
            self.home / ".cursor" / "mcp.json",
            self.home / ".claude.json",
            self.home / ".codeium" / "windsurf" / "mcp_config.json",
            self.home / ".vscode" / "mcp.json"
        ]
        
        for path in self.config_paths:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(self.initial_config, f)
                
    def tearDown(self):
        self.temp_dir.cleanup()

    @patch("installer.Path.cwd")
    @patch("installer.Path.home")
    @patch("installer.platform.system")
    @patch.dict(os.environ, {"CONTEXTL_ECOSYSTEM": "pip"}, clear=True)
    def test_pip_ecosystem(self, mock_system, mock_home, mock_cwd):
        mock_home.return_value = self.home
        mock_cwd.return_value = self.home
        mock_system.return_value = "Linux"
        
        # Run installer
        install_mcp(include_vscode_workspace=True)
        
        # Verify JSON
        for path in self.config_paths:
            with open(path, "r", encoding="utf-8") as f:
                config = json.load(f)
                
            self.assertIn("contextl", config["mcpServers"])
            self.assertEqual(config["mcpServers"]["contextl"]["command"], "contextl")
            self.assertEqual(config["mcpServers"]["contextl"]["args"], [])
            # Ensure existing settings are untouched
            self.assertIn("existing_server", config["mcpServers"])
            self.assertTrue(config["unrelated_setting"])
            
            # Verify Backup
            bak_path = path.with_suffix(path.suffix + ".bak")
            self.assertTrue(bak_path.exists())
            with open(bak_path, "r", encoding="utf-8") as bf:
                bak_config = json.load(bf)
            self.assertEqual(bak_config, self.initial_config)

    @patch("installer.Path.cwd")
    @patch("installer.Path.home")
    @patch("installer.platform.system")
    @patch.dict(os.environ, {"CONTEXTL_ECOSYSTEM": "npm"}, clear=True)
    def test_npm_ecosystem(self, mock_system, mock_home, mock_cwd):
        mock_home.return_value = self.home
        mock_cwd.return_value = self.home
        mock_system.return_value = "Linux"
        
        # Run installer
        install_mcp(include_vscode_workspace=True)
        
        # Verify JSON
        for path in self.config_paths:
            with open(path, "r", encoding="utf-8") as f:
                config = json.load(f)
                
            self.assertIn("contextl", config["mcpServers"])
            self.assertEqual(config["mcpServers"]["contextl"]["command"], "npx")
            self.assertEqual(config["mcpServers"]["contextl"]["args"], ["-y", "contextl"])
            self.assertIn("existing_server", config["mcpServers"])
            self.assertTrue(config["unrelated_setting"])

            # Verify Backup
            bak_path = path.with_suffix(path.suffix + ".bak")
            self.assertTrue(bak_path.exists())
            with open(bak_path, "r", encoding="utf-8") as bf:
                bak_config = json.load(bf)
            self.assertEqual(bak_config, self.initial_config)

    @patch("installer.Path.cwd")
    @patch("installer.Path.home")
    @patch("installer.platform.system")
    @patch.dict(os.environ, {}, clear=True)
    def test_direct_invocation_fallback(self, mock_system, mock_home, mock_cwd):
        # Should fallback to pip behavior when CONTEXTL_ECOSYSTEM is unset
        mock_home.return_value = self.home
        mock_cwd.return_value = self.home
        mock_system.return_value = "Linux"
        
        # Run installer
        install_mcp(include_vscode_workspace=True)
        
        # Verify JSON
        for path in self.config_paths:
            with open(path, "r", encoding="utf-8") as f:
                config = json.load(f)
                
            self.assertIn("contextl", config["mcpServers"])
            self.assertEqual(config["mcpServers"]["contextl"]["command"], "contextl")
            self.assertEqual(config["mcpServers"]["contextl"]["args"], [])
            self.assertIn("existing_server", config["mcpServers"])
            self.assertTrue(config["unrelated_setting"])

            # Verify Backup
            bak_path = path.with_suffix(path.suffix + ".bak")
            self.assertTrue(bak_path.exists())
            with open(bak_path, "r", encoding="utf-8") as bf:
                bak_config = json.load(bf)
            self.assertEqual(bak_config, self.initial_config)

if __name__ == "__main__":
    unittest.main()
