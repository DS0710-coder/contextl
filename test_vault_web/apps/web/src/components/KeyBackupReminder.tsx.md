# KeyBackupReminder.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/KeyBackupReminder.tsx`
- **Extension:** `.tsx`
- **Size:** 458 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/core/hooks/useKeyBackupReminder.tsx.md|apps/web/src/core/hooks/useKeyBackupReminder.tsx]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]

## Imported By (Dependents)
- [[apps/web/src/App.tsx.md|apps/web/src/App.tsx]]

## Source Code Snippet
```tsx
import { useBackupReminder } from "@core/hooks/useKeyBackupReminder.tsx";
import { useDevice } from "@core/stores";
import { useTranslation } from "react-i18next";

export const KeyBackupReminder = () => {
  const { setDialogOpen } = useDevice();
  const { t } = useTranslation("dialog");

  useBackupReminder({
    message: t("pkiBackupReminder.description"),
    onAccept: () => setDialogOpen("pkiBackup", true),
    enabled: true,
  });
  return null;
};
```