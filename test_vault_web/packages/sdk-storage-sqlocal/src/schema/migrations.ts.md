# migrations.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/schema/migrations.ts`
- **Extension:** `.ts`
- **Size:** 2364 bytes
- **Centrality Score:** 0.0060
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TEXT`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk-storage-sqlocal/src/db.ts.md|packages/sdk-storage-sqlocal/src/db.ts]]
- [[packages/sdk-storage-sqlocal/src/schema/index.ts.md|packages/sdk-storage-sqlocal/src/schema/index.ts]]
- [[packages/sdk-storage-sqlocal/src/schema/migrations.test.ts.md|packages/sdk-storage-sqlocal/src/schema/migrations.test.ts]]
- [[packages/sdk-storage-sqlocal/src/testing/createMemoryDb.ts.md|packages/sdk-storage-sqlocal/src/testing/createMemoryDb.ts]]

## Source Code Snippet
```ts
import { integer, sqliteTable } from "drizzle-orm/sqlite-core";

export const schemaVersion = sqliteTable("_schema", {
  version: integer("version").primaryKey(),
});

/**
 * Hand-written DDL applied at boot if `_schema` is empty or behind. Drizzle's
 * own migration tooling is great but adds a build-time step; we keep migrations
 * inline so the package self-bootstraps on first DB open.
 */
export const MIGRATIONS: ReadonlyArray<{ version: number; sql: string[] }> = [
  {
    version: 1,
    sql: [
      `CREATE TABLE IF NOT EXISTS messages (
        id INTEGER NOT NULL,
        device_id INTEGER NOT NULL,
        conversation_key TEXT NOT NULL,
        from_node INTEGER NOT NULL,
...
```