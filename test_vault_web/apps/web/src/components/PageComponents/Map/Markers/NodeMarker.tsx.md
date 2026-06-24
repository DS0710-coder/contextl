# NodeMarker.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Map/Markers/NodeMarker.tsx`
- **Extension:** `.tsx`
- **Size:** 2988 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/components/PageComponents/Map/cluster.ts.md|apps/web/src/components/PageComponents/Map/cluster.ts]]
- [[apps/web/src/components/UI/Avatar.tsx.md|apps/web/src/components/UI/Avatar.tsx]]
- [[apps/web/src/components/UI/Tooltip.tsx.md|apps/web/src/components/UI/Tooltip.tsx]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/WaypointLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/WaypointLayer.tsx]]

## Source Code Snippet
```tsx
import { cn } from "@app/core/utils/cn";
import type { PxOffset } from "@components/PageComponents/Map/cluster.ts";
import { Avatar } from "@components/UI/Avatar.tsx";
import {
  Tooltip,
  TooltipArrow,
  TooltipContent,
  TooltipPortal,
  TooltipProvider,
  TooltipTrigger,
} from "@components/UI/Tooltip.tsx";
import { memo } from "react";
import { Marker } from "react-map-gl/maplibre";

export const NodeMarker = memo(function NodeMarker({
  id,
  lng,
  lat,
  longLabel,
  tooltipLabel,
...
```