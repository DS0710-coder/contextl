# useLang.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useLang.ts`
- **Extension:** `.ts`
- **Size:** 1676 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Lang`
- `LangCode`
- `LanguageState`
- `useLang`

## Imports (Dependencies)
- [[apps/web/src/core/hooks/useLocalStorage.ts.md|apps/web/src/core/hooks/useLocalStorage.ts]]
- [[apps/web/src/i18n-config.ts.md|apps/web/src/i18n-config.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/LanguageSwitcher.tsx.md|apps/web/src/components/LanguageSwitcher.tsx]]
- [[apps/web/src/pages/Nodes/index.tsx.md|apps/web/src/pages/Nodes/index.tsx]]

## Source Code Snippet
```ts
import {
  FALLBACK_LANGUAGE_CODE,
  type Lang,
  type LangCode,
  supportedLanguages,
} from "@app/i18n-config.ts";
import { useCallback, useMemo } from "react";
import { useTranslation } from "react-i18next";
import useLocalStorage from "./useLocalStorage.ts";

const STORAGE_KEY = "language";

type LanguageState = {
  language: LangCode;
};

function useLang() {
  const { i18n } = useTranslation();
  const [_, setLanguageInStorage] = useLocalStorage<LanguageState | null>(
    STORAGE_KEY,
...
```