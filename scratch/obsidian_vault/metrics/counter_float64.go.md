# counter_float64.go

## Architecture Metrics
- **Path:** `metrics/counter_float64.go`
- **Extension:** `.go`
- **Size:** 1919 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `GetOrRegisterCounterFloat64`
- `NewCounterFloat64`
- `NewRegisteredCounterFloat64`
- `Count`
- `Clear`
- `Dec`
- `Inc`
- `Snapshot`
- `atomicAddFloat`

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

// GetOrRegisterCounterFloat64 returns an existing *CounterFloat64 or constructs and registers
// a new CounterFloat64.
func GetOrRegisterCounterFloat64(name string, r Registry) *CounterFloat64 {
	if r == nil {
		r = DefaultRegistry
	}
	return r.GetOrRegister(name, func() any { return NewCounterFloat64() }).(*CounterFloat64)
}

// NewCounterFloat64 constructs a new CounterFloat64.
func NewCounterFloat64() *CounterFloat64 {
	return new(CounterFloat64)
}
...
```