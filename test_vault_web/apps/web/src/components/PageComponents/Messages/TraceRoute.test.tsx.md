# TraceRoute.test.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Messages/TraceRoute.test.tsx`
- **Extension:** `.tsx`
- **Size:** 3916 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/components/PageComponents/Messages/TraceRoute.tsx.md|apps/web/src/components/PageComponents/Messages/TraceRoute.tsx]]
- [[apps/web/src/core/hooks/useNodesAsProto.ts.md|apps/web/src/core/hooks/useNodesAsProto.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
import { TraceRoute } from "@components/PageComponents/Messages/TraceRoute.tsx";
import { useNodesAsProto } from "@core/hooks/useNodesAsProto.ts";
import { Protobuf } from "@meshtastic/sdk";
import { render, screen } from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";

vi.mock("@core/hooks/useNodesAsProto.ts");

describe("TraceRoute", () => {
  const fromUser = {
    user: {
      $typeName: "meshtastic.User",
      longName: "Source Node",
      publicKey: new Uint8Array([1, 2, 3]),
      shortName: "Source",
      hwModel: 1,
      macaddr: new Uint8Array([0x01, 0x02, 0x03, 0x04]),
      id: "source-node",
      isLicensed: false,
      role: Protobuf.Config.Config_DeviceConfig_Role.CLIENT,
...
```