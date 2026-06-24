# theme-toggle.tsx

## Architecture Metrics
- **Path:** `packages/ui/src/lib/components/theme-toggle.tsx`
- **Extension:** `.tsx`
- **Size:** 1197 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ThemeToggle`

## Imports (Dependencies)
- [[packages/ui/src/components/theme-provider.tsx.md|packages/ui/src/components/theme-provider.tsx]]
- [[packages/ui/src/components/ui/button.tsx.md|packages/ui/src/components/ui/button.tsx]]
- [[packages/ui/src/components/ui/dropdown-menu.tsx.md|packages/ui/src/components/ui/dropdown-menu.tsx]]

## Imported By (Dependents)
- [[packages/ui/src/index.ts.md|packages/ui/src/index.ts]]

## Source Code Snippet
```tsx
import { Moon, Sun } from "lucide-react";
import { useTheme } from "@/components/theme-provider";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

export function ThemeToggle() {
  const { setTheme } = useTheme();

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <Button variant="outline" size="icon">
          <Sun className="size-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0" />
          <Moon className="absolute size-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100" />
          <span className="sr-only">Toggle theme</span>
...
```