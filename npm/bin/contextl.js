#!/usr/bin/env node
/**
 * contextl — npm entry point
 *
 * Locates a suitable Python 3.9+ interpreter, ensures `networkx` and `mcp`
 * are importable (installs them via pip if missing), then spawns mcp_server.py
 * with stdio inherited so any MCP-compatible IDE can talk to it directly.
 *
 * No npm runtime dependencies — only Node.js built-ins.
 */

"use strict";

const { execSync, spawn } = require("child_process");
const path = require("path");
const fs = require("fs");

// ---------------------------------------------------------------------------
// Paths
// ---------------------------------------------------------------------------

/** Directory containing the bundled Python engine files. */
const PYTHON_DIR = path.resolve(__dirname, "..", "python");

/** The MCP server entry point. */
const MCP_SERVER = path.join(PYTHON_DIR, "mcp_server.py");

// ---------------------------------------------------------------------------
// Python discovery
// ---------------------------------------------------------------------------

/**
 * Try to find a Python 3.9+ interpreter.
 * Tries the candidates in order; returns the first one that works.
 * Throws if none is found.
 */
function findPython() {
  const candidates = ["python3", "python", "python3.13", "python3.12", "python3.11", "python3.10", "python3.9"];

  for (const cmd of candidates) {
    try {
      const raw = execSync(
        `${cmd} -c "import sys; print(sys.version_info.major, sys.version_info.minor)"`,
        { stdio: ["pipe", "pipe", "pipe"], timeout: 5000 }
      ).toString().trim();

      const [major, minor] = raw.split(" ").map(Number);
      if (major === 3 && minor >= 9) {
        return cmd;
      }
    } catch {
      // Not found or wrong version — try next candidate
    }
  }

  throw new Error(
    "Python 3.9+ is required but was not found.\n" +
    "Install it from https://www.python.org/downloads/ and make sure it is on your PATH."
  );
}

// ---------------------------------------------------------------------------
// Dependency check & auto-install
// ---------------------------------------------------------------------------

/**
 * Check whether a Python package is importable.
 * Returns true if it can be imported, false otherwise.
 */
function isPyPackageAvailable(python, packageName) {
  try {
    execSync(`${python} -c "import ${packageName}"`, {
      stdio: ["pipe", "pipe", "pipe"],
      timeout: 10000,
    });
    return true;
  } catch {
    return false;
  }
}

/**
 * Install a pip package quietly.
 * Throws on failure.
 */
function pipInstall(python, packageName) {
  process.stderr.write(`[contextl] Installing ${packageName}…\n`);
  try {
    execSync(`${python} -m pip install --quiet ${packageName}`, {
      stdio: ["pipe", "pipe", "pipe"],
      timeout: 120_000,
    });
    process.stderr.write(`[contextl] ${packageName} installed.\n`);
  } catch (err) {
    throw new Error(
      `Failed to install ${packageName} via pip.\n` +
      `Run manually: pip install ${packageName}\n\n` +
      String(err)
    );
  }
}

/**
 * Ensure all required Python packages are available, installing if needed.
 */
function ensureDeps(python) {
  const required = [
    { importName: "networkx", pipName: "networkx" },
    { importName: "mcp",      pipName: "mcp" },
  ];

  for (const { importName, pipName } of required) {
    if (!isPyPackageAvailable(python, importName)) {
      pipInstall(python, pipName);
    }
  }
}

// ---------------------------------------------------------------------------
// Launch MCP server
// ---------------------------------------------------------------------------

/**
 * Spawn mcp_server.py and forward signals so the parent IDE can cleanly
 * shut it down.
 */
function launchServer(python) {
  if (!fs.existsSync(MCP_SERVER)) {
    throw new Error(`mcp_server.py not found at: ${MCP_SERVER}`);
  }

  const child = spawn(python, [MCP_SERVER], {
    stdio: "inherit",
    env: {
      ...process.env,
      PYTHONPATH: PYTHON_DIR,
      PYTHONUNBUFFERED: "1",
    },
  });

  // Forward termination signals to the child so it can shut down cleanly
  for (const sig of ["SIGINT", "SIGTERM"]) {
    process.on(sig, () => {
      if (!child.killed) child.kill(sig);
    });
  }

  child.on("exit", (code, signal) => {
    process.exit(signal ? 1 : (code ?? 0));
  });

  child.on("error", (err) => {
    process.stderr.write(`[contextl] Failed to start mcp_server.py: ${err.message}\n`);
    process.exit(1);
  });
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

function main() {
  let python;

  try {
    python = findPython();
  } catch (err) {
    process.stderr.write(`[contextl] ${err.message}\n`);
    process.exit(1);
  }

  try {
    ensureDeps(python);
  } catch (err) {
    process.stderr.write(`[contextl] Dependency error: ${err.message}\n`);
    process.exit(1);
  }

  launchServer(python);
}

main();
