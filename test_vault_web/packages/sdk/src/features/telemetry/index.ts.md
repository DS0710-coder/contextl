# index.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/telemetry/index.ts`
- **Extension:** `.ts`
- **Size:** 500 bytes
- **Centrality Score:** 0.0041
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/features/telemetry/TelemetryClient.ts.md|packages/sdk/src/features/telemetry/TelemetryClient.ts]]
- [[packages/sdk/src/features/telemetry/domain/TelemetryReading.ts.md|packages/sdk/src/features/telemetry/domain/TelemetryReading.ts]]
- [[packages/sdk/src/features/telemetry/domain/TelemetryRepository.ts.md|packages/sdk/src/features/telemetry/domain/TelemetryRepository.ts]]
- [[packages/sdk/src/features/telemetry/infrastructure/TelemetryMapper.ts.md|packages/sdk/src/features/telemetry/infrastructure/TelemetryMapper.ts]]
- [[packages/sdk/src/features/telemetry/infrastructure/repositories/InMemoryTelemetryRepository.ts.md|packages/sdk/src/features/telemetry/infrastructure/repositories/InMemoryTelemetryRepository.ts]]

## Imported By (Dependents)
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]

## Source Code Snippet
```ts
export { TelemetryClient } from "./TelemetryClient.ts";
export type { TelemetryClientOptions } from "./TelemetryClient.ts";
export type {
  TelemetryKind,
  TelemetryReading,
} from "./domain/TelemetryReading.ts";
export type {
  TelemetryRepository,
  TelemetryRetentionPolicy,
} from "./domain/TelemetryRepository.ts";
export { TelemetryMapper } from "./infrastructure/TelemetryMapper.ts";
export { InMemoryTelemetryRepository } from "./infrastructure/repositories/InMemoryTelemetryRepository.ts";
```