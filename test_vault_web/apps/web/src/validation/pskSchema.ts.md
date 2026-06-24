# pskSchema.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/pskSchema.ts`
- **Extension:** `.ts`
- **Size:** 2013 bytes
- **Centrality Score:** 0.0031
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `makePskHelpers`
- `tryParse`
- `isValidString`
- `isValidKey`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/validation/channel.ts.md|apps/web/src/validation/channel.ts]]
- [[apps/web/src/validation/config/security.ts.md|apps/web/src/validation/config/security.ts]]
- [[apps/web/src/validation/pskSchema.test.ts.md|apps/web/src/validation/pskSchema.test.ts]]

## Source Code Snippet
```ts
import { toByteArray } from "base64-js";
import { type ZodType, z } from "zod/v4";

export function makePskHelpers(allowedByteLengths: readonly number[]) {
  const bitsLabel = allowedByteLengths.map((b) => b * 8).join(" | ");
  const msgs = {
    format: "formValidation.invalidFormat.key",
    required: "formValidation.required.key",
    length: `formValidation.pskLength.${bitsLabel.replace(/ \| /g, "_")}bit`,
  } as const;

  function tryParse(str: string): Uint8Array | null {
    try {
      return toByteArray(str);
    } catch {
      return null;
    }
  }

  function isValidString(str: string): boolean {
...
```