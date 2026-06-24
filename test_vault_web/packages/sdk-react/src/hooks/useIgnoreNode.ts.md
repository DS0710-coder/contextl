# useIgnoreNode.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/hooks/useIgnoreNode.ts`
- **Extension:** `.ts`
- **Size:** 534 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useIgnoreNode`

## Imports (Dependencies)
- [[packages/sdk-react/src/adapters/useClient.ts.md|packages/sdk-react/src/adapters/useClient.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Source Code Snippet
```ts
import type { ResultType } from "better-result";
import { useCallback } from "react";
import { useClient } from "../adapters/useClient.ts";

export function useIgnoreNode() {
  const client = useClient();
  const ignore = useCallback(
    (nodeNum: number): Promise<ResultType<number, Error>> =>
      client.nodes.ignore(nodeNum),
    [client],
  );
  const unignore = useCallback(
    (nodeNum: number): Promise<ResultType<number, Error>> =>
      client.nodes.unignore(nodeNum),
    [client],
  );
  return { ignore, unignore };
}
```