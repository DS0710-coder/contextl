# useLocalStorage.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/hooks/useLocalStorage.ts`
- **Extension:** `.ts`
- **Size:** 3809 bytes
- **Centrality Score:** 0.0028
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `WindowEventMap`
- `UseLocalStorageOptions`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/core/hooks/useKeyBackupReminder.tsx.md|apps/web/src/core/hooks/useKeyBackupReminder.tsx]]
- [[apps/web/src/core/hooks/useLang.ts.md|apps/web/src/core/hooks/useLang.ts]]
- [[apps/web/src/core/hooks/useLocalStorage.test.ts.md|apps/web/src/core/hooks/useLocalStorage.test.ts]]
- [[apps/web/src/core/hooks/usePinnedItems.ts.md|apps/web/src/core/hooks/usePinnedItems.ts]]

## Source Code Snippet
```ts
import type { Dispatch, SetStateAction } from "react";
import { useCallback, useEffect, useRef, useState } from "react";

declare global {
  interface WindowEventMap {
    "local-storage": CustomEvent<{ key: string }>;
  }
}

type UseLocalStorageOptions<T> = {
  serializer?: (value: T) => string;
  deserializer?: (value: string) => T;
  initializeWithValue?: boolean;
};

const IS_SERVER = typeof window === "undefined";

export default function useLocalStorage<T>(
  key: string,
  initialValue: T | (() => T),
...
```