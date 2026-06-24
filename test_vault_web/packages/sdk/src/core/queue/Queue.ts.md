# Queue.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/queue/Queue.ts`
- **Extension:** `.ts`
- **Size:** 3637 bytes
- **Centrality Score:** 0.0049
- **In-Degree (Imported By):** 5
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Queue`

## Imports (Dependencies)
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/packet-codec/decodePacket.ts.md|packages/sdk/src/core/packet-codec/decodePacket.ts]]
- [[packages/sdk/src/shim/legacyMeshDevice.ts.md|packages/sdk/src/shim/legacyMeshDevice.ts]]
- [[packages/sdk/src/shim/legacyUtils.ts.md|packages/sdk/src/shim/legacyUtils.ts]]

## Source Code Snippet
```ts
import { fromBinary } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import { SimpleEventDispatcher } from "ste-simple-events";
import type { PacketError, QueueItem } from "../types.ts";

export class Queue {
  private queue: QueueItem[] = [];
  private lock = false;
  private ackNotifier = new SimpleEventDispatcher<number>();
  private errorNotifier = new SimpleEventDispatcher<PacketError>();
  private timeout: number;

  constructor() {
    this.timeout = 60000;
  }

  public getState(): QueueItem[] {
    return this.queue;
  }

...
```