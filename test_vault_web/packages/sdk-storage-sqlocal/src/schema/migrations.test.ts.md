# migrations.test.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/schema/migrations.test.ts`
- **Extension:** `.ts`
- **Size:** 1740 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk-storage-sqlocal/src/schema/migrations.ts.md|packages/sdk-storage-sqlocal/src/schema/migrations.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { describe, expect, it } from "vitest";
import initSqlJs from "sql.js";
import { MIGRATIONS } from "./migrations.ts";

async function freshSqlite() {
  const SQL = await initSqlJs({});
  return new SQL.Database();
}

describe("MIGRATIONS", () => {
  it("first migration creates messages, nodes, telemetry, _schema", async () => {
    const db = await freshSqlite();
    for (const stmt of MIGRATIONS[0]!.sql) db.run(stmt);
    db.run("INSERT INTO _schema (version) VALUES (?)", [
      MIGRATIONS[0]!.version,
    ]);

    const tables = db
      .exec(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name",
...
```