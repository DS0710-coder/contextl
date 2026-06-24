# telemetry.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/schema/telemetry.ts`
- **Extension:** `.ts`
- **Size:** 622 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TelemetryRow`
- `TelemetryInsert`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk-storage-sqlocal/src/schema/index.ts.md|packages/sdk-storage-sqlocal/src/schema/index.ts]]
- [[packages/sdk-storage-sqlocal/src/telemetry/SqlocalTelemetryRepository.ts.md|packages/sdk-storage-sqlocal/src/telemetry/SqlocalTelemetryRepository.ts]]

## Source Code Snippet
```ts
import { index, integer, sqliteTable, text } from "drizzle-orm/sqlite-core";

export const telemetry = sqliteTable(
  "telemetry",
  {
    id: integer("id").primaryKey({ autoIncrement: true }),
    deviceId: integer("device_id").notNull(),
    nodeNum: integer("node_num").notNull(),
    kind: text("kind").notNull(),
    ts: integer("ts").notNull(),
    payloadJson: text("payload_json").notNull(),
  },
  (t) => ({
    nodeTs: index("idx_telemetry_node_ts").on(t.deviceId, t.nodeNum, t.ts),
  }),
);

export type TelemetryRow = typeof telemetry.$inferSelect;
export type TelemetryInsert = typeof telemetry.$inferInsert;
```