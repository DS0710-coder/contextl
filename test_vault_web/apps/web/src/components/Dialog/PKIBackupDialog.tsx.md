# PKIBackupDialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/PKIBackupDialog.tsx`
- **Extension:** `.tsx`
- **Size:** 5147 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PkiBackupDialogProps`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Dialog.tsx.md|apps/web/src/components/UI/Dialog.tsx]]
- [[apps/web/src/core/hooks/useNodesAsProto.ts.md|apps/web/src/core/hooks/useNodesAsProto.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/DialogManager.tsx.md|apps/web/src/components/Dialog/DialogManager.tsx]]

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
import { useMyNodeAsProto } from "@core/hooks/useNodesAsProto.ts";
import { useDevice } from "@core/stores";
import { fromByteArray } from "base64-js";
import { DownloadIcon, PrinterIcon } from "lucide-react";
import React from "react";
import { useTranslation } from "react-i18next";

export interface PkiBackupDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
...
```