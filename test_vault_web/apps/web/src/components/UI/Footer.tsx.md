# Footer.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Footer.tsx`
- **Extension:** `.tsx`
- **Size:** 1860 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `FooterProps`

## Imports (Dependencies)
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]

## Imported By (Dependents)
- [[apps/web/src/App.tsx.md|apps/web/src/App.tsx]]
- [[apps/web/src/components/PageLayout.tsx.md|apps/web/src/components/PageLayout.tsx]]

## Source Code Snippet
```tsx
import { cn } from "@core/utils/cn.ts";
import React from "react";
import { Trans } from "react-i18next";

type FooterProps = {
  className?: string;
};

const Footer = ({ className, ...props }: FooterProps) => {
  const version = React.useMemo(
    () => String(import.meta.env.VITE_VERSION)?.toUpperCase() || "",
    [],
  );
  const commitHash = React.useMemo(
    () =>
      String(import.meta.env.VITE_COMMIT_HASH)
        ?.toUpperCase()
        .slice(0, 7) || "unk",
    [],
  );
...
```