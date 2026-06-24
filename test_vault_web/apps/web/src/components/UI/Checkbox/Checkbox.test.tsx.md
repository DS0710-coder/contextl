# Checkbox.test.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Checkbox/Checkbox.test.tsx`
- **Extension:** `.tsx`
- **Size:** 4782 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/components/UI/Checkbox/index.tsx.md|apps/web/src/components/UI/Checkbox/index.tsx]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
import { Checkbox } from "@components/UI/Checkbox/index.tsx";
import { cleanup, fireEvent, render, screen } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

describe("Checkbox", () => {
  beforeEach(cleanup);

  it("renders unchecked by default (uncontrolled)", () => {
    render(<Checkbox />);
    const checkbox = screen.getByRole("checkbox");
    const presentation = screen.getByRole("presentation");
    expect(checkbox).not.toBeChecked();
    // unchecked -> no filled bg class
    expect(presentation).not.toHaveClass("bg-slate-500");
  });

  it("respects defaultChecked in uncontrolled mode", () => {
    render(<Checkbox defaultChecked />);
    expect(screen.getByRole("checkbox")).toBeChecked();
  });
...
```