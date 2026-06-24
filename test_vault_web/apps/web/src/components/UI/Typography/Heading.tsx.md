# Heading.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Typography/Heading.tsx`
- **Extension:** `.tsx`
- **Size:** 872 bytes
- **Centrality Score:** 0.0020
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `HeadingProps`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/Form/DynamicForm.tsx.md|apps/web/src/components/Form/DynamicForm.tsx]]
- [[apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx.md|apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx]]
- [[apps/web/src/components/UI/ErrorPage.tsx.md|apps/web/src/components/UI/ErrorPage.tsx]]
- [[apps/web/src/components/UI/Sidebar/SidebarSection.tsx.md|apps/web/src/components/UI/Sidebar/SidebarSection.tsx]]

## Source Code Snippet
```tsx
import type React from "react";

const headingStyles = {
  h1: "scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl",
  h2: "scroll-m-20 border-b border-b-slate-200 pb-2 text-3xl font-semibold tracking-tight transition-colors first:mt-0 dark:border-b-slate-700",
  h3: "scroll-m-20 text-lg font-semibold tracking-tight",
  h4: "scroll-m-20 text-xl font-semibold tracking-tight",
  h5: "scroll-m-20 text-lg font-medium tracking-tight",
};

interface HeadingProps {
  as?: "h1" | "h2" | "h3" | "h4" | "h5";
  children: React.ReactNode;
  className?: string;
}

export const Heading = ({
  as: Component = "h1",
  children,
  className = "",
...
```