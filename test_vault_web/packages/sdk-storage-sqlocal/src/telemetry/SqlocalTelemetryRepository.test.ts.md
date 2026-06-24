# SqlocalTelemetryRepository.test.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/telemetry/SqlocalTelemetryRepository.test.ts`
- **Extension:** `.ts`
- **Size:** 3530 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `reading`

## Imports (Dependencies)
- [[packages/sdk-storage-sqlocal/src/db.ts.md|packages/sdk-storage-sqlocal/src/db.ts]]
- [[packages/sdk-storage-sqlocal/src/telemetry/SqlocalTelemetryRepository.ts.md|packages/sdk-storage-sqlocal/src/telemetry/SqlocalTelemetryRepository.ts]]
- [[packages/sdk-storage-sqlocal/src/testing/createMemoryDb.ts.md|packages/sdk-storage-sqlocal/src/testing/createMemoryDb.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { create } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import type { TelemetryReading } from "@meshtastic/sdk";
import { beforeEach, describe, expect, it } from "vitest";
import type { SqlocalDb } from "../db.ts";
import { createMemoryDb } from "../testing/createMemoryDb.ts";
import { SqlocalTelemetryRepository } from "./SqlocalTelemetryRepository.ts";

function reading(nodeNum: number, ms: number, battery = 80): TelemetryReading {
  return {
    nodeNum,
    time: new Date(ms),
    kind: "deviceMetrics",
    value: create(Protobuf.Telemetry.DeviceMetricsSchema, {
      batteryLevel: battery,
    }),
  };
}

describe("SqlocalTelemetryRepository", () => {
...
```