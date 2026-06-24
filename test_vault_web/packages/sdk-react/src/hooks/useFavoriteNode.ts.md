# useFavoriteNode.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/hooks/useFavoriteNode.ts`
- **Extension:** `.ts`
- **Size:** 548 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useFavoriteNode`

## Imports (Dependencies)
- [[packages/sdk-react/src/adapters/useClient.ts.md|packages/sdk-react/src/adapters/useClient.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Source Code Snippet
```ts
import type { ResultType } from "better-result";
import { useCallback } from "react";
import { useClient } from "../adapters/useClient.ts";

export function useFavoriteNode() {
  const client = useClient();
  const favorite = useCallback(
    (nodeNum: number): Promise<ResultType<number, Error>> =>
      client.nodes.favorite(nodeNum),
    [client],
  );
  const unfavorite = useCallback(
    (nodeNum: number): Promise<ResultType<number, Error>> =>
      client.nodes.unfavorite(nodeNum),
    [client],
  );
  return { favorite, unfavorite };
}
```