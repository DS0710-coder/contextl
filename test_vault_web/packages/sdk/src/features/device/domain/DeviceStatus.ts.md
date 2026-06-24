# DeviceStatus.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/device/domain/DeviceStatus.ts`
- **Extension:** `.ts`
- **Size:** 464 bytes
- **Centrality Score:** 0.0020
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `isConnected`
- `isConfigured`

## Imports (Dependencies)
- [[packages/sdk/src/core/transport/Transport.ts.md|packages/sdk/src/core/transport/Transport.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/config/domain/ConfigEditor.ts.md|packages/sdk/src/features/config/domain/ConfigEditor.ts]]
- [[packages/sdk/src/features/device/index.ts.md|packages/sdk/src/features/device/index.ts]]

## Source Code Snippet
```ts
import { DeviceStatusEnum } from "../../../core/transport/Transport.ts";

export { DeviceStatusEnum };

export function isConnected(status: DeviceStatusEnum): boolean {
  return (
    status === DeviceStatusEnum.DeviceConnected ||
    status === DeviceStatusEnum.DeviceConfiguring ||
    status === DeviceStatusEnum.DeviceConfigured
  );
}

export function isConfigured(status: DeviceStatusEnum): boolean {
  return status === DeviceStatusEnum.DeviceConfigured;
}
```