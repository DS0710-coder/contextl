# detectionSensor.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/moduleConfig/detectionSensor.ts`
- **Extension:** `.ts`
- **Size:** 662 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DetectionSensorValidation`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/ModuleConfig/DetectionSensor.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/DetectionSensor.tsx]]

## Source Code Snippet
```ts
import { Protobuf } from "@meshtastic/sdk";
import { z } from "zod/v4";

const detectionTriggerTypeEnum = z.enum(
  Protobuf.ModuleConfig.ModuleConfig_DetectionSensorConfig_TriggerType,
);

export const DetectionSensorValidationSchema = z.object({
  enabled: z.boolean(),
  minimumBroadcastSecs: z.coerce.number().int().min(0),
  stateBroadcastSecs: z.coerce.number().int().min(0),
  sendBell: z.boolean(),
  name: z.string().min(0).max(20),
  monitorPin: z.coerce.number().int().min(0),
  detectionTriggerType: detectionTriggerTypeEnum,
  usePullup: z.boolean(),
});

export type DetectionSensorValidation = z.infer<
  typeof DetectionSensorValidationSchema
...
```