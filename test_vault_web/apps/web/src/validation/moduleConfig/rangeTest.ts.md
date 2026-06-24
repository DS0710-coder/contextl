# rangeTest.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/moduleConfig/rangeTest.ts`
- **Extension:** `.ts`
- **Size:** 250 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `RangeTestValidation`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/ModuleConfig/RangeTest.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/RangeTest.tsx]]

## Source Code Snippet
```ts
import { z } from "zod/v4";

export const RangeTestValidationSchema = z.object({
  enabled: z.boolean(),
  sender: z.coerce.number().int().min(0),
  save: z.boolean(),
});

export type RangeTestValidation = z.infer<typeof RangeTestValidationSchema>;
```