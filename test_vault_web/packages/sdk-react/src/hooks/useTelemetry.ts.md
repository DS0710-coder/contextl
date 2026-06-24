# useTelemetry.ts

## Architecture Metrics
- **Path:** `packages/sdk-react/src/hooks/useTelemetry.ts`
- **Extension:** `.ts`
- **Size:** 725 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `UseTelemetryResult`
- `useTelemetry`

## Imports (Dependencies)
- [[packages/sdk-react/src/adapters/useClient.ts.md|packages/sdk-react/src/adapters/useClient.ts]]
- [[packages/sdk-react/src/adapters/useSignal.ts.md|packages/sdk-react/src/adapters/useSignal.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]

## Source Code Snippet
```ts
import type { TelemetryReading } from "@meshtastic/sdk";
import { useMemo } from "react";
import { useClient } from "../adapters/useClient.ts";
import { useSignal } from "../adapters/useSignal.ts";

export interface UseTelemetryResult {
  latest: TelemetryReading | undefined;
  history: TelemetryReading[];
}

export function useTelemetry(nodeNum: number): UseTelemetryResult {
  const client = useClient();
  const latestSig = useMemo(
    () => client.telemetry.latest(nodeNum),
    [client, nodeNum],
  );
  const historySig = useMemo(
    () => client.telemetry.history(nodeNum),
    [client, nodeNum],
  );
...
```