# RemoveNodeDialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/RemoveNodeDialog.tsx`
- **Extension:** `.tsx`
- **Size:** 1195 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `RemoveNodeDialogProps`

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/DialogWrapper.tsx.md|apps/web/src/components/Dialog/DialogWrapper.tsx]]
- [[apps/web/src/components/UI/Label.tsx.md|apps/web/src/components/UI/Label.tsx]]
- [[apps/web/src/core/hooks/useNodesAsProto.ts.md|apps/web/src/core/hooks/useNodesAsProto.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/DialogManager.tsx.md|apps/web/src/components/Dialog/DialogManager.tsx]]

## Source Code Snippet
```tsx
import { Label } from "@components/UI/Label.tsx";
import { useNodeAsProto } from "@core/hooks/useNodesAsProto.ts";
import { useAppStore } from "@core/stores";
import { useActiveClient } from "@meshtastic/sdk-react";
import { useTranslation } from "react-i18next";
import { DialogWrapper } from "./DialogWrapper.tsx";

export interface RemoveNodeDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
}

export const RemoveNodeDialog = ({
  open,
  onOpenChange,
}: RemoveNodeDialogProps) => {
  const { t } = useTranslation("dialog");
  const meshClient = useActiveClient();
  const { nodeNumToBeRemoved } = useAppStore();
  const node = useNodeAsProto(nodeNumToBeRemoved);
...
```