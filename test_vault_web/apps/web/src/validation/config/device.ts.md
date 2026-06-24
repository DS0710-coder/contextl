# device.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/config/device.ts`
- **Extension:** `.ts`
- **Size:** 763 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DeviceValidation`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Settings/Device/index.tsx.md|apps/web/src/components/PageComponents/Settings/Device/index.tsx]]

## Source Code Snippet
```ts
import { Protobuf } from "@meshtastic/sdk";
import { z } from "zod/v4";

const RoleEnum = z.enum(Protobuf.Config.Config_DeviceConfig_Role);
const RebroadcastModeEnum = z.enum(
  Protobuf.Config.Config_DeviceConfig_RebroadcastMode,
);

export const DeviceValidationSchema = z.object({
  role: RoleEnum,
  serialEnabled: z.boolean(),
  buttonGpio: z.coerce.number().int().min(0),
  buzzerGpio: z.coerce.number().int().min(0),
  rebroadcastMode: RebroadcastModeEnum,
  nodeInfoBroadcastSecs: z.coerce.number().int().min(0),
  doubleTapAsButtonPress: z.boolean(),
  isManaged: z.boolean(),
  disableTripleClick: z.boolean(),
  ledHeartbeatDisabled: z.boolean(),
  tzdef: z.string().max(65),
...
```