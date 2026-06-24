# useCopyToClipboard.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useCopyToClipboard.ts`
- **Extension:** `.ts`
- **Size:** 1267 bytes
- **Centrality Score:** 0.0015
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `UseCopyToClipboardProps`
- `useCopyToClipboard`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/UI/Input.tsx.md|apps/web/src/components/UI/Input.tsx]]

## Source Code Snippet
```ts
import { useCallback, useEffect, useRef, useState } from "react";

interface UseCopyToClipboardProps {
  timeout?: number;
}

export function useCopyToClipboard({
  timeout = 2000,
}: UseCopyToClipboardProps = {}) {
  const [isCopied, setIsCopied] = useState<boolean>(false);
  const timeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null);

  useEffect(() => {
    return () => {
      if (timeoutRef.current) {
        globalThis.clearTimeout(timeoutRef.current);
      }
    };
  }, []);

...
```