# NodeError.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/nodes/domain/NodeError.ts`
- **Extension:** `.ts`
- **Size:** 569 bytes
- **Centrality Score:** 0.0023
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NodeErrorType`
- `NodeError`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk/src/features/nodes/NodesClient.ts.md|packages/sdk/src/features/nodes/NodesClient.ts]]
- [[packages/sdk/src/features/nodes/index.ts.md|packages/sdk/src/features/nodes/index.ts]]
- [[packages/sdk/src/features/nodes/infrastructure/nodeValidation.ts.md|packages/sdk/src/features/nodes/infrastructure/nodeValidation.ts]]
- [[packages/sdk/src/features/nodes/state/nodeErrorsStore.ts.md|packages/sdk/src/features/nodes/state/nodeErrorsStore.ts]]

## Source Code Snippet
```ts
import type * as Protobuf from "@meshtastic/protobufs";

/**
 * Reasons a node may be flagged as untrusted or unreachable. The two
 * client-only kinds (`MISMATCH_PKI`, `DUPLICATE_PKI`) are produced by the
 * `nodeValidation` mapper when an incoming `NodeInfo` collides with the
 * stored public-key history. Routing errors come straight off the wire
 * via `Routing_Error`.
 */
export type NodeErrorType =
  | Protobuf.Mesh.Routing_Error
  | "MISMATCH_PKI"
  | "DUPLICATE_PKI";

export interface NodeError {
  readonly node: number;
  readonly error: NodeErrorType;
}
```