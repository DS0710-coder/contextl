# FilterComponents.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/generic/Filter/FilterComponents.tsx`
- **Extension:** `.tsx`
- **Size:** 6220 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `FilterAccordionItemProps`
- `RangeKeys`
- `FilterSliderProps`
- `EnumArrayKeys`
- `FilterMultiProps`
- `FilterToggleProps`
- `getNumberArray`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Accordion.tsx.md|apps/web/src/components/UI/Accordion.tsx]]
- [[apps/web/src/components/UI/Checkbox/index.tsx.md|apps/web/src/components/UI/Checkbox/index.tsx]]
- [[apps/web/src/components/UI/ScrollArea.tsx.md|apps/web/src/components/UI/ScrollArea.tsx]]
- [[apps/web/src/components/UI/Slider.tsx.md|apps/web/src/components/UI/Slider.tsx]]
- [[apps/web/src/components/UI/ToggleGroup.tsx.md|apps/web/src/components/UI/ToggleGroup.tsx]]
- [[apps/web/src/components/generic/Filter/useFilterNode.ts.md|apps/web/src/components/generic/Filter/useFilterNode.ts]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/generic/Filter/FilterControl.tsx.md|apps/web/src/components/generic/Filter/FilterControl.tsx]]

## Source Code Snippet
```tsx
import type { FilterState } from "@components/generic/Filter/useFilterNode.ts";
import {
  AccordionContent,
  AccordionHeader,
  AccordionItem,
  AccordionTrigger,
} from "@components/UI/Accordion.tsx";
import { Checkbox } from "@components/UI/Checkbox/index.tsx";
import { ScrollArea } from "@components/UI/ScrollArea.tsx";
import { Slider } from "@components/UI/Slider.tsx";
import { ToggleGroup, ToggleGroupItem } from "@components/UI/ToggleGroup.tsx";
import { cn } from "@core/utils/cn.ts";
import type { ReactNode } from "react";
import { useId } from "react";

interface FilterAccordionItemProps {
  label: string;
  children?: ReactNode;
}

...
```