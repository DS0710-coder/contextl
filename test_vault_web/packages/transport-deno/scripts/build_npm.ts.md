# build_npm.ts

## Architecture Metrics
- **Path:** `packages/transport-deno/scripts/build_npm.ts`
- **Extension:** `.ts`
- **Size:** 837 bytes
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
import { build, emptyDir } from "@deno/dnt";

await emptyDir("./npm");

await build({
  entryPoints: ["./mod.ts"],
  outDir: "./npm",
  shims: {
    // see JS docs for overview and more options
    deno: true,
  },
  package: {
    // package.json properties
    name: "@meshtastic/transport-deno",
    version: Deno.args[0],
    description:
      "A Deno transport layer for your project, enabling seamless integration with npm.",
    license: "GPL-3.0-only",
    repository: {
      type: "git",
...
```