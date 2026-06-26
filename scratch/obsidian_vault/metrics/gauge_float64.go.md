# gauge_float64.go

## Architecture Metrics
- **Path:** `metrics/gauge_float64.go`
- **Extension:** `.go`
- **Size:** 1386 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `GetOrRegisterGaugeFloat64`
- `Value`
- `NewGaugeFloat64`
- `NewRegisteredGaugeFloat64`
- `Snapshot`
- `Update`

## Imports (Dependencies)
- [[common/math/big.go.md|common/math/big.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"math"
	"sync/atomic"
)

// GetOrRegisterGaugeFloat64 returns an existing GaugeFloat64 or constructs and registers a
// new GaugeFloat64.
func GetOrRegisterGaugeFloat64(name string, r Registry) *GaugeFloat64 {
	if r == nil {
		r = DefaultRegistry
	}
	return r.GetOrRegister(name, func() any { return NewGaugeFloat64() }).(*GaugeFloat64)
}

// GaugeFloat64Snapshot is a read-only copy of a GaugeFloat64.
type GaugeFloat64Snapshot float64

// Value returns the value at the time the snapshot was taken.
...
```