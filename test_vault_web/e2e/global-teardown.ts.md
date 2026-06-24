# global-teardown.ts

## Architecture Metrics
- **Path:** `e2e/global-teardown.ts`
- **Extension:** `.ts`
- **Size:** 966 bytes
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

/**
 * Tears the mesh down only on explicit request (E2E_DOCKER_DOWN=1); otherwise it
 * is left running so repeated local runs are fast and node identities are stable.
 *
 * In CI we deliberately do NOT remove the containers here — the workflow dumps
 * device logs on failure and then runs `docker compose down` as a final step, so
 * removing them in this teardown would race (and discard) that log capture.
 */
const MODE = process.env.E2E_DEVICE_MODE ?? "docker";
const COMPOSE_FILE = "e2e/device/docker-compose.yml";

export default async function globalTeardown(): Promise<void> {
  if (MODE !== "docker") return;
  if (process.env.E2E_DOCKER_DOWN === "1") {
    console.log("[e2e] tearing down meshtasticd mesh ...");
    execSync(`docker compose -f ${COMPOSE_FILE} down -v`, { stdio: "inherit" });
  } else {
    console.log("[e2e] leaving meshtasticd mesh running (set E2E_DOCKER_DOWN=1 to stop).");
...
```