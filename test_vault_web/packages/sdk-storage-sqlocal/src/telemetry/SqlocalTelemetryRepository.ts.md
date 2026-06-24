# SqlocalTelemetryRepository.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/telemetry/SqlocalTelemetryRepository.ts`
- **Extension:** `.ts`
- **Size:** 6013 bytes
- **Centrality Score:** 0.0017
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `SqlocalTelemetryRepositoryOptions`
- `KnownKind`
- `SqlocalTelemetryRepository`
- `TelemetryRow`
- `readingToRow`
- `rowToReading`
- `base64Encode`
- `base64Decode`

## Imports (Dependencies)
- [[packages/sdk-storage-sqlocal/src/db.ts.md|packages/sdk-storage-sqlocal/src/db.ts]]
- [[packages/sdk-storage-sqlocal/src/schema/telemetry.ts.md|packages/sdk-storage-sqlocal/src/schema/telemetry.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-storage-sqlocal/src/telemetry/SqlocalTelemetryRepository.test.ts.md|packages/sdk-storage-sqlocal/src/telemetry/SqlocalTelemetryRepository.test.ts]]
- [[packages/sdk-storage-sqlocal/src/telemetry/index.ts.md|packages/sdk-storage-sqlocal/src/telemetry/index.ts]]

## Source Code Snippet
```ts
import { fromBinary, toBinary } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import type {
  TelemetryReading,
  TelemetryRepository,
  TelemetryRetentionPolicy,
} from "@meshtastic/sdk";
import { and, asc, count, desc, eq, gte, lt, sql } from "drizzle-orm";
import type { SqlocalDb } from "../db.ts";
import { telemetry } from "../schema/telemetry.ts";

export interface SqlocalTelemetryRepositoryOptions {
  deviceId: number;
}

const SCHEMA_FOR_KIND = {
  deviceMetrics: Protobuf.Telemetry.DeviceMetricsSchema,
  environmentMetrics: Protobuf.Telemetry.EnvironmentMetricsSchema,
  airQualityMetrics: Protobuf.Telemetry.AirQualityMetricsSchema,
  powerMetrics: Protobuf.Telemetry.PowerMetricsSchema,
...
```