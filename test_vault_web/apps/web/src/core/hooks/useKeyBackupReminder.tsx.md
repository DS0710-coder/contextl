# useKeyBackupReminder.tsx

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useKeyBackupReminder.tsx`
- **Extension:** `.tsx`
- **Size:** 3500 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `UseBackupReminderOptions`
- `ReminderState`
- `isReminderExpired`
- `useBackupReminder`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/core/hooks/useLocalStorage.ts.md|apps/web/src/core/hooks/useLocalStorage.ts]]
- [[apps/web/src/core/hooks/useToast.ts.md|apps/web/src/core/hooks/useToast.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/KeyBackupReminder.tsx.md|apps/web/src/components/KeyBackupReminder.tsx]]

## Source Code Snippet
```tsx
import { Button } from "@components/UI/Button.tsx";
import useLocalStorage from "@core/hooks/useLocalStorage.ts";
import { useToast } from "@core/hooks/useToast.ts";
import { useCallback, useEffect, useRef } from "react";
import { useTranslation } from "react-i18next";

interface UseBackupReminderOptions {
  reminderInDays?: number;
  message: string;
  onAccept?: () => void | Promise<void>;
  enabled: boolean;
}

interface ReminderState {
  expires: string;
}

const TOAST_APPEAR_DELAY = 10_000; // 10 seconds
const TOAST_DURATION = 30_000; // 30 seconds
const REMINDER_DAYS_ONE_WEEK = 7;
...
```