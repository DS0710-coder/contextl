# ClearAllStoresDialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/ClearAllStoresDialog/ClearAllStoresDialog.tsx`
- **Extension:** `.tsx`
- **Size:** 875 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ClearAllStoresDialogProps`

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/DialogWrapper.tsx.md|apps/web/src/components/Dialog/DialogWrapper.tsx]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/ClearAllStoresDialog/ClearAllStoresDialog.test.tsx.md|apps/web/src/components/Dialog/ClearAllStoresDialog/ClearAllStoresDialog.test.tsx]]
- [[apps/web/src/components/Dialog/DialogManager.tsx.md|apps/web/src/components/Dialog/DialogManager.tsx]]

## Source Code Snippet
```tsx
import { clearAllStores } from "@core/stores";
import { useTranslation } from "react-i18next";
import { DialogWrapper } from "../DialogWrapper.tsx";

export interface ClearAllStoresDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
}

export const ClearAllStoresDialog = ({
  open,
  onOpenChange,
}: ClearAllStoresDialogProps) => {
  const { t } = useTranslation("dialog");

  const handleClearAllStores = () => {
    clearAllStores();

    // Reload the app to ensure all state is cleared
    window.location.href = "/";
...
```