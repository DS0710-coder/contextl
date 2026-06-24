# vitest.config.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/vitest.config.ts`
- **Extension:** `.ts`
- **Size:** 291 bytes
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
    name: "@meshtastic/sdk-react",
    environment: "jsdom",
    include: [
      "src/**/*.test.ts",
      "src/**/*.test.tsx",
      "tests/**/*.test.ts",
      "tests/**/*.test.tsx",
    ],
  },
});
```