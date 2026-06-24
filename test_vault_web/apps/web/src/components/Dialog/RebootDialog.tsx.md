# RebootDialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/RebootDialog.tsx`
- **Extension:** `.tsx`
- **Size:** 4613 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `RebootDialogProps`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Checkbox/index.tsx.md|apps/web/src/components/UI/Checkbox/index.tsx]]
- [[apps/web/src/components/UI/Dialog.tsx.md|apps/web/src/components/UI/Dialog.tsx]]
- [[apps/web/src/components/UI/Input.tsx.md|apps/web/src/components/UI/Input.tsx]]
- [[apps/web/src/components/UI/Label.tsx.md|apps/web/src/components/UI/Label.tsx]]
- [[apps/web/src/components/UI/Separator.tsx.md|apps/web/src/components/UI/Separator.tsx]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/DialogManager.tsx.md|apps/web/src/components/Dialog/DialogManager.tsx]]
- [[apps/web/src/components/Dialog/RebootDialog.test.tsx.md|apps/web/src/components/Dialog/RebootDialog.test.tsx]]

## Source Code Snippet
```tsx
import { Button } from "@components/UI/Button.tsx";
import { Checkbox } from "@components/UI/Checkbox/index.tsx";
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@components/UI/Dialog.tsx";
import { Input } from "@components/UI/Input.tsx";
import { Label } from "@components/UI/Label.tsx";
import { Separator } from "@components/UI/Separator.tsx";
import { useDevice } from "@core/stores";
import { ClockIcon, OctagonXIcon, RefreshCwIcon } from "lucide-react";
import { useState } from "react";
import { useTranslation } from "react-i18next";

export interface RebootDialogProps {
  open: boolean;
...
```