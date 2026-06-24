# useTheme.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useTheme.ts`
- **Extension:** `.ts`
- **Size:** 1292 bytes
- **Centrality Score:** 0.0016
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Theme`
- `useTheme`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/App.tsx.md|apps/web/src/App.tsx]]
- [[apps/web/src/components/Map.tsx.md|apps/web/src/components/Map.tsx]]
- [[apps/web/src/components/ThemeSwitcher.tsx.md|apps/web/src/components/ThemeSwitcher.tsx]]

## Source Code Snippet
```ts
import { useCallback, useEffect, useState } from "react";

type Theme = "light" | "dark" | "system";

export function useTheme() {
  const getSystemTheme = () =>
    globalThis.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";

  const getStoredPreference = useCallback(
    (): Theme => (localStorage.getItem("theme") as Theme) || "system",
    [],
  );

  const [preference, setPreference] = useState<Theme>(() =>
    typeof window !== "undefined" ? getStoredPreference() : "light",
  );

  const theme = preference === "system" ? getSystemTheme() : preference;
...
```