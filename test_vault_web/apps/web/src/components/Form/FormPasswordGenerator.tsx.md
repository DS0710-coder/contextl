# FormPasswordGenerator.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Form/FormPasswordGenerator.tsx`
- **Extension:** `.tsx`
- **Size:** 2101 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PasswordGeneratorProps`
- `PasswordGenerator`

## Imports (Dependencies)
- [[apps/web/src/components/Form/DynamicForm.tsx.md|apps/web/src/components/Form/DynamicForm.tsx]]
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Generator.tsx.md|apps/web/src/components/UI/Generator.tsx]]
- [[apps/web/src/core/hooks/usePasswordVisibilityToggle.ts.md|apps/web/src/core/hooks/usePasswordVisibilityToggle.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/Form/DynamicFormField.tsx.md|apps/web/src/components/Form/DynamicFormField.tsx]]

## Source Code Snippet
```tsx
import type {
  BaseFormBuilderProps,
  GenericFormElementProps,
} from "@components/Form/DynamicForm.tsx";
import { Generator } from "@components/UI/Generator.tsx";
import { usePasswordVisibilityToggle } from "@core/hooks/usePasswordVisibilityToggle.ts";
import { Controller, type FieldValues } from "react-hook-form";
import type { ButtonVariant } from "../UI/Button.tsx";

export interface PasswordGeneratorProps<T> extends BaseFormBuilderProps<T> {
  type: "passwordGenerator";
  id: string;
  hide?: boolean;
  bits?: { text: string; value: string; key: string }[];
  devicePSKBitCount: number;
  inputChange?: React.ChangeEventHandler<HTMLInputElement>;
  selectChange?: (event: string) => void;
  actionButtons: {
    text: string;
    onClick: React.MouseEventHandler<HTMLButtonElement>;
...
```