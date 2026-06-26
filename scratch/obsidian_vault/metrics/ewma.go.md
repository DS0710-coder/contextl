# ewma.go

## Architecture Metrics
- **Path:** `metrics/ewma.go`
- **Extension:** `.go`
- **Size:** 2605 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `EWMA`
- `Rate`
- `NewEWMA`
- `NewEWMA1`
- `NewEWMA5`
- `NewEWMA15`
- `Snapshot`
- `tick`
- `fetchInstantRate`
- `updateRate`
- `Update`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/math/big.go.md|common/math/big.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"math"
	"sync"
	"sync/atomic"
	"time"
)

// EWMASnapshot is a read-only copy of an EWMA.
type EWMASnapshot float64

// Rate returns the rate of events per second at the time the snapshot was
// taken.
func (a EWMASnapshot) Rate() float64 { return float64(a) }

// NewEWMA constructs a new EWMA with the given alpha.
func NewEWMA(alpha float64) *EWMA {
	return &EWMA{alpha: alpha}
}
...
```