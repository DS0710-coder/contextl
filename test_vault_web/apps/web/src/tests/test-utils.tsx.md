# test-utils.tsx

## Architecture Metrics
- **Path:** `apps/web/src/tests/test-utils.tsx`
- **Extension:** `.tsx`
- **Size:** 950 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/DeviceWrapper.tsx.md|apps/web/src/DeviceWrapper.tsx]]
- [[apps/web/src/i18n-config.ts.md|apps/web/src/i18n-config.ts]]
- [[apps/web/src/routes.tsx.md|apps/web/src/routes.tsx]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
import {
  createMemoryHistory,
  createRouter,
  RouterProvider,
} from "@tanstack/react-router";
import { type RenderOptions, render } from "@testing-library/react";
import type { ReactElement } from "react";
import "@app/i18n-config.ts";

import { DeviceWrapper } from "@app/DeviceWrapper.tsx";
import { routeTree } from "../routes.tsx";

const Providers = () => {
  const memoryHistory = createMemoryHistory({
    initialEntries: ["/"],
  });

  const router = createRouter({
    routeTree,
    history: memoryHistory,
...
```