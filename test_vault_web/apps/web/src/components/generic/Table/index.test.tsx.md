# index.test.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/generic/Table/index.test.tsx`
- **Extension:** `.tsx`
- **Size:** 4151 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DataRow`
- `Heading`

## Imports (Dependencies)
- [[apps/web/src/components/generic/Mono.tsx.md|apps/web/src/components/generic/Mono.tsx]]
- [[apps/web/src/components/generic/Table/index.tsx.md|apps/web/src/components/generic/Table/index.tsx]]
- [[apps/web/src/components/generic/TimeAgo.tsx.md|apps/web/src/components/generic/TimeAgo.tsx]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
import { Mono } from "@components/generic/Mono.tsx";
import {
  type DataRow,
  type Heading,
  Table,
} from "@components/generic/Table/index.tsx";
import { TimeAgo } from "@components/generic/TimeAgo.tsx";
import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, it } from "vitest";

// @ts-types="react"

describe("Generic Table", () => {
  it("Can render an empty table.", () => {
    render(<Table headings={[]} rows={[]} />);
    expect(screen.getByRole("table")).toBeInTheDocument();
  });

  it("Can render a table with headers and no rows.", async () => {
    const headings: Heading[] = [
...
```