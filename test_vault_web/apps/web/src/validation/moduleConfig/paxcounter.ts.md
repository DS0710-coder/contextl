# paxcounter.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/moduleConfig/paxcounter.ts`
- **Extension:** `.ts`
- **Size:** 333 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PaxcounterValidation`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/ModuleConfig/Paxcounter.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Paxcounter.tsx]]

## Source Code Snippet
```ts
import { z } from "zod/v4";

export const PaxcounterValidationSchema = z.object({
  enabled: z.boolean(),
  paxcounterUpdateInterval: z.coerce.number().int().min(0),
  bleThreshold: z.coerce.number().int(),
  wifiThreshold: z.coerce.number().int(),
});

export type PaxcounterValidation = z.infer<typeof PaxcounterValidationSchema>;
```