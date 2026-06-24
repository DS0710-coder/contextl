# SNRLayer.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Map/Layers/SNRLayer.tsx`
- **Extension:** `.tsx`
- **Size:** 8483 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `LngLat`
- `SNRLayerProps`
- `SNRTooltipProps`
- `NeighborPlus`
- `NeighborInfoPlus`
- `RemoteInfo`
- `DirectInfo`
- `NeighborInfos`
- `Pair`
- `arcSegment`
- `upsertPair`
- `makeFeature`
- `pushIfFeature`
- `generateNeighborLines`

## Imports (Dependencies)
- [[apps/web/src/components/PageComponents/Map/Tools/MapLayerTool.tsx.md|apps/web/src/components/PageComponents/Map/Tools/MapLayerTool.tsx]]
- [[apps/web/src/components/generic/Mono.tsx.md|apps/web/src/components/generic/Mono.tsx]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]
- [[apps/web/src/core/utils/geo.ts.md|apps/web/src/core/utils/geo.ts]]
- [[apps/web/src/core/utils/signalColor.ts.md|apps/web/src/core/utils/signalColor.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Map/index.tsx.md|apps/web/src/pages/Map/index.tsx]]

## Source Code Snippet
```tsx
import { Mono } from "@app/components/generic/Mono";
import { cn } from "@app/core/utils/cn";
import { getSignalColor } from "@app/core/utils/signalColor";
import type { VisibilityState } from "@components/PageComponents/Map/Tools/MapLayerTool";
import { useDevice } from "@core/stores";
import {
  distanceMeters,
  hasPos,
  type LngLat,
  lngLatToMercator,
  mercatorToLngLat,
  toLngLat,
} from "@core/utils/geo";
import type { Protobuf } from "@meshtastic/sdk";
import type { Feature, FeatureCollection } from "geojson";
import { useTranslation } from "react-i18next";
import { Layer, Source } from "react-map-gl/maplibre";

const ARC_SEGMENTS = 32;
const ARC_OFFSET = 0.01; // 1% of distance
...
```