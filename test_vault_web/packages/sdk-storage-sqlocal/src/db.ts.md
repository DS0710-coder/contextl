# db.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/db.ts`
- **Extension:** `.ts`
- **Size:** 1792 bytes
- **Centrality Score:** 0.0043
- **In-Degree (Imported By):** 11
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `CreateSqlocalDbOptions`
- `SqlocalDb`
- `RawSql`

## Imports (Dependencies)
- [[packages/sdk-storage-sqlocal/src/schema/migrations.ts.md|packages/sdk-storage-sqlocal/src/schema/migrations.ts]]

## Imported By (Dependents)
- [[packages/sdk-storage-sqlocal/mod.ts.md|packages/sdk-storage-sqlocal/mod.ts]]
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.test.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.test.ts]]
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.ts]]
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.test.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.test.ts]]
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.ts]]
- [[packages/sdk-storage-sqlocal/src/nodes/SqlocalNodesRepository.test.ts.md|packages/sdk-storage-sqlocal/src/nodes/SqlocalNodesRepository.test.ts]]
- [[packages/sdk-storage-sqlocal/src/nodes/SqlocalNodesRepository.ts.md|packages/sdk-storage-sqlocal/src/nodes/SqlocalNodesRepository.ts]]
- [[packages/sdk-storage-sqlocal/src/telemetry/SqlocalTelemetryRepository.test.ts.md|packages/sdk-storage-sqlocal/src/telemetry/SqlocalTelemetryRepository.test.ts]]
- [[packages/sdk-storage-sqlocal/src/telemetry/SqlocalTelemetryRepository.ts.md|packages/sdk-storage-sqlocal/src/telemetry/SqlocalTelemetryRepository.ts]]
- [[packages/sdk-storage-sqlocal/src/testing/createMemoryDb.ts.md|packages/sdk-storage-sqlocal/src/testing/createMemoryDb.ts]]
- [[packages/sdk-storage-sqlocal/tests/sqlocal-opfs.browser.test.ts.md|packages/sdk-storage-sqlocal/tests/sqlocal-opfs.browser.test.ts]]

## Source Code Snippet
```ts
import { drizzle } from "drizzle-orm/sqlite-proxy";
import type { BaseSQLiteDatabase } from "drizzle-orm/sqlite-core";
import { SQLocalDrizzle } from "sqlocal/drizzle";
import * as schema from "./schema/index.ts";
import { MIGRATIONS } from "./schema/migrations.ts";

export interface CreateSqlocalDbOptions {
  /** OPFS path. Defaults to "meshtastic.db". */
  databasePath?: string;
}

export type SqlocalDb = BaseSQLiteDatabase<"async", unknown, typeof schema>;

/**
 * Opens (or creates) the OPFS-backed SQLite database, applies migrations, and
 * returns a Drizzle client typed against the schema. One instance per origin —
 * sqlocal serializes writes via Web Locks under the hood.
 */
export async function createSqlocalDb(
  options: CreateSqlocalDbOptions = {},
...
```