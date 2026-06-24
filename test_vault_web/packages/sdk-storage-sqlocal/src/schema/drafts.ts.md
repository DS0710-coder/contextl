# drafts.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/schema/drafts.ts`
- **Extension:** `.ts`
- **Size:** 526 bytes
- **Centrality Score:** 0.0012
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DraftRow`
- `DraftInsert`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalDraftRepository.ts]]
- [[packages/sdk-storage-sqlocal/src/schema/index.ts.md|packages/sdk-storage-sqlocal/src/schema/index.ts]]

## Source Code Snippet
```ts
import {
  integer,
  primaryKey,
  sqliteTable,
  text,
} from "drizzle-orm/sqlite-core";

export const drafts = sqliteTable(
  "drafts",
  {
    deviceId: integer("device_id").notNull(),
    conversationKey: text("conversation_key").notNull(),
    text: text("text").notNull(),
    updatedAt: integer("updated_at").notNull(),
  },
  (t) => ({
    pk: primaryKey({ columns: [t.deviceId, t.conversationKey] }),
  }),
);

...
```