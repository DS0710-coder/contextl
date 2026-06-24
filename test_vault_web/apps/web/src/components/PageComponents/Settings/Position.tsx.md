# Position.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Settings/Position.tsx`
- **Extension:** `.tsx`
- **Size:** 11595 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 10

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PositionValidation`
- `DynamicFormFormInit`
- `FlagName`
- `PositionConfigProps`
- `UseBrowserLocationButton`

## Imports (Dependencies)
- [[apps/web/src/components/Form/DynamicForm.tsx.md|apps/web/src/components/Form/DynamicForm.tsx]]
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/core/hooks/useNodesAsProto.ts.md|apps/web/src/core/hooks/useNodesAsProto.ts]]
- [[apps/web/src/core/hooks/usePositionFlags.ts.md|apps/web/src/core/hooks/usePositionFlags.ts]]
- [[apps/web/src/core/hooks/useToast.ts.md|apps/web/src/core/hooks/useToast.ts]]
- [[apps/web/src/core/hooks/useWaitForConfig.ts.md|apps/web/src/core/hooks/useWaitForConfig.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/validation/config/position.ts.md|apps/web/src/validation/config/position.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Settings/DeviceConfig.tsx.md|apps/web/src/pages/Settings/DeviceConfig.tsx]]

## Source Code Snippet
```tsx
import { useWaitForConfig } from "@app/core/hooks/useWaitForConfig";
import {
  type PositionValidation,
  PositionValidationSchema,
} from "@app/validation/config/position.ts";
import { create } from "@bufbuild/protobuf";
import {
  DynamicForm,
  type DynamicFormFormInit,
} from "@components/Form/DynamicForm.tsx";
import { Button } from "@components/UI/Button.tsx";
import {
  type FlagName,
  usePositionFlags,
} from "@core/hooks/usePositionFlags.ts";
import { useMyNodeAsProto } from "@core/hooks/useNodesAsProto.ts";
import { useToast } from "@core/hooks/useToast.ts";
import { useDevice } from "@core/stores";
import { Protobuf } from "@meshtastic/sdk";
import { useConfigEditor, useSignal } from "@meshtastic/sdk-react";
...
```