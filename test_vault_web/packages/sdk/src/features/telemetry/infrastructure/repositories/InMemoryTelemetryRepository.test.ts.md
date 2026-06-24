# InMemoryTelemetryRepository.test.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/telemetry/infrastructure/repositories/InMemoryTelemetryRepository.test.ts`
- **Extension:** `.ts`
- **Size:** 2322 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/features/telemetry/domain/TelemetryReading.ts.md|packages/sdk/src/features/telemetry/domain/TelemetryReading.ts]]
- [[packages/sdk/src/features/telemetry/infrastructure/repositories/InMemoryTelemetryRepository.ts.md|packages/sdk/src/features/telemetry/infrastructure/repositories/InMemoryTelemetryRepository.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { describe, expect, it } from "vitest";
import type { TelemetryReading } from "../../domain/TelemetryReading.ts";
import { InMemoryTelemetryRepository } from "./InMemoryTelemetryRepository.ts";

const reading = (nodeNum: number, ms: number): TelemetryReading => ({
  nodeNum,
  time: new Date(ms),
  kind: "deviceMetrics",
  value: { batteryLevel: 50 } as TelemetryReading["value"],
});

describe("InMemoryTelemetryRepository", () => {
  it("appends and loads recent readings per node", async () => {
    const repo = new InMemoryTelemetryRepository();
    await repo.append(reading(1, 1000));
    await repo.append(reading(1, 2000));
    await repo.append(reading(2, 1500));

    expect(await repo.loadRecent(1, 10)).toHaveLength(2);
    expect(await repo.loadRecent(2, 10)).toHaveLength(1);
...
```