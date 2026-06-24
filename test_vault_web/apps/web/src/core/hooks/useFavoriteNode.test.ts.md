# useFavoriteNode.test.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useFavoriteNode.test.ts`
- **Extension:** `.ts`
- **Size:** 2518 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/core/hooks/useFavoriteNode.ts.md|apps/web/src/core/hooks/useFavoriteNode.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { act, renderHook } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { useFavoriteNode } from "./useFavoriteNode.ts";

const mockToast = vi.fn();
const mockSdkFavorite = vi.fn();
const mockSdkUnfavorite = vi.fn();
const mockByNum = vi.fn();
const { mockUseActiveClient } = vi.hoisted(() => ({
  mockUseActiveClient: vi.fn(),
}));

vi.mock("@meshtastic/sdk-react", () => ({
  useActiveClient: mockUseActiveClient,
}));

vi.mock("@core/hooks/useToast.ts", () => ({
  useToast: () => ({
    toast: mockToast,
  }),
...
```