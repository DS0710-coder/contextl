# ResetNodeDbDialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/ResetNodeDbDialog/ResetNodeDbDialog.tsx`
- **Extension:** `.tsx`
- **Size:** 1214 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ResetNodeDbDialogProps`

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/DialogWrapper.tsx.md|apps/web/src/components/Dialog/DialogWrapper.tsx]]
- [[apps/web/src/core/hooks/useToast.ts.md|apps/web/src/core/hooks/useToast.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/DialogManager.tsx.md|apps/web/src/components/Dialog/DialogManager.tsx]]
- [[apps/web/src/components/Dialog/ResetNodeDbDialog/ResetNodeDbDialog.test.tsx.md|apps/web/src/components/Dialog/ResetNodeDbDialog/ResetNodeDbDialog.test.tsx]]

## Source Code Snippet
```tsx
import { toast } from "@core/hooks/useToast.ts";
import { useActiveClient } from "@meshtastic/sdk-react";
import { useTranslation } from "react-i18next";
import { DialogWrapper } from "../DialogWrapper.tsx";

export interface ResetNodeDbDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
}

export const ResetNodeDbDialog = ({
  open,
  onOpenChange,
}: ResetNodeDbDialogProps) => {
  const { t } = useTranslation("dialog");
  const meshClient = useActiveClient();

  const handleResetNodeDb = () => {
    if (!meshClient) return;
    meshClient.nodes
...
```