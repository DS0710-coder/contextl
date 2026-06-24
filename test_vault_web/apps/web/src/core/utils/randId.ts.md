# randId.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/randId.ts`
- **Extension:** `.ts`
- **Size:** 75 bytes
- **Centrality Score:** 0.0019
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/core/utils/randId.test.ts.md|apps/web/src/core/utils/randId.test.ts]]
- [[apps/web/src/pages/Connections/useConnections.ts.md|apps/web/src/pages/Connections/useConnections.ts]]
- [[apps/web/src/pages/Connections/utils.ts.md|apps/web/src/pages/Connections/utils.ts]]

## Source Code Snippet
```ts
export const randId = () => {
  return Math.floor(Math.random() * 1e9);
};
```