# DialogManager.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/DialogManager.tsx`
- **Extension:** `.tsx`
- **Size:** 3987 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 16

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/ClearAllStoresDialog/ClearAllStoresDialog.tsx.md|apps/web/src/components/Dialog/ClearAllStoresDialog/ClearAllStoresDialog.tsx]]
- [[apps/web/src/components/Dialog/ClientNotificationDialog/ClientNotificationDialog.tsx.md|apps/web/src/components/Dialog/ClientNotificationDialog/ClientNotificationDialog.tsx]]
- [[apps/web/src/components/Dialog/DeleteMessagesDialog/DeleteMessagesDialog.tsx.md|apps/web/src/components/Dialog/DeleteMessagesDialog/DeleteMessagesDialog.tsx]]
- [[apps/web/src/components/Dialog/FactoryResetConfigDialog/FactoryResetConfigDialog.tsx.md|apps/web/src/components/Dialog/FactoryResetConfigDialog/FactoryResetConfigDialog.tsx]]
- [[apps/web/src/components/Dialog/FactoryResetDeviceDialog/FactoryResetDeviceDialog.tsx.md|apps/web/src/components/Dialog/FactoryResetDeviceDialog/FactoryResetDeviceDialog.tsx]]
- [[apps/web/src/components/Dialog/ImportDialog.tsx.md|apps/web/src/components/Dialog/ImportDialog.tsx]]
- [[apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx.md|apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx]]
- [[apps/web/src/components/Dialog/PKIBackupDialog.tsx.md|apps/web/src/components/Dialog/PKIBackupDialog.tsx]]
- [[apps/web/src/components/Dialog/QRDialog.tsx.md|apps/web/src/components/Dialog/QRDialog.tsx]]
- [[apps/web/src/components/Dialog/RebootDialog.tsx.md|apps/web/src/components/Dialog/RebootDialog.tsx]]
- [[apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.tsx.md|apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.tsx]]
- [[apps/web/src/components/Dialog/RemoveNodeDialog.tsx.md|apps/web/src/components/Dialog/RemoveNodeDialog.tsx]]
- [[apps/web/src/components/Dialog/ResetNodeDbDialog/ResetNodeDbDialog.tsx.md|apps/web/src/components/Dialog/ResetNodeDbDialog/ResetNodeDbDialog.tsx]]
- [[apps/web/src/components/Dialog/ShutdownDialog.tsx.md|apps/web/src/components/Dialog/ShutdownDialog.tsx]]
- [[apps/web/src/components/Dialog/UnsafeRolesDialog/UnsafeRolesDialog.tsx.md|apps/web/src/components/Dialog/UnsafeRolesDialog/UnsafeRolesDialog.tsx]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]

## Imported By (Dependents)
- [[apps/web/src/App.tsx.md|apps/web/src/App.tsx]]
- [[apps/web/src/routes.tsx.md|apps/web/src/routes.tsx]]

## Source Code Snippet
```tsx
import { FactoryResetConfigDialog } from "@app/components/Dialog/FactoryResetConfigDialog/FactoryResetConfigDialog";
import { FactoryResetDeviceDialog } from "@app/components/Dialog/FactoryResetDeviceDialog/FactoryResetDeviceDialog";
import { ClearAllStoresDialog } from "@components/Dialog/ClearAllStoresDialog/ClearAllStoresDialog.tsx";
import { ClientNotificationDialog } from "@components/Dialog/ClientNotificationDialog/ClientNotificationDialog.tsx";
import { DeleteMessagesDialog } from "@components/Dialog/DeleteMessagesDialog/DeleteMessagesDialog.tsx";
import { ImportDialog } from "@components/Dialog/ImportDialog.tsx";
import { NodeDetailsDialog } from "@components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx";
import { PkiBackupDialog } from "@components/Dialog/PKIBackupDialog.tsx";
import { QRDialog } from "@components/Dialog/QRDialog.tsx";
import { RebootDialog } from "@components/Dialog/RebootDialog.tsx";
import { RefreshKeysDialog } from "@components/Dialog/RefreshKeysDialog/RefreshKeysDialog.tsx";
import { RemoveNodeDialog } from "@components/Dialog/RemoveNodeDialog.tsx";
import { ResetNodeDbDialog } from "@components/Dialog/ResetNodeDbDialog/ResetNodeDbDialog.tsx";
import { ShutdownDialog } from "@components/Dialog/ShutdownDialog.tsx";
import { UnsafeRolesDialog } from "@components/Dialog/UnsafeRolesDialog/UnsafeRolesDialog.tsx";
import { useDevice } from "@core/stores";

export const DialogManager = () => {
  const { config, dialog, setDialogOpen } = useDevice();
  return (
...
```