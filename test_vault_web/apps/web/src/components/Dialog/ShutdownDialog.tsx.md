# ShutdownDialog.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/ShutdownDialog.tsx`
- **Extension:** `.tsx`
- **Size:** 1647 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ShutdownDialogProps`

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/DialogWrapper.tsx.md|apps/web/src/components/Dialog/DialogWrapper.tsx]]
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Input.tsx.md|apps/web/src/components/UI/Input.tsx]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/DialogManager.tsx.md|apps/web/src/components/Dialog/DialogManager.tsx]]

## Source Code Snippet
```tsx
import { Button } from "@components/UI/Button.tsx";
import { Input } from "@components/UI/Input.tsx";
import { useDevice } from "@core/stores";
import { ClockIcon, PowerIcon } from "lucide-react";
import { useState } from "react";
import { useTranslation } from "react-i18next";
import { DialogWrapper } from "./DialogWrapper.tsx";

export interface ShutdownDialogProps {
  open: boolean;
  onOpenChange: (open: boolean) => void;
}

export const ShutdownDialog = ({ open, onOpenChange }: ShutdownDialogProps) => {
  const { t } = useTranslation("dialog");
  const { connection } = useDevice();
  const [time, setTime] = useState<number>(5);

  const handleScheduledShutdown = () => {
    connection?.shutdown(time * 60).then(() => onOpenChange(false));
...
```