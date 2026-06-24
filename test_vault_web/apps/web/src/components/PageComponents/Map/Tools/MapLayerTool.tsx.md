# MapLayerTool.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Map/Tools/MapLayerTool.tsx`
- **Extension:** `.tsx`
- **Size:** 5952 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `VisibilityState`
- `MapLayerToolProps`
- `CheckboxProps`
- `MapLayerTool`

## Imports (Dependencies)
- [[apps/web/src/components/PageComponents/Map/Layers/HeatmapLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/HeatmapLayer.tsx]]
- [[apps/web/src/components/UI/Checkbox/index.tsx.md|apps/web/src/components/UI/Checkbox/index.tsx]]
- [[apps/web/src/components/UI/Popover.tsx.md|apps/web/src/components/UI/Popover.tsx]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Map/Layers/SNRLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/SNRLayer.tsx]]
- [[apps/web/src/pages/Map/index.tsx.md|apps/web/src/pages/Map/index.tsx]]

## Source Code Snippet
```tsx
import type { HeatmapMode } from "@components/PageComponents/Map/Layers/HeatmapLayer.tsx";
import { Checkbox } from "@components/UI/Checkbox/index.tsx";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@components/UI/Popover.tsx";
import { cn } from "@core/utils/cn.ts";
import { LayersIcon } from "lucide-react";
import { type ReactNode, useMemo } from "react";
import { useTranslation } from "react-i18next";

export interface VisibilityState {
  nodeMarkers: boolean;
  directNeighbors: boolean;
  remoteNeighbors: boolean;
  positionPrecision: boolean;
  traceroutes: boolean;
  waypoints: boolean;
  heatmap: boolean;
...
```