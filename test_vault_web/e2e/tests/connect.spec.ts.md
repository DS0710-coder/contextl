# connect.spec.ts

## Architecture Metrics
- **Path:** `e2e/tests/connect.spec.ts`
- **Extension:** `.ts`
- **Size:** 526 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[e2e/fixtures/test.ts.md|e2e/fixtures/test.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { expect, test } from "../fixtures/test.ts";

/**
 * T0 — the app can connect to a REAL device over the HTTP(S) phone API and
 * complete the config handshake far enough to show the messaging UI.
 */
test("connects to a real device over HTTPS and reaches the message view", async ({
  page,
  connectionPage,
  messagesPage,
  device,
}) => {
  await connectionPage.connectHttp({ host: device.host, tls: device.tls });
  await messagesPage.waitReady();
  await expect(page).toHaveURL(/\/messages\/broadcast\/0/);
});
```