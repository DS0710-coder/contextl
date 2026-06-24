# transport.test.ts

## Architecture Metrics
- **Path:** `packages/transport-http/src/transport.test.ts`
- **Extension:** `.ts`
- **Size:** 6630 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `MockInstance`
- `stubFetch`
- `makeAbortAwareHang`

## Imports (Dependencies)
- [[packages/transport-http/src/transport.ts.md|packages/transport-http/src/transport.ts]]
- [[tests/utils/transportContract.ts.md|tests/utils/transportContract.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import {
  afterEach,
  beforeEach,
  describe,
  expect,
  it,
  type MockInstance,
  vi,
} from "vitest";
import { runTransportContract } from "../../../tests/utils/transportContract.ts";
import { TransportHTTP } from "./transport.ts";

let abortTimeoutSpy: MockInstance | undefined;
beforeEach(() => {
  abortTimeoutSpy = vi
    .spyOn(
      globalThis.AbortSignal as unknown as { timeout(ms: number): AbortSignal },
      "timeout",
    )
    .mockImplementation((ms: number) => {
...
```