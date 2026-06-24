# playwright.config.ts

## Architecture Metrics
- **Path:** `playwright.config.ts`
- **Extension:** `.ts`
- **Size:** 1769 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { defineConfig, devices } from "@playwright/test";

/**
 * End-to-end suite that drives the real web app against a REAL Meshtastic device
 * (a simulated `meshtasticd` node by default, or physical hardware) over the
 * HTTP(S) phone API, and exercises text messaging across a two-node mesh.
 *
 * Topology is brought up in e2e/global-setup.ts. The off-browser "mesh peer"
 * (e2e/peer/peer.py) drives/asserts the second node. See e2e/README.md.
 */
const WEB_PORT = Number(process.env.E2E_WEB_PORT ?? 3100);

export default defineConfig({
  testDir: "./e2e/tests",
  outputDir: "./e2e/.results",
  globalSetup: "./e2e/global-setup.ts",
  globalTeardown: "./e2e/global-teardown.ts",

  // Tests share a single two-node mesh + one device identity, so run serially.
  fullyParallel: false,
...
```