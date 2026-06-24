# channel.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/channel.ts`
- **Extension:** `.ts`
- **Size:** 1292 bytes
- **Centrality Score:** 0.0015
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `makeChannelSchema`
- `ChannelValidation`

## Imports (Dependencies)
- [[apps/web/src/core/utils/string.ts.md|apps/web/src/core/utils/string.ts]]
- [[apps/web/src/validation/pskSchema.ts.md|apps/web/src/validation/pskSchema.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Channels/Channel.tsx.md|apps/web/src/components/PageComponents/Channels/Channel.tsx]]
- [[apps/web/src/validation/channel.test.ts.md|apps/web/src/validation/channel.test.ts]]

## Source Code Snippet
```ts
import { validateMaxByteLength } from "@core/utils/string.ts";
import { Protobuf } from "@meshtastic/sdk";
import { z } from "zod/v4";
import { makePskHelpers } from "./pskSchema.ts";

const RoleEnum = z.enum(Protobuf.Channel.Channel_Role);

const moduleSettingsSchema = z.object({
  positionPrecision: z.union([
    z.literal(0),
    z.coerce.number().int().min(10).max(19),
    z.literal(32),
  ]),
});

export function makeChannelSchema(allowedBytes: number) {
  const { stringSchema } = makePskHelpers([allowedBytes]);

  const ChannelSettingsSchema = z.object({
    channelNum: z.coerce.number().int().min(0).max(7),
...
```