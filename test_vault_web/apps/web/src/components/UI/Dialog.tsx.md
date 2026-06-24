# Dialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Dialog.tsx`
- **Extension:** `.tsx`
- **Size:** 4031 bytes
- **Centrality Score:** 0.0042
- **In-Degree (Imported By):** 15
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/ConnectingOverlay.tsx.md|apps/web/src/components/ConnectingOverlay.tsx]]
- [[apps/web/src/components/Dialog/ClientNotificationDialog/ClientNotificationDialog.tsx.md|apps/web/src/components/Dialog/ClientNotificationDialog/ClientNotificationDialog.tsx]]
- [[apps/web/src/components/Dialog/DialogWrapper.tsx.md|apps/web/src/components/Dialog/DialogWrapper.tsx]]
- [[apps/web/src/components/Dialog/ImportDialog.tsx.md|apps/web/src/components/Dialog/ImportDialog.tsx]]
- [[apps/web/src/components/Dialog/LocationResponseDialog.tsx.md|apps/web/src/components/Dialog/LocationResponseDialog.tsx]]
- [[apps/web/src/components/Dialog/ManagedModeDialog.tsx.md|apps/web/src/components/Dialog/ManagedModeDialog.tsx]]
- [[apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx.md|apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx]]
- [[apps/web/src/components/Dialog/PKIBackupDialog.tsx.md|apps/web/src/components/Dialog/PKIBackupDialog.tsx]]
- [[apps/web/src/components/Dialog/PkiRegenerateDialog.tsx.md|apps/web/src/components/Dialog/PkiRegenerateDialog.tsx]]
- [[apps/web/src/components/Dialog/QRDialog.tsx.md|apps/web/src/components/Dialog/QRDialog.tsx]]
- [[apps/web/src/components/Dialog/RebootDialog.tsx.md|apps/web/src/components/Dialog/RebootDialog.tsx]]
- [[apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.tsx.md|apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.tsx]]
- [[apps/web/src/components/Dialog/TracerouteResponseDialog.tsx.md|apps/web/src/components/Dialog/TracerouteResponseDialog.tsx]]
- [[apps/web/src/components/Dialog/UnsafeRolesDialog/UnsafeRolesDialog.tsx.md|apps/web/src/components/Dialog/UnsafeRolesDialog/UnsafeRolesDialog.tsx]]
- [[apps/web/src/components/UI/Command.tsx.md|apps/web/src/components/UI/Command.tsx]]

## Source Code Snippet
```tsx
import { cn } from "@core/utils/cn.ts";
import * as DialogPrimitive from "@radix-ui/react-dialog";
import { X } from "lucide-react";
import * as React from "react";

const Dialog = DialogPrimitive.Root;

const DialogTrigger = DialogPrimitive.Trigger;

const DialogPortal = ({
  children,
  ...props
}: DialogPrimitive.DialogPortalProps) => (
  <DialogPrimitive.Portal {...props}>
    <div className="fixed inset-0 z-50 flex items-start justify-center sm:items-center">
      {children}
    </div>
  </DialogPrimitive.Portal>
);
DialogPortal.displayName = DialogPrimitive.Portal.displayName;
...
```