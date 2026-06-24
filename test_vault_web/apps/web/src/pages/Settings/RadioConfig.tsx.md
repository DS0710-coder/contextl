# RadioConfig.tsx

## Architecture Metrics
- **Path:** `apps/web/src/pages/Settings/RadioConfig.tsx`
- **Extension:** `.tsx`
- **Size:** 3199 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ConfigProps`
- `TabItem`

## Imports (Dependencies)
- [[apps/web/src/components/PageComponents/Channels/Channels.tsx.md|apps/web/src/components/PageComponents/Channels/Channels.tsx]]
- [[apps/web/src/components/PageComponents/Settings/LoRa.tsx.md|apps/web/src/components/PageComponents/Settings/LoRa.tsx]]
- [[apps/web/src/components/PageComponents/Settings/Security/Security.tsx.md|apps/web/src/components/PageComponents/Settings/Security/Security.tsx]]
- [[apps/web/src/components/UI/Spinner.tsx.md|apps/web/src/components/UI/Spinner.tsx]]
- [[apps/web/src/components/UI/Tabs.tsx.md|apps/web/src/components/UI/Tabs.tsx]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Settings/index.tsx.md|apps/web/src/pages/Settings/index.tsx]]

## Source Code Snippet
```tsx
import { Channels } from "@app/components/PageComponents/Channels/Channels";
import { LoRa } from "@components/PageComponents/Settings/LoRa.tsx";
import { Security } from "@components/PageComponents/Settings/Security/Security.tsx";
import { Spinner } from "@components/UI/Spinner.tsx";
import {
  Tabs,
  TabsContent,
  TabsList,
  TabsTrigger,
} from "@components/UI/Tabs.tsx";
import type { ValidConfigType } from "@core/stores";
import { useConfigEditor, useSignal } from "@meshtastic/sdk-react";
import { type ComponentType, Suspense, useMemo } from "react";
import type { UseFormReturn } from "react-hook-form";
import { useTranslation } from "react-i18next";

interface ConfigProps {
  onFormInit: <T extends object>(methods: UseFormReturn<T>) => void;
}

...
```