# network.ts

## Architecture Metrics
- **Path:** `apps/web/src/validation/config/network.ts`
- **Extension:** `.ts`
- **Size:** 834 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NetworkValidation`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Settings/Network/index.tsx.md|apps/web/src/components/PageComponents/Settings/Network/index.tsx]]

## Source Code Snippet
```ts
import { Protobuf } from "@meshtastic/sdk";
import { z } from "zod/v4";

const AddressModeEnum = z.enum(
  Protobuf.Config.Config_NetworkConfig_AddressMode,
);
const ProtocolFlagsEnum = z.enum(
  Protobuf.Config.Config_NetworkConfig_ProtocolFlags,
);

export const NetworkValidationIpV4ConfigSchema = z.object({
  ip: z.ipv4(),
  gateway: z.ipv4(),
  subnet: z.ipv4(),
  dns: z.ipv4(),
});

export const NetworkValidationSchema = z.object({
  wifiEnabled: z.boolean(),
  wifiSsid: z.string().max(33),
...
```