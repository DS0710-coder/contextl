# MeshClient.progress.test.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/core/client/MeshClient.progress.test.ts`
- **Extension:** `.ts`
- **Size:** 3610 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/testing/createFakeTransport.ts.md|packages/sdk/src/core/testing/createFakeTransport.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { create } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import { describe, expect, it } from "vitest";
import { createFakeTransport } from "../testing/createFakeTransport.ts";
import { MeshClient } from "./MeshClient.ts";

describe("MeshClient.progress", () => {
  it("starts in the idle phase before configure() is called", () => {
    const { transport } = createFakeTransport();
    const client = new MeshClient({ transport });
    expect(client.progress.value.phase).toBe("idle");
  });

  it("flips to configuring with empty counters when configure() runs", async () => {
    const { transport } = createFakeTransport();
    const client = new MeshClient({ transport });
    void client.configure();
    expect(client.progress.value.phase).toBe("configuring");
    expect(client.progress.value).toEqual({
      phase: "configuring",
...
```