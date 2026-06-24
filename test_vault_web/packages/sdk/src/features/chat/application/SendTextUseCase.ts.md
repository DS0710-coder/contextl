# SendTextUseCase.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/application/SendTextUseCase.ts`
- **Extension:** `.ts`
- **Size:** 2520 bytes
- **Centrality Score:** 0.0017
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Destination`
- `SendTextInput`
- `EmptyMessageError`
- `MessageTooLongError`
- `SendTextError`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/chat/ChatClient.send.test.ts.md|packages/sdk/src/features/chat/ChatClient.send.test.ts]]
- [[packages/sdk/src/features/chat/ChatClient.ts.md|packages/sdk/src/features/chat/ChatClient.ts]]
- [[packages/sdk/src/features/chat/application/SendTextUseCase.test.ts.md|packages/sdk/src/features/chat/application/SendTextUseCase.test.ts]]
- [[packages/sdk/src/features/chat/index.ts.md|packages/sdk/src/features/chat/index.ts]]

## Source Code Snippet
```ts
import * as Protobuf from "@meshtastic/protobufs";
import { Result } from "better-result";
import type { ResultType } from "better-result";
import type { MeshClient } from "../../../core/client/MeshClient.ts";
import {
  ChannelNumber,
  type Destination,
  Emitter,
} from "../../../core/types.ts";

export interface SendTextInput {
  text: string;
  destination?: Destination;
  wantAck?: boolean;
  channel?: ChannelNumber;
  replyId?: number;
  emoji?: number;
  /**
   * Override the auto-generated packet id. Used by callers (e.g. the
   * chat slice's optimistic-append path) that need to know the id
...
```