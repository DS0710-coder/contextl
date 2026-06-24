# mqtt.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/moduleConfig/mqtt.ts`
- **Extension:** `.ts`
- **Size:** 738 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `MqttValidation`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/ModuleConfig/MQTT.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/MQTT.tsx]]

## Source Code Snippet
```ts
import { z } from "zod/v4";

export const MqttValidationMapReportSettingsSchema = z.object({
  publishIntervalSecs: z.coerce.number().int(),
  positionPrecision: z.coerce.number().int(),
  shouldReportLocation: z.boolean(),
});

export const MqttValidationSchema = z.object({
  enabled: z.boolean(),
  address: z.string().min(0).max(63),
  username: z.string().min(0).max(63),
  password: z.string().min(0).max(63),
  encryptionEnabled: z.boolean(),
  jsonEnabled: z.boolean(),
  tlsEnabled: z.boolean(),
  root: z.string().max(31),
  proxyToClientEnabled: z.boolean(),
  mapReportingEnabled: z.boolean(),
  mapReportSettings: MqttValidationMapReportSettingsSchema,
...
```