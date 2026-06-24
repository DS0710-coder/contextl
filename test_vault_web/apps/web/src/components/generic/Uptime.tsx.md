# Uptime.tsx

## Architecture Metrics
- **Path:** `apps/web/src/components/generic/Uptime.tsx`
- **Extension:** `.tsx`
- **Size:** 494 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `UptimeProps`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx.md|apps/web/src/components/Dialog/NodeDetailsDialog/NodeDetailsDialog.tsx]]

## Source Code Snippet
```tsx
export interface UptimeProps {
  seconds: number;
}

const getUptime = (seconds: number): string => {
  const days = Math.floor(seconds / 86400);
  const hours = Math.floor((seconds % 86400) / 3600);
  const minutes = Math.floor(((seconds % 86400) % 3600) / 60);
  const secondsLeft = Math.floor(((seconds % 86400) % 3600) % 60);
  return `${days}d ${hours}h ${minutes}m ${secondsLeft}s`;
};

export const Uptime = ({ seconds }: UptimeProps) => {
  return <span>{getUptime(seconds)}</span>;
};
```