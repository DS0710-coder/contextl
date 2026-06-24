# GetMetadataUseCase.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/device/application/GetMetadataUseCase.ts`
- **Extension:** `.ts`
- **Size:** 433 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `getMetadata`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]
- [[packages/sdk/src/features/device/infrastructure/AdminMessageSender.ts.md|packages/sdk/src/features/device/infrastructure/AdminMessageSender.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/device/DeviceClient.ts.md|packages/sdk/src/features/device/DeviceClient.ts]]

## Source Code Snippet
```ts
import type { MeshClient } from "../../../core/client/MeshClient.ts";
import { ChannelNumber } from "../../../core/types.ts";
import { sendAdminMessage } from "../infrastructure/AdminMessageSender.ts";

export function getMetadata(
  client: MeshClient,
  nodeNum: number,
): Promise<number> {
  return sendAdminMessage(
    client,
    { case: "getDeviceMetadataRequest", value: true },
    nodeNum,
    ChannelNumber.Admin,
  );
}
```