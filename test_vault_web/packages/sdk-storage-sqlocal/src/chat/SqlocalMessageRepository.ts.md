# SqlocalMessageRepository.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.ts`
- **Extension:** `.ts`
- **Size:** 5384 bytes
- **Centrality Score:** 0.0015
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `SqlocalMessageRepositoryOptions`
- `SqlocalMessageRepository`
- `MessageRow`
- `rowToMessage`
- `messageToRow`

## Imports (Dependencies)
- [[packages/sdk-storage-sqlocal/src/coordination/MultiTabCoordinator.ts.md|packages/sdk-storage-sqlocal/src/coordination/MultiTabCoordinator.ts]]
- [[packages/sdk-storage-sqlocal/src/db.ts.md|packages/sdk-storage-sqlocal/src/db.ts]]
- [[packages/sdk-storage-sqlocal/src/schema/chat.ts.md|packages/sdk-storage-sqlocal/src/schema/chat.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.test.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.test.ts]]
- [[packages/sdk-storage-sqlocal/src/chat/index.ts.md|packages/sdk-storage-sqlocal/src/chat/index.ts]]
- [[packages/sdk-storage-sqlocal/tests/sqlocal-opfs.browser.test.ts.md|packages/sdk-storage-sqlocal/tests/sqlocal-opfs.browser.test.ts]]

## Source Code Snippet
```ts
import type {
  ConversationKey,
  Message,
  MessageRepository,
  RetentionPolicy,
} from "@meshtastic/sdk";
import { conversationKeyString, MessageState } from "@meshtastic/sdk";
import { and, desc, eq, lt, sql } from "drizzle-orm";
import { type MultiTabCoordinator } from "../coordination/MultiTabCoordinator.ts";
import type { SqlocalDb } from "../db.ts";
import { messages } from "../schema/chat.ts";

export interface SqlocalMessageRepositoryOptions {
  /** Identifies the device (matches MeshRegistry ConnectionId). */
  deviceId: number;
  /** Optional cross-tab coordinator. If omitted, mutations are silent. */
  coordinator?: MultiTabCoordinator;
}

export class SqlocalMessageRepository implements MessageRepository {
...
```