# InMemoryNodesRepository.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/nodes/infrastructure/repositories/InMemoryNodesRepository.ts`
- **Extension:** `.ts`
- **Size:** 859 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `InMemoryNodesRepository`

## Imports (Dependencies)
- [[packages/sdk/src/features/nodes/domain/Node.ts.md|packages/sdk/src/features/nodes/domain/Node.ts]]
- [[packages/sdk/src/features/nodes/domain/NodesRepository.ts.md|packages/sdk/src/features/nodes/domain/NodesRepository.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/nodes/NodesClient.ts.md|packages/sdk/src/features/nodes/NodesClient.ts]]
- [[packages/sdk/src/features/nodes/index.ts.md|packages/sdk/src/features/nodes/index.ts]]

## Source Code Snippet
```ts
import type { Node } from "../../domain/Node.ts";
import type { NodesRepository } from "../../domain/NodesRepository.ts";

/**
 * Default in-memory NodesRepository — no persistence across reloads.
 */
export class InMemoryNodesRepository implements NodesRepository {
  private readonly map = new Map<number, Node>();

  async loadAll(): Promise<Node[]> {
    return Array.from(this.map.values());
  }

  async get(nodeNum: number): Promise<Node | undefined> {
    return this.map.get(nodeNum);
  }

  async upsert(node: Node): Promise<void> {
    this.map.set(node.num, node);
  }
...
```