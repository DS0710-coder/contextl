# createMemoryDb.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/testing/createMemoryDb.ts`
- **Extension:** `.ts`
- **Size:** 893 bytes
- **Centrality Score:** 0.0020
- **In-Degree (Imported By):** 5
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk-storage-sqlocal/src/db.ts.md|packages/sdk-storage-sqlocal/src/db.ts]]
- [[packages/sdk-storage-sqlocal/src/schema/migrations.ts.md|packages/sdk-storage-sqlocal/src/schema/migrations.ts]]

## Imported By (Dependents)
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.test.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.test.ts]]
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.test.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.test.ts]]
- [[packages/sdk-storage-sqlocal/src/nodes/SqlocalNodesRepository.test.ts.md|packages/sdk-storage-sqlocal/src/nodes/SqlocalNodesRepository.test.ts]]
- [[packages/sdk-storage-sqlocal/src/telemetry/SqlocalTelemetryRepository.test.ts.md|packages/sdk-storage-sqlocal/src/telemetry/SqlocalTelemetryRepository.test.ts]]
- [[packages/sdk-storage-sqlocal/src/testing/index.ts.md|packages/sdk-storage-sqlocal/src/testing/index.ts]]

## Source Code Snippet
```ts
import { drizzle } from "drizzle-orm/sql-js";
import initSqlJs from "sql.js";
import * as schema from "../schema/index.ts";
import { MIGRATIONS } from "../schema/migrations.ts";
import type { SqlocalDb } from "../db.ts";

/**
 * In-memory database backed by sql.js, for tests and other Node contexts.
 * Same Drizzle interface as the production sqlocal connection so repository
 * code is portable between browser and test runs.
 */
export async function createMemoryDb(): Promise<SqlocalDb> {
  const SQL = await initSqlJs({});
  const sqlite = new SQL.Database();

  for (const migration of MIGRATIONS) {
    for (const statement of migration.sql) {
      sqlite.run(statement);
    }
    sqlite.run("INSERT OR IGNORE INTO _schema (version) VALUES (?)", [
...
```