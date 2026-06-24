# PopupWrapper.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Map/Popups/PopupWrapper.tsx`
- **Extension:** `.tsx`
- **Size:** 855 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PopupState`

## Imports (Dependencies)
- [[apps/web/src/components/PageComponents/Map/cluster.ts.md|apps/web/src/components/PageComponents/Map/cluster.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/WaypointLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/WaypointLayer.tsx]]
- [[apps/web/src/pages/Map/index.tsx.md|apps/web/src/pages/Map/index.tsx]]

## Source Code Snippet
```tsx
import type { PxOffset } from "@components/PageComponents/Map/cluster.ts";
import type { WaypointWithMetadata } from "@core/stores";
import { memo } from "react";
import { Popup } from "react-map-gl/maplibre";

export type PopupState =
  | { type: "node"; num: number; offset: PxOffset }
  | { type: "waypoint"; waypoint: WaypointWithMetadata };

export const PopupWrapper = memo(function SelectedNodePopup({
  lng,
  lat,
  offset,
  onClose,
  children,
}: {
  lng: number;
  lat: number;
  offset?: PxOffset;
  onClose: () => void;
...
```