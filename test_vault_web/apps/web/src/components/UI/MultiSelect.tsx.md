# MultiSelect.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/MultiSelect.tsx`
- **Extension:** `.tsx`
- **Size:** 1545 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `MultiSelectProps`
- `MultiSelectItemProps`

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Form/FormMultiSelect.tsx.md|apps/web/src/components/Form/FormMultiSelect.tsx]]

## Source Code Snippet
```tsx
import * as CheckboxPrimitive from "@radix-ui/react-checkbox";
import { Check } from "lucide-react";
import { cn } from "../../core/utils/cn.ts";

interface MultiSelectProps {
  children: React.ReactNode;
  className?: string;
}

const MultiSelect = ({ children, className = "" }: MultiSelectProps) => {
  return (
    <div className={cn("flex flex-wrap gap-2", className)}>{children}</div>
  );
};

interface MultiSelectItemProps {
  name: string;
  value: string;
  checked: boolean;
  onCheckedChange: (name: string, value: boolean) => void;
...
```