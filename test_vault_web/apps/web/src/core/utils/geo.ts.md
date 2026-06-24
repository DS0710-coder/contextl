# geo.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/geo.ts`
- **Extension:** `.ts`
- **Size:** 2517 bytes
- **Centrality Score:** 0.0022
- **In-Degree (Imported By):** 8
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `LngLat`
- `Mercator`
- `Bounds`
- `lngLatToMercator`
- `mercatorToLngLat`
- `distanceMeters`
- `precisionBitsToMeters`
- `bearingDegrees`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Map/Layers/HeatmapLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/HeatmapLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/PrecisionLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/PrecisionLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/SNRLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/SNRLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Layers/WaypointLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/WaypointLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/WaypointDetail.tsx.md|apps/web/src/components/PageComponents/Map/Popups/WaypointDetail.tsx]]
- [[apps/web/src/core/hooks/useMapFitting.ts.md|apps/web/src/core/hooks/useMapFitting.ts]]
- [[apps/web/src/pages/Map/index.tsx.md|apps/web/src/pages/Map/index.tsx]]

## Source Code Snippet
```ts
import { bbox, lineString } from "@turf/turf";

export type LngLat = [number, number];
export type Mercator = [number, number];
export type Bounds = [[number, number], [number, number]];

const INT_DEG = 1e7;
const EARTH_RADIUS = 6378137;

export const toLngLat = (position?: {
  latitudeI?: number;
  longitudeI?: number;
}): LngLat => [
  (position?.longitudeI ?? 0) / INT_DEG,
  (position?.latitudeI ?? 0) / INT_DEG,
];

export const hasPos = (position?: {
  latitudeI?: number;
  longitudeI?: number;
...
```