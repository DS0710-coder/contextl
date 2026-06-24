# StackBadge.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Map/Markers/StackBadge.tsx`
- **Extension:** `.tsx`
- **Size:** 758 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `StackBadgeProps`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx]]

## Source Code Snippet
```tsx
import { Marker } from "react-map-gl/maplibre";

type StackBadgeProps = {
  lng: number;
  lat: number;
  count: number; // n = size-1
  isVisible?: boolean;
  onClick: (e: { originalEvent: MouseEvent }) => void;
};

export const StackBadge = ({
  lng,
  lat,
  count,
  isVisible = true,
  onClick,
}: StackBadgeProps) => {
  return (
    <Marker
      longitude={lng}
...
```