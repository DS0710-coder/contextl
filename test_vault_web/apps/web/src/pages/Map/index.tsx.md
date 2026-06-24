# index.tsx

## Architecture Metrics
- **Path:** `apps/web/src/pages/Map/index.tsx`
- **Extension:** `.tsx`
- **Size:** 9676 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 17

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `VisibilityState`
- `FilterState`
- `HeatmapMode`
- `SNRTooltipProps`

## Imports (Dependencies)
- [[apps/web/src/components/Map.tsx.md|apps/web/src/components/Map.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/HeatmapLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/HeatmapLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/PrecisionLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/PrecisionLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/SNRLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/SNRLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/WaypointLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/WaypointLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/PopupWrapper.tsx.md|apps/web/src/components/PageComponents/Map/Popups/PopupWrapper.tsx]]
- [[apps/web/src/components/PageComponents/Map/Tools/MapLayerTool.tsx.md|apps/web/src/components/PageComponents/Map/Tools/MapLayerTool.tsx]]
- [[apps/web/src/components/PageLayout.tsx.md|apps/web/src/components/PageLayout.tsx]]
- [[apps/web/src/components/Sidebar.tsx.md|apps/web/src/components/Sidebar.tsx]]
- [[apps/web/src/components/generic/Filter/FilterControl.tsx.md|apps/web/src/components/generic/Filter/FilterControl.tsx]]
- [[apps/web/src/components/generic/Filter/useFilterNode.ts.md|apps/web/src/components/generic/Filter/useFilterNode.ts]]
- [[apps/web/src/core/hooks/useMapFitting.ts.md|apps/web/src/core/hooks/useMapFitting.ts]]
- [[apps/web/src/core/hooks/useNodesAsProto.ts.md|apps/web/src/core/hooks/useNodesAsProto.ts]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]
- [[apps/web/src/core/utils/geo.ts.md|apps/web/src/core/utils/geo.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/routes.tsx.md|apps/web/src/routes.tsx]]

## Source Code Snippet
```tsx
import {
  defaultVisibilityState,
  MapLayerTool,
  type VisibilityState,
} from "@app/components/PageComponents/Map/Tools/MapLayerTool.tsx";
import { FilterControl } from "@components/generic/Filter/FilterControl.tsx";
import {
  type FilterState,
  useFilterNode,
} from "@components/generic/Filter/useFilterNode.ts";
import { BaseMap } from "@components/Map.tsx";
import {
  HeatmapLayer,
  type HeatmapMode,
} from "@components/PageComponents/Map/Layers/HeatmapLayer.tsx";
import { NodesLayer } from "@components/PageComponents/Map/Layers/NodesLayer.tsx";
import { PrecisionLayer } from "@components/PageComponents/Map/Layers/PrecisionLayer.tsx";
import {
  SNRLayer,
  SNRTooltip,
...
```