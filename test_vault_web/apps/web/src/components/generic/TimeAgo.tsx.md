# TimeAgo.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/generic/TimeAgo.tsx`
- **Extension:** `.tsx`
- **Size:** 3533 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 7
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TimeAgoProps`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx.md|apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx.md|apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/WaypointDetail.tsx.md|apps/web/src/components/PageComponents/Map/Popups/WaypointDetail.tsx]]
- [[apps/web/src/components/generic/Filter/FilterControl.tsx.md|apps/web/src/components/generic/Filter/FilterControl.tsx]]
- [[apps/web/src/components/generic/Table/index.test.tsx.md|apps/web/src/components/generic/Table/index.test.tsx]]
- [[apps/web/src/pages/Connections/index.tsx.md|apps/web/src/pages/Connections/index.tsx]]
- [[apps/web/src/pages/Nodes/index.tsx.md|apps/web/src/pages/Nodes/index.tsx]]

## Source Code Snippet
```tsx
import {
  Tooltip,
  TooltipContent,
  TooltipPortal,
  TooltipProvider,
  TooltipTrigger,
} from "@radix-ui/react-tooltip";
import { useEffect, useMemo, useState } from "react";
import { useTranslation } from "react-i18next";

export interface TimeAgoProps {
  timestamp: number | Date;
  locale?: string;
  tooltipOptions?: Intl.DateTimeFormatOptions;
  className?: string;
}

const TIME_UNITS: Array<[Intl.RelativeTimeFormatUnit, number]> = [
  ["year", 31536000],
  ["month", 2592000],
...
```