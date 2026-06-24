# App.tsx

## Architecture Metrics
- **Path:** `apps/web/src/App.tsx`
- **Extension:** `.tsx`
- **Size:** 2449 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 12

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `App`

## Imports (Dependencies)
- [[apps/web/src/DeviceWrapper.tsx.md|apps/web/src/DeviceWrapper.tsx]]
- [[apps/web/src/components/CommandPalette/index.tsx.md|apps/web/src/components/CommandPalette/index.tsx]]
- [[apps/web/src/components/ConnectingOverlay.tsx.md|apps/web/src/components/ConnectingOverlay.tsx]]
- [[apps/web/src/components/Dialog/DialogManager.tsx.md|apps/web/src/components/Dialog/DialogManager.tsx]]
- [[apps/web/src/components/KeyBackupReminder.tsx.md|apps/web/src/components/KeyBackupReminder.tsx]]
- [[apps/web/src/components/RegionSetupReminder.tsx.md|apps/web/src/components/RegionSetupReminder.tsx]]
- [[apps/web/src/components/Toaster.tsx.md|apps/web/src/components/Toaster.tsx]]
- [[apps/web/src/components/UI/ErrorPage.tsx.md|apps/web/src/components/UI/ErrorPage.tsx]]
- [[apps/web/src/components/UI/Footer.tsx.md|apps/web/src/components/UI/Footer.tsx]]
- [[apps/web/src/core/hooks/useTheme.ts.md|apps/web/src/core/hooks/useTheme.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/pages/Connections/index.tsx.md|apps/web/src/pages/Connections/index.tsx]]

## Imported By (Dependents)
- [[apps/web/src/routes.tsx.md|apps/web/src/routes.tsx]]

## Source Code Snippet
```tsx
import { DeviceWrapper } from "@app/DeviceWrapper.tsx";
import { CommandPalette } from "@components/CommandPalette/index.tsx";
import { ConnectingOverlay } from "@components/ConnectingOverlay.tsx";
import { DialogManager } from "@components/Dialog/DialogManager.tsx";
import { KeyBackupReminder } from "@components/KeyBackupReminder.tsx";
import { RegionSetupReminder } from "@components/RegionSetupReminder.tsx";
import { Toaster } from "@components/Toaster.tsx";
import { ErrorPage } from "@components/UI/ErrorPage.tsx";
import Footer from "@components/UI/Footer.tsx";
import { useTheme } from "@core/hooks/useTheme.ts";
import { SidebarProvider, useAppStore, useDeviceStore } from "@core/stores";
import { Connections } from "@pages/Connections/index.tsx";
import { Outlet } from "@tanstack/react-router";
import { TanStackRouterDevtools } from "@tanstack/react-router-devtools";
import { ErrorBoundary } from "react-error-boundary";
import { MapProvider } from "react-map-gl/maplibre";

export function App() {
  useTheme();

...
```