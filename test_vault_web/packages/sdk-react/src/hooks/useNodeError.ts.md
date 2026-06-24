# useNodeError.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/hooks/useNodeError.ts`
- **Extension:** `.ts`
- **Size:** 873 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useNodeErrors`
- `useNodeError`
- `useHasNodeError`

## Imports (Dependencies)
- [[packages/sdk-react/src/adapters/useActiveClient.ts.md|packages/sdk-react/src/adapters/useActiveClient.ts]]
- [[packages/sdk-react/src/adapters/useSignal.ts.md|packages/sdk-react/src/adapters/useSignal.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Source Code Snippet
```ts
import type { NodeError } from "@meshtastic/sdk";
import { useActiveClient } from "../adapters/useActiveClient.ts";
import { useSignal } from "../adapters/useSignal.ts";

const EMPTY: ReadonlyArray<NodeError> = [];
const EMPTY_SIGNAL = {
  value: EMPTY,
  peek: () => EMPTY,
  subscribe: () => () => {},
};

/**
 * Returns the current per-node error array from the active client. Empty
 * when no client is active or no errors have been recorded.
 */
export function useNodeErrors(): ReadonlyArray<NodeError> {
  const client = useActiveClient();
  return useSignal(client?.nodes.errors ?? EMPTY_SIGNAL);
}

...
```