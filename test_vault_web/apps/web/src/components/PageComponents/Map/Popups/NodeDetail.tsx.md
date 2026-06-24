# NodeDetail.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx`
- **Extension:** `.tsx`
- **Size:** 7305 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NodeDetailProps`
- `handleDirectMessage`

## Imports (Dependencies)
- [[apps/web/src/components/BatteryStatus.tsx.md|apps/web/src/components/BatteryStatus.tsx]]
- [[apps/web/src/components/UI/Avatar.tsx.md|apps/web/src/components/UI/Avatar.tsx]]
- [[apps/web/src/components/UI/Separator.tsx.md|apps/web/src/components/UI/Separator.tsx]]
- [[apps/web/src/components/UI/Typography/Heading.tsx.md|apps/web/src/components/UI/Typography/Heading.tsx]]
- [[apps/web/src/components/UI/Typography/Subtle.tsx.md|apps/web/src/components/UI/Typography/Subtle.tsx]]
- [[apps/web/src/components/generic/Mono.tsx.md|apps/web/src/components/generic/Mono.tsx]]
- [[apps/web/src/components/generic/TimeAgo.tsx.md|apps/web/src/components/generic/TimeAgo.tsx]]
- [[apps/web/src/core/utils/string.ts.md|apps/web/src/core/utils/string.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx.md|apps/web/src/components/PageComponents/Map/Layers/NodesLayer.tsx]]

## Source Code Snippet
```tsx
import BatteryStatus from "@components/BatteryStatus.tsx";
import { Mono } from "@components/generic/Mono.tsx";
import { TimeAgo } from "@components/generic/TimeAgo.tsx";
import { Avatar } from "@components/UI/Avatar.tsx";
import { Separator } from "@components/UI/Separator.tsx";
import { Heading } from "@components/UI/Typography/Heading.tsx";
import { Subtle } from "@components/UI/Typography/Subtle.tsx";
import { formatQuantity } from "@core/utils/string.ts";
import type { Protobuf as ProtobufType } from "@meshtastic/sdk";
import { Protobuf } from "@meshtastic/sdk";
import {
  Tooltip,
  TooltipContent,
  TooltipPortal,
  TooltipProvider,
  TooltipTrigger,
} from "@radix-ui/react-tooltip";
import { useNavigate } from "@tanstack/react-router";
import {
  Dot,
...
```