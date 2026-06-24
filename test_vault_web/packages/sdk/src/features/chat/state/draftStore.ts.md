# draftStore.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/state/draftStore.ts`
- **Extension:** `.ts`
- **Size:** 1223 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ReadonlySignal`
- `ConversationKey`
- `DraftStore`

## Imports (Dependencies)
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/features/chat/domain/MessageRepository.ts.md|packages/sdk/src/features/chat/domain/MessageRepository.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/chat/ChatClient.ts.md|packages/sdk/src/features/chat/ChatClient.ts]]

## Source Code Snippet
```ts
import { type Signal, signal } from "@preact/signals-core";
import {
  type ReadonlySignal,
  toReadonly,
} from "../../../core/signals/createStore.ts";
import {
  type ConversationKey,
  conversationKeyString,
} from "../domain/MessageRepository.ts";

/**
 * Per-conversation draft text exposed as readonly signals. Lazy creation:
 * a signal is only allocated when a consumer subscribes to that
 * conversation's draft.
 */
export class DraftStore {
  private readonly buckets = new Map<string, Signal<string>>();
  private readonly read = new Map<string, ReadonlySignal<string>>();

  get(key: ConversationKey): ReadonlySignal<string> {
...
```