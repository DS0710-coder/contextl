# MessagesPage.ts

## Architecture Metrics
- **Path:** `e2e/pages/MessagesPage.ts`
- **Extension:** `.ts`
- **Size:** 1957 bytes
- **Centrality Score:** 0.0016
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `MessagesPage`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[e2e/fixtures/test.ts.md|e2e/fixtures/test.ts]]

## Source Code Snippet
```ts
import { expect, type Locator, type Page } from "@playwright/test";

/** The Messages page: compose box + rendered message list. */
export class MessagesPage {
  constructor(private readonly page: Page) {}

  input(): Locator {
    return this.page.locator('input[name="messageInput"]');
  }

  sendButton(): Locator {
    return this.page.locator('form[name="messageInput"] button[type="submit"]');
  }

  /** A rendered message bubble (an <li>) containing the given text. */
  message(text: string): Locator {
    return this.page.getByRole("listitem").filter({ hasText: text });
  }

  /** Wait until the device is configured enough that the composer is usable. */
...
```