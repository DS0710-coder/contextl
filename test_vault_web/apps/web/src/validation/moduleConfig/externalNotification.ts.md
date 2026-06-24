# externalNotification.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/moduleConfig/externalNotification.ts`
- **Extension:** `.ts`
- **Size:** 715 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ExternalNotificationValidation`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/ModuleConfig/ExternalNotification.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/ExternalNotification.tsx]]

## Source Code Snippet
```ts
import { z } from "zod/v4";

export const ExternalNotificationValidationSchema = z.object({
  enabled: z.boolean(),
  outputMs: z.coerce.number().int().min(0),
  output: z.coerce.number().int().min(0),
  outputVibra: z.coerce.number().int().min(0),
  outputBuzzer: z.coerce.number().int().min(0),
  active: z.boolean(),
  alertMessage: z.boolean(),
  alertMessageVibra: z.boolean(),
  alertMessageBuzzer: z.boolean(),
  alertBell: z.boolean(),
  alertBellVibra: z.boolean(),
  alertBellBuzzer: z.boolean(),
  usePwm: z.boolean(),
  nagTimeout: z.coerce.number().int().min(0),
  useI2sAsBuzzer: z.boolean(),
});

...
```