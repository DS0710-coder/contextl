# NodeDetailsDialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx`
- **Extension:** `.tsx`
- **Size:** 17202 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 15

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NodeDetailsDialogProps`
- `handleDirectMessage`
- `handleRequestPosition`
- `handleTraceroute`
- `handleInitiateKeyVerification`
- `handleNodeRemove`
- `handleToggleFavorite`
- `handleToggleIgnored`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Accordion.tsx.md|apps/web/src/components/UI/Accordion.tsx]]
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Dialog.tsx.md|apps/web/src/components/UI/Dialog.tsx]]
- [[apps/web/src/components/UI/Separator.tsx.md|apps/web/src/components/UI/Separator.tsx]]
- [[apps/web/src/components/UI/Tooltip.tsx.md|apps/web/src/components/UI/Tooltip.tsx]]
- [[apps/web/src/components/generic/DeviceImage.tsx.md|apps/web/src/components/generic/DeviceImage.tsx]]
- [[apps/web/src/components/generic/TimeAgo.tsx.md|apps/web/src/components/generic/TimeAgo.tsx]]
- [[apps/web/src/components/generic/Uptime.tsx.md|apps/web/src/components/generic/Uptime.tsx]]
- [[apps/web/src/core/hooks/useFavoriteNode.ts.md|apps/web/src/core/hooks/useFavoriteNode.ts]]
- [[apps/web/src/core/hooks/useIgnoreNode.ts.md|apps/web/src/core/hooks/useIgnoreNode.ts]]
- [[apps/web/src/core/hooks/useNodesAsProto.ts.md|apps/web/src/core/hooks/useNodesAsProto.ts]]
- [[apps/web/src/core/hooks/useToast.ts.md|apps/web/src/core/hooks/useToast.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/DialogManager.tsx.md|apps/web/src/components/Dialog/DialogManager.tsx]]

## Source Code Snippet
```tsx
import { DeviceImage } from "@components/generic/DeviceImage.tsx";
import { TimeAgo } from "@components/generic/TimeAgo.tsx";
import { Uptime } from "@components/generic/Uptime.tsx";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@components/UI/Accordion.tsx";
import { Button } from "@components/UI/Button.tsx";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@components/UI/Dialog.tsx";
import { Separator } from "@components/UI/Separator.tsx";
import {
...
```