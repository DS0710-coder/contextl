# telemetryStore.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/telemetry/state/telemetryStore.ts`
- **Extension:** `.ts`
- **Size:** 2059 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ReadonlySignal`
- `TelemetryStore`

## Imports (Dependencies)
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/features/telemetry/domain/TelemetryReading.ts.md|packages/sdk/src/features/telemetry/domain/TelemetryReading.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/telemetry/TelemetryClient.ts.md|packages/sdk/src/features/telemetry/TelemetryClient.ts]]

## Source Code Snippet
```ts
import { type Signal, signal } from "@preact/signals-core";
import {
  type ReadonlySignal,
  toReadonly,
} from "../../../core/signals/createStore.ts";
import type { TelemetryReading } from "../domain/TelemetryReading.ts";

const MAX_HISTORY = 256;

export class TelemetryStore {
  private readonly latest = new Map<
    number,
    Signal<TelemetryReading | undefined>
  >();
  private readonly latestRead = new Map<
    number,
    ReadonlySignal<TelemetryReading | undefined>
  >();
  private readonly history = new Map<number, Signal<TelemetryReading[]>>();
  private readonly historyRead = new Map<
...
```