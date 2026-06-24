# Slider.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Slider.tsx`
- **Extension:** `.tsx`
- **Size:** 2410 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `SliderProps`
- `Slider`

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/generic/Filter/FilterComponents.tsx.md|apps/web/src/components/generic/Filter/FilterComponents.tsx]]

## Source Code Snippet
```tsx
import { cn } from "@core/utils/cn.ts";
import * as SliderPrimitive from "@radix-ui/react-slider";
import { useId, useState } from "react";

export interface SliderProps {
  value: number[];
  step?: number;
  min?: number;
  max: number;
  onValueChange?: (value: number[]) => void;
  onValueCommit?: (value: number[]) => void;
  id?: string;
  disabled?: boolean;
  className?: string;
  trackClassName?: string;
  rangeClassName?: string;
  thumbClassName?: string;
}

export function Slider({
...
```