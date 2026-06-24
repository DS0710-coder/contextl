# useDirectChat.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/hooks/useDirectChat.ts`
- **Extension:** `.ts`
- **Size:** 1326 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `UseDirectChatResult`
- `useDirectChat`

## Imports (Dependencies)
- [[packages/sdk-react/src/adapters/useClient.ts.md|packages/sdk-react/src/adapters/useClient.ts]]
- [[packages/sdk-react/src/adapters/useSignal.ts.md|packages/sdk-react/src/adapters/useSignal.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Source Code Snippet
```ts
import type {
  ConversationKey,
  Message,
  SendTextError,
  SendTextInput,
} from "@meshtastic/sdk";
import type { ResultType } from "better-result";
import { useCallback, useMemo } from "react";
import { useClient } from "../adapters/useClient.ts";
import { useSignal } from "../adapters/useSignal.ts";

export interface UseDirectChatResult {
  messages: Message[];
  send(input: SendTextInput): Promise<ResultType<number, SendTextError>>;
  loadOlder(before: Date, limit?: number): Promise<Message[]>;
}

/**
 * Direct-message conversation with a single peer node. The bucket is keyed
 * by the peer (so messages from-me-to-peer and from-peer-to-me share one
...
```