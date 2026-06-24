# nodesStore.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/nodes/state/nodesStore.ts`
- **Extension:** `.ts`
- **Size:** 173 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NodesStore`

## Imports (Dependencies)
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/features/nodes/domain/Node.ts.md|packages/sdk/src/features/nodes/domain/Node.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/nodes/NodesClient.ts.md|packages/sdk/src/features/nodes/NodesClient.ts]]

## Source Code Snippet
```ts
import { SignalMap } from "../../../core/signals/createStore.ts";
import type { Node } from "../domain/Node.ts";

export class NodesStore extends SignalMap<number, Node> {}
```