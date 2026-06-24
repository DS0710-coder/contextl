# Button.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Button.tsx`
- **Extension:** `.tsx`
- **Size:** 2718 bytes
- **Centrality Score:** 0.0074
- **In-Degree (Imported By):** 29
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ButtonVariant`
- `ButtonProps`

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/ConnectingOverlay.tsx.md|apps/web/src/components/ConnectingOverlay.tsx]]
- [[apps/web/src/components/DeviceInfoPanel.tsx.md|apps/web/src/components/DeviceInfoPanel.tsx]]
- [[apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx.md|apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx]]
- [[apps/web/src/components/Dialog/ClientNotificationDialog/ClientNotificationDialog.tsx.md|apps/web/src/components/Dialog/ClientNotificationDialog/ClientNotificationDialog.tsx]]
- [[apps/web/src/components/Dialog/DialogWrapper.tsx.md|apps/web/src/components/Dialog/DialogWrapper.tsx]]
- [[apps/web/src/components/Dialog/ImportDialog.tsx.md|apps/web/src/components/Dialog/ImportDialog.tsx]]
- [[apps/web/src/components/Dialog/ManagedModeDialog.tsx.md|apps/web/src/components/Dialog/ManagedModeDialog.tsx]]
- [[apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx.md|apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx]]
- [[apps/web/src/components/Dialog/PKIBackupDialog.tsx.md|apps/web/src/components/Dialog/PKIBackupDialog.tsx]]
- [[apps/web/src/components/Dialog/PkiRegenerateDialog.tsx.md|apps/web/src/components/Dialog/PkiRegenerateDialog.tsx]]
- [[apps/web/src/components/Dialog/RebootDialog.tsx.md|apps/web/src/components/Dialog/RebootDialog.tsx]]
- [[apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.tsx.md|apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.tsx]]
- [[apps/web/src/components/Dialog/ShutdownDialog.tsx.md|apps/web/src/components/Dialog/ShutdownDialog.tsx]]
- [[apps/web/src/components/Dialog/UnsafeRolesDialog/UnsafeRolesDialog.tsx.md|apps/web/src/components/Dialog/UnsafeRolesDialog/UnsafeRolesDialog.tsx]]
- [[apps/web/src/components/Form/DynamicForm.tsx.md|apps/web/src/components/Form/DynamicForm.tsx]]
- [[apps/web/src/components/Form/FormPasswordGenerator.tsx.md|apps/web/src/components/Form/FormPasswordGenerator.tsx]]
- [[apps/web/src/components/LanguageSwitcher.tsx.md|apps/web/src/components/LanguageSwitcher.tsx]]
- [[apps/web/src/components/PageComponents/Channels/Channels.tsx.md|apps/web/src/components/PageComponents/Channels/Channels.tsx]]
- [[apps/web/src/components/PageComponents/Connections/ConnectionStatusBadge.tsx.md|apps/web/src/components/PageComponents/Connections/ConnectionStatusBadge.tsx]]
- [[apps/web/src/components/PageComponents/Messages/MessageInput.tsx.md|apps/web/src/components/PageComponents/Messages/MessageInput.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Position.tsx.md|apps/web/src/components/PageComponents/Settings/Position.tsx]]
- [[apps/web/src/components/RegionSetupReminder.tsx.md|apps/web/src/components/RegionSetupReminder.tsx]]
- [[apps/web/src/components/ThemeSwitcher.tsx.md|apps/web/src/components/ThemeSwitcher.tsx]]
- [[apps/web/src/components/UI/AlertDialog.tsx.md|apps/web/src/components/UI/AlertDialog.tsx]]
- [[apps/web/src/components/UI/Generator.tsx.md|apps/web/src/components/UI/Generator.tsx]]
- [[apps/web/src/components/UI/Sidebar/SidebarButton.tsx.md|apps/web/src/components/UI/Sidebar/SidebarButton.tsx]]
- [[apps/web/src/core/hooks/useKeyBackupReminder.tsx.md|apps/web/src/core/hooks/useKeyBackupReminder.tsx]]
- [[apps/web/src/core/hooks/useToast.test.tsx.md|apps/web/src/core/hooks/useToast.test.tsx]]
- [[apps/web/src/pages/Connections/index.tsx.md|apps/web/src/pages/Connections/index.tsx]]

## Source Code Snippet
```tsx
import { cn } from "@core/utils/cn.ts";
import { cva, type VariantProps } from "class-variance-authority";
import type * as React from "react";

const buttonVariants = cva(
  "inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors focus:outline-none focus:ring-2 focus:ring-slate-400 focus:ring-offset-2 disabled:opacity-50 dark:focus:ring-slate-400 disabled:cursor-not-allowed dark:focus:ring-offset-slate-900 cursor-pointer",
  {
    variants: {
      variant: {
        default:
          "bg-slate-900 text-white dark:bg-slate-50 hover:dark:bg-slate-200 dark:text-slate-900 hover:bg-slate-500",
        destructive:
          "bg-red-500 text-white hover:bg-red-600 dark:hover:bg-red-600",
        success:
          "bg-green-500 text-white hover:bg-green-600 dark:hover:bg-green-600",
        outline:
          "bg-transparent border border-slate-400 hover:text-slate-400 dark:hover:text-slate-300 dark:border-slate-400 dark:text-slate-100 ",
        subtle:
          "bg-slate-100 text-slate-700 hover:bg-slate-200 dark:bg-slate-500 dark:text-white dark:hover:bg-slate-400",
        ghost:
...
```