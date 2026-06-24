# SendTextUseCase.test.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/application/SendTextUseCase.test.ts`
- **Extension:** `.ts`
- **Size:** 1693 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `makeClient`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/features/chat/application/SendTextUseCase.ts.md|packages/sdk/src/features/chat/application/SendTextUseCase.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { Result } from "better-result";
import { describe, expect, it, vi } from "vitest";
import {
  EmptyMessageError,
  MessageTooLongError,
  sendText,
} from "./SendTextUseCase.ts";
import type { MeshClient } from "../../../core/client/MeshClient.ts";

function makeClient(sendPacket = vi.fn().mockResolvedValue(123)) {
  return {
    log: { debug: vi.fn() },
    sendPacket,
  } as unknown as MeshClient;
}

describe("sendText", () => {
  it("rejects empty text with EmptyMessageError", async () => {
    const client = makeClient();
    const result = await sendText(client, { text: "" });
...
```