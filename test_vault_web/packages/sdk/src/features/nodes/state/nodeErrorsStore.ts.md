# nodeErrorsStore.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/nodes/state/nodeErrorsStore.ts`
- **Extension:** `.ts`
- **Size:** 193 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NodeErrorsStore`

## Imports (Dependencies)
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/features/nodes/domain/NodeError.ts.md|packages/sdk/src/features/nodes/domain/NodeError.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/nodes/NodesClient.ts.md|packages/sdk/src/features/nodes/NodesClient.ts]]

## Source Code Snippet
```ts
import { SignalMap } from "../../../core/signals/createStore.ts";
import type { NodeError } from "../domain/NodeError.ts";

export class NodeErrorsStore extends SignalMap<number, NodeError> {}
```