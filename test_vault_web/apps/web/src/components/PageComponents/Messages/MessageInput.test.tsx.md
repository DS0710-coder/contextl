# MessageInput.test.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Messages/MessageInput.test.tsx`
- **Extension:** `.tsx`
- **Size:** 7476 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[apps/web/src/components/PageComponents/Messages/MessageInput.tsx.md|apps/web/src/components/PageComponents/Messages/MessageInput.tsx]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```tsx
import type { ConversationKey } from "@meshtastic/sdk";
import {
  act,
  fireEvent,
  render,
  screen,
  waitFor,
} from "@testing-library/react";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { MessageInput, type MessageInputProps } from "./MessageInput.tsx";

vi.mock("@components/UI/Button.tsx", () => ({
  Button: vi.fn(({ type, className, children, onClick, onSubmit, ...rest }) => (
    <button
      type={type}
      className={className}
      onClick={onClick}
      onSubmit={onSubmit}
      {...rest}
    >
...
```