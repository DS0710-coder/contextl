# types.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/stores/appStore/types.ts`
- **Extension:** `.ts`
- **Size:** 108 bytes
- **Centrality Score:** 0.0019
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `RasterSource`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/core/stores/appStore/appStore.test.ts.md|apps/web/src/core/stores/appStore/appStore.test.ts]]
- [[apps/web/src/core/stores/appStore/index.ts.md|apps/web/src/core/stores/appStore/index.ts]]

## Source Code Snippet
```ts
export interface RasterSource {
  enabled: boolean;
  title: string;
  tiles: string;
  tileSize: number;
}
```