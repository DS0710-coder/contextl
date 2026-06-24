# vitest.config.ts

## Architecture Metrics
- **Path:** `packages/sdk/vitest.config.ts`
- **Extension:** `.ts`
- **Size:** 209 bytes
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
    name: "@meshtastic/sdk",
    environment: "node",
    include: ["src/**/*.test.ts", "tests/**/*.test.ts"],
  },
});
```