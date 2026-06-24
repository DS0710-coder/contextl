# ManagedModeDialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/ManagedModeDialog.tsx`
- **Extension:** `.tsx`
- **Size:** 1903 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ManagedModeDialogProps`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Checkbox/index.tsx.md|apps/web/src/components/UI/Checkbox/index.tsx]]
- [[apps/web/src/components/UI/Dialog.tsx.md|apps/web/src/components/UI/Dialog.tsx]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Settings/Security/Security.tsx.md|apps/web/src/components/PageComponents/Settings/Security/Security.tsx]]

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
import { useState } from "react";
import { Trans, useTranslation } from "react-i18next";

export interface ManagedModeDialogProps {
  open: boolean;
  onOpenChange: () => void;
  onSubmit: () => void;
}

...
```