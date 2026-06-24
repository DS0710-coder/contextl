# ChannelChat.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Messages/ChannelChat.tsx`
- **Extension:** `.tsx`
- **Size:** 4737 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ChannelChatProps`
- `toTs`
- `startOfLocalDay`
- `formatDateLabelFromDayKey`
- `DayGroup`
- `groupMessagesByDay`

## Imports (Dependencies)
- [[apps/web/src/components/PageComponents/Messages/MessageItem.tsx.md|apps/web/src/components/PageComponents/Messages/MessageItem.tsx]]
- [[apps/web/src/components/UI/Separator.tsx.md|apps/web/src/components/UI/Separator.tsx]]
- [[apps/web/src/components/UI/Skeleton.tsx.md|apps/web/src/components/UI/Skeleton.tsx]]
- [[apps/web/src/core/stores/messageStore/index.ts.md|apps/web/src/core/stores/messageStore/index.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Messages.tsx.md|apps/web/src/pages/Messages.tsx]]

## Source Code Snippet
```tsx
import { MessageItem } from "@components/PageComponents/Messages/MessageItem.tsx";
import { Separator } from "@components/UI/Separator";
import { Skeleton } from "@components/UI/Skeleton.tsx";
import type { Message } from "@core/stores/messageStore";
import type { TFunction } from "i18next";
import { InboxIcon } from "lucide-react";
import { Fragment, Suspense, useMemo } from "react";
import { useTranslation } from "react-i18next";

export interface ChannelChatProps {
  messages?: Message[];
}

function toTs(d: Message["date"]): number {
  return typeof d === "number" ? d : Date.parse(String(d));
}

function startOfLocalDay(ts: number): number {
  const d = new Date(ts);
  d.setHours(0, 0, 0, 0);
...
```