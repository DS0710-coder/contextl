# index.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/position/index.ts`
- **Extension:** `.ts`
- **Size:** 177 bytes
- **Centrality Score:** 0.0041
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/features/position/PositionClient.ts.md|packages/sdk/src/features/position/PositionClient.ts]]
- [[packages/sdk/src/features/position/domain/Position.ts.md|packages/sdk/src/features/position/domain/Position.ts]]
- [[packages/sdk/src/features/position/infrastructure/PositionMapper.ts.md|packages/sdk/src/features/position/infrastructure/PositionMapper.ts]]

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]

## Source Code Snippet
```ts
export { PositionClient } from "./PositionClient.ts";
export type { Position } from "./domain/Position.ts";
export { PositionMapper } from "./infrastructure/PositionMapper.ts";
```