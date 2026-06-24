# index.ts

## Architecture Metrics
- **Path:** `packages/ui/src/index.ts`
- **Extension:** `.ts`
- **Size:** 404 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/ui/src/components/theme-provider.tsx.md|packages/ui/src/components/theme-provider.tsx]]
- [[packages/ui/src/components/ui/badge.tsx.md|packages/ui/src/components/ui/badge.tsx]]
- [[packages/ui/src/components/ui/sidebar.tsx.md|packages/ui/src/components/ui/sidebar.tsx]]
- [[packages/ui/src/lib/components/Sidebar/AppSidebar.tsx.md|packages/ui/src/lib/components/Sidebar/AppSidebar.tsx]]
- [[packages/ui/src/lib/components/index.ts.md|packages/ui/src/lib/components/index.ts]]
- [[packages/ui/src/lib/components/theme-toggle.tsx.md|packages/ui/src/lib/components/theme-toggle.tsx]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
export { ThemeProvider, useTheme } from "@/components/theme-provider";
export * from "@/components/ui/badge.tsx";
export * from "@/components/ui/sidebar";
export { AppSidebar } from "./lib/components/index.ts";

// Types
export type {
  AppSidebarProps,
  NavLink,
  SidebarSectionProps,
} from "./lib/components/Sidebar/AppSidebar.tsx";

export { ThemeToggle } from "./lib/components/theme-toggle.tsx";
```