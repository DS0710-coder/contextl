# transportContract.ts

## Architecture Metrics
- **Path:** `tests/utils/transportContract.ts`
- **Extension:** `.ts`
- **Size:** 3605 bytes
- **Centrality Score:** 0.0020
- **In-Degree (Imported By):** 5
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DeviceOutput`
- `Transport`
- `TransportContract`
- `runTransportContract`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/transport-http/src/transport.test.ts.md|packages/transport-http/src/transport.test.ts]]
- [[packages/transport-node-serial/src/transport.test.ts.md|packages/transport-node-serial/src/transport.test.ts]]
- [[packages/transport-node/src/transport.test.ts.md|packages/transport-node/src/transport.test.ts]]
- [[packages/transport-web-bluetooth/src/transport.test.ts.md|packages/transport-web-bluetooth/src/transport.test.ts]]
- [[packages/transport-web-serial/src/transport.test.ts.md|packages/transport-web-serial/src/transport.test.ts]]

## Source Code Snippet
```ts
import {
  DeviceStatusEnum,
  type DeviceOutput,
  type Transport,
} from "@meshtastic/sdk";
import { describe, expect, it } from "vitest";

export interface TransportContract {
  name: string;
  create: () => Promise<Transport>;
  setup?: () => void | Promise<void>;
  teardown?: () => void | Promise<void>;
  pushIncoming?: (bytes: Uint8Array) => void | Promise<void>;
  assertLastWritten?: (bytes: Uint8Array) => void;
  triggerDisconnect?: () => void | Promise<void>;
}

async function readUntilType(
  reader: ReadableStreamDefaultReader<DeviceOutput>,
  expectedType: DeviceOutput["type"],
...
```