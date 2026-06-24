# vitest.config.ts

## Architecture Metrics
- **Path:** `apps/web/vitest.config.ts`
- **Extension:** `.ts`
- **Size:** 1018 bytes
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
import path from "node:path";
import { fileURLToPath } from "node:url";
import react from "@vitejs/plugin-react";
import { enableMapSet } from "immer";
import { defineProject } from "vitest/config";

enableMapSet();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const pkgRoot = __dirname;
const srcDir = path.resolve(pkgRoot, "src");
const publicDir = path.resolve(pkgRoot, "public");

export default defineProject({
  plugins: [react()],
  resolve: {
    alias: {
      "@app": srcDir,
      "@public": publicDir,
...
```