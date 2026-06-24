# FormWrapper.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Form/FormWrapper.tsx`
- **Extension:** `.tsx`
- **Size:** 1163 bytes
- **Centrality Score:** 0.0015
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `FieldWrapperProps`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Label.tsx.md|apps/web/src/components/UI/Label.tsx]]

## Imported By (Dependents)
- [[apps/web/src/components/Form/DynamicForm.tsx.md|apps/web/src/components/Form/DynamicForm.tsx]]

## Source Code Snippet
```tsx
import { Label } from "@components/UI/Label.tsx";

export interface FieldWrapperProps {
  label: string;
  fieldName: string;
  description?: string;
  disabled?: boolean;
  children?: React.ReactNode;
  valid?: boolean;
  validationText?: string;
}

export const FieldWrapper = ({
  label,
  fieldName,
  description,
  children,
  valid,
  validationText,
}: FieldWrapperProps) => (
...
```