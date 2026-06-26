# gauge.go

## Architecture Metrics
- **Path:** `metrics/gauge.go`
- **Extension:** `.go`
- **Size:** 1641 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Value`
- `GetOrRegisterGauge`
- `NewGauge`
- `NewRegisteredGauge`
- `Snapshot`
- `Update`
- `UpdateIfGt`
- `Dec`
- `Inc`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import "sync/atomic"

// GaugeSnapshot is a read-only copy of a Gauge.
type GaugeSnapshot int64

// Value returns the value at the time the snapshot was taken.
func (g GaugeSnapshot) Value() int64 { return int64(g) }

// GetOrRegisterGauge returns an existing Gauge or constructs and registers a
// new Gauge.
func GetOrRegisterGauge(name string, r Registry) *Gauge {
	if r == nil {
		r = DefaultRegistry
	}
	return r.GetOrRegister(name, func() any { return NewGauge() }).(*Gauge)
}

// NewGauge constructs a new Gauge.
...
```