# Channels.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Channels/Channels.tsx`
- **Extension:** `.tsx`
- **Size:** 3709 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ConfigProps`

## Imports (Dependencies)
- [[apps/web/src/components/PageComponents/Channels/Channel.tsx.md|apps/web/src/components/PageComponents/Channels/Channel.tsx]]
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Spinner.tsx.md|apps/web/src/components/UI/Spinner.tsx]]
- [[apps/web/src/components/UI/Tabs.tsx.md|apps/web/src/components/UI/Tabs.tsx]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Messages.tsx.md|apps/web/src/pages/Messages.tsx]]
- [[apps/web/src/pages/Settings/RadioConfig.tsx.md|apps/web/src/pages/Settings/RadioConfig.tsx]]

## Source Code Snippet
```tsx
import { Channel } from "@app/components/PageComponents/Channels/Channel";
import { create } from "@bufbuild/protobuf";
import { Button } from "@components/UI/Button.tsx";
import { Spinner } from "@components/UI/Spinner.tsx";
import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from "@components/UI/Tabs.tsx";
import { useDevice } from "@core/stores";
import { Protobuf } from "@meshtastic/sdk";
import { useChannels, useConfigEditor, useSignal } from "@meshtastic/sdk-react";
import i18next from "i18next";
import { QrCodeIcon, UploadIcon } from "lucide-react";
import { Suspense, useMemo } from "react";
import type { UseFormReturn } from "react-hook-form";
import { useTranslation } from "react-i18next";

interface ConfigProps {
...
```