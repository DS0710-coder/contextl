# User.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Settings/User.tsx`
- **Extension:** `.tsx`
- **Size:** 4605 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `UserValidation`
- `DynamicFormFormInit`
- `UserConfigProps`

## Imports (Dependencies)
- [[apps/web/src/components/Form/DynamicForm.tsx.md|apps/web/src/components/Form/DynamicForm.tsx]]
- [[apps/web/src/core/hooks/useNodesAsProto.ts.md|apps/web/src/core/hooks/useNodesAsProto.ts]]
- [[apps/web/src/validation/config/user.ts.md|apps/web/src/validation/config/user.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Settings/DeviceConfig.tsx.md|apps/web/src/pages/Settings/DeviceConfig.tsx]]

## Source Code Snippet
```tsx
import {
  type UserValidation,
  UserValidationSchema,
} from "@app/validation/config/user.ts";
import { create } from "@bufbuild/protobuf";
import {
  DynamicForm,
  type DynamicFormFormInit,
} from "@components/Form/DynamicForm.tsx";
import { useMyNodeAsProto } from "@core/hooks/useNodesAsProto.ts";
import { Protobuf } from "@meshtastic/sdk";
import { useConfigEditor, useSignal } from "@meshtastic/sdk-react";
import { useEffect } from "react";
import { useTranslation } from "react-i18next";

interface UserConfigProps {
  onFormInit: DynamicFormFormInit<UserValidation>;
}

const EMPTY_OWNER_SIGNAL = {
...
```