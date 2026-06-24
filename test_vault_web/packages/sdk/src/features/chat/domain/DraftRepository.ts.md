# DraftRepository.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/domain/DraftRepository.ts`
- **Extension:** `.ts`
- **Size:** 505 bytes
- **Centrality Score:** 0.0018
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DraftRepository`

## Imports (Dependencies)
- [[packages/sdk/src/features/chat/domain/MessageRepository.ts.md|packages/sdk/src/features/chat/domain/MessageRepository.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/chat/ChatClient.ts.md|packages/sdk/src/features/chat/ChatClient.ts]]
- [[packages/sdk/src/features/chat/index.ts.md|packages/sdk/src/features/chat/index.ts]]
- [[packages/sdk/src/features/chat/infrastructure/repositories/InMemoryDraftRepository.ts.md|packages/sdk/src/features/chat/infrastructure/repositories/InMemoryDraftRepository.ts]]

## Source Code Snippet
```ts
import type { ConversationKey } from "./MessageRepository.ts";

/**
 * Persists per-conversation draft text. Implementations can be in-memory
 * (lost on reload) or backed by SQLite for users who expect drafts to
 * survive a refresh.
 */
export interface DraftRepository {
  load(key: ConversationKey): Promise<string>;
  save(key: ConversationKey, text: string): Promise<void>;
  clear(key: ConversationKey): Promise<void>;
  loadAll(): Promise<ReadonlyArray<{ key: ConversationKey; text: string }>>;
}
```