# chat.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/schema/chat.ts`
- **Extension:** `.ts`
- **Size:** 1286 bytes
- **Centrality Score:** 0.0012
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `MessageRow`
- `MessageInsert`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.ts]]
- [[packages/sdk-storage-sqlocal/src/schema/index.ts.md|packages/sdk-storage-sqlocal/src/schema/index.ts]]

## Source Code Snippet
```ts
import { index, integer, sqliteTable, text } from "drizzle-orm/sqlite-core";

export const messages = sqliteTable(
  "messages",
  {
    /**
     * Composite primary key would be ideal, but Meshtastic packet IDs are
     * already 32-bit random values; collisions across devices are rare. We
     * scope reads by (device_id, conversation_key) so collisions only
     * matter within a single device's history.
     */
    id: integer("id").notNull(),
    deviceId: integer("device_id").notNull(),
    conversationKey: text("conversation_key").notNull(),
    fromNode: integer("from_node").notNull(),
    toNode: integer("to_node").notNull(),
    channel: integer("channel").notNull(),
    rxTime: integer("rx_time").notNull(),
    type: text("type", { enum: ["broadcast", "direct"] }).notNull(),
    text: text("text").notNull(),
...
```