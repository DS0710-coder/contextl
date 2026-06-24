# index.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Settings/Network/index.tsx`
- **Extension:** `.tsx`
- **Size:** 7011 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NetworkValidation`
- `DynamicFormFormInit`
- `NetworkConfigProps`

## Imports (Dependencies)
- [[apps/web/src/components/Form/DynamicForm.tsx.md|apps/web/src/components/Form/DynamicForm.tsx]]
- [[apps/web/src/core/hooks/useWaitForConfig.ts.md|apps/web/src/core/hooks/useWaitForConfig.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/core/utils/ip.ts.md|apps/web/src/core/utils/ip.ts]]
- [[apps/web/src/validation/config/network.ts.md|apps/web/src/validation/config/network.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Settings/DeviceConfig.tsx.md|apps/web/src/pages/Settings/DeviceConfig.tsx]]

## Source Code Snippet
```tsx
import { useWaitForConfig } from "@app/core/hooks/useWaitForConfig";
import {
  type NetworkValidation,
  NetworkValidationSchema,
} from "@app/validation/config/network.ts";
import { create } from "@bufbuild/protobuf";
import {
  DynamicForm,
  type DynamicFormFormInit,
} from "@components/Form/DynamicForm.tsx";
import { useDevice } from "@core/stores";
import {
  convertIntToIpAddress,
  convertIpAddressToInt,
} from "@core/utils/ip.ts";
import { Protobuf } from "@meshtastic/sdk";
import { useConfigEditor, useSignal } from "@meshtastic/sdk-react";
import { useTranslation } from "react-i18next";

interface NetworkConfigProps {
...
```