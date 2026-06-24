# MeshRegistry.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/registry/MeshRegistry.ts`
- **Extension:** `.ts`
- **Size:** 3926 bytes
- **Centrality Score:** 0.0042
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ConnectionId`
- `RegistryEntry`
- `MeshRegistry`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/registry/MeshRegistry.test.ts.md|packages/sdk/src/core/registry/MeshRegistry.test.ts]]
- [[packages/sdk/src/core/registry/index.ts.md|packages/sdk/src/core/registry/index.ts]]

## Source Code Snippet
```ts
import { type Signal, signal } from "@preact/signals-core";
import { MeshClient, type MeshClientOptions } from "../client/MeshClient.ts";
import { type ReadonlySignal, toReadonly } from "../signals/createStore.ts";

export type ConnectionId = number;

export interface RegistryEntry {
  readonly id: ConnectionId;
  readonly client: MeshClient;
}

/**
 * Manages multiple `MeshClient` instances keyed by connection id.
 *
 * Use this when an application holds more than one device connection at a
 * time (e.g. multi-radio UIs). Single-device consumers can ignore this and
 * instantiate `MeshClient` directly.
 */
export class MeshRegistry {
  private readonly clients = new Map<ConnectionId, MeshClient>();
...
```