# storeForward.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/moduleConfig/storeForward.ts`
- **Extension:** `.ts`
- **Size:** 401 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `StoreForwardValidation`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/ModuleConfig/StoreForward.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/StoreForward.tsx]]

## Source Code Snippet
```ts
import { z } from "zod/v4";

export const StoreForwardValidationSchema = z.object({
  enabled: z.boolean(),
  heartbeat: z.boolean(),
  records: z.coerce.number().int().min(0),
  historyReturnMax: z.coerce.number().int().min(0),
  historyReturnWindow: z.coerce.number().int().min(0),
  isServer: z.boolean(),
});

export type StoreForwardValidation = z.infer<
  typeof StoreForwardValidationSchema
>;
```