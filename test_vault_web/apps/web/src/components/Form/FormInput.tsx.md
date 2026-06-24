# FormInput.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Form/FormInput.tsx`
- **Extension:** `.tsx`
- **Size:** 2727 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `InputFieldProps`
- `GenericInput`

## Imports (Dependencies)
- [[apps/web/src/components/Form/DynamicForm.tsx.md|apps/web/src/components/Form/DynamicForm.tsx]]
- [[apps/web/src/components/UI/Input.tsx.md|apps/web/src/components/UI/Input.tsx]]

## Imported By (Dependents)
- [[apps/web/src/components/Form/DynamicFormField.tsx.md|apps/web/src/components/Form/DynamicFormField.tsx]]

## Source Code Snippet
```tsx
import type {
  BaseFormBuilderProps,
  GenericFormElementProps,
} from "@components/Form/DynamicForm.tsx";
import { Input } from "@components/UI/Input.tsx";
import type { ChangeEventHandler } from "react";
import { type FieldValues, useController } from "react-hook-form";

export interface InputFieldProps<T> extends BaseFormBuilderProps<T> {
  type: "text" | "number" | "password";
  inputChange?: ChangeEventHandler;
  prefix?: string;
  properties?: {
    id?: string;
    suffix?: string;
    step?: number;
    className?: string;
    fieldLength?: {
      min?: number;
      max?: number;
...
```