# sqlocal-opfs.browser.test.ts

## Architecture Metrics
- **Path:** `packages/sdk-storage-sqlocal/tests/sqlocal-opfs.browser.test.ts`
- **Extension:** `.ts`
- **Size:** 1543 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `msg`

## Imports (Dependencies)
- [[packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.ts.md|packages/sdk-storage-sqlocal/src/chat/SqlocalMessageRepository.ts]]
- [[packages/sdk-storage-sqlocal/src/db.ts.md|packages/sdk-storage-sqlocal/src/db.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { ChannelNumber, type Message, MessageState } from "@meshtastic/sdk";
import { describe, expect, it } from "vitest";
import { SqlocalMessageRepository } from "../src/chat/SqlocalMessageRepository.ts";
import { createSqlocalDb } from "../src/db.ts";

/**
 * Browser-mode end-to-end test: opens a real OPFS-backed SQLite database via
 * sqlocal, exercises the chat repository, asserts persistence across two
 * separate `createSqlocalDb()` calls (simulating page reload).
 *
 * Run with `pnpm --filter @meshtastic/sdk-storage-sqlocal test:browser`.
 */

function msg(id: number, ms: number, text = "t"): Message {
  return {
    id,
    from: 1,
    to: 0xffffffff,
    channel: ChannelNumber.Primary,
    rxTime: new Date(ms),
...
```