# ChatClient.drafts.test.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/chat/ChatClient.drafts.test.ts`
- **Extension:** `.ts`
- **Size:** 1979 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/testing/createFakeTransport.ts.md|packages/sdk/src/core/testing/createFakeTransport.ts]]
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]
- [[packages/sdk/src/features/chat/infrastructure/repositories/InMemoryDraftRepository.ts.md|packages/sdk/src/features/chat/infrastructure/repositories/InMemoryDraftRepository.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { describe, expect, it } from "vitest";
import { MeshClient } from "../../core/client/MeshClient.ts";
import { createFakeTransport } from "../../core/testing/createFakeTransport.ts";
import { ChannelNumber } from "../../core/types.ts";
import { InMemoryDraftRepository } from "./infrastructure/repositories/InMemoryDraftRepository.ts";

describe("ChatClient drafts", () => {
  it("starts empty and tracks set/clear via the signal", () => {
    const { transport } = createFakeTransport();
    const client = new MeshClient({ transport });
    const conv = { kind: "channel" as const, channel: ChannelNumber.Primary };
    expect(client.chat.drafts.get(conv).value).toBe("");

    client.chat.drafts.set(conv, "wip text");
    expect(client.chat.drafts.get(conv).value).toBe("wip text");

    client.chat.drafts.clear(conv);
    expect(client.chat.drafts.get(conv).value).toBe("");
  });

...
```