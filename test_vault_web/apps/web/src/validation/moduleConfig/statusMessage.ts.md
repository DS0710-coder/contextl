# statusMessage.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/moduleConfig/statusMessage.ts`
- **Extension:** `.ts`
- **Size:** 214 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `StatusMessageValidation`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/ModuleConfig/StatusMessage.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/StatusMessage.tsx]]

## Source Code Snippet
```ts
import { z } from "zod/v4";

export const StatusMessageValidationSchema = z.object({
  nodeStatus: z.string().max(200),
});

export type StatusMessageValidation = z.infer<
  typeof StatusMessageValidationSchema
>;
```