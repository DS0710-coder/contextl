# RefreshKeysDialog.test.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.test.tsx`
- **Extension:** `.tsx`
- **Size:** 1485 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.tsx.md|apps/web/src/components/Dialog/RefreshKeysDialog/RefreshKeysDialog.tsx]]
- [[apps/web/src/components/Dialog/RefreshKeysDialog/useRefreshKeysDialog.ts.md|apps/web/src/components/Dialog/RefreshKeysDialog/useRefreshKeysDialog.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
import { CurrentDeviceContext, useDeviceStore } from "@core/stores";
import { MeshRegistry } from "@meshtastic/sdk";
import { MeshRegistryProvider } from "@meshtastic/sdk-react";
import { render } from "@testing-library/react";
import { afterEach, beforeEach, expect, test, vi } from "vitest";
import { RefreshKeysDialog } from "./RefreshKeysDialog.tsx";
import { useRefreshKeysDialog } from "./useRefreshKeysDialog.ts";

vi.mock("./useRefreshKeysDialog");

const mockUseRefreshKeysDialog = vi.mocked(useRefreshKeysDialog);

const getInitialState = () =>
  useDeviceStore.getInitialState?.() ?? {
    devices: new Map(),
    remoteDevices: new Map(),
  };

beforeEach(() => {
  useDeviceStore.setState(getInitialState(), true);
...
```