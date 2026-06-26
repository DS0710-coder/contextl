# counter.go

## Architecture Metrics
- **Path:** `metrics/counter.go`
- **Extension:** `.go`
- **Size:** 1416 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `GetOrRegisterCounter`
- `NewCounter`
- `NewRegisteredCounter`
- `Count`
- `Clear`
- `Dec`
- `Inc`
- `Snapshot`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"sync/atomic"
)

// GetOrRegisterCounter returns an existing Counter or constructs and registers
// a new Counter.
func GetOrRegisterCounter(name string, r Registry) *Counter {
	if r == nil {
		r = DefaultRegistry
	}
	return r.GetOrRegister(name, func() any { return NewCounter() }).(*Counter)
}

// NewCounter constructs a new Counter.
func NewCounter() *Counter {
	return new(Counter)
}

...
```