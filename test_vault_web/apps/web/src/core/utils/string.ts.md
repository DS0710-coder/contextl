# string.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/string.ts`
- **Extension:** `.ts`
- **Size:** 2292 bytes
- **Centrality Score:** 0.0013
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PluralForms`
- `FormatOptions`
- `formatQuantity`
- `LengthValidationResult`
- `validateMaxByteLength`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx.md|apps/web/src/components/PageComponents/Map/Popups/NodeDetail.tsx]]
- [[apps/web/src/validation/channel.ts.md|apps/web/src/validation/channel.ts]]

## Source Code Snippet
```ts
interface PluralForms {
  one: string;
  other: string;
  [key: string]: string;
}

interface FormatOptions {
  locale?: string;
  pluralRules?: Intl.PluralRulesOptions;
  numberFormat?: Intl.NumberFormatOptions;
}

export function formatQuantity(
  value: number,
  forms: PluralForms,
  options: FormatOptions = {},
) {
  const {
    locale = "en-US",
    pluralRules: pluralOptions = { type: "cardinal" },
...
```