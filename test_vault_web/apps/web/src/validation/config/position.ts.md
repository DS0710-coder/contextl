# position.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/config/position.ts`
- **Extension:** `.ts`
- **Size:** 965 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PositionValidation`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Settings/Position.tsx.md|apps/web/src/components/PageComponents/Settings/Position.tsx]]

## Source Code Snippet
```ts
import { Protobuf } from "@meshtastic/sdk";
import { z } from "zod/v4";

const GpsModeEnum = z.enum(Protobuf.Config.Config_PositionConfig_GpsMode);

export const PositionValidationSchema = z.object({
  positionBroadcastSecs: z.coerce.number().int().min(0),
  positionBroadcastSmartEnabled: z.boolean(),
  fixedPosition: z.boolean(),
  gpsUpdateInterval: z.coerce.number().int().min(0),
  positionFlags: z.coerce.number().int().min(0),
  rxGpio: z.coerce.number().int().min(0),
  txGpio: z.coerce.number().int().min(0),
  broadcastSmartMinimumDistance: z.coerce.number().int().min(0),
  broadcastSmartMinimumIntervalSecs: z.coerce.number().int().min(0),
  gpsEnGpio: z.coerce.number().int().min(0),
  gpsMode: GpsModeEnum,
  latitude: z.coerce.number().min(-90).max(90).optional(),
  longitude: z.coerce.number().min(-180).max(180).optional(),
  altitude: z.coerce.number().optional(),
...
```