# Node.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/nodes/domain/Node.ts`
- **Extension:** `.ts`
- **Size:** 504 bytes
- **Centrality Score:** 0.0063
- **In-Degree (Imported By):** 7
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Node`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk/src/features/nodes/NodesClient.ts.md|packages/sdk/src/features/nodes/NodesClient.ts]]
- [[packages/sdk/src/features/nodes/domain/NodesRepository.ts.md|packages/sdk/src/features/nodes/domain/NodesRepository.ts]]
- [[packages/sdk/src/features/nodes/index.ts.md|packages/sdk/src/features/nodes/index.ts]]
- [[packages/sdk/src/features/nodes/infrastructure/NodeMapper.ts.md|packages/sdk/src/features/nodes/infrastructure/NodeMapper.ts]]
- [[packages/sdk/src/features/nodes/infrastructure/nodeValidation.ts.md|packages/sdk/src/features/nodes/infrastructure/nodeValidation.ts]]
- [[packages/sdk/src/features/nodes/infrastructure/repositories/InMemoryNodesRepository.ts.md|packages/sdk/src/features/nodes/infrastructure/repositories/InMemoryNodesRepository.ts]]
- [[packages/sdk/src/features/nodes/state/nodesStore.ts.md|packages/sdk/src/features/nodes/state/nodesStore.ts]]

## Source Code Snippet
```ts
import type * as Protobuf from "@meshtastic/protobufs";

export interface Node {
  readonly num: number;
  readonly user?: Protobuf.Mesh.User;
  readonly position?: Protobuf.Mesh.Position;
  readonly deviceMetrics?: Protobuf.Telemetry.DeviceMetrics;
  readonly lastHeard?: number;
  readonly snr?: number;
  readonly channel?: number;
  readonly viaMqtt?: boolean;
  readonly hopsAway?: number;
  readonly isFavorite: boolean;
  readonly isIgnored: boolean;
  readonly isKeyManuallyVerified?: boolean;
}
```