# PkiRegenerateDialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/PkiRegenerateDialog.tsx`
- **Extension:** `.tsx`
- **Size:** 1432 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PkiRegenerateDialogProps`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Dialog.tsx.md|apps/web/src/components/UI/Dialog.tsx]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Channels/Channel.tsx.md|apps/web/src/components/PageComponents/Channels/Channel.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Security/Security.tsx.md|apps/web/src/components/PageComponents/Settings/Security/Security.tsx]]

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
import { useTranslation } from "react-i18next";

export interface PkiRegenerateDialogProps {
  text: {
    title: string;
    description: string;
    button: string;
  };
  open: boolean;
  onOpenChange: () => void;
...
```