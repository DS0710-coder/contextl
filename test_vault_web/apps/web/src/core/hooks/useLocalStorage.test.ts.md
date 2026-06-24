# useLocalStorage.test.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useLocalStorage.test.ts`
- **Extension:** `.ts`
- **Size:** 1567 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/core/hooks/useLocalStorage.ts.md|apps/web/src/core/hooks/useLocalStorage.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { act, renderHook } from "@testing-library/react";
import { beforeEach, describe, expect, it } from "vitest";
import useLocalStorage from "./useLocalStorage.ts";

describe("useLocalStorage", () => {
  const key = "test-key";

  beforeEach(() => {
    localStorage.clear();
  });

  it("should initialize with initial value if localStorage is empty", () => {
    const { result } = renderHook(() => useLocalStorage(key, "initial"));
    const [value] = result.current;
    expect(value).toBe("initial");
  });

  it("should read existing value from localStorage", () => {
    localStorage.setItem(key, JSON.stringify("stored"));
    const { result } = renderHook(() => useLocalStorage(key, "initial"));
...
```