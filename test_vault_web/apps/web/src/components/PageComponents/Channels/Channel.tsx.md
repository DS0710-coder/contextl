# Channel.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Channels/Channel.tsx`
- **Extension:** `.tsx`
- **Size:** 10276 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ChannelValidation`
- `DynamicFormFormInit`
- `SettingsPanelProps`

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/PkiRegenerateDialog.tsx.md|apps/web/src/components/Dialog/PkiRegenerateDialog.tsx]]
- [[apps/web/src/components/Form/DynamicForm.tsx.md|apps/web/src/components/Form/DynamicForm.tsx]]
- [[apps/web/src/components/Form/createZodResolver.ts.md|apps/web/src/components/Form/createZodResolver.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/validation/channel.ts.md|apps/web/src/validation/channel.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Channels/Channels.tsx.md|apps/web/src/components/PageComponents/Channels/Channels.tsx]]

## Source Code Snippet
```tsx
import {
  type ChannelValidation,
  makeChannelSchema,
} from "@app/validation/channel.ts";
import { create } from "@bufbuild/protobuf";
import { PkiRegenerateDialog } from "@components/Dialog/PkiRegenerateDialog.tsx";
import { createZodResolver } from "@components/Form/createZodResolver.ts";
import {
  DynamicForm,
  type DynamicFormFormInit,
} from "@components/Form/DynamicForm.tsx";
import { useDevice } from "@core/stores";
import { Protobuf } from "@meshtastic/sdk";
import { useConfigEditor, useSignal } from "@meshtastic/sdk-react";
import { fromByteArray, toByteArray } from "base64-js";
import cryptoRandomString from "crypto-random-string";
import { useEffect, useMemo, useRef, useState } from "react";
import { type DefaultValues, useForm } from "react-hook-form";
import { useTranslation } from "react-i18next";

...
```