# WaypointLayer.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Map/Layers/WaypointLayer.tsx`
- **Extension:** `.tsx`
- **Size:** 2799 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `WaypointLayerProps`

## Imports (Dependencies)
- [[apps/web/src/components/PageComponents/Map/Markers/NodeMarker.tsx.md|apps/web/src/components/PageComponents/Map/Markers/NodeMarker.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/PopupWrapper.tsx.md|apps/web/src/components/PageComponents/Map/Popups/PopupWrapper.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/WaypointDetail.tsx.md|apps/web/src/components/PageComponents/Map/Popups/WaypointDetail.tsx]]
- [[apps/web/src/core/hooks/useMapFitting.ts.md|apps/web/src/core/hooks/useMapFitting.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/core/utils/geo.ts.md|apps/web/src/core/utils/geo.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Map/index.tsx.md|apps/web/src/pages/Map/index.tsx]]

## Source Code Snippet
```tsx
import { NodeMarker } from "@components/PageComponents/Map/Markers/NodeMarker.tsx";
import type { PopupState } from "@components/PageComponents/Map/Popups/PopupWrapper.tsx";
import { PopupWrapper } from "@components/PageComponents/Map/Popups/PopupWrapper.tsx";
import { WaypointDetail } from "@components/PageComponents/Map/Popups/WaypointDetail.tsx";
import { useMapFitting } from "@core/hooks/useMapFitting";
import { useDevice, type WaypointWithMetadata } from "@core/stores";
import type { Protobuf } from "@meshtastic/sdk";
import { useCallback } from "react";
import type { MapRef } from "react-map-gl/maplibre";

export interface WaypointLayerProps {
  mapRef: MapRef | undefined;
  myNode: Protobuf.Mesh.NodeInfo | undefined;
  isVisible: boolean;
  popupState: PopupState | undefined;
  setPopupState: (state: PopupState | undefined) => void;
}

import { toLngLat } from "@core/utils/geo.ts";

...
```