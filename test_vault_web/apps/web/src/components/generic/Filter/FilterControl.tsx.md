# FilterControl.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/generic/Filter/FilterControl.tsx`
- **Extension:** `.tsx`
- **Size:** 13355 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ComponentProps`
- `ReactNode`
- `PopoverContentProps`
- `FilterControlProps`
- `RangeLabelContentProps`
- `RangeLabelContent`
- `FilterControl`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Accordion.tsx.md|apps/web/src/components/UI/Accordion.tsx]]
- [[apps/web/src/components/UI/Input.tsx.md|apps/web/src/components/UI/Input.tsx]]
- [[apps/web/src/components/UI/Popover.tsx.md|apps/web/src/components/UI/Popover.tsx]]
- [[apps/web/src/components/generic/Filter/FilterComponents.tsx.md|apps/web/src/components/generic/Filter/FilterComponents.tsx]]
- [[apps/web/src/components/generic/Filter/useFilterNode.ts.md|apps/web/src/components/generic/Filter/useFilterNode.ts]]
- [[apps/web/src/components/generic/TimeAgo.tsx.md|apps/web/src/components/generic/TimeAgo.tsx]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]
- [[apps/web/src/core/utils/debounce.ts.md|apps/web/src/core/utils/debounce.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Map/index.tsx.md|apps/web/src/pages/Map/index.tsx]]
- [[apps/web/src/pages/Nodes/index.tsx.md|apps/web/src/pages/Nodes/index.tsx]]

## Source Code Snippet
```tsx
import {
  FilterAccordionItem,
  FilterMulti,
  FilterSlider,
  FilterToggle,
} from "@components/generic/Filter/FilterComponents.tsx";
import type { FilterState } from "@components/generic/Filter/useFilterNode.ts";
import { TimeAgo } from "@components/generic/TimeAgo.tsx";
import { Accordion } from "@components/UI/Accordion.tsx";
import { Input } from "@components/UI/Input.tsx";
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@components/UI/Popover.tsx";
import { cn } from "@core/utils/cn.ts";
import { debounce } from "@core/utils/debounce.ts";
import { Protobuf } from "@meshtastic/sdk";
import { FunnelIcon } from "lucide-react";
import {
...
```