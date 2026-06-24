# Messages.tsx

## Architecture Metrics
- **Path:** `apps/web/src/pages/Messages.tsx`
- **Extension:** `.tsx`
- **Size:** 11205 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 17

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NodeInfoWithUnread`
- `SelectMessageChat`

## Imports (Dependencies)
- [[apps/web/src/components/PageComponents/Channels/Channels.tsx.md|apps/web/src/components/PageComponents/Channels/Channels.tsx]]
- [[apps/web/src/components/PageComponents/Messages/ChannelChat.tsx.md|apps/web/src/components/PageComponents/Messages/ChannelChat.tsx]]
- [[apps/web/src/components/PageComponents/Messages/MessageInput.tsx.md|apps/web/src/components/PageComponents/Messages/MessageInput.tsx]]
- [[apps/web/src/components/PageLayout.tsx.md|apps/web/src/components/PageLayout.tsx]]
- [[apps/web/src/components/Sidebar.tsx.md|apps/web/src/components/Sidebar.tsx]]
- [[apps/web/src/components/UI/Avatar.tsx.md|apps/web/src/components/UI/Avatar.tsx]]
- [[apps/web/src/components/UI/Input.tsx.md|apps/web/src/components/UI/Input.tsx]]
- [[apps/web/src/components/UI/Sidebar/SidebarButton.tsx.md|apps/web/src/components/UI/Sidebar/SidebarButton.tsx]]
- [[apps/web/src/components/UI/Sidebar/SidebarSection.tsx.md|apps/web/src/components/UI/Sidebar/SidebarSection.tsx]]
- [[apps/web/src/core/hooks/useChatAsLegacyMessages.ts.md|apps/web/src/core/hooks/useChatAsLegacyMessages.ts]]
- [[apps/web/src/core/hooks/useNodesAsProto.ts.md|apps/web/src/core/hooks/useNodesAsProto.ts]]
- [[apps/web/src/core/hooks/useToast.ts.md|apps/web/src/core/hooks/useToast.ts]]
- [[apps/web/src/core/stores/index.ts.md|apps/web/src/core/stores/index.ts]]
- [[apps/web/src/core/utils/cn.ts.md|apps/web/src/core/utils/cn.ts]]
- [[apps/web/src/routes.tsx.md|apps/web/src/routes.tsx]]
- [[packages/sdk-react/mod.ts.md|packages/sdk-react/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/routes.tsx.md|apps/web/src/routes.tsx]]

## Source Code Snippet
```tsx
import { messagesWithParamsRoute } from "@app/routes.tsx";
import { ChannelChat } from "@components/PageComponents/Messages/ChannelChat.tsx";
import { MessageInput } from "@components/PageComponents/Messages/MessageInput.tsx";
import { PageLayout } from "@components/PageLayout.tsx";
import { Sidebar } from "@components/Sidebar.tsx";
import { Avatar } from "@components/UI/Avatar.tsx";
import { Input } from "@components/UI/Input.tsx";
import { SidebarButton } from "@components/UI/Sidebar/SidebarButton.tsx";
import { SidebarSection } from "@components/UI/Sidebar/SidebarSection.tsx";
import { useChatAsLegacyMessages } from "@core/hooks/useChatAsLegacyMessages.ts";
import { useNodesAsProto } from "@core/hooks/useNodesAsProto.ts";
import { useToast } from "@core/hooks/useToast.ts";
import { MessageType, useSidebar } from "@core/stores";
import { cn } from "@core/utils/cn.ts";
import { Protobuf, Types } from "@meshtastic/sdk";
import {
  useActiveClient,
  useChannels,
  useNodeErrors,
  useUnreadByKey,
...
```