# Tak.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/ModuleConfig/Tak.tsx`
- **Extension:** `.tsx`
- **Size:** 2127 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TakValidation`
- `DynamicFormFormInit`
- `TakModuleConfigProps`

## Imports (Dependencies)
- [[apps/web/src/components/Form/DynamicForm.tsx.md|apps/web/src/components/Form/DynamicForm.tsx]]
- [[apps/web/src/core/hooks/useWaitForConfig.ts.md|apps/web/src/core/hooks/useWaitForConfig.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/core/utils/deepCompareConfig.ts.md|apps/web/src/core/utils/deepCompareConfig.ts]]
- [[apps/web/src/validation/moduleConfig/tak.ts.md|apps/web/src/validation/moduleConfig/tak.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Settings/ModuleConfig.tsx.md|apps/web/src/pages/Settings/ModuleConfig.tsx]]

## Source Code Snippet
```tsx
import { useWaitForConfig } from "@app/core/hooks/useWaitForConfig";
import {
  type TakValidation,
  TakValidationSchema,
} from "@app/validation/moduleConfig/tak.ts";
import {
  DynamicForm,
  type DynamicFormFormInit,
} from "@components/Form/DynamicForm.tsx";
import { useDevice } from "@core/stores";
import { deepCompareConfig } from "@core/utils/deepCompareConfig.ts";
import { Protobuf } from "@meshtastic/core";
import { useTranslation } from "react-i18next";

interface TakModuleConfigProps {
  onFormInit: DynamicFormFormInit<TakValidation>;
}

export const Tak = ({ onFormInit }: TakModuleConfigProps) => {
  useWaitForConfig({ moduleConfigCase: "tak" });
...
```