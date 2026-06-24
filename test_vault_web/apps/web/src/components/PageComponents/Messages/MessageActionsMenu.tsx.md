# MessageActionsMenu.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Messages/MessageActionsMenu.tsx`
- **Extension:** `.tsx`
- **Size:** 2741 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `MessageActionsMenuProps`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Tooltip.tsx.md|apps/web/src/components/UI/Tooltip.tsx]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Messages/MessageItem.tsx.md|apps/web/src/components/PageComponents/Messages/MessageItem.tsx]]

## Source Code Snippet
```tsx
import {
  Tooltip,
  TooltipArrow,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "@components/UI/Tooltip.tsx";
import { cn } from "@core/utils/cn.ts";
import { Reply, SmilePlus } from "lucide-react";
import { useTranslation } from "react-i18next";

interface MessageActionsMenuProps {
  onAddReaction?: () => void;
  onReply?: () => void;
}

export const MessageActionsMenu = ({
  onAddReaction,
  onReply,
}: MessageActionsMenuProps) => {
...
```