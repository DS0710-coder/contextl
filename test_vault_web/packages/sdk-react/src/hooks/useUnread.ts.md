# useUnread.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/hooks/useUnread.ts`
- **Extension:** `.ts`
- **Size:** 1319 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useTotalUnread`
- `useUnreadCount`
- `useUnreadByKey`

## Imports (Dependencies)
- [[packages/sdk-react/src/adapters/useActiveClient.ts.md|packages/sdk-react/src/adapters/useActiveClient.ts]]
- [[packages/sdk-react/src/adapters/useSignal.ts.md|packages/sdk-react/src/adapters/useSignal.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Source Code Snippet
```ts
import type { ConversationKey } from "@meshtastic/sdk";
import { useActiveClient } from "../adapters/useActiveClient.ts";
import { useSignal } from "../adapters/useSignal.ts";

const EMPTY_NUMBER_SIGNAL = {
  value: 0,
  peek: () => 0,
  subscribe: () => () => {},
} as const;

const EMPTY_MAP_SIGNAL = {
  value: new Map<string, number>() as ReadonlyMap<string, number>,
  peek: () => new Map<string, number>() as ReadonlyMap<string, number>,
  subscribe: () => () => {},
} as const;

/**
 * Total unread count across every conversation on the active client.
 * Returns 0 when no client is active.
 */
...
```