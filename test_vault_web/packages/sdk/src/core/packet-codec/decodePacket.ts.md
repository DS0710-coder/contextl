# decodePacket.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/packet-codec/decodePacket.ts`
- **Extension:** `.ts`
- **Size:** 18674 bytes
- **Centrality Score:** 0.0018
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PacketSink`
- `handleMeshPacket`
- `handleDecodedPacket`

## Imports (Dependencies)
- [[packages/sdk/src/core/constants/index.ts.md|packages/sdk/src/core/constants/index.ts]]
- [[packages/sdk/src/core/event-bus/EventBus.ts.md|packages/sdk/src/core/event-bus/EventBus.ts]]
- [[packages/sdk/src/core/queue/Queue.ts.md|packages/sdk/src/core/queue/Queue.ts]]
- [[packages/sdk/src/core/transport/Transport.ts.md|packages/sdk/src/core/transport/Transport.ts]]
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]
- [[packages/sdk/src/core/xmodem/Xmodem.ts.md|packages/sdk/src/core/xmodem/Xmodem.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/packet-codec/index.ts.md|packages/sdk/src/core/packet-codec/index.ts]]

## Source Code Snippet
```ts
import { fromBinary } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import type { Logger } from "tslog";
import { Constants } from "../constants/index.ts";
import type { EventBus } from "../event-bus/EventBus.ts";
import type { Queue } from "../queue/Queue.ts";
import type { DeviceOutput } from "../transport/Transport.ts";
import { DeviceStatusEnum } from "../transport/Transport.ts";
import { ChannelNumber, Emitter, type PacketMetadata } from "../types.ts";
import type { Xmodem } from "../xmodem/Xmodem.ts";

/**
 * A minimal client-shape surface that the packet decoder writes into.
 * MeshClient and the legacy MeshDevice shim both implement this.
 */
export interface PacketSink {
  log: Logger<unknown>;
  events: EventBus;
  queue: Queue;
  xModem: Xmodem;
...
```