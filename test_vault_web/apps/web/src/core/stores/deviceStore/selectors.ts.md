# selectors.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/stores/deviceStore/selectors.ts`
- **Extension:** `.ts`
- **Size:** 2877 bytes
- **Centrality Score:** 0.0027
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useActiveConnection`
- `useDefaultConnection`
- `useFirstSavedConnection`
- `useAddSavedConnection`
- `useUpdateSavedConnection`
- `useRemoveSavedConnection`
- `useActiveConnectionId`
- `useSetActiveConnectionId`
- `useConnectionStatus`
- `useDeviceForConnection`
- `useConnectionForDevice`
- `useIsConnecting`
- `useConnectionError`
- `useSavedConnections`
- `useIsConnected`

## Imports (Dependencies)
- [[apps/web/src/core/stores/deviceStore/index.ts.md|apps/web/src/core/stores/deviceStore/index.ts]]
- [[apps/web/src/core/stores/deviceStore/types.ts.md|apps/web/src/core/stores/deviceStore/types.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Sidebar.tsx.md|apps/web/src/components/Sidebar.tsx]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]

## Source Code Snippet
```ts
import type { Device } from "./index.ts";
import { useDeviceStore } from "./index.ts";
import type { Connection, ConnectionId } from "./types.ts";

/**
 * Hook to get the currently active connection
 */
export function useActiveConnection(): Connection | undefined {
  return useDeviceStore((s) => s.getActiveConnection());
}

/**
 * Hook to get the HTTP connection marked as default
 */
export function useDefaultConnection(): Connection | undefined {
  return useDeviceStore((s) => s.savedConnections.find((c) => c.isDefault));
}

/**
 * Hook to get the first saved connection
...
```