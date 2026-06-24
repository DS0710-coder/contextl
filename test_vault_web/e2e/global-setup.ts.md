# global-setup.ts

## Architecture Metrics
- **Path:** `e2e/global-setup.ts`
- **Extension:** `.ts`
- **Size:** 3223 bytes
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
import { execSync } from "node:child_process";
import { request } from "node:https";
import { Socket } from "node:net";

/**
 * Brings up the device topology and waits until it is reachable.
 *
 * - docker mode (default): starts the two `meshtasticd` sim nodes via compose.
 * - hardware mode (E2E_DEVICE_MODE=hardware): skips compose; expects the env
 *   endpoints to point at real devices.
 */
const MODE = process.env.E2E_DEVICE_MODE ?? "docker";
const COMPOSE_FILE = "e2e/device/docker-compose.yml";
const NODE_A_URL = process.env.E2E_NODE_A_URL ?? "https://127.0.0.1:9443";
const PEER_HOST = process.env.E2E_PEER_HOST ?? "127.0.0.1";
const PEER_PORT = Number(process.env.E2E_PEER_PORT ?? 14404);

const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

/** Poll the device HTTPS phone API until it answers (cert is self-signed). */
...
```