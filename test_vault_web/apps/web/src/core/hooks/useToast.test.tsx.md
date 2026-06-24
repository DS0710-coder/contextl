# useToast.test.tsx

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useToast.test.tsx`
- **Extension:** `.tsx`
- **Size:** 2233 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/core/hooks/useToast.ts.md|apps/web/src/core/hooks/useToast.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
import { Button } from "@components/UI/Button.tsx";
import { useToast } from "@core/hooks/useToast.ts";
import { act, renderHook } from "@testing-library/react";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";

describe("useToast", () => {
  beforeEach(() => {
    // Reset toast memory state before each test
    // our hook uses global memory to store toasts
    // @ts-expect-error - internal test reset
    globalThis.memoryState = { toasts: [] };
    vi.useFakeTimers();
  });

  afterEach(() => {
    vi.useRealTimers();
  });

  it("should create a toast with title, description, and action", () => {
    const { result } = renderHook(() => useToast());
...
```