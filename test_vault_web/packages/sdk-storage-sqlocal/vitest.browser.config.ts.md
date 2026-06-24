# vitest.browser.config.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/vitest.browser.config.ts`
- **Extension:** `.ts`
- **Size:** 785 bytes
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
import { defineProject } from "vitest/config";

/**
 * Browser-mode tests for the OPFS-backed SQLite path.
 *
 * Runs separately from the Node `vitest run` so CI can opt in (and the
 * Playwright browser binary download isn't a hard requirement for the
 * fast unit-test loop).
 *
 * Run with:
 *   pnpm --filter @meshtastic/sdk-storage-sqlocal test:browser
 *
 * Requires `@vitest/browser` + Playwright. Install with:
 *   pnpm add -D -w @vitest/browser playwright
 */
export default defineProject({
  test: {
    name: "@meshtastic/sdk-storage-sqlocal:browser",
    include: ["src/**/*.browser.test.ts", "tests/**/*.browser.test.ts"],
    browser: {
...
```