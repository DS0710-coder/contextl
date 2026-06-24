# Map.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Map.tsx`
- **Extension:** `.tsx`
- **Size:** 3032 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `MapLayerMouseEvent`
- `MapRef`
- `MapProps`

## Imports (Dependencies)
- [[apps/web/src/core/hooks/useTheme.ts.md|apps/web/src/core/hooks/useTheme.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Map/index.tsx.md|apps/web/src/pages/Map/index.tsx]]

## Source Code Snippet
```tsx
import { useTheme } from "@core/hooks/useTheme.ts";
import { useEffect, useMemo, useRef } from "react";
import { useTranslation } from "react-i18next";
import MapGl, {
  AttributionControl,
  type MapLayerMouseEvent,
  type MapRef,
  NavigationControl,
  ScaleControl,
} from "react-map-gl/maplibre";

interface MapProps {
  children?: React.ReactNode;
  onLoad?: (map: MapRef) => void;
  onMouseMove?: (event: MapLayerMouseEvent) => void;
  onClick?: (event: MapLayerMouseEvent) => void;
  interactiveLayerIds?: string[];
  initialViewState?: {
    latitude?: number;
    longitude?: number;
...
```