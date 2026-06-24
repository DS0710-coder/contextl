# index.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/generic/Table/index.tsx`
- **Extension:** `.tsx`
- **Size:** 4808 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Heading`
- `Cell`
- `DataRow`
- `TableProps`
- `numericHops`

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/generic/Table/index.test.tsx.md|apps/web/src/components/generic/Table/index.test.tsx]]
- [[apps/web/src/pages/Nodes/index.tsx.md|apps/web/src/pages/Nodes/index.tsx]]

## Source Code Snippet
```tsx
import { cn } from "@core/utils/cn.ts";
import { ChevronDownIcon, ChevronUpIcon } from "lucide-react";
import React, { useMemo, useState } from "react";

export interface Heading {
  title: string;
  sortable: boolean;
}

interface Cell {
  content: React.ReactNode;
  sortValue: string | number;
}

export interface DataRow {
  id: string | number;
  isFavorite?: boolean;
  cells: Cell[];
}

...
```