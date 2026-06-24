# security.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/config/security.ts`
- **Extension:** `.ts`
- **Size:** 1359 bytes
- **Centrality Score:** 0.0015
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `makeSecuritySchema`
- `RawSecurity`
- `ParsedSecurity`

## Imports (Dependencies)
- [[apps/web/src/validation/pskSchema.ts.md|apps/web/src/validation/pskSchema.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Settings/Security/Security.tsx.md|apps/web/src/components/PageComponents/Settings/Security/Security.tsx]]
- [[apps/web/src/validation/config/security.test.ts.md|apps/web/src/validation/config/security.test.ts]]

## Source Code Snippet
```ts
import { type ZodType, z } from "zod/v4";
import { makePskHelpers } from "./../pskSchema.ts";

const { stringSchema, bytesSchema, isValidKey } = makePskHelpers([32]); // 256-bit

const isManagedRequiredMsg = "formValidation.required.managed";

function makeSecuritySchema<KeyT>(
  keyMaker: (optional: boolean) => ZodType<KeyT>,
) {
  return z
    .object({
      isManaged: z.boolean(),
      adminChannelEnabled: z.boolean(),
      debugLogApiEnabled: z.boolean(),
      serialEnabled: z.boolean(),

      privateKey: keyMaker(false),
      publicKey: keyMaker(false),
      adminKey: z.tuple([keyMaker(true), keyMaker(true), keyMaker(true)]),
...
```