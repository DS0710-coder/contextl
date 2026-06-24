# lora.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/config/lora.ts`
- **Extension:** `.ts`
- **Size:** 1265 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `LoRaValidation`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Settings/LoRa.tsx.md|apps/web/src/components/PageComponents/Settings/LoRa.tsx]]

## Source Code Snippet
```ts
import { Protobuf } from "@meshtastic/sdk";
import { z } from "zod/v4";

const ModemPresetEnum = z.enum(Protobuf.Config.Config_LoRaConfig_ModemPreset);
const RegionCodeEnum = z.enum(Protobuf.Config.Config_LoRaConfig_RegionCode);
const FemLnaModeEnum = z.enum(Protobuf.Config.Config_LoRaConfig_FEM_LNA_Mode);

export const LoRaValidationSchema = z.object({
  usePreset: z.boolean(),
  modemPreset: ModemPresetEnum,
  bandwidth: z.coerce.number().int(),
  spreadFactor: z.coerce.number().int().max(12),
  codingRate: z.coerce.number().int().min(0).max(10),
  frequencyOffset: z.coerce.number().int(),
  region: RegionCodeEnum,
  hopLimit: z.coerce.number().int().min(0).max(7),
  txEnabled: z.boolean(),
  txPower: z.coerce.number().int().min(0),
  channelNum: z.coerce.number().int(),
  overrideDutyCycle: z.boolean(),
...
```