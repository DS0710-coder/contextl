# NodesLayer.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx`
- **Extension:** `.tsx`
- **Size:** 5571 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 10

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PxOffset`
- `NodeMarkerProps`

## Imports (Dependencies)
- [[apps/web/src/components/PageComponents/Map/Layers/PrecisionLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/PrecisionLayer.tsx]]
- [[apps/web/src/components/PageComponents/Map/Markers/NodeMarker.tsx.md|apps/web/src/components/PageComponents/Map/Markers/NodeMarker.tsx]]
- [[apps/web/src/components/PageComponents/Map/Markers/StackBadge.tsx.md|apps/web/src/components/PageComponents/Map/Markers/StackBadge.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx.md|apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/PopupWrapper.tsx.md|apps/web/src/components/PageComponents/Map/Popups/PopupWrapper.tsx]]
- [[apps/web/src/components/PageComponents/Map/cluster.ts.md|apps/web/src/components/PageComponents/Map/cluster.ts]]
- [[apps/web/src/core/hooks/useMapFitting.ts.md|apps/web/src/core/hooks/useMapFitting.ts]]
- [[apps/web/src/core/utils/geo.ts.md|apps/web/src/core/utils/geo.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Map/index.tsx.md|apps/web/src/pages/Map/index.tsx]]

## Source Code Snippet
```tsx
import {
  fanOutOffsetsPx,
  groupNodesByIdenticalCoords,
  type PxOffset,
} from "@components/PageComponents/Map/cluster.ts";
import {
  generatePrecisionCircles,
  SourcePrecisionCircles,
} from "@components/PageComponents/Map/Layers/PrecisionLayer.tsx";
import { NodeMarker } from "@components/PageComponents/Map/Markers/NodeMarker.tsx";
import { StackBadge } from "@components/PageComponents/Map/Markers/StackBadge.tsx";
import { NodeDetail } from "@components/PageComponents/Map/Popups/NodeDetail.tsx";
import type { PopupState } from "@components/PageComponents/Map/Popups/PopupWrapper.tsx";
import { PopupWrapper } from "@components/PageComponents/Map/Popups/PopupWrapper.tsx";
import { useMapFitting } from "@core/hooks/useMapFitting";
import { hasPos, toLngLat } from "@core/utils/geo.ts";
import type { Protobuf } from "@meshtastic/sdk";
import { useNodeErrors } from "@meshtastic/sdk-react";
import { useCallback, useMemo } from "react";
import { useTranslation } from "react-i18next";
...
```