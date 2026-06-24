# Input.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Input.tsx`
- **Extension:** `.tsx`
- **Size:** 7435 bytes
- **Centrality Score:** 0.0026
- **In-Degree (Imported By):** 12
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `InputActionType`
- `InputProps`

## Imports (Dependencies)
- [[apps/web/src/core/hooks/useCopyToClipboard.ts.md|apps/web/src/core/hooks/useCopyToClipboard.ts]]
- [[apps/web/src/core/hooks/usePasswordVisibilityToggle.ts.md|apps/web/src/core/hooks/usePasswordVisibilityToggle.ts]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx.md|apps/web/src/components/Dialog/AddConnectionDialog/AddConnectionDialog.tsx]]
- [[apps/web/src/components/Dialog/ClientNotificationDialog/ClientNotificationDialog.tsx.md|apps/web/src/components/Dialog/ClientNotificationDialog/ClientNotificationDialog.tsx]]
- [[apps/web/src/components/Dialog/ImportDialog.tsx.md|apps/web/src/components/Dialog/ImportDialog.tsx]]
- [[apps/web/src/components/Dialog/QRDialog.tsx.md|apps/web/src/components/Dialog/QRDialog.tsx]]
- [[apps/web/src/components/Dialog/RebootDialog.tsx.md|apps/web/src/components/Dialog/RebootDialog.tsx]]
- [[apps/web/src/components/Dialog/ShutdownDialog.tsx.md|apps/web/src/components/Dialog/ShutdownDialog.tsx]]
- [[apps/web/src/components/Form/FormInput.tsx.md|apps/web/src/components/Form/FormInput.tsx]]
- [[apps/web/src/components/PageComponents/Messages/MessageInput.tsx.md|apps/web/src/components/PageComponents/Messages/MessageInput.tsx]]
- [[apps/web/src/components/UI/Generator.tsx.md|apps/web/src/components/UI/Generator.tsx]]
- [[apps/web/src/components/generic/Filter/FilterControl.tsx.md|apps/web/src/components/generic/Filter/FilterControl.tsx]]
- [[apps/web/src/pages/Messages.tsx.md|apps/web/src/pages/Messages.tsx]]
- [[apps/web/src/pages/Nodes/index.tsx.md|apps/web/src/pages/Nodes/index.tsx]]

## Source Code Snippet
```tsx
import { useCopyToClipboard } from "@core/hooks/useCopyToClipboard.ts";
import { usePasswordVisibilityToggle } from "@core/hooks/usePasswordVisibilityToggle.ts";
import { cn } from "@core/utils/cn.ts";
import { cva, type VariantProps } from "class-variance-authority";
import { Check, Copy, Eye, EyeOff, type LucideIcon, X } from "lucide-react";
import * as React from "react";
import { useTranslation } from "react-i18next";

const cnInvalidBase = "border-2 border-red-500 dark:border-red-500";
const cnDirtyBase = "border-2 border-sky-500 dark:border-sky-500";

const inputVariants = cva(
  "flex h-10 w-full rounded-md border border-slate-300 bg-transparent py-2 px-3 text-sm placeholder:text-slate-400 focus:outline-none focus:ring-1 focus:ring-slate-400 disabled:cursor-not-allowed disabled:opacity-50 dark:border-slate-500 dark:bg-transparent dark:text-slate-100 dark:focus:ring-slate-400 dark:focus:ring-offset-slate-600",
  {
    variants: {
      variant: {
        default: "border-slate-300 dark:border-slate-500",
        invalid: `${cnInvalidBase} focus:ring-red-500 dark:focus:ring-red-500`,
        dirty: `${cnDirtyBase} focus:ring-sky-500 dark:focus:ring-sky-500`,
      },
...
```