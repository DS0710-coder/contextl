# audio.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/moduleConfig/audio.ts`
- **Extension:** `.ts`
- **Size:** 556 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `AudioValidation`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/ModuleConfig/Audio.tsx.md|apps/web/src/components/PageComponents/ModuleConfig/Audio.tsx]]

## Source Code Snippet
```ts
import { Protobuf } from "@meshtastic/sdk";
import { z } from "zod/v4";

const Audio_BaudEnum = z.enum(
  Protobuf.ModuleConfig.ModuleConfig_AudioConfig_Audio_Baud,
);

export const AudioValidationSchema = z.object({
  codec2Enabled: z.boolean(),
  pttPin: z.coerce.number().int().min(0),
  bitrate: Audio_BaudEnum,
  i2sWs: z.coerce.number().int().min(0),
  i2sSd: z.coerce.number().int().min(0),
  i2sDin: z.coerce.number().int().min(0),
  i2sSck: z.coerce.number().int().min(0),
});

export type AudioValidation = z.infer<typeof AudioValidationSchema>;
```