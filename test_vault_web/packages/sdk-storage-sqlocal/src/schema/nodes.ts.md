# nodes.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/schema/nodes.ts`
- **Extension:** `.ts`
- **Size:** 1102 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NodeRow`
- `NodeInsert`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk-storage-sqlocal/src/nodes/SqlocalNodesRepository.ts.md|packages/sdk-storage-sqlocal/src/nodes/SqlocalNodesRepository.ts]]
- [[packages/sdk-storage-sqlocal/src/schema/index.ts.md|packages/sdk-storage-sqlocal/src/schema/index.ts]]

## Source Code Snippet
```ts
import {
  index,
  integer,
  primaryKey,
  sqliteTable,
  text,
} from "drizzle-orm/sqlite-core";

/**
 * Snapshot of the device's NodeDB. Position / metrics / user are stored as
 * JSON blobs (proto-shape) — slice infrastructure mappers are responsible
 * for serialization. Last-heard duplicates the column for sortable indexes.
 */
export const nodes = sqliteTable(
  "nodes",
  {
    deviceId: integer("device_id").notNull(),
    num: integer("num").notNull(),
    lastHeard: integer("last_heard"),
    snr: integer("snr"),
...
```