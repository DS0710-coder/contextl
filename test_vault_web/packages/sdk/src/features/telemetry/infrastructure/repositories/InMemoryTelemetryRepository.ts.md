# InMemoryTelemetryRepository.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/telemetry/infrastructure/repositories/InMemoryTelemetryRepository.ts`
- **Extension:** `.ts`
- **Size:** 2138 bytes
- **Centrality Score:** 0.0021
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `InMemoryTelemetryRepository`

## Imports (Dependencies)
- [[packages/sdk/src/features/telemetry/domain/TelemetryReading.ts.md|packages/sdk/src/features/telemetry/domain/TelemetryReading.ts]]
- [[packages/sdk/src/features/telemetry/domain/TelemetryRepository.ts.md|packages/sdk/src/features/telemetry/domain/TelemetryRepository.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/telemetry/TelemetryClient.persistence.test.ts.md|packages/sdk/src/features/telemetry/TelemetryClient.persistence.test.ts]]
- [[packages/sdk/src/features/telemetry/TelemetryClient.ts.md|packages/sdk/src/features/telemetry/TelemetryClient.ts]]
- [[packages/sdk/src/features/telemetry/index.ts.md|packages/sdk/src/features/telemetry/index.ts]]
- [[packages/sdk/src/features/telemetry/infrastructure/repositories/InMemoryTelemetryRepository.test.ts.md|packages/sdk/src/features/telemetry/infrastructure/repositories/InMemoryTelemetryRepository.test.ts]]

## Source Code Snippet
```ts
import type { TelemetryReading } from "../../domain/TelemetryReading.ts";
import type {
  TelemetryRepository,
  TelemetryRetentionPolicy,
} from "../../domain/TelemetryRepository.ts";

/**
 * Default in-memory TelemetryRepository. No persistence across reloads.
 * Suitable for tests and for single-session apps that do not need history.
 */
export class InMemoryTelemetryRepository implements TelemetryRepository {
  private readonly buckets = new Map<number, TelemetryReading[]>();

  async loadRecent(
    nodeNum: number,
    limit: number,
  ): Promise<TelemetryReading[]> {
    return (this.buckets.get(nodeNum) ?? []).slice(-limit);
  }

...
```