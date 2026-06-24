# FormSelect.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Form/FormSelect.tsx`
- **Extension:** `.tsx`
- **Size:** 2986 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `SelectFieldProps`
- `SelectInput`

## Imports (Dependencies)
- [[apps/web/src/components/Form/DynamicForm.tsx.md|apps/web/src/components/Form/DynamicForm.tsx]]
- [[apps/web/src/components/UI/Select.tsx.md|apps/web/src/components/UI/Select.tsx]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Form/DynamicFormField.tsx.md|apps/web/src/components/Form/DynamicFormField.tsx]]

## Source Code Snippet
```tsx
import type {
  BaseFormBuilderProps,
  GenericFormElementProps,
} from "@components/Form/DynamicForm.tsx";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@components/UI/Select.tsx";
import { cn } from "@core/utils/cn.ts";
import { type FieldValues, useController } from "react-hook-form";

export interface SelectFieldProps<T> extends BaseFormBuilderProps<T> {
  type: "select";
  selectChange?: (e: string, name: string) => void;
  validate?: (newValue: string) => Promise<boolean>;
  defaultValue?: string;
  properties: BaseFormBuilderProps<T>["properties"] & {
...
```