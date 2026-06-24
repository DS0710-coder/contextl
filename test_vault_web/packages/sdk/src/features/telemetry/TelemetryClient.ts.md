# TelemetryClient.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/telemetry/TelemetryClient.ts`
- **Extension:** `.ts`
- **Size:** 2960 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TelemetryClientOptions`
- `TelemetryClient`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/features/telemetry/domain/TelemetryReading.ts.md|packages/sdk/src/features/telemetry/domain/TelemetryReading.ts]]
- [[packages/sdk/src/features/telemetry/domain/TelemetryRepository.ts.md|packages/sdk/src/features/telemetry/domain/TelemetryRepository.ts]]
- [[packages/sdk/src/features/telemetry/infrastructure/TelemetryMapper.ts.md|packages/sdk/src/features/telemetry/infrastructure/TelemetryMapper.ts]]
- [[packages/sdk/src/features/telemetry/infrastructure/repositories/InMemoryTelemetryRepository.ts.md|packages/sdk/src/features/telemetry/infrastructure/repositories/InMemoryTelemetryRepository.ts]]
- [[packages/sdk/src/features/telemetry/state/telemetryStore.ts.md|packages/sdk/src/features/telemetry/state/telemetryStore.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/telemetry/index.ts.md|packages/sdk/src/features/telemetry/index.ts]]

## Source Code Snippet
```ts
import type { MeshClient } from "../../core/client/MeshClient.ts";
import type { ReadonlySignal } from "../../core/signals/createStore.ts";
import type { TelemetryReading } from "./domain/TelemetryReading.ts";
import type {
  TelemetryRepository,
  TelemetryRetentionPolicy,
} from "./domain/TelemetryRepository.ts";
import { InMemoryTelemetryRepository } from "./infrastructure/repositories/InMemoryTelemetryRepository.ts";
import { TelemetryMapper } from "./infrastructure/TelemetryMapper.ts";
import { TelemetryStore } from "./state/telemetryStore.ts";

export interface TelemetryClientOptions {
  repository?: TelemetryRepository;
  retention?: TelemetryRetentionPolicy;
}

const HYDRATE_LIMIT = 256;

export class TelemetryClient {
  private readonly store: TelemetryStore;
...
```