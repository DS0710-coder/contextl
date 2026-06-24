# ConnectionPage.ts

## Architecture Metrics
- **Path:** `e2e/pages/ConnectionPage.ts`
- **Extension:** `.ts`
- **Size:** 1577 bytes
- **Centrality Score:** 0.0016
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ConnectionPage`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[e2e/fixtures/test.ts.md|e2e/fixtures/test.ts]]

## Source Code Snippet
```ts
import { expect, type Page } from "@playwright/test";

/**
 * Drives the "Add Connection" dialog to connect to a device over the HTTP(S)
 * phone API. The dialog defaults to the HTTP tab; "Save connection" only enables
 * after a successful "Test connection". On success the app navigates to
 * /messages/broadcast/0.
 */
export class ConnectionPage {
  constructor(private readonly page: Page) {}

  async connectHttp(opts: { host: string; tls: boolean; name?: string }): Promise<void> {
    const { host, tls, name = "E2E Device" } = opts;
    const page = this.page;

    await page.goto("/");
    await page.getByRole("button", { name: "Add Connection" }).first().click();

    const dialog = page.getByRole("dialog");
    await expect(dialog).toBeVisible();
...
```