# FormToggle.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Form/FormToggle.tsx`
- **Extension:** `.tsx`
- **Size:** 1293 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ToggleFieldProps`
- `ToggleInput`

## Imports (Dependencies)
- [[apps/web/src/components/Form/DynamicForm.tsx.md|apps/web/src/components/Form/DynamicForm.tsx]]
- [[apps/web/src/components/UI/Switch.tsx.md|apps/web/src/components/UI/Switch.tsx]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Form/DynamicFormField.tsx.md|apps/web/src/components/Form/DynamicFormField.tsx]]

## Source Code Snippet
```tsx
import type {
  BaseFormBuilderProps,
  GenericFormElementProps,
} from "@components/Form/DynamicForm.tsx";
import { Switch } from "@components/UI/Switch.tsx";
import { cn } from "@core/utils/cn.ts";
import { Controller, type FieldValues } from "react-hook-form";

export interface ToggleFieldProps<T> extends BaseFormBuilderProps<T> {
  type: "toggle";
  inputChange?: (value: boolean) => void;
}

export function ToggleInput<T extends FieldValues>({
  control,
  disabled,
  field,
  isDirty,
  invalid,
}: GenericFormElementProps<T, ToggleFieldProps<T>>) {
...
```