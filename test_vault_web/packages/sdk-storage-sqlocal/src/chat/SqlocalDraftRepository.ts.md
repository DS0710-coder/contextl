# SqlocalDraftRepository.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.ts`
- **Extension:** `.ts`
- **Size:** 2551 bytes
- **Centrality Score:** 0.0013
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `SqlocalDraftRepositoryOptions`
- `SqlocalDraftRepository`
- `parseKey`

## Imports (Dependencies)
- [[packages/sdk-storage-sqlocal/src/db.ts.md|packages/sdk-storage-sqlocal/src/db.ts]]
- [[packages/sdk-storage-sqlocal/src/schema/drafts.ts.md|packages/sdk-storage-sqlocal/src/schema/drafts.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.test.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.test.ts]]
- [[packages/sdk-storage-sqlocal/src/chat/index.ts.md|packages/sdk-storage-sqlocal/src/chat/index.ts]]

## Source Code Snippet
```ts
import type { ConversationKey, DraftRepository } from "@meshtastic/sdk";
import { conversationKeyString } from "@meshtastic/sdk";
import { and, eq, sql } from "drizzle-orm";
import type { SqlocalDb } from "../db.ts";
import { drafts } from "../schema/drafts.ts";

export interface SqlocalDraftRepositoryOptions {
  deviceId: number;
}

/**
 * Per-conversation draft persistence. Single row per (device_id,
 * conversation_key); upsert on save, delete on clear or empty save.
 */
export class SqlocalDraftRepository implements DraftRepository {
  private readonly db: SqlocalDb;
  private readonly deviceId: number;

  constructor(db: SqlocalDb, options: SqlocalDraftRepositoryOptions) {
    this.db = db;
...
```