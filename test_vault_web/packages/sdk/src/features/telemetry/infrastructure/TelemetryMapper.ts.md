# TelemetryMapper.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/telemetry/infrastructure/TelemetryMapper.ts`
- **Extension:** `.ts`
- **Size:** 480 bytes
- **Centrality Score:** 0.0016
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]
- [[packages/sdk/src/features/telemetry/domain/TelemetryReading.ts.md|packages/sdk/src/features/telemetry/domain/TelemetryReading.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/telemetry/TelemetryClient.ts.md|packages/sdk/src/features/telemetry/TelemetryClient.ts]]
- [[packages/sdk/src/features/telemetry/index.ts.md|packages/sdk/src/features/telemetry/index.ts]]

## Source Code Snippet
```ts
import type { PacketMetadata } from "../../../core/types.ts";
import type * as Protobuf from "@meshtastic/protobufs";
import type { TelemetryReading } from "../domain/TelemetryReading.ts";

export const TelemetryMapper = {
  fromPacket(
    packet: PacketMetadata<Protobuf.Telemetry.Telemetry>,
  ): TelemetryReading {
    return {
      nodeNum: packet.from,
      time: packet.rxTime,
      kind: packet.data.variant.case,
      value: packet.data.variant.value,
    };
  },
};
```