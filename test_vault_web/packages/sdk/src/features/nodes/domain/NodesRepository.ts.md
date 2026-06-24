# NodesRepository.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/nodes/domain/NodesRepository.ts`
- **Extension:** `.ts`
- **Size:** 633 bytes
- **Centrality Score:** 0.0020
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NodesRepository`

## Imports (Dependencies)
- [[packages/sdk/src/features/nodes/domain/Node.ts.md|packages/sdk/src/features/nodes/domain/Node.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/nodes/NodesClient.ts.md|packages/sdk/src/features/nodes/NodesClient.ts]]
- [[packages/sdk/src/features/nodes/index.ts.md|packages/sdk/src/features/nodes/index.ts]]
- [[packages/sdk/src/features/nodes/infrastructure/repositories/InMemoryNodesRepository.ts.md|packages/sdk/src/features/nodes/infrastructure/repositories/InMemoryNodesRepository.ts]]

## Source Code Snippet
```ts
import type { Node } from "./Node.ts";

/**
 * Persists the device's view of the mesh node DB.
 *
 * Snapshot semantics: each `upsert` overwrites the previous row for that
 * node number. Implementations can keep additional history (e.g. a
 * lastHeard timestamp series) but must always return the most recent
 * snapshot from `loadAll` and `get`.
 */
export interface NodesRepository {
  loadAll(): Promise<Node[]>;
  get(nodeNum: number): Promise<Node | undefined>;
  upsert(node: Node): Promise<void>;
  upsertBatch(nodes: ReadonlyArray<Node>): Promise<void>;
  remove(nodeNum: number): Promise<void>;
  clear(): Promise<void>;
}
```