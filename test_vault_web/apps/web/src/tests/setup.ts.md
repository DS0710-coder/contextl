# setup.ts

## Architecture Metrics
- **Path:** `apps/web/src/tests/setup.ts`
- **Extension:** `.ts`
- **Size:** 2356 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { cleanup } from "@testing-library/react";
import { enableMapSet } from "immer";
import { afterEach, vi } from "vitest";
import "@testing-library/jest-dom";
import "@testing-library/user-event";
import channelsEN from "@public/i18n/locales/en/channels.json" with { type: "json" };
import commandPaletteEN from "@public/i18n/locales/en/commandPalette.json" with { type: "json" };
import commonEN from "@public/i18n/locales/en/common.json" with { type: "json" };
import configEN from "@public/i18n/locales/en/config.json" with { type: "json" };
import connectionsEN from "@public/i18n/locales/en/connections.json" with { type: "json" };
import dialogEN from "@public/i18n/locales/en/dialog.json" with { type: "json" };
import messagesEN from "@public/i18n/locales/en/messages.json" with { type: "json" };
import moduleConfigEN from "@public/i18n/locales/en/moduleConfig.json" with { type: "json" };
import nodesEN from "@public/i18n/locales/en/nodes.json" with { type: "json" };
import uiEN from "@public/i18n/locales/en/ui.json" with { type: "json" };
import i18n from "i18next";
import { initReactI18next } from "react-i18next";

enableMapSet();

...
```