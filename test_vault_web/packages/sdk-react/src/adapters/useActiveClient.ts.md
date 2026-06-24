# useActiveClient.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/adapters/useActiveClient.ts`
- **Extension:** `.ts`
- **Size:** 289 bytes
- **Centrality Score:** 0.0027
- **In-Degree (Imported By):** 6
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useActiveClient`

## Imports (Dependencies)
- [[packages/sdk-react/src/adapters/useMeshRegistry.ts.md|packages/sdk-react/src/adapters/useMeshRegistry.ts]]
- [[packages/sdk-react/src/adapters/useSignal.ts.md|packages/sdk-react/src/adapters/useSignal.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk-react/src/hooks/useChannels.ts.md|packages/sdk-react/src/hooks/useChannels.ts]]
- [[packages/sdk-react/src/hooks/useConfigEditor.ts.md|packages/sdk-react/src/hooks/useConfigEditor.ts]]
- [[packages/sdk-react/src/hooks/useConnectionProgress.ts.md|packages/sdk-react/src/hooks/useConnectionProgress.ts]]
- [[packages/sdk-react/src/hooks/useNodeError.ts.md|packages/sdk-react/src/hooks/useNodeError.ts]]
- [[packages/sdk-react/src/hooks/useUnread.ts.md|packages/sdk-react/src/hooks/useUnread.ts]]

## Source Code Snippet
```ts
import type { MeshClient } from "@meshtastic/sdk";
import { useMeshRegistry } from "./useMeshRegistry.ts";
import { useSignal } from "./useSignal.ts";

export function useActiveClient(): MeshClient | undefined {
  const registry = useMeshRegistry();
  return useSignal(registry.active);
}
```