# RebootService.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/device/application/RebootService.ts`
- **Extension:** `.ts`
- **Size:** 1103 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `shutdown`
- `reboot`
- `rebootOta`
- `factoryResetDevice`
- `factoryResetConfig`
- `enterDfuMode`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/features/device/infrastructure/AdminMessageSender.ts.md|packages/sdk/src/features/device/infrastructure/AdminMessageSender.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/device/DeviceClient.ts.md|packages/sdk/src/features/device/DeviceClient.ts]]

## Source Code Snippet
```ts
import type { MeshClient } from "../../../core/client/MeshClient.ts";
import { sendAdminMessage } from "../infrastructure/AdminMessageSender.ts";

export function shutdown(client: MeshClient, seconds: number): Promise<number> {
  return sendAdminMessage(client, { case: "shutdownSeconds", value: seconds });
}

export function reboot(client: MeshClient, seconds: number): Promise<number> {
  return sendAdminMessage(client, { case: "rebootSeconds", value: seconds });
}

export function rebootOta(
  client: MeshClient,
  seconds: number,
): Promise<number> {
  return sendAdminMessage(client, { case: "rebootOtaSeconds", value: seconds });
}

export function factoryResetDevice(client: MeshClient): Promise<number> {
  return sendAdminMessage(client, { case: "factoryResetDevice", value: 1 });
...
```