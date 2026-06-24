# UnsafeRolesDialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/UnsafeRolesDialog/UnsafeRolesDialog.tsx`
- **Extension:** `.tsx`
- **Size:** 2894 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `RouterRoleDialogProps`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Checkbox/index.tsx.md|apps/web/src/components/UI/Checkbox/index.tsx]]
- [[apps/web/src/components/UI/Dialog.tsx.md|apps/web/src/components/UI/Dialog.tsx]]
- [[apps/web/src/components/UI/Typography/Link.tsx.md|apps/web/src/components/UI/Typography/Link.tsx]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/core/utils/eventBus.ts.md|apps/web/src/core/utils/eventBus.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/DialogManager.tsx.md|apps/web/src/components/Dialog/DialogManager.tsx]]

## Source Code Snippet
```tsx
import { Button } from "@components/UI/Button.tsx";
import { Checkbox } from "@components/UI/Checkbox/index.tsx";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@components/UI/Dialog.tsx";
import { Link } from "@components/UI/Typography/Link.tsx";
import { useDevice } from "@core/stores";
import { eventBus } from "@core/utils/eventBus.ts";
import { useState } from "react";
import { useTranslation } from "react-i18next";

export interface RouterRoleDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
...
```