# MessageItem.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Messages/MessageItem.tsx`
- **Extension:** `.tsx`
- **Size:** 8658 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 8

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useSuspendingMyNode`
- `MessageStatusInfo`
- `MessageItemProps`

## Imports (Dependencies)
- [[apps/web/src/components/PageComponents/Messages/MessageActionsMenu.tsx.md|apps/web/src/components/PageComponents/Messages/MessageActionsMenu.tsx]]
- [[apps/web/src/components/UI/Avatar.tsx.md|apps/web/src/components/UI/Avatar.tsx]]
- [[apps/web/src/components/UI/Tooltip.tsx.md|apps/web/src/components/UI/Tooltip.tsx]]
- [[apps/web/src/core/hooks/useNodesAsProto.ts.md|apps/web/src/core/hooks/useNodesAsProto.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/core/stores/messageStore/index.ts.md|apps/web/src/core/stores/messageStore/index.ts]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Messages/ChannelChat.tsx.md|apps/web/src/components/PageComponents/Messages/ChannelChat.tsx]]

## Source Code Snippet
```tsx
import { Avatar } from "@components/UI/Avatar.tsx";
import {
  Tooltip,
  TooltipArrow,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@components/UI/Tooltip.tsx";
import {
  useMyNodeAsProto,
  useNodeAsProto,
} from "@core/hooks/useNodesAsProto.ts";
import { useAppStore, useDevice } from "@core/stores";
import { type Message, MessageState } from "@core/stores/messageStore";
import { cn } from "@core/utils/cn.ts";
import { type Protobuf, Types } from "@meshtastic/sdk";
import type { LucideIcon } from "lucide-react";
import { AlertCircle, CheckCircle2, CircleEllipsis } from "lucide-react";
import { type ReactNode, useMemo } from "react";
import { useTranslation } from "react-i18next";
...
```