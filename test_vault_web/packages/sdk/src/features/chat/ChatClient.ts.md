# ChatClient.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/ChatClient.ts`
- **Extension:** `.ts`
- **Size:** 12455 bytes
- **Centrality Score:** 0.0020
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 15

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ReadonlySignal`
- `SendTextError`
- `SendTextInput`
- `ChatClientOptions`
- `ChatDrafts`
- `ChatUnread`
- `ChatClient`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/constants/index.ts.md|packages/sdk/src/core/constants/index.ts]]
- [[packages/sdk/src/core/identifiers/PacketId.ts.md|packages/sdk/src/core/identifiers/PacketId.ts]]
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]
- [[packages/sdk/src/features/chat/application/SendTextUseCase.ts.md|packages/sdk/src/features/chat/application/SendTextUseCase.ts]]
- [[packages/sdk/src/features/chat/domain/DraftRepository.ts.md|packages/sdk/src/features/chat/domain/DraftRepository.ts]]
- [[packages/sdk/src/features/chat/domain/Message.ts.md|packages/sdk/src/features/chat/domain/Message.ts]]
- [[packages/sdk/src/features/chat/domain/MessageRepository.ts.md|packages/sdk/src/features/chat/domain/MessageRepository.ts]]
- [[packages/sdk/src/features/chat/domain/MessageState.ts.md|packages/sdk/src/features/chat/domain/MessageState.ts]]
- [[packages/sdk/src/features/chat/infrastructure/MessageMapper.ts.md|packages/sdk/src/features/chat/infrastructure/MessageMapper.ts]]
- [[packages/sdk/src/features/chat/infrastructure/repositories/InMemoryDraftRepository.ts.md|packages/sdk/src/features/chat/infrastructure/repositories/InMemoryDraftRepository.ts]]
- [[packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.ts.md|packages/sdk/src/features/chat/infrastructure/repositories/InMemoryMessageRepository.ts]]
- [[packages/sdk/src/features/chat/state/chatStore.ts.md|packages/sdk/src/features/chat/state/chatStore.ts]]
- [[packages/sdk/src/features/chat/state/draftStore.ts.md|packages/sdk/src/features/chat/state/draftStore.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/features/chat/index.ts.md|packages/sdk/src/features/chat/index.ts]]

## Source Code Snippet
```ts
import { signal } from "@preact/signals-core";
import type { ResultType } from "better-result";
import type { MeshClient } from "../../core/client/MeshClient.ts";
import { Constants } from "../../core/constants/index.ts";
import { generatePacketId } from "../../core/identifiers/PacketId.ts";
import {
  type ReadonlySignal,
  toReadonly,
} from "../../core/signals/createStore.ts";
import type { ChannelNumber } from "../../core/types.ts";
import type { DraftRepository } from "./domain/DraftRepository.ts";
import type { Message } from "./domain/Message.ts";
import type {
  ConversationKey,
  MessageRepository,
  RetentionPolicy,
} from "./domain/MessageRepository.ts";
import { MessageState } from "./domain/MessageState.ts";
import { MessageMapper } from "./infrastructure/MessageMapper.ts";
import { InMemoryDraftRepository } from "./infrastructure/repositories/InMemoryDraftRepository.ts";
...
```