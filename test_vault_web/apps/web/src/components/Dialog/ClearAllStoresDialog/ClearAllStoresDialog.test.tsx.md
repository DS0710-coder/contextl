# ClearAllStoresDialog.test.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/ClearAllStoresDialog/ClearAllStoresDialog.test.tsx`
- **Extension:** `.tsx`
- **Size:** 2220 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/ClearAllStoresDialog/ClearAllStoresDialog.tsx.md|apps/web/src/components/Dialog/ClearAllStoresDialog/ClearAllStoresDialog.tsx]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
import { fireEvent, render, screen } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { ClearAllStoresDialog } from "./ClearAllStoresDialog.tsx";

const mockClearAllStores = vi.fn();

vi.mock("@core/stores", () => ({
  CurrentDeviceContext: {
    _currentValue: { deviceId: 1234 },
  },
  clearAllStores: () => mockClearAllStores(),
}));

describe("ClearAllStoresDialog", () => {
  const mockOnOpenChange = vi.fn();

  // Capture window.location.href assignment without triggering real navigation
  const originalLocation = window.location;
  let assignedHref: string | undefined;

...
```