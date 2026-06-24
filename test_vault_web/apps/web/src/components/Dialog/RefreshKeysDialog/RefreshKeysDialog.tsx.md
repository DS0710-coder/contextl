# RefreshKeysDialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.tsx`
- **Extension:** `.tsx`
- **Size:** 2792 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `RefreshKeysDialogProps`

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/RefreshKeysDialog/useRefreshKeysDialog.ts.md|apps/web/src/components/Dialog/RefreshKeysDialog/useRefreshKeysDialog.ts]]
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Dialog.tsx.md|apps/web/src/components/UI/Dialog.tsx]]
- [[apps/web/src/core/hooks/useNodesAsProto.ts.md|apps/web/src/core/hooks/useNodesAsProto.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/DialogManager.tsx.md|apps/web/src/components/Dialog/DialogManager.tsx]]
- [[apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.test.tsx.md|apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.test.tsx]]

## Source Code Snippet
```tsx
import { Button } from "@components/UI/Button.tsx";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@components/UI/Dialog.tsx";
import { useNodeAsProto } from "@core/hooks/useNodesAsProto.ts";
import { useNodeErrors } from "@meshtastic/sdk-react";
import { LockKeyholeOpenIcon } from "lucide-react";
import { useTranslation } from "react-i18next";
import { useRefreshKeysDialog } from "./useRefreshKeysDialog.ts";

export interface RefreshKeysDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
}

export const RefreshKeysDialog = ({
...
```