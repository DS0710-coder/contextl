# chatStore.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/state/chatStore.ts`
- **Extension:** `.ts`
- **Size:** 3374 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ChatStore`

## Imports (Dependencies)
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]
- [[packages/sdk/src/features/chat/domain/Message.ts.md|packages/sdk/src/features/chat/domain/Message.ts]]
- [[packages/sdk/src/features/chat/domain/MessageState.ts.md|packages/sdk/src/features/chat/domain/MessageState.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/chat/ChatClient.ts.md|packages/sdk/src/features/chat/ChatClient.ts]]

## Source Code Snippet
```ts
import { type Signal, signal } from "@preact/signals-core";
import type { ReadonlySignal } from "../../../core/signals/createStore.ts";
import { toReadonly } from "../../../core/signals/createStore.ts";
import type { ChannelNumber } from "../../../core/types.ts";
import type { Message } from "../domain/Message.ts";
import { MessageState } from "../domain/MessageState.ts";

/**
 * Messages grouped by conversation bucket. Direct messages are keyed by
 * `direct:<peerNodeNum>`; broadcast messages by `channel:<channelNumber>`.
 */
export class ChatStore {
  private readonly buckets = new Map<string, Signal<Message[]>>();
  private readonly readBuckets = new Map<string, ReadonlySignal<Message[]>>();

  channelKey(channel: ChannelNumber): string {
    return `channel:${channel}`;
  }

  directKey(peer: number): string {
...
```