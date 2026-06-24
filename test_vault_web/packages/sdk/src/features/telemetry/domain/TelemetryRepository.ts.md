# TelemetryRepository.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/telemetry/domain/TelemetryRepository.ts`
- **Extension:** `.ts`
- **Size:** 1037 bytes
- **Centrality Score:** 0.0025
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TelemetryRetentionPolicy`
- `TelemetryRepository`

## Imports (Dependencies)
- [[packages/sdk/src/features/telemetry/domain/TelemetryReading.ts.md|packages/sdk/src/features/telemetry/domain/TelemetryReading.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/telemetry/TelemetryClient.ts.md|packages/sdk/src/features/telemetry/TelemetryClient.ts]]
- [[packages/sdk/src/features/telemetry/index.ts.md|packages/sdk/src/features/telemetry/index.ts]]
- [[packages/sdk/src/features/telemetry/infrastructure/repositories/InMemoryTelemetryRepository.ts.md|packages/sdk/src/features/telemetry/infrastructure/repositories/InMemoryTelemetryRepository.ts]]

## Source Code Snippet
```ts
import type { TelemetryReading } from "./TelemetryReading.ts";

export interface TelemetryRetentionPolicy {
  /** Keep at most this many readings per node. */
  maxPerNode?: number;
  /** Drop anything older than this many ms. */
  olderThanMs?: number;
}

/**
 * Port for persisting telemetry readings. Implementations live in adapter
 * packages (e.g. `@meshtastic/sdk-storage-sqlocal`) or in-memory within the
 * SDK itself.
 *
 * Reads are paginated by node so consumers can lazy-load history on scroll
 * rather than rehydrating every reading at boot.
 */
export interface TelemetryRepository {
  loadRecent(nodeNum: number, limit: number): Promise<TelemetryReading[]>;
  loadBefore(
...
```