# heartbeat.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/connections/heartbeat.ts`
- **Extension:** `.ts`
- **Size:** 1542 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `stopHeartbeat`
- `startConfigHeartbeat`
- `startMaintenanceHeartbeat`

## Imports (Dependencies)
- [[apps/web/src/core/stores/deviceStore/types.ts.md|apps/web/src/core/stores/deviceStore/types.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Connections/useConnections.ts.md|apps/web/src/pages/Connections/useConnections.ts]]

## Source Code Snippet
```ts
import type { ConnectionId } from "@core/stores/deviceStore/types";
import type { MeshDevice } from "@meshtastic/sdk";

const HEARTBEAT_INTERVAL_MS = 5 * 60 * 1000; // 5 minutes (post-config)
const CONFIG_HEARTBEAT_INTERVAL_MS = 5_000; // 5s (during initial config)

const heartbeats = new Map<ConnectionId, ReturnType<typeof setInterval>>();

/**
 * Stops + clears any active heartbeat for the connection. Safe to call when
 * no heartbeat is running.
 */
export function stopHeartbeat(id: ConnectionId): void {
  const h = heartbeats.get(id);
  if (!h) return;
  clearInterval(h);
  heartbeats.delete(id);
}

/**
...
```