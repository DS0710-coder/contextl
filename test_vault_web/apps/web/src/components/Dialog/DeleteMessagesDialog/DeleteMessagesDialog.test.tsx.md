# DeleteMessagesDialog.test.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/DeleteMessagesDialog/DeleteMessagesDialog.test.tsx`
- **Extension:** `.tsx`
- **Size:** 3171 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/DeleteMessagesDialog/DeleteMessagesDialog.tsx.md|apps/web/src/components/Dialog/DeleteMessagesDialog/DeleteMessagesDialog.tsx]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
import { DeleteMessagesDialog } from "@components/Dialog/DeleteMessagesDialog/DeleteMessagesDialog.tsx";
import { useActiveClient } from "@meshtastic/sdk-react";
import { fireEvent, render, screen } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

const mockClearAll = vi.fn();

vi.mock("@meshtastic/sdk-react", () => ({
  useActiveClient: vi.fn(() => ({
    chat: { clearAll: mockClearAll },
  })),
}));

describe("DeleteMessagesDialog", () => {
  const mockOnOpenChange = vi.fn();

  beforeEach(() => {
    mockOnOpenChange.mockClear();
    mockClearAll.mockClear();
    vi.mocked(useActiveClient).mockReturnValue({
...
```