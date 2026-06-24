# vitest.config.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/vitest.config.ts`
- **Extension:** `.ts`
- **Size:** 423 bytes
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

export default defineProject({
  test: {
    name: "@meshtastic/sdk-storage-sqlocal",
    environment: "node",
    include: ["src/**/*.test.ts", "tests/**/*.test.ts"],
    // Browser-mode tests run via vitest.browser.config.ts so they don't
    // execute under the Node runner where OPFS is unavailable.
    exclude: ["**/*.browser.test.ts", "**/node_modules/**"],
  },
});
```