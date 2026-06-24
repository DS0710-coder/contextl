# Security.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Settings/Security/Security.tsx`
- **Extension:** `.tsx`
- **Size:** 9923 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 10

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ParsedSecurity`
- `RawSecurity`
- `DynamicFormFormInit`
- `SecurityConfigProps`

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/ManagedModeDialog.tsx.md|apps/web/src/components/Dialog/ManagedModeDialog.tsx]]
- [[apps/web/src/components/Dialog/PkiRegenerateDialog.tsx.md|apps/web/src/components/Dialog/PkiRegenerateDialog.tsx]]
- [[apps/web/src/components/Form/DynamicForm.tsx.md|apps/web/src/components/Form/DynamicForm.tsx]]
- [[apps/web/src/components/Form/createZodResolver.ts.md|apps/web/src/components/Form/createZodResolver.ts]]
- [[apps/web/src/core/hooks/useWaitForConfig.ts.md|apps/web/src/core/hooks/useWaitForConfig.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/core/utils/x25519.ts.md|apps/web/src/core/utils/x25519.ts]]
- [[apps/web/src/validation/config/security.ts.md|apps/web/src/validation/config/security.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Settings/RadioConfig.tsx.md|apps/web/src/pages/Settings/RadioConfig.tsx]]

## Source Code Snippet
```tsx
import { useWaitForConfig } from "@app/core/hooks/useWaitForConfig";
import {
  type ParsedSecurity,
  type RawSecurity,
  RawSecuritySchema,
} from "@app/validation/config/security.ts";
import { ManagedModeDialog } from "@components/Dialog/ManagedModeDialog.tsx";
import { PkiRegenerateDialog } from "@components/Dialog/PkiRegenerateDialog.tsx";
import { createZodResolver } from "@components/Form/createZodResolver.ts";
import {
  DynamicForm,
  type DynamicFormFormInit,
} from "@components/Form/DynamicForm.tsx";
import { useDevice } from "@core/stores";
import { getX25519PrivateKey, getX25519PublicKey } from "@core/utils/x25519.ts";
import { Protobuf } from "@meshtastic/sdk";
import { useConfigEditor, useSignal } from "@meshtastic/sdk-react";
import { fromByteArray, toByteArray } from "base64-js";
import { useEffect, useState } from "react";
import { type DefaultValues, useForm } from "react-hook-form";
...
```