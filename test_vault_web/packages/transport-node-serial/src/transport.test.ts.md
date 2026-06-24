# transport.test.ts

## Architecture Metrics
- **Path:** `packages/transport-node-serial/src/transport.test.ts`
- **Extension:** `.ts`
- **Size:** 5026 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DeviceOutput`
- `isStatusEvent`
- `FakeSerialPort`
- `stubCoreTransforms`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/transport-node-serial/src/transport.ts.md|packages/transport-node-serial/src/transport.ts]]
- [[tests/utils/transportContract.ts.md|tests/utils/transportContract.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { Duplex } from "node:stream";
import * as MeshSDK from "@meshtastic/sdk";
import {
  DeviceStatusEnum,
  type DeviceOutput,
  toDeviceStream,
} from "@meshtastic/sdk";
import type { SerialPort } from "serialport";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { runTransportContract } from "../../../tests/utils/transportContract.ts";
import { TransportNodeSerial } from "./transport.ts";

function isStatusEvent(
  output: DeviceOutput | undefined,
): output is Extract<DeviceOutput, { type: "status" }> {
  return output !== undefined && output.type === "status";
}

class FakeSerialPort extends Duplex {
  public lastWritten: Uint8Array | undefined;
...
```