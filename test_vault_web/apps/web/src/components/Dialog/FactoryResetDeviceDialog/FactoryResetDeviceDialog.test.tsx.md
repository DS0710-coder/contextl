# FactoryResetDeviceDialog.test.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/FactoryResetDeviceDialog/FactoryResetDeviceDialog.test.tsx`
- **Extension:** `.tsx`
- **Size:** 2357 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/FactoryResetDeviceDialog/FactoryResetDeviceDialog.tsx.md|apps/web/src/components/Dialog/FactoryResetDeviceDialog/FactoryResetDeviceDialog.tsx]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { FactoryResetDeviceDialog } from "./FactoryResetDeviceDialog.tsx";

const mockFactoryResetDevice = vi.fn();
const mockRemoveDevice = vi.fn();
const mockToast = vi.fn();

vi.mock("@core/stores", () => {
  const useDeviceStore = Object.assign(vi.fn(), {
    getState: () => ({ removeDevice: mockRemoveDevice }),
  });

  return {
    CurrentDeviceContext: {
      _currentValue: { deviceId: 1234 },
    },
    useDevice: () => ({
      id: 42,
      connection: { factoryResetDevice: mockFactoryResetDevice },
...
```