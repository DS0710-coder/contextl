# transport.test.ts

## Architecture Metrics
- **Path:** `packages/transport-web-serial/src/transport.test.ts`
- **Extension:** `.ts`
- **Size:** 9675 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DeviceOutput`
- `stubCoreTransforms`
- `stubNavigatorSerial`
- `SerialDisconnectHandler`
- `FakeSerialPort`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/transport-web-serial/src/transport.ts.md|packages/transport-web-serial/src/transport.ts]]
- [[tests/utils/transportContract.ts.md|tests/utils/transportContract.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import * as MeshSDK from "@meshtastic/sdk";
import {
  DeviceStatusEnum,
  type DeviceOutput,
  toDeviceStream,
} from "@meshtastic/sdk";
import { Result } from "better-result";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { runTransportContract } from "../../../tests/utils/transportContract.ts";
import { SerialConnectError, TransportWebSerial } from "./transport.ts";

function stubCoreTransforms() {
  const toDevice = () =>
    new TransformStream<Uint8Array, Uint8Array>({
      transform(chunk, controller) {
        controller.enqueue(chunk);
      },
    });

  // maps raw bytes -> DeviceOutput.packet
...
```