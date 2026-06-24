# serial.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/moduleConfig/serial.ts`
- **Extension:** `.ts`
- **Size:** 653 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `SerialValidation`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/ModuleConfig/Serial.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Serial.tsx]]

## Source Code Snippet
```ts
import { Protobuf } from "@meshtastic/sdk";
import { z } from "zod/v4";

const Serial_BaudEnum = z.enum(
  Protobuf.ModuleConfig.ModuleConfig_SerialConfig_Serial_Baud,
);
const Serial_ModeEnum = z.enum(
  Protobuf.ModuleConfig.ModuleConfig_SerialConfig_Serial_Mode,
);

export const SerialValidationSchema = z.object({
  enabled: z.boolean(),
  echo: z.boolean(),
  rxd: z.coerce.number().int().min(0),
  txd: z.coerce.number().int().min(0),
  baud: Serial_BaudEnum,
  timeout: z.coerce.number().int().min(0),
  mode: Serial_ModeEnum,
  overrideConsoleSerialPort: z.boolean(),
});
...
```