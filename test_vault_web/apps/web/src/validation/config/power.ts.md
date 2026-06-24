# power.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/config/power.ts`
- **Extension:** `.ts`
- **Size:** 545 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PowerValidation`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Settings/Power.tsx.md|apps/web/src/components/PageComponents/Settings/Power.tsx]]

## Source Code Snippet
```ts
import { z } from "zod/v4";

export const PowerValidationSchema = z.object({
  isPowerSaving: z.boolean(),
  onBatteryShutdownAfterSecs: z.coerce.number().int().min(0),
  adcMultiplierOverride: z.coerce.number().min(0).max(4),
  waitBluetoothSecs: z.coerce.number().int().min(0),
  sdsSecs: z.coerce.number().int().min(0),
  lsSecs: z.coerce.number().int().min(0),
  minWakeSecs: z.coerce.number().int().min(0),
  deviceBatteryInaAddress: z.coerce.number().int().min(0),
});

export type PowerValidation = z.infer<typeof PowerValidationSchema>;
```