# HeartbeatService.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/device/application/HeartbeatService.ts`
- **Extension:** `.ts`
- **Size:** 296 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `startHeartbeat`
- `sendHeartbeat`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import type { MeshClient } from "../../../core/client/MeshClient.ts";

export function startHeartbeat(client: MeshClient, intervalMs: number): void {
  client.setHeartbeatInterval(intervalMs);
}

export function sendHeartbeat(client: MeshClient): Promise<number> {
  return client.heartbeat();
}
```