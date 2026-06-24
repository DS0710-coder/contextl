# bluetooth.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/config/bluetooth.ts`
- **Extension:** `.ts`
- **Size:** 407 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BluetoothValidation`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Settings/Bluetooth.tsx.md|apps/web/src/components/PageComponents/Settings/Bluetooth.tsx]]

## Source Code Snippet
```ts
import { Protobuf } from "@meshtastic/sdk";
import { z } from "zod/v4";

const PairingModeEnum = z.enum(
  Protobuf.Config.Config_BluetoothConfig_PairingMode,
);

export const BluetoothValidationSchema = z.object({
  enabled: z.boolean(),
  mode: PairingModeEnum,
  fixedPin: z.coerce.number().int().min(100000).max(999999),
});

export type BluetoothValidation = z.infer<typeof BluetoothValidationSchema>;
```