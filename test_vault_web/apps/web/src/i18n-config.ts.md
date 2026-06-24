# i18n-config.ts

## Architecture Metrics
- **Path:** `apps/web/src/i18n-config.ts`
- **Extension:** `.ts`
- **Size:** 1805 bytes
- **Centrality Score:** 0.0016
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Lang`
- `LangCode`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/LanguageSwitcher.tsx.md|apps/web/src/components/LanguageSwitcher.tsx]]
- [[apps/web/src/core/hooks/useLang.ts.md|apps/web/src/core/hooks/useLang.ts]]
- [[apps/web/src/index.tsx.md|apps/web/src/index.tsx]]
- [[apps/web/src/tests/test-utils.tsx.md|apps/web/src/tests/test-utils.tsx]]

## Source Code Snippet
```ts
import i18next from "i18next";
import LanguageDetector from "i18next-browser-languagedetector";
import Backend from "i18next-http-backend";
import { initReactI18next } from "react-i18next";

export type Lang = {
  code: Intl.Locale["language"];
  name: string;
  flag: string;
  region?: Intl.Locale["region"];
};

export type LangCode = Lang["code"];

export const supportedLanguages: Lang[] = [
  { code: "fi", name: "Suomi", flag: "🇫🇮" },
  { code: "de", name: "Deutsch", flag: "🇩🇪" },
  { code: "en", name: "English", flag: "🇺🇸" },
  { code: "fr", name: "Français", flag: "🇫🇷" },
  { code: "ru", name: "Русский", flag: "🇷🇺" },
...
```