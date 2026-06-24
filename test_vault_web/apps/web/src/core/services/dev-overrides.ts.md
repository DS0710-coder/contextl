# dev-overrides.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/services/dev-overrides.ts`
- **Extension:** `.ts`
- **Size:** 271 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/core/services/featureFlags.ts.md|apps/web/src/core/services/featureFlags.ts]]

## Imported By (Dependents)
- [[apps/web/src/index.tsx.md|apps/web/src/index.tsx]]

## Source Code Snippet
```ts
import { featureFlags } from "@core/services/featureFlags";

const isDev = typeof import.meta !== "undefined" && import.meta.env?.DEV;
console.log(`Dev mode: ${isDev}`);

if (isDev) {
  featureFlags.setOverrides({
    persistMessages: true,
    persistApp: true,
  });
}
```