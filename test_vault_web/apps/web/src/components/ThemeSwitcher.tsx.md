# ThemeSwitcher.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/ThemeSwitcher.tsx`
- **Extension:** `.tsx`
- **Size:** 3144 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ThemePreference`
- `ThemeSwitcherProps`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Typography/Subtle.tsx.md|apps/web/src/components/UI/Typography/Subtle.tsx]]
- [[apps/web/src/core/hooks/useTheme.ts.md|apps/web/src/core/hooks/useTheme.ts]]
- [[apps/web/src/core/hooks/useToggleVisiblility.ts.md|apps/web/src/core/hooks/useToggleVisiblility.ts]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/DeviceInfoPanel.tsx.md|apps/web/src/components/DeviceInfoPanel.tsx]]

## Source Code Snippet
```tsx
import { Monitor, Moon, Sun } from "lucide-react";
import { useTranslation } from "react-i18next";
import { useTheme } from "../core/hooks/useTheme.ts";
import { useToggleVisibility } from "../core/hooks/useToggleVisiblility.ts";
import { cn } from "../core/utils/cn.ts";
import { Button } from "./UI/Button.tsx";
import { Subtle } from "./UI/Typography/Subtle.tsx";

type ThemePreference = "light" | "dark" | "system";

interface ThemeSwitcherProps {
  className?: string;
  disableHover?: boolean;
}

const TOOLTIP_TIMEOUT = 2000; // 2 seconds

export default function ThemeSwitcher({
  className: passedClassName = "",
  disableHover = false,
...
```