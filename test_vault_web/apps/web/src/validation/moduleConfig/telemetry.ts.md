# telemetry.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/moduleConfig/telemetry.ts`
- **Extension:** `.ts`
- **Size:** 709 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TelemetryValidation`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/ModuleConfig/Telemetry.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Telemetry.tsx]]

## Source Code Snippet
```ts
import { z } from "zod/v4";

export const TelemetryValidationSchema = z.object({
  deviceTelemetryEnabled: z.boolean(),
  deviceUpdateInterval: z.coerce.number().int().min(0),
  environmentUpdateInterval: z.coerce.number().int().min(0),
  environmentMeasurementEnabled: z.boolean(),
  environmentScreenEnabled: z.boolean(),
  environmentDisplayFahrenheit: z.boolean(),
  airQualityEnabled: z.boolean(),
  airQualityInterval: z.coerce.number().int().min(0),
  powerMeasurementEnabled: z.boolean(),
  powerUpdateInterval: z.coerce.number().int().min(0),
  powerScreenEnabled: z.boolean(),
  airQualityScreenEnabled: z.boolean(),
});

export type TelemetryValidation = z.infer<typeof TelemetryValidationSchema>;
```