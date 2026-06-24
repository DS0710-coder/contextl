# useConnection.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/hooks/useConnection.ts`
- **Extension:** `.ts`
- **Size:** 948 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `UseConnectionResult`
- `useConnection`

## Imports (Dependencies)
- [[packages/sdk-react/src/adapters/useClient.ts.md|packages/sdk-react/src/adapters/useClient.ts]]
- [[packages/sdk-react/src/adapters/useSignal.ts.md|packages/sdk-react/src/adapters/useSignal.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Source Code Snippet
```ts
import { DeviceStatusEnum } from "@meshtastic/sdk";
import { useCallback } from "react";
import { useClient } from "../adapters/useClient.ts";
import { useSignal } from "../adapters/useSignal.ts";

export interface UseConnectionResult {
  status: DeviceStatusEnum;
  isConnected: boolean;
  isConnecting: boolean;
  connect(): Promise<void>;
  disconnect(): Promise<void>;
}

export function useConnection(): UseConnectionResult {
  const client = useClient();
  const status = useSignal(client.device.status);
  const connect = useCallback(() => client.connect(), [client]);
  const disconnect = useCallback(() => client.disconnect(), [client]);

  return {
...
```