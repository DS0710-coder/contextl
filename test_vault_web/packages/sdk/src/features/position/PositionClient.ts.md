# PositionClient.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/position/PositionClient.ts`
- **Extension:** `.ts`
- **Size:** 1674 bytes
- **Centrality Score:** 0.0019
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PositionClient`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/features/position/application/PositionUseCases.ts.md|packages/sdk/src/features/position/application/PositionUseCases.ts]]
- [[packages/sdk/src/features/position/domain/Position.ts.md|packages/sdk/src/features/position/domain/Position.ts]]
- [[packages/sdk/src/features/position/infrastructure/PositionMapper.ts.md|packages/sdk/src/features/position/infrastructure/PositionMapper.ts]]
- [[packages/sdk/src/features/position/state/positionStore.ts.md|packages/sdk/src/features/position/state/positionStore.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/position/index.ts.md|packages/sdk/src/features/position/index.ts]]

## Source Code Snippet
```ts
import type * as Protobuf from "@meshtastic/protobufs";
import type { ResultType } from "better-result";
import type { MeshClient } from "../../core/client/MeshClient.ts";
import type { ReadonlySignal } from "../../core/signals/createStore.ts";
import type { Position } from "./domain/Position.ts";
import { PositionMapper } from "./infrastructure/PositionMapper.ts";
import {
  removeFixedPosition,
  requestPosition,
  setFixedPosition,
  setPosition,
} from "./application/PositionUseCases.ts";
import { PositionStore } from "./state/positionStore.ts";

export class PositionClient {
  private readonly client: MeshClient;
  private readonly store: PositionStore;
  public readonly list: ReadonlySignal<ReadonlyArray<Position>>;

  constructor(client: MeshClient) {
...
```