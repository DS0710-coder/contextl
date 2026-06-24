# hooks.test.tsx

## Architecture Metrics
- **Path:** `packages/sdk-react/tests/hooks.test.tsx`
- **Extension:** `.tsx`
- **Size:** 1563 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `setup`

## Imports (Dependencies)
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
import { act, render, renderHook, waitFor } from "@testing-library/react";
import { MeshClient } from "@meshtastic/sdk";
import { createFakeTransport } from "@meshtastic/sdk/testing";
import { ChannelNumber } from "@meshtastic/sdk";
import { describe, expect, it } from "vitest";
import { MeshProvider, useChat, useMeshDevice } from "../mod.ts";

function setup() {
  const handle = createFakeTransport();
  const client = new MeshClient({ transport: handle.transport });
  const wrapper = ({ children }: { children: React.ReactNode }) => (
    <MeshProvider client={client}>{children}</MeshProvider>
  );
  return { client, handle, wrapper };
}

describe("sdk-react hooks", () => {
  it("useMeshDevice re-renders on myNodeInfo", async () => {
    const { handle, wrapper } = setup();
    const { result } = renderHook(() => useMeshDevice(), { wrapper });
...
```