# EventBus.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/event-bus/EventBus.ts`
- **Extension:** `.ts`
- **Size:** 4820 bytes
- **Centrality Score:** 0.0061
- **In-Degree (Imported By):** 7
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `EventBus`

## Imports (Dependencies)
- [[packages/sdk/src/core/transport/Transport.ts.md|packages/sdk/src/core/transport/Transport.ts]]
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/event-bus/EventBus.test.ts.md|packages/sdk/src/core/event-bus/EventBus.test.ts]]
- [[packages/sdk/src/core/event-bus/index.ts.md|packages/sdk/src/core/event-bus/index.ts]]
- [[packages/sdk/src/core/packet-codec/decodePacket.ts.md|packages/sdk/src/core/packet-codec/decodePacket.ts]]
- [[packages/sdk/src/shim/legacyMeshDevice.ts.md|packages/sdk/src/shim/legacyMeshDevice.ts]]
- [[packages/sdk/src/shim/legacyUtils.ts.md|packages/sdk/src/shim/legacyUtils.ts]]

## Source Code Snippet
```ts
import type * as Protobuf from "@meshtastic/protobufs";
import { SimpleEventDispatcher } from "ste-simple-events";
import type { DeviceStatusEnum } from "../transport/Transport.ts";
import type { LogEventPacket, PacketMetadata } from "../types.ts";

/**
 * Typed event bus. Ports the former `EventSystem` into the SDK.
 *
 * Slice infrastructure subscribes here and materializes signals. External code
 * should prefer slice stores over raw bus subscriptions.
 */
export class EventBus {
  public readonly onLogEvent = new SimpleEventDispatcher<LogEventPacket>();
  public readonly onFromRadio =
    new SimpleEventDispatcher<Protobuf.Mesh.FromRadio>();
  public readonly onMeshPacket =
    new SimpleEventDispatcher<Protobuf.Mesh.MeshPacket>();
  public readonly onMyNodeInfo =
    new SimpleEventDispatcher<Protobuf.Mesh.MyNodeInfo>();
  public readonly onNodeInfoPacket =
...
```