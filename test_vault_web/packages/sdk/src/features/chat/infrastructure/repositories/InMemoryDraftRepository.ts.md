# InMemoryDraftRepository.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/infrastructure/repositories/InMemoryDraftRepository.ts`
- **Extension:** `.ts`
- **Size:** 941 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ConversationKey`
- `InMemoryDraftRepository`

## Imports (Dependencies)
- [[packages/sdk/src/features/chat/domain/DraftRepository.ts.md|packages/sdk/src/features/chat/domain/DraftRepository.ts]]
- [[packages/sdk/src/features/chat/domain/MessageRepository.ts.md|packages/sdk/src/features/chat/domain/MessageRepository.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/chat/ChatClient.drafts.test.ts.md|packages/sdk/src/features/chat/ChatClient.drafts.test.ts]]
- [[packages/sdk/src/features/chat/ChatClient.ts.md|packages/sdk/src/features/chat/ChatClient.ts]]
- [[packages/sdk/src/features/chat/index.ts.md|packages/sdk/src/features/chat/index.ts]]

## Source Code Snippet
```ts
import {
  type ConversationKey,
  conversationKeyString,
} from "../../domain/MessageRepository.ts";
import type { DraftRepository } from "../../domain/DraftRepository.ts";

export class InMemoryDraftRepository implements DraftRepository {
  private readonly map = new Map<
    string,
    { key: ConversationKey; text: string }
  >();

  async load(key: ConversationKey): Promise<string> {
    return this.map.get(conversationKeyString(key))?.text ?? "";
  }

  async save(key: ConversationKey, text: string): Promise<void> {
    if (text.length === 0) {
      this.map.delete(conversationKeyString(key));
      return;
...
```