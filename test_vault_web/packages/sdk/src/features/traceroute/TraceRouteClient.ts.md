# TraceRouteClient.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/traceroute/TraceRouteClient.ts`
- **Extension:** `.ts`
- **Size:** 1188 bytes
- **Centrality Score:** 0.0025
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TraceRouteClient`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/features/traceroute/application/TraceRouteUseCase.ts.md|packages/sdk/src/features/traceroute/application/TraceRouteUseCase.ts]]
- [[packages/sdk/src/features/traceroute/domain/TraceRoute.ts.md|packages/sdk/src/features/traceroute/domain/TraceRoute.ts]]
- [[packages/sdk/src/features/traceroute/state/tracerouteStore.ts.md|packages/sdk/src/features/traceroute/state/tracerouteStore.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/traceroute/index.ts.md|packages/sdk/src/features/traceroute/index.ts]]

## Source Code Snippet
```ts
import type { ResultType } from "better-result";
import type { MeshClient } from "../../core/client/MeshClient.ts";
import type { ReadonlySignal } from "../../core/signals/createStore.ts";
import type { TraceRoute } from "./domain/TraceRoute.ts";
import { runTraceRoute } from "./application/TraceRouteUseCase.ts";
import { TraceRouteStore } from "./state/tracerouteStore.ts";

export class TraceRouteClient {
  private readonly client: MeshClient;
  private readonly store: TraceRouteStore;
  public readonly list: ReadonlySignal<ReadonlyArray<TraceRoute>>;

  constructor(client: MeshClient) {
    this.client = client;
    this.store = new TraceRouteStore();
    this.list = this.store.read;

    client.events.onTraceRoutePacket.subscribe((packet) => {
      this.store.set(packet.from, {
        destination: packet.from,
...
```