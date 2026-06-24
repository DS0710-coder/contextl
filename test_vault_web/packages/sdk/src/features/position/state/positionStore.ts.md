# positionStore.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/position/state/positionStore.ts`
- **Extension:** `.ts`
- **Size:** 188 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PositionStore`

## Imports (Dependencies)
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/features/position/domain/Position.ts.md|packages/sdk/src/features/position/domain/Position.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/position/PositionClient.ts.md|packages/sdk/src/features/position/PositionClient.ts]]

## Source Code Snippet
```ts
import { SignalMap } from "../../../core/signals/createStore.ts";
import type { Position } from "../domain/Position.ts";

export class PositionStore extends SignalMap<number, Position> {}
```