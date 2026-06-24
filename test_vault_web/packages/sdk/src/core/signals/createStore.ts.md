# createStore.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/signals/createStore.ts`
- **Extension:** `.ts`
- **Size:** 2391 bytes
- **Centrality Score:** 0.0138
- **In-Degree (Imported By):** 26
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ReadonlySignal`
- `Signal`
- `ReadonlySignal`
- `createStore`
- `toReadonly`
- `SignalMap`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/registry/MeshRegistry.ts.md|packages/sdk/src/core/registry/MeshRegistry.ts]]
- [[packages/sdk/src/core/signals/createStore.test.ts.md|packages/sdk/src/core/signals/createStore.test.ts]]
- [[packages/sdk/src/core/signals/index.ts.md|packages/sdk/src/core/signals/index.ts]]
- [[packages/sdk/src/features/channels/ChannelsClient.ts.md|packages/sdk/src/features/channels/ChannelsClient.ts]]
- [[packages/sdk/src/features/channels/state/channelsStore.ts.md|packages/sdk/src/features/channels/state/channelsStore.ts]]
- [[packages/sdk/src/features/chat/ChatClient.ts.md|packages/sdk/src/features/chat/ChatClient.ts]]
- [[packages/sdk/src/features/chat/state/chatStore.ts.md|packages/sdk/src/features/chat/state/chatStore.ts]]
- [[packages/sdk/src/features/chat/state/draftStore.ts.md|packages/sdk/src/features/chat/state/draftStore.ts]]
- [[packages/sdk/src/features/config/ConfigClient.ts.md|packages/sdk/src/features/config/ConfigClient.ts]]
- [[packages/sdk/src/features/config/domain/ConfigEditor.ts.md|packages/sdk/src/features/config/domain/ConfigEditor.ts]]
- [[packages/sdk/src/features/config/state/configStore.ts.md|packages/sdk/src/features/config/state/configStore.ts]]
- [[packages/sdk/src/features/device/DeviceClient.ts.md|packages/sdk/src/features/device/DeviceClient.ts]]
- [[packages/sdk/src/features/device/state/deviceStore.ts.md|packages/sdk/src/features/device/state/deviceStore.ts]]
- [[packages/sdk/src/features/files/FilesClient.ts.md|packages/sdk/src/features/files/FilesClient.ts]]
- [[packages/sdk/src/features/files/state/filesStore.ts.md|packages/sdk/src/features/files/state/filesStore.ts]]
- [[packages/sdk/src/features/nodes/NodesClient.ts.md|packages/sdk/src/features/nodes/NodesClient.ts]]
- [[packages/sdk/src/features/nodes/state/nodeErrorsStore.ts.md|packages/sdk/src/features/nodes/state/nodeErrorsStore.ts]]
- [[packages/sdk/src/features/nodes/state/nodesStore.ts.md|packages/sdk/src/features/nodes/state/nodesStore.ts]]
- [[packages/sdk/src/features/position/PositionClient.ts.md|packages/sdk/src/features/position/PositionClient.ts]]
- [[packages/sdk/src/features/position/state/positionStore.ts.md|packages/sdk/src/features/position/state/positionStore.ts]]
- [[packages/sdk/src/features/telemetry/TelemetryClient.ts.md|packages/sdk/src/features/telemetry/TelemetryClient.ts]]
- [[packages/sdk/src/features/telemetry/state/telemetryStore.ts.md|packages/sdk/src/features/telemetry/state/telemetryStore.ts]]
- [[packages/sdk/src/features/traceroute/TraceRouteClient.ts.md|packages/sdk/src/features/traceroute/TraceRouteClient.ts]]
- [[packages/sdk/src/features/traceroute/state/tracerouteStore.ts.md|packages/sdk/src/features/traceroute/state/tracerouteStore.ts]]

## Source Code Snippet
```ts
import {
  type ReadonlySignal as PreactReadonlySignal,
  type Signal,
  signal,
} from "@preact/signals-core";

/**
 * Reactive read-only view of a signal.
 *
 * Compatible with React's useSyncExternalStore contract: consumers subscribe
 * for change notifications and call `value` / `peek()` to read.
 */
export interface ReadonlySignal<T> {
  readonly value: T;
  peek(): T;
  subscribe(listener: (value: T) => void): () => void;
}

/**
 * Wraps a preact signal into the SDK's ReadonlySignal interface. The listener
...
```