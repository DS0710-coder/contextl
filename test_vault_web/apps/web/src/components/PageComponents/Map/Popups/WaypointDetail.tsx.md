# WaypointDetail.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Map/Popups/WaypointDetail.tsx`
- **Extension:** `.tsx`
- **Size:** 6984 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `WaypointDetailProps`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Separator.tsx.md|apps/web/src/components/UI/Separator.tsx]]
- [[apps/web/src/components/generic/TimeAgo.tsx.md|apps/web/src/components/generic/TimeAgo.tsx]]
- [[apps/web/src/core/hooks/useNodesAsProto.ts.md|apps/web/src/core/hooks/useNodesAsProto.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/core/utils/geo.ts.md|apps/web/src/core/utils/geo.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Map/Layers/WaypointLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/WaypointLayer.tsx]]

## Source Code Snippet
```tsx
import { TimeAgo } from "@components/generic/TimeAgo";
import { Separator } from "@components/UI/Separator.tsx";
import { useNodeAsProto } from "@core/hooks/useNodesAsProto.ts";
import type { WaypointWithMetadata } from "@core/stores";
import {
  bearingDegrees,
  distanceMeters,
  hasPos,
  toLngLat,
} from "@core/utils/geo";
import type { Protobuf } from "@meshtastic/sdk";
import {
  ClockFadingIcon,
  ClockPlusIcon,
  CompassIcon,
  MapPinnedIcon,
  MoveHorizontalIcon,
  NavigationIcon,
  RotateCwIcon,
  UserLockIcon,
...
```