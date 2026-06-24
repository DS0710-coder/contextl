# MessageInput.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/PageComponents/Messages/MessageInput.tsx`
- **Extension:** `.tsx`
- **Size:** 2384 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `MessageInputProps`

## Imports (Dependencies)
- [[apps/web/src/components/UI/Button.tsx.md|apps/web/src/components/UI/Button.tsx]]
- [[apps/web/src/components/UI/Input.tsx.md|apps/web/src/components/UI/Input.tsx]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/components/PageComponents/Messages/MessageInput.test.tsx.md|apps/web/src/components/PageComponents/Messages/MessageInput.test.tsx]]
- [[apps/web/src/pages/Messages.tsx.md|apps/web/src/pages/Messages.tsx]]

## Source Code Snippet
```tsx
import { Button } from "@components/UI/Button.tsx";
import { Input } from "@components/UI/Input.tsx";
import type { ConversationKey } from "@meshtastic/sdk";
import { useDraft } from "@meshtastic/sdk-react";
import { SendIcon } from "lucide-react";
import { startTransition, useState } from "react";
import { useTranslation } from "react-i18next";

export interface MessageInputProps {
  onSend: (message: string) => void;
  conversation: ConversationKey;
  maxBytes: number;
}

export const MessageInput = ({
  onSend,
  conversation,
  maxBytes,
}: MessageInputProps) => {
  const { text: persistedDraft, setText, clear } = useDraft(conversation);
...
```