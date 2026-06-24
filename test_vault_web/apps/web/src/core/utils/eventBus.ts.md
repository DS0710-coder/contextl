# eventBus.ts

## Architecture Metrics
- **Path:** `apps/web/src/core/utils/eventBus.ts`
- **Extension:** `.ts`
- **Size:** 1330 bytes
- **Centrality Score:** 0.0023
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `EventMap`
- `EventName`
- `EventCallback`
- `EventBus`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/UnsafeRolesDialog/UnsafeRolesDialog.tsx.md|apps/web/src/components/Dialog/UnsafeRolesDialog/UnsafeRolesDialog.tsx]]
- [[apps/web/src/components/Dialog/UnsafeRolesDialog/useUnsafeRolesDialog.test.tsx.md|apps/web/src/components/Dialog/UnsafeRolesDialog/useUnsafeRolesDialog.test.tsx]]
- [[apps/web/src/components/Dialog/UnsafeRolesDialog/useUnsafeRolesDialog.ts.md|apps/web/src/components/Dialog/UnsafeRolesDialog/useUnsafeRolesDialog.ts]]
- [[apps/web/src/core/utils/eventBus.test.ts.md|apps/web/src/core/utils/eventBus.test.ts]]

## Source Code Snippet
```ts
export type EventMap = {
  "dialog:unsafeRoles": {
    action: "confirm" | "dismiss";
  };
};

export type EventName = keyof EventMap;
export type EventCallback<T extends EventName> = (data: EventMap[T]) => void;

class EventBus {
  private listeners: { [K in EventName]?: Array<EventCallback<K>> } = {};

  public on<T extends EventName>(
    event: T,
    callback: EventCallback<T>,
  ): () => void {
    if (!this.listeners[event]) {
      this.listeners[event] = [];
    }

...
```