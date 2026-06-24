# NodeMapper.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/nodes/infrastructure/NodeMapper.ts`
- **Extension:** `.ts`
- **Size:** 594 bytes
- **Centrality Score:** 0.0020
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/features/nodes/domain/Node.ts.md|packages/sdk/src/features/nodes/domain/Node.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/nodes/NodesClient.ts.md|packages/sdk/src/features/nodes/NodesClient.ts]]
- [[packages/sdk/src/features/nodes/index.ts.md|packages/sdk/src/features/nodes/index.ts]]
- [[packages/sdk/src/features/nodes/infrastructure/NodeMapper.test.ts.md|packages/sdk/src/features/nodes/infrastructure/NodeMapper.test.ts]]

## Source Code Snippet
```ts
import type * as Protobuf from "@meshtastic/protobufs";
import type { Node } from "../domain/Node.ts";

export const NodeMapper = {
  fromProto(info: Protobuf.Mesh.NodeInfo): Node {
    return {
      num: info.num,
      user: info.user,
      position: info.position,
      deviceMetrics: info.deviceMetrics,
      lastHeard: info.lastHeard,
      snr: info.snr,
      channel: info.channel,
      viaMqtt: info.viaMqtt,
      hopsAway: info.hopsAway,
      isFavorite: info.isFavorite,
      isIgnored: info.isIgnored,
      isKeyManuallyVerified: info.isKeyManuallyVerified,
    };
  },
...
```