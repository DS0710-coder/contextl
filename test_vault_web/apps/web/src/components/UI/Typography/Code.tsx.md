# Code.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/UI/Typography/Code.tsx`
- **Extension:** `.tsx`
- **Size:** 303 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `CodeProps`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
export interface CodeProps {
  children: React.ReactNode;
}

export const Code = ({ children }: CodeProps) => (
  <code className="relative rounded-sm bg-slate-100 px-[0.3rem] py-[0.2rem] text-sm font-semibold font-mono text-slate-900 dark:bg-slate-800 dark:text-slate-400">
    {children}
  </code>
);
```