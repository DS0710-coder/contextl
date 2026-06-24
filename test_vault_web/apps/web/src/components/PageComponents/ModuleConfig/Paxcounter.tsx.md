# Paxcounter.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/ModuleConfig/Paxcounter.tsx`
- **Extension:** `.tsx`
- **Size:** 3032 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PaxcounterValidation`
- `DynamicFormFormInit`
- `PaxcounterModuleConfigProps`

## Imports (Dependencies)
- [[apps/web/src/components/Form/DynamicForm.tsx.md|apps/web/src/components/Form/DynamicForm.tsx]]
- [[apps/web/src/core/hooks/useWaitForConfig.ts.md|apps/web/src/core/hooks/useWaitForConfig.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/validation/moduleConfig/paxcounter.ts.md|apps/web/src/validation/moduleConfig/paxcounter.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Settings/ModuleConfig.tsx.md|apps/web/src/pages/Settings/ModuleConfig.tsx]]

## Source Code Snippet
```tsx
import { useWaitForConfig } from "@app/core/hooks/useWaitForConfig";
import {
  type PaxcounterValidation,
  PaxcounterValidationSchema,
} from "@app/validation/moduleConfig/paxcounter.ts";
import {
  DynamicForm,
  type DynamicFormFormInit,
} from "@components/Form/DynamicForm.tsx";
import { useDevice } from "@core/stores";
import { Protobuf } from "@meshtastic/sdk";
import { useConfigEditor, useSignal } from "@meshtastic/sdk-react";
import { useTranslation } from "react-i18next";

interface PaxcounterModuleConfigProps {
  onFormInit: DynamicFormFormInit<PaxcounterValidation>;
}

const EMPTY_MODULES_SIGNAL = {
  value: {} as {
...
```