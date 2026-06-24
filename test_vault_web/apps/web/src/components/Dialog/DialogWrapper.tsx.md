# DialogWrapper.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/DialogWrapper.tsx`
- **Extension:** `.tsx`
- **Size:** 3217 bytes
- **Centrality Score:** 0.0034
- **In-Degree (Imported By):** 8
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DialogVariant`
- `DialogType`
- `DialogWrapperProps`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Dialog.tsx.md|apps/web/src/components/UI/Dialog.tsx]]
- [[apps/web/src/components/UI/Separator.tsx.md|apps/web/src/components/UI/Separator.tsx]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx.md|apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx]]
- [[apps/web/src/components/Dialog/ClearAllStoresDialog/ClearAllStoresDialog.tsx.md|apps/web/src/components/Dialog/ClearAllStoresDialog/ClearAllStoresDialog.tsx]]
- [[apps/web/src/components/Dialog/DeleteMessagesDialog/DeleteMessagesDialog.tsx.md|apps/web/src/components/Dialog/DeleteMessagesDialog/DeleteMessagesDialog.tsx]]
- [[apps/web/src/components/Dialog/FactoryResetConfigDialog/FactoryResetConfigDialog.tsx.md|apps/web/src/components/Dialog/FactoryResetConfigDialog/FactoryResetConfigDialog.tsx]]
- [[apps/web/src/components/Dialog/FactoryResetDeviceDialog/FactoryResetDeviceDialog.tsx.md|apps/web/src/components/Dialog/FactoryResetDeviceDialog/FactoryResetDeviceDialog.tsx]]
- [[apps/web/src/components/Dialog/RemoveNodeDialog.tsx.md|apps/web/src/components/Dialog/RemoveNodeDialog.tsx]]
- [[apps/web/src/components/Dialog/ResetNodeDbDialog/ResetNodeDbDialog.tsx.md|apps/web/src/components/Dialog/ResetNodeDbDialog/ResetNodeDbDialog.tsx]]
- [[apps/web/src/components/Dialog/ShutdownDialog.tsx.md|apps/web/src/components/Dialog/ShutdownDialog.tsx]]

## Source Code Snippet
```tsx
import { Button } from "@components/UI/Button.tsx";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@components/UI/Dialog.tsx";
import { Separator } from "@components/UI/Separator.tsx";
import type { ReactNode } from "react";
import { useTranslation } from "react-i18next";

export type DialogVariant = "default" | "destructive";
export type DialogType = "confirm" | "alert" | "info" | "custom";

export interface DialogWrapperProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
...
```