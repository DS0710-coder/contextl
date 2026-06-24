# theme-provider.tsx

## Architecture Metrics
- **Path:** `packages/ui/src/components/theme-provider.tsx`
- **Extension:** `.tsx`
- **Size:** 1751 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Theme`
- `ThemeProviderProps`
- `ThemeProviderState`
- `ThemeProvider`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/ui/src/index.ts.md|packages/ui/src/index.ts]]
- [[packages/ui/src/lib/components/theme-toggle.tsx.md|packages/ui/src/lib/components/theme-toggle.tsx]]

## Source Code Snippet
```tsx
import { createContext, useContext, useEffect, useState } from "react";

type Theme = "dark" | "light" | "system";

type ThemeProviderProps = {
  children: React.ReactNode;
  defaultTheme?: Theme;
  storageKey?: string;
};

type ThemeProviderState = {
  theme: Theme;
  setTheme: (theme: Theme) => void;
};

const initialState: ThemeProviderState = {
  theme: "system",
  setTheme: () => null,
};

...
```