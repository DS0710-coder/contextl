# TrafficManagement.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/ModuleConfig/TrafficManagement.tsx`
- **Extension:** `.tsx`
- **Size:** 5927 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TrafficManagementValidation`
- `DynamicFormFormInit`
- `TrafficManagementModuleConfigProps`

## Imports (Dependencies)
- [[apps/web/src/components/Form/DynamicForm.tsx.md|apps/web/src/components/Form/DynamicForm.tsx]]
- [[apps/web/src/core/hooks/useWaitForConfig.ts.md|apps/web/src/core/hooks/useWaitForConfig.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/core/utils/deepCompareConfig.ts.md|apps/web/src/core/utils/deepCompareConfig.ts]]
- [[apps/web/src/validation/moduleConfig/trafficManagement.ts.md|apps/web/src/validation/moduleConfig/trafficManagement.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Settings/ModuleConfig.tsx.md|apps/web/src/pages/Settings/ModuleConfig.tsx]]

## Source Code Snippet
```tsx
import { useWaitForConfig } from "@app/core/hooks/useWaitForConfig";
import {
  type TrafficManagementValidation,
  TrafficManagementValidationSchema,
} from "@app/validation/moduleConfig/trafficManagement.ts";
import {
  DynamicForm,
  type DynamicFormFormInit,
} from "@components/Form/DynamicForm.tsx";
import { useDevice } from "@core/stores";
import { deepCompareConfig } from "@core/utils/deepCompareConfig.ts";
import { useTranslation } from "react-i18next";

interface TrafficManagementModuleConfigProps {
  onFormInit: DynamicFormFormInit<TrafficManagementValidation>;
}

export const TrafficManagement = ({
  onFormInit,
}: TrafficManagementModuleConfigProps) => {
...
```