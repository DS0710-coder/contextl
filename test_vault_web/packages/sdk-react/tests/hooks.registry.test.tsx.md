# hooks.registry.test.tsx

## Architecture Metrics
- **Path:** `packages/sdk-react/tests/hooks.registry.test.tsx`
- **Extension:** `.tsx`
- **Size:** 4596 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `makeRegistry`

## Imports (Dependencies)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
import { create } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import { ChannelNumber, MeshRegistry } from "@meshtastic/sdk";
import { createFakeTransport } from "@meshtastic/sdk/testing";
import { act, renderHook, waitFor } from "@testing-library/react";
import { describe, expect, it } from "vitest";
import {
  MeshRegistryProvider,
  useChannels,
  useMeshDevice,
  useNode,
  useNodes,
} from "../mod.ts";

function makeRegistry(deviceCount: number) {
  const registry = new MeshRegistry();
  const handles: ReturnType<typeof createFakeTransport>[] = [];
  for (let i = 0; i < deviceCount; i++) {
    const handle = createFakeTransport();
    handles.push(handle);
...
```