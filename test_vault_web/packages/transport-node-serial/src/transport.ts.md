# transport.ts

## Architecture Metrics
- **Path:** `packages/transport-node-serial/src/transport.ts`
- **Extension:** `.ts`
- **Size:** 5322 bytes
- **Centrality Score:** 0.0016
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DeviceOutput`
- `Transport`
- `TransportNodeSerial`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/transport-node-serial/mod.ts.md|packages/transport-node-serial/mod.ts]]
- [[packages/transport-node-serial/src/transport.test.ts.md|packages/transport-node-serial/src/transport.test.ts]]

## Source Code Snippet
```ts
import { Readable, Writable } from "node:stream";
import {
  DeviceStatusEnum,
  type DeviceOutput,
  fromDeviceStream,
  toDeviceStream,
  type Transport,
} from "@meshtastic/sdk";
import { SerialPort } from "serialport";

/**
 * Node.js Serial transport for Meshtastic.
 *
 * Implements {@link Transport} on top of a Node `SerialPort`.
 * Use {@link TransportNodeSerial.create} for a convenient factory, or
 * `new TransportNodeSerial(port)` if you already have an open port.
 */
export class TransportNodeSerial implements Transport {
  private readonly _toDevice: WritableStream<Uint8Array>;
  private readonly _fromDevice: ReadableStream<DeviceOutput>;
...
```