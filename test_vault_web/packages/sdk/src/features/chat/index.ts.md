# index.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/index.ts`
- **Extension:** `.ts`
- **Size:** 907 bytes
- **Centrality Score:** 0.0041
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `SendTextError`
- `SendTextInput`

## Imports (Dependencies)
- [[packages/sdk/src/features/chat/ChatClient.ts.md|packages/sdk/src/features/chat/ChatClient.ts]]
- [[packages/sdk/src/features/chat/application/SendTextUseCase.ts.md|packages/sdk/src/features/chat/application/SendTextUseCase.ts]]
- [[packages/sdk/src/features/chat/domain/DraftRepository.ts.md|packages/sdk/src/features/chat/domain/DraftRepository.ts]]
- [[packages/sdk/src/features/chat/domain/Message.ts.md|packages/sdk/src/features/chat/domain/Message.ts]]
- [[packages/sdk/src/features/chat/domain/MessageRepository.ts.md|packages/sdk/src/features/chat/domain/MessageRepository.ts]]
- [[packages/sdk/src/features/chat/domain/MessageState.ts.md|packages/sdk/src/features/chat/domain/MessageState.ts]]
- [[packages/sdk/src/features/chat/infrastructure/MessageMapper.ts.md|packages/sdk/src/features/chat/infrastructure/MessageMapper.ts]]
- [[packages/sdk/src/features/chat/infrastructure/repositories/InMemoryDraftRepository.ts.md|packages/sdk/src/features/chat/infrastructure/repositories/InMemoryDraftRepository.ts]]
- [[packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.ts.md|packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.ts]]

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]

## Source Code Snippet
```ts
export { ChatClient } from "./ChatClient.ts";
export type {
  ChatClientOptions,
  ChatDrafts,
  ChatUnread,
} from "./ChatClient.ts";
export type { DraftRepository } from "./domain/DraftRepository.ts";
export { InMemoryDraftRepository } from "./infrastructure/repositories/InMemoryDraftRepository.ts";
export type { Message } from "./domain/Message.ts";
export { MessageState } from "./domain/MessageState.ts";
export type {
  ConversationKey,
  MessageRepository,
  RetentionPolicy,
} from "./domain/MessageRepository.ts";
export { conversationKeyString } from "./domain/MessageRepository.ts";
export { MessageMapper } from "./infrastructure/MessageMapper.ts";
export { InMemoryMessageRepository } from "./infrastructure/repositories/InMemoryMessageRepository.ts";
export {
  EmptyMessageError,
...
```