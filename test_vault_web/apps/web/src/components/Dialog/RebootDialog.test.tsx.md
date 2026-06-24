# RebootDialog.test.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/Dialog/RebootDialog.test.tsx`
- **Extension:** `.tsx`
- **Size:** 5748 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/components/Dialog/RebootDialog.tsx.md|apps/web/src/components/Dialog/RebootDialog.tsx]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
import { act, fireEvent, render, screen } from "@testing-library/react";
import type {
  ButtonHTMLAttributes,
  ClassAttributes,
  InputHTMLAttributes,
  ReactNode,
} from "react";
import type { JSX } from "react/jsx-runtime";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { RebootDialog } from "./RebootDialog.tsx";

const rebootMock = vi.fn();
const rebootOtaMock = vi.fn();
let mockConnection:
  | {
      rebootOta: (delay: number) => void;
      reboot: (delay: number) => void;
    }
  | undefined = {
  reboot: rebootMock,
...
```