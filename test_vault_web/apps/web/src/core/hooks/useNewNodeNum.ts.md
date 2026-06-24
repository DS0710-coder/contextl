# useNewNodeNum.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useNewNodeNum.ts`
- **Extension:** `.ts`
- **Size:** 258 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useNewNodeNum`

## Imports (Dependencies)
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/core/subscriptions.ts.md|apps/web/src/core/subscriptions.ts]]

## Source Code Snippet
```ts
import { useDeviceStore } from "@core/stores";
import type { Protobuf } from "@meshtastic/sdk";

export function useNewNodeNum(
  id: number,
  nodeInfo: Protobuf.Mesh.MyNodeInfo,
): void {
  useDeviceStore.getState().getDevice(id)?.setHardware(nodeInfo);
}
```