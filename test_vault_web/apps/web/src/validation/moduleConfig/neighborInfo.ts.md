# neighborInfo.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/moduleConfig/neighborInfo.ts`
- **Extension:** `.ts`
- **Size:** 283 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NeighborInfoValidation`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/ModuleConfig/NeighborInfo.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/NeighborInfo.tsx]]

## Source Code Snippet
```ts
import { z } from "zod/v4";

export const NeighborInfoValidationSchema = z.object({
  enabled: z.boolean(),
  updateInterval: z.coerce.number().int().min(0),
  transmitOverLora: z.boolean(),
});

export type NeighborInfoValidation = z.infer<
  typeof NeighborInfoValidationSchema
>;
```