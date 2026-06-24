# useToast.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useToast.ts`
- **Extension:** `.ts`
- **Size:** 4151 bytes
- **Centrality Score:** 0.0047
- **In-Degree (Imported By):** 15
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ToasterToast`
- `genId`
- `ActionType`
- `Action`
- `State`
- `dispatch`
- `Toast`
- `toast`
- `useToast`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Toast.tsx.md|apps/web/src/components/UI/Toast.tsx]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx.md|apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx]]
- [[apps/web/src/components/Dialog/FactoryResetConfigDialog/FactoryResetConfigDialog.tsx.md|apps/web/src/components/Dialog/FactoryResetConfigDialog/FactoryResetConfigDialog.tsx]]
- [[apps/web/src/components/Dialog/FactoryResetDeviceDialog/FactoryResetDeviceDialog.tsx.md|apps/web/src/components/Dialog/FactoryResetDeviceDialog/FactoryResetDeviceDialog.tsx]]
- [[apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx.md|apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx]]
- [[apps/web/src/components/Dialog/ResetNodeDbDialog/ResetNodeDbDialog.tsx.md|apps/web/src/components/Dialog/ResetNodeDbDialog/ResetNodeDbDialog.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Position.tsx.md|apps/web/src/components/PageComponents/Settings/Position.tsx]]
- [[apps/web/src/components/RegionSetupReminder.tsx.md|apps/web/src/components/RegionSetupReminder.tsx]]
- [[apps/web/src/components/Toaster.tsx.md|apps/web/src/components/Toaster.tsx]]
- [[apps/web/src/core/hooks/useFavoriteNode.ts.md|apps/web/src/core/hooks/useFavoriteNode.ts]]
- [[apps/web/src/core/hooks/useIgnoreNode.ts.md|apps/web/src/core/hooks/useIgnoreNode.ts]]
- [[apps/web/src/core/hooks/useKeyBackupReminder.tsx.md|apps/web/src/core/hooks/useKeyBackupReminder.tsx]]
- [[apps/web/src/core/hooks/useToast.test.tsx.md|apps/web/src/core/hooks/useToast.test.tsx]]
- [[apps/web/src/pages/Connections/index.tsx.md|apps/web/src/pages/Connections/index.tsx]]
- [[apps/web/src/pages/Messages.tsx.md|apps/web/src/pages/Messages.tsx]]
- [[apps/web/src/pages/Settings/index.tsx.md|apps/web/src/pages/Settings/index.tsx]]

## Source Code Snippet
```ts
import type { ToastActionElement, ToastProps } from "@components/UI/Toast.tsx";
import { type ReactNode, useSyncExternalStore } from "react";

const TOAST_LIMIT = 1;
const TOAST_REMOVE_DELAY = 1000000;

type ToasterToast = ToastProps & {
  id: string;
  title?: ReactNode;
  description?: ReactNode;
  action?: ToastActionElement;
  delay?: number;
};

const actionTypes = {
  ADD_TOAST: "ADD_TOAST",
  UPDATE_TOAST: "UPDATE_TOAST",
  DISMISS_TOAST: "DISMISS_TOAST",
  REMOVE_TOAST: "REMOVE_TOAST",
} as const;
...
```