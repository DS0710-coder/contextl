# transport.ts

## Architecture Metrics
- **Path:** `packages/transport-node/src/transport.ts`
- **Extension:** `.ts`
- **Size:** 6135 bytes
- **Centrality Score:** 0.0016
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DeviceOutput`
- `Transport`
- `TransportNode`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/transport-node/mod.ts.md|packages/transport-node/mod.ts]]
- [[packages/transport-node/src/transport.test.ts.md|packages/transport-node/src/transport.test.ts]]

## Source Code Snippet
```ts
import { Socket } from "node:net";
import { Readable, Writable } from "node:stream";
import {
  DeviceStatusEnum,
  type DeviceOutput,
  fromDeviceStream,
  toDeviceStream,
  type Transport,
} from "@meshtastic/sdk";

/**
 * Node.js TCP transport for Meshtastic.
 *
 * Implements {@link Transport} on top of a Node `net.Socket`.
 * Use {@link TransportNode.create} to open a new connection, or
 * construct directly with an existing socket.
 */
export class TransportNode implements Transport {
  private readonly _toDevice: WritableStream<Uint8Array>;
  private readonly _fromDevice: ReadableStream<DeviceOutput>;
...
```