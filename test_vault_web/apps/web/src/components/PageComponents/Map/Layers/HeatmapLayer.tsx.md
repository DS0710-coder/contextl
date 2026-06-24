# HeatmapLayer.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Map/Layers/HeatmapLayer.tsx`
- **Extension:** `.tsx`
- **Size:** 2685 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `HeatmapMode`
- `HeatmapLayerProps`

## Imports (Dependencies)
- [[apps/web/src/core/utils/geo.ts.md|apps/web/src/core/utils/geo.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Map/Tools/MapLayerTool.tsx.md|apps/web/src/components/PageComponents/Map/Tools/MapLayerTool.tsx]]
- [[apps/web/src/pages/Map/index.tsx.md|apps/web/src/pages/Map/index.tsx]]

## Source Code Snippet
```tsx
import { hasPos, toLngLat } from "@core/utils/geo";
import type { Protobuf } from "@meshtastic/sdk";
import type { Feature, FeatureCollection } from "geojson";
import type { HeatmapLayerSpecification } from "maplibre-gl";
import { useMemo } from "react";
import { Layer, Source } from "react-map-gl/maplibre";

export type HeatmapMode = "density" | "snr";

export interface HeatmapLayerProps {
  id: string;
  filteredNodes: Protobuf.Mesh.NodeInfo[];
  mode: HeatmapMode;
  isVisible: boolean;
}

export const HeatmapLayer = ({
  id,
  filteredNodes,
  mode,
...
```