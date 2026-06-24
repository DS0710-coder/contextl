# useMapFitting.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useMapFitting.ts`
- **Extension:** `.ts`
- **Size:** 1264 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useMapFitting`

## Imports (Dependencies)
- [[apps/web/src/core/utils/geo.ts.md|apps/web/src/core/utils/geo.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/WaypointLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/WaypointLayer.tsx]]
- [[apps/web/src/pages/Map/index.tsx.md|apps/web/src/pages/Map/index.tsx]]

## Source Code Snippet
```ts
import { boundsFromLngLat, type LngLat, toLngLat } from "@core/utils/geo";
import type { Protobuf } from "@meshtastic/sdk";
import { useCallback } from "react";
import type { MapRef } from "react-map-gl/maplibre";

export function useMapFitting(map: MapRef | undefined) {
  const focusLngLat = useCallback(
    (position: LngLat) => {
      if (!map) {
        return;
      }
      const [lng, lat] = position;
      map.easeTo({
        center: [lng, lat],
        zoom: map.getZoom(),
      });
    },
    [map],
  );

...
```