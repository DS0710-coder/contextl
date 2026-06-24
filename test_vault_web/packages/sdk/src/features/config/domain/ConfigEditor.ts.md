# ConfigEditor.ts

## Architecture Metrics
- **Path:** `packages/sdk/src/features/config/domain/ConfigEditor.ts`
- **Extension:** `.ts`
- **Size:** 14838 bytes
- **Centrality Score:** 0.0016
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 10

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ReadonlySignal`
- `ConfigEditor`
- `buildRadioConfig`
- `buildModuleConfig`
- `shallowEqual`

## Imports (Dependencies)
- [[packages/sdk/src/core/client/MeshClient.ts.md|packages/sdk/src/core/client/MeshClient.ts]]
- [[packages/sdk/src/core/signals/createStore.ts.md|packages/sdk/src/core/signals/createStore.ts]]
- [[packages/sdk/src/features/channels/application/ChannelUseCases.ts.md|packages/sdk/src/features/channels/application/ChannelUseCases.ts]]
- [[packages/sdk/src/features/config/application/ConfigUseCases.ts.md|packages/sdk/src/features/config/application/ConfigUseCases.ts]]
- [[packages/sdk/src/features/config/domain/ModuleConfig.ts.md|packages/sdk/src/features/config/domain/ModuleConfig.ts]]
- [[packages/sdk/src/features/config/domain/RadioConfig.ts.md|packages/sdk/src/features/config/domain/RadioConfig.ts]]
- [[packages/sdk/src/features/config/infrastructure/ConfigMapper.ts.md|packages/sdk/src/features/config/infrastructure/ConfigMapper.ts]]
- [[packages/sdk/src/features/device/domain/DeviceStatus.ts.md|packages/sdk/src/features/device/domain/DeviceStatus.ts]]
- [[packages/sdk/src/features/device/infrastructure/AdminMessageSender.ts.md|packages/sdk/src/features/device/infrastructure/AdminMessageSender.ts]]
- [[packages/sdk/src/features/nodes/application/SetOwnerUseCase.ts.md|packages/sdk/src/features/nodes/application/SetOwnerUseCase.ts]]

## Imported By (Dependents)
- [[packages/sdk/src/features/config/ConfigClient.ts.md|packages/sdk/src/features/config/ConfigClient.ts]]
- [[packages/sdk/src/features/config/index.ts.md|packages/sdk/src/features/config/index.ts]]

## Source Code Snippet
```ts
import { create } from "@bufbuild/protobuf";
import * as Protobuf from "@meshtastic/protobufs";
import { signal } from "@preact/signals-core";
import { Result } from "better-result";
import type { ResultType } from "better-result";
import type { MeshClient } from "../../../core/client/MeshClient.ts";
import {
  type ReadonlySignal,
  toReadonly,
} from "../../../core/signals/createStore.ts";
import { setChannel } from "../../channels/application/ChannelUseCases.ts";
import { DeviceStatusEnum } from "../../device/domain/DeviceStatus.ts";
import { sendAdminMessage } from "../../device/infrastructure/AdminMessageSender.ts";
import { setOwner } from "../../nodes/application/SetOwnerUseCase.ts";
import {
  beginEditSettings,
  commitEditSettings,
  setConfig,
  setModuleConfig,
} from "../application/ConfigUseCases.ts";
...
```