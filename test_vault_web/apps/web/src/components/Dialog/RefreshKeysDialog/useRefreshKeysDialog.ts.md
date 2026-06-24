# useRefreshKeysDialog.ts

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/RefreshKeysDialog/useRefreshKeysDialog.ts`
- **Extension:** `.ts`
- **Size:** 736 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useRefreshKeysDialog`

## Imports (Dependencies)
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.test.tsx.md|apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.test.tsx]]
- [[apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.tsx.md|apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.tsx]]

## Source Code Snippet
```ts
import { useDevice } from "@core/stores";
import { useActiveClient, useNodeErrors } from "@meshtastic/sdk-react";
import { useCallback } from "react";

export function useRefreshKeysDialog() {
  const { setDialogOpen } = useDevice();
  const meshClient = useActiveClient();
  const error = useNodeErrors()[0];

  const handleCloseDialog = useCallback(() => {
    setDialogOpen("refreshKeys", false);
  }, [setDialogOpen]);

  const handleNodeRemove = useCallback(() => {
    if (!meshClient || !error) return;
    meshClient.nodes.clearError(error.node);
    handleCloseDialog();
    void meshClient.nodes.remove(error.node);
  }, [meshClient, error, handleCloseDialog]);

...
```