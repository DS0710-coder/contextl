# SqlocalDraftRepository.test.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.test.ts`
- **Extension:** `.ts`
- **Size:** 2463 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.ts]]
- [[packages/sdk-storage-sqlocal/src/db.ts.md|packages/sdk-storage-sqlocal/src/db.ts]]
- [[packages/sdk-storage-sqlocal/src/testing/createMemoryDb.ts.md|packages/sdk-storage-sqlocal/src/testing/createMemoryDb.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { ChannelNumber } from "@meshtastic/sdk";
import { beforeEach, describe, expect, it } from "vitest";
import type { SqlocalDb } from "../db.ts";
import { createMemoryDb } from "../testing/createMemoryDb.ts";
import { SqlocalDraftRepository } from "./SqlocalDraftRepository.ts";

describe("SqlocalDraftRepository", () => {
  let db: SqlocalDb;
  let repo: SqlocalDraftRepository;

  beforeEach(async () => {
    db = await createMemoryDb();
    repo = new SqlocalDraftRepository(db, { deviceId: 1 });
  });

  it("save then load returns the same text", async () => {
    await repo.save(
      { kind: "channel", channel: ChannelNumber.Primary },
      "hello",
    );
...
```