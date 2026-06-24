# ChatClient.send.test.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/ChatClient.send.test.ts`
- **Extension:** `.ts`
- **Size:** 5779 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `SendResult`
- `sendBroadcast`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/testing/createFakeTransport.ts.md|packages/sdk/src/core/testing/createFakeTransport.ts]]
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]
- [[packages/sdk/src/features/chat/application/SendTextUseCase.ts.md|packages/sdk/src/features/chat/application/SendTextUseCase.ts]]
- [[packages/sdk/src/features/chat/domain/MessageState.ts.md|packages/sdk/src/features/chat/domain/MessageState.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import type { ResultType } from "better-result";
import { describe, expect, it } from "vitest";
import { MeshClient } from "../../core/client/MeshClient.ts";
import { createFakeTransport } from "../../core/testing/createFakeTransport.ts";
import { ChannelNumber } from "../../core/types.ts";
import type { SendTextError } from "./application/SendTextUseCase.ts";
import { MessageState } from "./domain/MessageState.ts";

type SendResult = ResultType<number, SendTextError>;

/**
 * `client.chat.send` resolves only after the packet is ack'd via
 * `client.queue.processAck(id)`. The fake transport doesn't drive that
 * for us, so this helper polls the queue and acks any pending items
 * until the send promise settles.
 */
async function withAckFlush<T>(
  client: MeshClient,
  run: () => Promise<T>,
): Promise<T> {
...
```