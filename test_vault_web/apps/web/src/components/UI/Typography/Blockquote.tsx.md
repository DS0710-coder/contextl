# Blockquote.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Typography/Blockquote.tsx`
- **Extension:** `.tsx`
- **Size:** 293 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BlockquoteProps`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
export interface BlockquoteProps {
  children: React.ReactNode;
}

export const BlockQuote = ({ children }: BlockquoteProps) => (
  <blockquote className="mt-6 border-l-2 border-slate-300 pl-6 italic text-slate-800 dark:border-slate-600 dark:text-slate-200">
    {children}
  </blockquote>
);
```