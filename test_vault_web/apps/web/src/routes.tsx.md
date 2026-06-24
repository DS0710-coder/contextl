# routes.tsx

## Architecture Metrics
- **Path:** `apps/web/src/routes.tsx`
- **Extension:** `.tsx`
- **Size:** 4564 bytes
- **Centrality Score:** 0.0012
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 8

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `AppContext`

## Imports (Dependencies)
- [[apps/web/src/App.tsx.md|apps/web/src/App.tsx]]
- [[apps/web/src/components/Dialog/DialogManager.tsx.md|apps/web/src/components/Dialog/DialogManager.tsx]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/pages/Connections/index.tsx.md|apps/web/src/pages/Connections/index.tsx]]
- [[apps/web/src/pages/Map/index.tsx.md|apps/web/src/pages/Map/index.tsx]]
- [[apps/web/src/pages/Messages.tsx.md|apps/web/src/pages/Messages.tsx]]
- [[apps/web/src/pages/Nodes/index.tsx.md|apps/web/src/pages/Nodes/index.tsx]]
- [[apps/web/src/pages/Settings/index.tsx.md|apps/web/src/pages/Settings/index.tsx]]

## Imported By (Dependents)
- [[apps/web/src/index.tsx.md|apps/web/src/index.tsx]]
- [[apps/web/src/pages/Messages.tsx.md|apps/web/src/pages/Messages.tsx]]
- [[apps/web/src/pages/Settings/index.tsx.md|apps/web/src/pages/Settings/index.tsx]]
- [[apps/web/src/tests/test-utils.tsx.md|apps/web/src/tests/test-utils.tsx]]

## Source Code Snippet
```tsx
import { DialogManager } from "@components/Dialog/DialogManager.tsx";
import type { useAppStore } from "@core/stores";
import { Connections } from "@pages/Connections/index.tsx";
import MapPage from "@pages/Map/index.tsx";
import MessagesPage from "@pages/Messages.tsx";
import NodesPage from "@pages/Nodes/index.tsx";
import ConfigPage from "@pages/Settings/index.tsx";
import {
  createRootRouteWithContext,
  createRoute,
  createRouter,
  redirect,
} from "@tanstack/react-router";
import type { useTranslation } from "react-i18next";
import { z } from "zod/v4";
import { App } from "./App.tsx";

interface AppContext {
  stores: {
    app: ReturnType<typeof useAppStore>;
...
```