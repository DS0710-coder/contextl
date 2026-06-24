# channel.test.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/channel.test.ts`
- **Extension:** `.ts`
- **Size:** 3652 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `makeBase64OfLength`

## Imports (Dependencies)
- [[apps/web/src/validation/channel.ts.md|apps/web/src/validation/channel.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { fromByteArray } from "base64-js";
import { describe, expect, it } from "vitest";
import { makeChannelSchema } from "./channel.ts";

const mockRole = 0;

function makeBase64OfLength(len: number): string {
  return fromByteArray(new Uint8Array(len));
}

describe("makeChannelSchema", () => {
  const allowedBytes = 16;
  const schema = makeChannelSchema(allowedBytes);

  const validBase64 = makeBase64OfLength(allowedBytes);

  const validSettings = {
    channelNum: 3,
    psk: validBase64,
    name: "TestName",
...
```