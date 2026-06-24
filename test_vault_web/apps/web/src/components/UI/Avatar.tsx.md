# Avatar.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Avatar.tsx`
- **Extension:** `.tsx`
- **Size:** 3390 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 7
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `AvatarProps`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Tooltip.tsx.md|apps/web/src/components/UI/Tooltip.tsx]]
- [[apps/web/src/core/hooks/useNodesAsProto.ts.md|apps/web/src/core/hooks/useNodesAsProto.ts]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]
- [[apps/web/src/core/utils/color.ts.md|apps/web/src/core/utils/color.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/CommandPalette/index.tsx.md|apps/web/src/components/CommandPalette/index.tsx]]
- [[apps/web/src/components/DeviceInfoPanel.tsx.md|apps/web/src/components/DeviceInfoPanel.tsx]]
- [[apps/web/src/components/PageComponents/Map/Markers/NodeMarker.tsx.md|apps/web/src/components/PageComponents/Map/Markers/NodeMarker.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx.md|apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx]]
- [[apps/web/src/components/PageComponents/Messages/MessageItem.tsx.md|apps/web/src/components/PageComponents/Messages/MessageItem.tsx]]
- [[apps/web/src/pages/Messages.tsx.md|apps/web/src/pages/Messages.tsx]]
- [[apps/web/src/pages/Nodes/index.tsx.md|apps/web/src/pages/Nodes/index.tsx]]

## Source Code Snippet
```tsx
import { useNodeAsProto } from "@app/core/hooks/useNodesAsProto.ts";
import { getColorFromNodeNum, isLightColor } from "@app/core/utils/color";
import {
  Tooltip,
  TooltipArrow,
  TooltipContent,
  TooltipPortal,
  TooltipProvider,
  TooltipTrigger,
} from "@components/UI/Tooltip.tsx";
import { cn } from "@core/utils/cn.ts";
import { LockKeyholeOpenIcon, StarIcon } from "lucide-react";
import { useTranslation } from "react-i18next";

interface AvatarProps {
  nodeNum: number;
  size?: "sm" | "lg";
  className?: string;
  showError?: boolean;
  showFavorite?: boolean;
...
```