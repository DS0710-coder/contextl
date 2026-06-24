# SqlocalMessageRepository.test.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.test.ts`
- **Extension:** `.ts`
- **Size:** 3188 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `msg`

## Imports (Dependencies)
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.ts]]
- [[packages/sdk-storage-sqlocal/src/db.ts.md|packages/sdk-storage-sqlocal/src/db.ts]]
- [[packages/sdk-storage-sqlocal/src/testing/createMemoryDb.ts.md|packages/sdk-storage-sqlocal/src/testing/createMemoryDb.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { ChannelNumber, type Message, MessageState } from "@meshtastic/sdk";
import { beforeEach, describe, expect, it } from "vitest";
import type { SqlocalDb } from "../db.ts";
import { createMemoryDb } from "../testing/createMemoryDb.ts";
import { SqlocalMessageRepository } from "./SqlocalMessageRepository.ts";

function msg(id: number, ms: number, text = "t"): Message {
  return {
    id,
    from: 1,
    to: 0xffffffff,
    channel: ChannelNumber.Primary,
    rxTime: new Date(ms),
    type: "broadcast",
    text,
    state: MessageState.Ack,
  };
}

describe("SqlocalMessageRepository (sql.js test driver)", () => {
...
```