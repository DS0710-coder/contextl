# transport.ts

## Architecture Metrics
- **Path:** `packages/transport-http/src/transport.ts`
- **Extension:** `.ts`
- **Size:** 6831 bytes
- **Centrality Score:** 0.0019
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DeviceOutput`
- `Transport`
- `toArrayBuffer`
- `TransportHTTP`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/transport-http/mod.ts.md|packages/transport-http/mod.ts]]
- [[packages/transport-http/src/transport.test.ts.md|packages/transport-http/src/transport.test.ts]]

## Source Code Snippet
```ts
import {
  DeviceStatusEnum,
  type DeviceOutput,
  type Transport,
} from "@meshtastic/sdk";

const FETCH_INTERVAL_MS = 3000;
const READ_TIMEOUT_MS = 7000;
const WRITE_TIMEOUT_MS = 4000;

function toArrayBuffer(uint8array: Uint8Array): ArrayBuffer {
  if (
    uint8array.buffer instanceof ArrayBuffer &&
    uint8array.byteOffset === 0 &&
    uint8array.byteLength === uint8array.buffer.byteLength
  ) {
    return uint8array.buffer;
  }
  return uint8array.slice().buffer;
}
...
```