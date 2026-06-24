# LanguageSwitcher.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/LanguageSwitcher.tsx`
- **Extension:** `.tsx`
- **Size:** 3010 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `LanguageSwitcherProps`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/DropdownMenu.tsx.md|apps/web/src/components/UI/DropdownMenu.tsx]]
- [[apps/web/src/components/UI/Typography/Subtle.tsx.md|apps/web/src/components/UI/Typography/Subtle.tsx]]
- [[apps/web/src/core/hooks/useLang.ts.md|apps/web/src/core/hooks/useLang.ts]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]
- [[apps/web/src/i18n-config.ts.md|apps/web/src/i18n-config.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/DeviceInfoPanel.tsx.md|apps/web/src/components/DeviceInfoPanel.tsx]]
- [[apps/web/src/pages/Connections/index.tsx.md|apps/web/src/pages/Connections/index.tsx]]

## Source Code Snippet
```tsx
import type { LangCode } from "@app/i18n-config.ts";
import useLang from "@core/hooks/useLang.ts";
import { cn } from "@core/utils/cn.ts";
import { t } from "i18next";
import { Check, Languages } from "lucide-react";
import { useCallback } from "react";
import { useTranslation } from "react-i18next";
import { Button } from "./UI/Button.tsx";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "./UI/DropdownMenu.tsx";
import { Subtle } from "./UI/Typography/Subtle.tsx";

interface LanguageSwitcherProps {
  disableHover?: boolean;
}

...
```