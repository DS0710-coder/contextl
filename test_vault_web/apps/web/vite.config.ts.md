# vite.config.ts

## Architecture Metrics
- **Path:** `apps/web/vite.config.ts`
- **Extension:** `.ts`
- **Size:** 3246 bytes
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
import path from "node:path";
import process from "node:process";
import tailwindcss from "@tailwindcss/vite";
import basicSsl from "@vitejs/plugin-basic-ssl";
import react from "@vitejs/plugin-react";
import { defineConfig, loadEnv } from "vite";
import { createHtmlPlugin } from "vite-plugin-html";
import { VitePWA } from "vite-plugin-pwa";

let hash = "";
let version = "v0.0.0";
try {
  hash = execSync("git rev-parse --short HEAD", { encoding: "utf8" }).trim();
} catch (error) {
  console.error("Error getting git hash:", error);
  hash = "DEV";
}

try {
...
```