# index.tsx

## Architecture Metrics
- **Path:** `apps/web/src/index.tsx`
- **Extension:** `.tsx`
- **Size:** 1445 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Register`
- `IndexPage`

## Imports (Dependencies)
- [[apps/web/src/core/meshRegistry.ts.md|apps/web/src/core/meshRegistry.ts]]
- [[apps/web/src/core/services/dev-overrides.ts.md|apps/web/src/core/services/dev-overrides.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/i18n-config.ts.md|apps/web/src/i18n-config.ts]]
- [[apps/web/src/routes.tsx.md|apps/web/src/routes.tsx]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
import React from "react";
import "@app/index.css";

// Import feature flags and dev overrides
import "@core/services/dev-overrides.ts";
import { enableMapSet } from "immer";
import "maplibre-gl/dist/maplibre-gl.css";
import { Suspense } from "react";
import { createRoot } from "react-dom/client";
import "./i18n-config.ts";
import { router } from "@app/routes.tsx";
import { meshRegistry } from "@core/meshRegistry.ts";
import { useAppStore } from "@core/stores";
import { MeshRegistryProvider } from "@meshtastic/sdk-react";
import { type createRouter, RouterProvider } from "@tanstack/react-router";
import { useTranslation } from "react-i18next";

declare module "@tanstack/react-router" {
  interface Register {
    router: ReturnType<typeof createRouter>;
...
```