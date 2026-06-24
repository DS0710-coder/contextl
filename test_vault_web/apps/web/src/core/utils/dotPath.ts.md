# dotPath.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/dotPath.ts`
- **Extension:** `.ts`
- **Size:** 492 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DotPath`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/core/utils/dotPath.test.ts.md|apps/web/src/core/utils/dotPath.test.ts]]

## Source Code Snippet
```ts
export type DotPath = { [key: string]: unknown } | unknown[];

export const dotPaths = <T extends DotPath>(obj: T, prefix = ""): string[] => {
  if (Array.isArray(obj)) {
    return obj.flatMap((v, i) =>
      v && typeof v === "object"
        ? dotPaths(v as DotPath, `${prefix}${i}.`)
        : [`${prefix}${i}`],
    );
  }
  return Object.entries(obj).flatMap(([k, v]) =>
    v && typeof v === "object"
      ? dotPaths(v as DotPath, `${prefix}${k}.`)
      : [`${prefix}${k}`],
  );
};
```