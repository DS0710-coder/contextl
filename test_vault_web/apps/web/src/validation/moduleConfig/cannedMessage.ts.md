# cannedMessage.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/moduleConfig/cannedMessage.ts`
- **Extension:** `.ts`
- **Size:** 773 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `CannedMessageValidation`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/ModuleConfig/CannedMessage.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/CannedMessage.tsx]]

## Source Code Snippet
```ts
import { Protobuf } from "@meshtastic/sdk";
import { z } from "zod/v4";

const InputEventCharEnum = z.enum(
  Protobuf.ModuleConfig.ModuleConfig_CannedMessageConfig_InputEventChar,
);

export const CannedMessageValidationSchema = z.object({
  rotary1Enabled: z.boolean(),
  inputbrokerPinA: z.coerce.number().int().min(0),
  inputbrokerPinB: z.coerce.number().int().min(0),
  inputbrokerPinPress: z.coerce.number().int().min(0),
  inputbrokerEventCw: InputEventCharEnum,
  inputbrokerEventCcw: InputEventCharEnum,
  inputbrokerEventPress: InputEventCharEnum,
  updown1Enabled: z.boolean(),
  enabled: z.boolean(),
  allowInputSource: z.string().max(30),
  sendBell: z.boolean(),
});
...
```