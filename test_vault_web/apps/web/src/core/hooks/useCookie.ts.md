# useCookie.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useCookie.ts`
- **Extension:** `.ts`
- **Size:** 1331 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `CookieHookResult`
- `useCookie`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import Cookies from "js-cookie";
import { useCallback, useState } from "react";

interface CookieHookResult<T> {
  value: T | undefined;
  setCookie: (value: T, options?: Cookies.CookieAttributes) => void;
  removeCookie: () => void;
}

function useCookie<T extends object>(
  cookieName: string,
  initialValue?: T,
): CookieHookResult<T> {
  const [cookieValue, setCookieValue] = useState<T | undefined>(() => {
    try {
      const cookie = Cookies.get(cookieName);
      return cookie ? (JSON.parse(cookie) as T) : initialValue;
    } catch (error) {
      console.error(`Error parsing cookie ${cookieName}:`, error);
      return initialValue;
...
```