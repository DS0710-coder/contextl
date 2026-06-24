# ambientLighting.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/moduleConfig/ambientLighting.ts`
- **Extension:** `.ts`
- **Size:** 400 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `AmbientLightingValidation`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/ModuleConfig/AmbientLighting.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/AmbientLighting.tsx]]

## Source Code Snippet
```ts
import { z } from "zod/v4";

export const AmbientLightingValidationSchema = z.object({
  ledState: z.boolean(),
  current: z.coerce.number().int().min(0),
  red: z.coerce.number().int().min(0).max(255),
  green: z.coerce.number().int().min(0).max(255),
  blue: z.coerce.number().int().min(0).max(255),
});

export type AmbientLightingValidation = z.infer<
  typeof AmbientLightingValidationSchema
>;
```