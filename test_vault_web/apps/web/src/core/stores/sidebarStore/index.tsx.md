# index.tsx

## Architecture Metrics
- **Path:** `apps/web/src/core/stores/sidebarStore/index.tsx`
- **Extension:** `.tsx`
- **Size:** 1095 bytes
- **Centrality Score:** 0.0026
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `SidebarContextProps`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]

## Source Code Snippet
```tsx
import type React from "react";
import { createContext, useContext, useMemo, useState } from "react";

interface SidebarContextProps {
  isCollapsed: boolean;
  setIsCollapsed: React.Dispatch<React.SetStateAction<boolean>>;
  toggleSidebar: () => void;
}

const SidebarContext = createContext<SidebarContextProps | undefined>(
  undefined,
);

export const SidebarProvider: React.FC<{ children: React.ReactNode }> = ({
  children,
}) => {
  const [isCollapsed, setIsCollapsed] = useState<boolean>(false);

  const toggleSidebar = useMemo(
    () => () => {
...
```