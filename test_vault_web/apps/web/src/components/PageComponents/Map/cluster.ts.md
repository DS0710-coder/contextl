# cluster.ts

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Map/cluster.ts`
- **Extension:** `.ts`
- **Size:** 1376 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ClusterKey`
- `PxOffset`
- `makeClusterKey`
- `groupNodesByIdenticalCoords`
- `hashToAngle`
- `fanOutOffsetsPx`

## Imports (Dependencies)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Markers/NodeMarker.tsx.md|apps/web/src/components/PageComponents/Map/Markers/NodeMarker.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/PopupWrapper.tsx.md|apps/web/src/components/PageComponents/Map/Popups/PopupWrapper.tsx]]

## Source Code Snippet
```ts
import type { Protobuf } from "@meshtastic/sdk";

export type ClusterKey = string;
export type PxOffset = [number, number];

export function makeClusterKey(pos: Protobuf.Mesh.Position): ClusterKey {
  return `${pos.latitudeI},${pos.longitudeI}`;
}

export function groupNodesByIdenticalCoords(
  nodes: Protobuf.Mesh.NodeInfo[],
): Map<ClusterKey, Protobuf.Mesh.NodeInfo[]> {
  const map = new Map<ClusterKey, Protobuf.Mesh.NodeInfo[]>();
  for (const node of nodes) {
    if (!node.position) {
      continue;
    }

    const key = makeClusterKey(node.position);
    const arr = map.get(key);
...
```