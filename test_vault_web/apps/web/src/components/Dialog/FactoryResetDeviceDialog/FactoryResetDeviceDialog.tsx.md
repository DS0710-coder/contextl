# FactoryResetDeviceDialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/FactoryResetDeviceDialog/FactoryResetDeviceDialog.tsx`
- **Extension:** `.tsx`
- **Size:** 1406 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `FactoryResetDeviceDialogProps`

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/DialogWrapper.tsx.md|apps/web/src/components/Dialog/DialogWrapper.tsx]]
- [[apps/web/src/core/hooks/useToast.ts.md|apps/web/src/core/hooks/useToast.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/DialogManager.tsx.md|apps/web/src/components/Dialog/DialogManager.tsx]]
- [[apps/web/src/components/Dialog/FactoryResetDeviceDialog/FactoryResetDeviceDialog.test.tsx.md|apps/web/src/components/Dialog/FactoryResetDeviceDialog/FactoryResetDeviceDialog.test.tsx]]

## Source Code Snippet
```tsx
import { toast } from "@core/hooks/useToast.ts";
import { useDevice, useDeviceStore } from "@core/stores";
import { useTranslation } from "react-i18next";
import { DialogWrapper } from "../DialogWrapper.tsx";

export interface FactoryResetDeviceDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
}

export const FactoryResetDeviceDialog = ({
  open,
  onOpenChange,
}: FactoryResetDeviceDialogProps) => {
  const { t } = useTranslation("dialog");
  const { connection, id } = useDevice();

  const handleFactoryResetDevice = () => {
    connection?.factoryResetDevice().catch((error) => {
      toast({
...
```