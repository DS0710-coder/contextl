# FormMultiSelect.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Form/FormMultiSelect.tsx`
- **Extension:** `.tsx`
- **Size:** 2364 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `MultiSelectFieldProps`
- `MultiSelectInput`

## Imports (Dependencies)
- [[apps/web/src/components/Form/DynamicForm.tsx.md|apps/web/src/components/Form/DynamicForm.tsx]]
- [[apps/web/src/components/UI/MultiSelect.tsx.md|apps/web/src/components/UI/MultiSelect.tsx]]
- [[apps/web/src/core/hooks/usePositionFlags.ts.md|apps/web/src/core/hooks/usePositionFlags.ts]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Form/DynamicFormField.tsx.md|apps/web/src/components/Form/DynamicFormField.tsx]]

## Source Code Snippet
```tsx
import type {
  BaseFormBuilderProps,
  GenericFormElementProps,
} from "@components/Form/DynamicForm.tsx";
import type { FLAGS_CONFIG } from "@core/hooks/usePositionFlags.ts";
import { cn } from "@core/utils/cn.ts";
import type { FieldValues } from "react-hook-form";
import { useTranslation } from "react-i18next";
import { MultiSelect, MultiSelectItem } from "../UI/MultiSelect.tsx";

export interface MultiSelectFieldProps<T> extends BaseFormBuilderProps<T> {
  type: "multiSelect";
  placeholder?: string;
  onValueChange: (name: string) => void;
  isChecked: (name: string) => boolean;
  value: string[];
  properties: BaseFormBuilderProps<T>["properties"] & {
    enumValue: { [s: string]: string | number } | typeof FLAGS_CONFIG;
    formatEnumName?: boolean;
  };
...
```