# useChat.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/hooks/useChat.ts`
- **Extension:** `.ts`
- **Size:** 1105 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `UseChatResult`
- `useChat`

## Imports (Dependencies)
- [[packages/sdk-react/src/adapters/useClient.ts.md|packages/sdk-react/src/adapters/useClient.ts]]
- [[packages/sdk-react/src/adapters/useSignal.ts.md|packages/sdk-react/src/adapters/useSignal.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Source Code Snippet
```ts
import type {
  ChannelNumber,
  ConversationKey,
  Message,
  SendTextError,
  SendTextInput,
} from "@meshtastic/sdk";
import type { ResultType } from "better-result";
import { useCallback, useMemo } from "react";
import { useClient } from "../adapters/useClient.ts";
import { useSignal } from "../adapters/useSignal.ts";

export interface UseChatResult {
  messages: Message[];
  send(input: SendTextInput): Promise<ResultType<number, SendTextError>>;
  loadOlder(before: Date, limit?: number): Promise<Message[]>;
}

export function useChat(channel: ChannelNumber): UseChatResult {
  const client = useClient();
...
```