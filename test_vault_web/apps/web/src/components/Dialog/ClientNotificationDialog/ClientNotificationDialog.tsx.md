# ClientNotificationDialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/ClientNotificationDialog/ClientNotificationDialog.tsx`
- **Extension:** `.tsx`
- **Size:** 5521 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ClientNotificationDialogProps`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Dialog.tsx.md|apps/web/src/components/UI/Dialog.tsx]]
- [[apps/web/src/components/UI/Input.tsx.md|apps/web/src/components/UI/Input.tsx]]
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
import { Input } from "@components/UI/Input.tsx";
import { useDevice } from "@core/stores";
import { Protobuf } from "@meshtastic/core";
import { useState } from "react";
import { useTranslation } from "react-i18next";

const MessageType = Protobuf.Admin.KeyVerificationAdmin_MessageType;

export interface ClientNotificationDialogProps {
  open: boolean;
...
```