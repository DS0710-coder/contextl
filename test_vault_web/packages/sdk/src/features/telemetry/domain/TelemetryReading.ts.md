# TelemetryReading.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/telemetry/domain/TelemetryReading.ts`
- **Extension:** `.ts`
- **Size:** 324 bytes
- **Centrality Score:** 0.0061
- **In-Degree (Imported By):** 7
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TelemetryKind`
- `TelemetryReading`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/sdk/src/features/telemetry/TelemetryClient.ts.md|packages/sdk/src/features/telemetry/TelemetryClient.ts]]
- [[packages/sdk/src/features/telemetry/domain/TelemetryRepository.ts.md|packages/sdk/src/features/telemetry/domain/TelemetryRepository.ts]]
- [[packages/sdk/src/features/telemetry/index.ts.md|packages/sdk/src/features/telemetry/index.ts]]
- [[packages/sdk/src/features/telemetry/infrastructure/TelemetryMapper.ts.md|packages/sdk/src/features/telemetry/infrastructure/TelemetryMapper.ts]]
- [[packages/sdk/src/features/telemetry/infrastructure/repositories/InMemoryTelemetryRepository.test.ts.md|packages/sdk/src/features/telemetry/infrastructure/repositories/InMemoryTelemetryRepository.test.ts]]
- [[packages/sdk/src/features/telemetry/infrastructure/repositories/InMemoryTelemetryRepository.ts.md|packages/sdk/src/features/telemetry/infrastructure/repositories/InMemoryTelemetryRepository.ts]]
- [[packages/sdk/src/features/telemetry/state/telemetryStore.ts.md|packages/sdk/src/features/telemetry/state/telemetryStore.ts]]

## Source Code Snippet
```ts
import type * as Protobuf from "@meshtastic/protobufs";

export type TelemetryKind = Protobuf.Telemetry.Telemetry["variant"]["case"];

export interface TelemetryReading {
  readonly nodeNum: number;
  readonly time: Date;
  readonly kind: TelemetryKind;
  readonly value: Protobuf.Telemetry.Telemetry["variant"]["value"];
}
```