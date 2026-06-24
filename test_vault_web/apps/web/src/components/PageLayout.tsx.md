# PageLayout.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageLayout.tsx`
- **Extension:** `.tsx`
- **Size:** 4285 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ActionItem`
- `PageLayoutProps`

## Imports (Dependencies)
- [[apps/web/src/components/UI/ErrorPage.tsx.md|apps/web/src/components/UI/ErrorPage.tsx]]
- [[apps/web/src/components/UI/Footer.tsx.md|apps/web/src/components/UI/Footer.tsx]]
- [[apps/web/src/components/UI/Spinner.tsx.md|apps/web/src/components/UI/Spinner.tsx]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/pages/Map/index.tsx.md|apps/web/src/pages/Map/index.tsx]]
- [[apps/web/src/pages/Messages.tsx.md|apps/web/src/pages/Messages.tsx]]
- [[apps/web/src/pages/Nodes/index.tsx.md|apps/web/src/pages/Nodes/index.tsx]]
- [[apps/web/src/pages/Settings/index.tsx.md|apps/web/src/pages/Settings/index.tsx]]

## Source Code Snippet
```tsx
import { ErrorPage } from "@components/UI/ErrorPage.tsx";
import Footer from "@components/UI/Footer.tsx";
import { Spinner } from "@components/UI/Spinner.tsx";
import { cn } from "@core/utils/cn.ts";
import type { LucideIcon } from "lucide-react";
import type React from "react";
import { ErrorBoundary } from "react-error-boundary";

export interface ActionItem {
  key: string;
  icon?: LucideIcon;
  iconClasses?: string;
  onClick: () => void;
  disabled?: boolean;
  isLoading?: boolean;
  ariaLabel?: string;
  label?: string;
  className?: string;
}

...
```