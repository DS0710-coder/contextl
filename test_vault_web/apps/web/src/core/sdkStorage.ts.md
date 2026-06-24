# sdkStorage.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/sdkStorage.ts`
- **Extension:** `.ts`
- **Size:** 1438 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `SqlocalDb`
- `getStorageDb`

## Imports (Dependencies)
- [[packages/sdk-storage-sqlocal/mod.ts.md|packages/sdk-storage-sqlocal/mod.ts]]
- [[packages/sdk/mod.ts.md|packages/sdk/mod.ts]]

## Imported By (Dependents)
- [[apps/web/src/core/connections/sdkClient.ts.md|apps/web/src/core/connections/sdkClient.ts]]

## Source Code Snippet
```ts
import { createLogger } from "@meshtastic/sdk";
import {
  createSqlocalDb,
  MultiTabCoordinator,
  type SqlocalDb,
} from "@meshtastic/sdk-storage-sqlocal";

const log = createLogger("sdkStorage");

/**
 * Lazy singletons for the chat (and future nodes/telemetry) persistence layer.
 *
 * `getStorageDb()` opens the OPFS-backed SQLite database on first call and
 * returns the same Drizzle client on subsequent calls. `coordinator` is a
 * shared `MultiTabCoordinator` for cross-tab change broadcasts.
 *
 * The database is opened only when a feature actually needs it; importing
 * this module is side-effect-free so unit tests that don't touch storage
 * stay fast and headless-safe.
 */
...
```