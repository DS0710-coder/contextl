# ConfigEditor.test.ts

## Architecture Metrics
- **Path:** `apps/web/src/sdk-preview/features/config/__tests__/ConfigEditor.test.ts`
- **Extension:** `.ts`
- **Size:** 5708 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `emitter`
- `makePort`

## Imports (Dependencies)
- [[apps/web/src/sdk-preview/core/index.ts.md|apps/web/src/sdk-preview/core/index.ts]]
- [[apps/web/src/sdk-preview/features/config/domain/ConfigEditor.ts.md|apps/web/src/sdk-preview/features/config/domain/ConfigEditor.ts]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```ts
import { create } from "@bufbuild/protobuf";
import { Protobuf, Types } from "@meshtastic/core";
import { Result } from "better-result";
import { describe, expect, it } from "vitest";
import type { MeshClientPort, Subscribable } from "../../../core/index.ts";
import { ConfigEditor } from "../domain/ConfigEditor.ts";

/** Controllable in-test emitter satisfying `Subscribable<T>`. */
function emitter<T>(): Subscribable<T> & { emit: (value: T) => void } {
  const listeners = new Set<(value: T) => void>();
  return {
    subscribe(listener) {
      listeners.add(listener);
      return () => listeners.delete(listener);
    },
    emit(value) {
      for (const listener of [...listeners]) {
        listener(value);
      }
    },
...
```