# TelemetryClient.persistence.test.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/telemetry/TelemetryClient.persistence.test.ts`
- **Extension:** `.ts`
- **Size:** 2713 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/testing/createFakeTransport.ts.md|packages/sdk/src/core/testing/createFakeTransport.ts]]
- [[packages/sdk/src/core/types.ts.md|packages/sdk/src/core/types.ts]]
- [[packages/sdk/src/features/telemetry/infrastructure/repositories/InMemoryTelemetryRepository.ts.md|packages/sdk/src/features/telemetry/infrastructure/repositories/InMemoryTelemetryRepository.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { create } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import { describe, expect, it } from "vitest";
import { MeshClient } from "../../core/client/MeshClient.ts";
import { createFakeTransport } from "../../core/testing/createFakeTransport.ts";
import { ChannelNumber } from "../../core/types.ts";
import { InMemoryTelemetryRepository } from "./infrastructure/repositories/InMemoryTelemetryRepository.ts";

const dispatch = (
  client: MeshClient,
  from: number,
  ms: number,
  battery = 80,
): void => {
  client.events.onTelemetryPacket.dispatch({
    id: ms,
    from,
    to: 0,
    channel: ChannelNumber.Primary,
    type: "broadcast",
...
```