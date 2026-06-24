# useFavoriteNode.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useFavoriteNode.ts`
- **Extension:** `.ts`
- **Size:** 1384 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `FavoriteNodeOptions`
- `useFavoriteNode`

## Imports (Dependencies)
- [[apps/web/src/core/hooks/useToast.ts.md|apps/web/src/core/hooks/useToast.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx.md|apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx]]
- [[apps/web/src/core/hooks/useFavoriteNode.test.ts.md|apps/web/src/core/hooks/useFavoriteNode.test.ts]]

## Source Code Snippet
```ts
import { useToast } from "@core/hooks/useToast.ts";
import { useActiveClient } from "@meshtastic/sdk-react";
import { useCallback } from "react";
import { useTranslation } from "react-i18next";

interface FavoriteNodeOptions {
  nodeNum: number;
  isFavorite: boolean;
}

/**
 * Toggles the favorite flag on a node. Drives the SDK NodesClient which
 * sends the matching admin message and flips the local flag on success.
 */
export function useFavoriteNode() {
  const meshClient = useActiveClient();
  const { t } = useTranslation();
  const { toast } = useToast();

  const updateFavoriteCB = useCallback(
...
```