# TraceRouteUseCase.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/traceroute/application/TraceRouteUseCase.ts`
- **Extension:** `.ts`
- **Size:** 793 bytes
- **Centrality Score:** 0.0012
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/traceroute/TraceRouteClient.ts.md|packages/sdk/src/features/traceroute/TraceRouteClient.ts]]

## Source Code Snippet
```ts
import { create, toBinary } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import { Result } from "better-result";
import type { ResultType } from "better-result";
import type { MeshClient } from "../../../core/client/MeshClient.ts";

export async function runTraceRoute(
  client: MeshClient,
  destination: number,
): Promise<ResultType<number, Error>> {
  try {
    const routeDiscovery = create(Protobuf.Mesh.RouteDiscoverySchema, {
      route: [],
    });
    const id = await client.sendPacket(
      toBinary(Protobuf.Mesh.RouteDiscoverySchema, routeDiscovery),
      Protobuf.Portnums.PortNum.TRACEROUTE_APP,
      destination,
    );
    return Result.ok(id);
...
```