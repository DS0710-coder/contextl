# Position.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/position/domain/Position.ts`
- **Extension:** `.ts`
- **Size:** 175 bytes
- **Centrality Score:** 0.0035
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Position`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk/src/features/position/PositionClient.ts.md|packages/sdk/src/features/position/PositionClient.ts]]
- [[packages/sdk/src/features/position/index.ts.md|packages/sdk/src/features/position/index.ts]]
- [[packages/sdk/src/features/position/infrastructure/PositionMapper.ts.md|packages/sdk/src/features/position/infrastructure/PositionMapper.ts]]
- [[packages/sdk/src/features/position/state/positionStore.ts.md|packages/sdk/src/features/position/state/positionStore.ts]]

## Source Code Snippet
```ts
export interface Position {
  readonly nodeNum: number;
  readonly latitudeI?: number;
  readonly longitudeI?: number;
  readonly altitude?: number;
  readonly time?: Date;
}
```