# pskSchema.test.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/pskSchema.test.ts`
- **Extension:** `.ts`
- **Size:** 6337 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `makeBase64OfLength`

## Imports (Dependencies)
- [[apps/web/src/validation/pskSchema.ts.md|apps/web/src/validation/pskSchema.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { fromByteArray } from "base64-js";
import { describe, expect, it } from "vitest";
import { makePskHelpers } from "./pskSchema.ts";

function makeBase64OfLength(len: number): string {
  return fromByteArray(new Uint8Array(len));
}

describe("stringSchema", () => {
  it("accepts valid base64 string of allowed length", () => {
    const { stringSchema } = makePskHelpers([16]);
    const valid = makeBase64OfLength(16);
    expect(() => stringSchema().parse(valid)).not.toThrow();
  });

  it("rejects base64 string of disallowed length", () => {
    const { stringSchema, msgs } = makePskHelpers([16]);
    const invalid = makeBase64OfLength(8);
    const result = stringSchema().safeParse(invalid);
    expect(result.success).toBe(false);
...
```