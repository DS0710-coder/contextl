# ErrorPage.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/ErrorPage.tsx`
- **Extension:** `.tsx`
- **Size:** 3577 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ErrorPage`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Typography/Heading.tsx.md|apps/web/src/components/UI/Typography/Heading.tsx]]
- [[apps/web/src/components/UI/Typography/Link.tsx.md|apps/web/src/components/UI/Typography/Link.tsx]]
- [[apps/web/src/components/UI/Typography/P.tsx.md|apps/web/src/components/UI/Typography/P.tsx]]
- [[apps/web/src/core/utils/github.ts.md|apps/web/src/core/utils/github.ts]]

## Imported By (Dependents)
- [[apps/web/src/App.tsx.md|apps/web/src/App.tsx]]
- [[apps/web/src/components/PageLayout.tsx.md|apps/web/src/components/PageLayout.tsx]]

## Source Code Snippet
```tsx
import { Heading } from "@components/UI/Typography/Heading.tsx";
import { Link } from "@components/UI/Typography/Link.tsx";
import { P } from "@components/UI/Typography/P.tsx";
import newGithubIssueUrl from "@core/utils/github.ts";
import { ExternalLink } from "lucide-react";
import { Trans, useTranslation } from "react-i18next";

export function ErrorPage({ error }: { error: Error }) {
  const { t } = useTranslation();

  if (!error) {
    return null;
  }

  return (
    <article className="w-full h-screen overflow-y-auto bg-background-primary text-text-primary">
      <section className="flex shrink md:flex-row gap-16 mt-20 px-4 md:px-8 text-lg md:text-xl space-y-2 place-items-center dark:bg-background-primary text-slate-900 dark:text-text-primary">
        <div>
          <Heading as="h2" className="text-text-primary">
            {t("errorPage.title")}
...
```