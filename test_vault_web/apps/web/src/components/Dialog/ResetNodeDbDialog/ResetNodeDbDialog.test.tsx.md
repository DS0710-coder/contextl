# ResetNodeDbDialog.test.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/ResetNodeDbDialog/ResetNodeDbDialog.test.tsx`
- **Extension:** `.tsx`
- **Size:** 2014 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/ResetNodeDbDialog/ResetNodeDbDialog.tsx.md|apps/web/src/components/Dialog/ResetNodeDbDialog/ResetNodeDbDialog.tsx]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
import { fireEvent, render, screen, waitFor } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { ResetNodeDbDialog } from "./ResetNodeDbDialog.tsx";

const mockResetNodes = vi.fn();
const mockClearAll = vi.fn();

const { mockUseActiveClient } = vi.hoisted(() => ({
  mockUseActiveClient: vi.fn(),
}));

vi.mock("@meshtastic/sdk-react", () => ({
  useActiveClient: mockUseActiveClient,
}));

describe("ResetNodeDbDialog", () => {
  const mockOnOpenChange = vi.fn();

  beforeEach(() => {
    vi.clearAllMocks();
...
```