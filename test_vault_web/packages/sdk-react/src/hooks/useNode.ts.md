# useNode.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/hooks/useNode.ts`
- **Extension:** `.ts`
- **Size:** 356 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useNode`

## Imports (Dependencies)
- [[packages/sdk-react/src/adapters/useClient.ts.md|packages/sdk-react/src/adapters/useClient.ts]]
- [[packages/sdk-react/src/adapters/useSignalValue.ts.md|packages/sdk-react/src/adapters/useSignalValue.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Source Code Snippet
```ts
import type { Node } from "@meshtastic/sdk";
import { useClient } from "../adapters/useClient.ts";
import { useSignalValue } from "../adapters/useSignalValue.ts";

export function useNode(nodeNum: number): Node | undefined {
  const client = useClient();
  return useSignalValue(client.nodes.list, (list) =>
    list.find((n) => n.num === nodeNum),
  );
}
```