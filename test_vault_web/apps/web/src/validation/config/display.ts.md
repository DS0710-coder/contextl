# display.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/config/display.ts`
- **Extension:** `.ts`
- **Size:** 1113 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DisplayValidation`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Settings/Display.tsx.md|apps/web/src/components/PageComponents/Settings/Display.tsx]]

## Source Code Snippet
```ts
import { Protobuf } from "@meshtastic/sdk";
import { z } from "zod/v4";

const GpsCoordinateEnum = z.enum(
  Protobuf.Config.Config_DisplayConfig_DeprecatedGpsCoordinateFormat,
);
const DisplayUnitsEnum = z.enum(
  Protobuf.Config.Config_DisplayConfig_DisplayUnits,
);
const OledTypeEnum = z.enum(Protobuf.Config.Config_DisplayConfig_OledType);
const DisplayModeEnum = z.enum(
  Protobuf.Config.Config_DisplayConfig_DisplayMode,
);
const CompassOrientationEnum = z.enum(
  Protobuf.Config.Config_DisplayConfig_CompassOrientation,
);

export const DisplayValidationSchema = z.object({
  screenOnSecs: z.coerce.number().int().min(0),
  gpsFormat: GpsCoordinateEnum,
...
```