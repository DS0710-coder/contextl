# collapsible.tsx

## Architecture Metrics
- **Path:** `packages/ui/src/components/ui/collapsible.tsx`
- **Extension:** `.tsx`
- **Size:** 791 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Collapsible`
- `CollapsibleTrigger`
- `CollapsibleContent`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[packages/ui/src/lib/components/Sidebar/AppSidebar.tsx.md|packages/ui/src/lib/components/Sidebar/AppSidebar.tsx]]

## Source Code Snippet
```tsx
import * as CollapsiblePrimitive from "@radix-ui/react-collapsible";

function Collapsible({
  ...props
}: React.ComponentProps<typeof CollapsiblePrimitive.Root>) {
  return <CollapsiblePrimitive.Root data-slot="collapsible" {...props} />;
}

function CollapsibleTrigger({
  ...props
}: React.ComponentProps<typeof CollapsiblePrimitive.CollapsibleTrigger>) {
  return (
    <CollapsiblePrimitive.CollapsibleTrigger
      data-slot="collapsible-trigger"
      {...props}
    />
  );
}

function CollapsibleContent({
...
```