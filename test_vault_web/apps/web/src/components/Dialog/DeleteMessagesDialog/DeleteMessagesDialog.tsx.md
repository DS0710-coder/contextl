# DeleteMessagesDialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/DeleteMessagesDialog/DeleteMessagesDialog.tsx`
- **Extension:** `.tsx`
- **Size:** 1021 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DeleteMessagesDialogProps`

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/DialogWrapper.tsx.md|apps/web/src/components/Dialog/DialogWrapper.tsx]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/DeleteMessagesDialog/DeleteMessagesDialog.test.tsx.md|apps/web/src/components/Dialog/DeleteMessagesDialog/DeleteMessagesDialog.test.tsx]]
- [[apps/web/src/components/Dialog/DialogManager.tsx.md|apps/web/src/components/Dialog/DialogManager.tsx]]

## Source Code Snippet
```tsx
import { useActiveClient } from "@meshtastic/sdk-react";
import { AlertTriangleIcon } from "lucide-react";
import { useTranslation } from "react-i18next";
import { DialogWrapper } from "../DialogWrapper.tsx";

export interface DeleteMessagesDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
}

export const DeleteMessagesDialog = ({
  open,
  onOpenChange,
}: DeleteMessagesDialogProps) => {
  const { t } = useTranslation("dialog");
  const meshClient = useActiveClient();

  const handleConfirm = () => {
    void meshClient?.chat.clearAll();
    onOpenChange(false);
...
```