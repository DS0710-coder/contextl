# useTraceroute.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/hooks/useTraceroute.ts`
- **Extension:** `.ts`
- **Size:** 395 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `useTraceroute`

## Imports (Dependencies)
- [[packages/sdk-react/src/adapters/useClient.ts.md|packages/sdk-react/src/adapters/useClient.ts]]
- [[packages/sdk-react/src/adapters/useSignalValue.ts.md|packages/sdk-react/src/adapters/useSignalValue.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Source Code Snippet
```ts
import type { TraceRoute } from "@meshtastic/sdk";
import { useClient } from "../adapters/useClient.ts";
import { useSignalValue } from "../adapters/useSignalValue.ts";

export function useTraceroute(destination: number): TraceRoute | undefined {
  const client = useClient();
  return useSignalValue(client.traceroute.list, (list) =>
    list.find((t) => t.destination === destination),
  );
}
```