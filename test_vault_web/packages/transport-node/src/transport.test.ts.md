# transport.test.ts

## Architecture Metrics
- **Path:** `packages/transport-node/src/transport.test.ts`
- **Extension:** `.ts`
- **Size:** 4927 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DeviceOutput`
- `isStatusEvent`
- `FakeSocket`
- `stubCoreTransforms`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/transport-node/src/transport.ts.md|packages/transport-node/src/transport.ts]]
- [[tests/utils/transportContract.ts.md|tests/utils/transportContract.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import type { Socket } from "node:net";
import { Duplex } from "node:stream";
import * as MeshSDK from "@meshtastic/sdk";
import {
  DeviceStatusEnum,
  type DeviceOutput,
  toDeviceStream,
} from "@meshtastic/sdk";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { runTransportContract } from "../../../tests/utils/transportContract.ts";
import { TransportNode } from "./transport.ts";

function isStatusEvent(
  out: DeviceOutput | undefined,
): out is Extract<DeviceOutput, { type: "status" }> {
  return !!out && (out as any).type === "status";
}

class FakeSocket extends Duplex {
  public lastWritten: Uint8Array | undefined;
...
```