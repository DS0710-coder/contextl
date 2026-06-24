# PrecisionLayer.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Map/Layers/PrecisionLayer.tsx`
- **Extension:** `.tsx`
- **Size:** 3091 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PrecisionLayerProps`
- `CircleProps`
- `generatePrecisionCircles`

## Imports (Dependencies)
- [[apps/web/src/core/utils/color.ts.md|apps/web/src/core/utils/color.ts]]
- [[apps/web/src/core/utils/geo.ts.md|apps/web/src/core/utils/geo.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx]]
- [[apps/web/src/pages/Map/index.tsx.md|apps/web/src/pages/Map/index.tsx]]

## Source Code Snippet
```tsx
import { getColorFromNodeNum, isLightColor } from "@app/core/utils/color";
import { precisionBitsToMeters, toLngLat } from "@core/utils/geo.ts";
import type { Protobuf } from "@meshtastic/sdk";
import { circle } from "@turf/turf";
import type { Feature, FeatureCollection, Polygon } from "geojson";
import { Layer, Source } from "react-map-gl/maplibre";

export interface PrecisionLayerProps {
  id: string;
  filteredNodes: Protobuf.Mesh.NodeInfo[];
  isVisible: boolean;
}

type CircleProps = {
  r: number;
  g: number;
  b: number;
  a?: number;
  sortKey: number;
};
...
```