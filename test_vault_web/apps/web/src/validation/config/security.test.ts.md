# security.test.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/config/security.test.ts`
- **Extension:** `.ts`
- **Size:** 3199 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `makeBase64OfLength`

## Imports (Dependencies)
- [[apps/web/src/validation/config/security.ts.md|apps/web/src/validation/config/security.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { fromByteArray } from "base64-js";
import { describe, expect, it } from "vitest";
import { ParsedSecuritySchema, RawSecuritySchema } from "./security.ts";

function makeBase64OfLength(len: number): string {
  return fromByteArray(new Uint8Array(len));
}

describe("RawSecuritySchema", () => {
  const validKey = makeBase64OfLength(32);

  it("accepts valid security config", () => {
    const result = RawSecuritySchema.safeParse({
      isManaged: false,
      adminChannelEnabled: true,
      debugLogApiEnabled: false,
      serialEnabled: true,
      privateKey: validKey,
      publicKey: validKey,
      adminKey: [validKey, "", ""],
...
```