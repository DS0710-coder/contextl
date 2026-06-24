# test.ts

## Architecture Metrics
- **Path:** `e2e/fixtures/test.ts`
- **Extension:** `.ts`
- **Size:** 974 bytes
- **Centrality Score:** 0.0020
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `DeviceInfo`
- `Fixtures`

## Imports (Dependencies)
- [[e2e/pages/ConnectionPage.ts.md|e2e/pages/ConnectionPage.ts]]
- [[e2e/pages/MessagesPage.ts.md|e2e/pages/MessagesPage.ts]]

## Imported By (Dependents)
- [[e2e/tests/connect.spec.ts.md|e2e/tests/connect.spec.ts]]
- [[e2e/tests/messaging.broadcast.spec.ts.md|e2e/tests/messaging.broadcast.spec.ts]]
- [[e2e/tests/messaging.direct.spec.ts.md|e2e/tests/messaging.direct.spec.ts]]

## Source Code Snippet
```ts
import { test as base, expect } from "@playwright/test";
import { ConnectionPage } from "../pages/ConnectionPage.ts";
import { MessagesPage } from "../pages/MessagesPage.ts";

export type DeviceInfo = {
  /** host:port the browser connects to, e.g. "127.0.0.1:9443". */
  host: string;
  /** Whether the device webserver is HTTPS. */
  tls: boolean;
};

type Fixtures = {
  connectionPage: ConnectionPage;
  messagesPage: MessagesPage;
  device: DeviceInfo;
};

export const test = base.extend<Fixtures>({
  connectionPage: async ({ page }, use) => {
    await use(new ConnectionPage(page));
...
```