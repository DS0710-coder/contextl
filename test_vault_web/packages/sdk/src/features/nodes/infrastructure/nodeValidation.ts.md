# nodeValidation.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/nodes/infrastructure/nodeValidation.ts`
- **Extension:** `.ts`
- **Size:** 2498 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `equalKey`
- `ValidatedNodeInfo`
- `validateIncomingNode`

## Imports (Dependencies)
- [[packages/sdk/src/features/nodes/domain/Node.ts.md|packages/sdk/src/features/nodes/domain/Node.ts]]
- [[packages/sdk/src/features/nodes/domain/NodeError.ts.md|packages/sdk/src/features/nodes/domain/NodeError.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/nodes/NodesClient.ts.md|packages/sdk/src/features/nodes/NodesClient.ts]]
- [[packages/sdk/src/features/nodes/index.ts.md|packages/sdk/src/features/nodes/index.ts]]

## Source Code Snippet
```ts
import type * as Protobuf from "@meshtastic/protobufs";
import type { Node } from "../domain/Node.ts";
import type { NodeErrorType } from "../domain/NodeError.ts";

/**
 * Byte-equal compare for two public keys. Empty / undefined keys never
 * match each other.
 */
export function equalKey(
  a?: Uint8Array | null,
  b?: Uint8Array | null,
): boolean {
  if (!a || !b) return false;
  if (a === b) return true;
  if (a.byteLength !== b.byteLength) return false;
  for (let i = 0; i < a.byteLength; i++) {
    if (a[i] !== b[i]) return false;
  }
  return true;
}
...
```