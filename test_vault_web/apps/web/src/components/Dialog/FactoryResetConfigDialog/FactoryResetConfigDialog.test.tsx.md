# FactoryResetConfigDialog.test.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/FactoryResetConfigDialog/FactoryResetConfigDialog.test.tsx`
- **Extension:** `.tsx`
- **Size:** 1869 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/FactoryResetConfigDialog/FactoryResetConfigDialog.tsx.md|apps/web/src/components/Dialog/FactoryResetConfigDialog/FactoryResetConfigDialog.tsx]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { FactoryResetConfigDialog } from "./FactoryResetConfigDialog.tsx";

const mockFactoryReset = vi.fn();
const mockToast = vi.fn();

vi.mock("@core/stores", () => ({
  CurrentDeviceContext: {
    _currentValue: { deviceId: 1234 },
  },
  useDevice: () => ({
    connection: {
      factoryResetConfig: mockFactoryReset,
    },
  }),
}));

vi.mock("@core/hooks/useToast.ts", () => ({
  toast: (...args: unknown[]) => mockToast(...args),
...
```