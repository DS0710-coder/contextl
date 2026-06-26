# timer.go

## Architecture Metrics
- **Path:** `metrics/timer.go`
- **Extension:** `.go`
- **Size:** 4799 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Timer`
- `TimerSnapshot`
- `GetOrRegisterTimer`
- `NewCustomTimer`
- `NewRegisteredTimer`
- `NewTimer`
- `Snapshot`
- `Stop`
- `Time`
- `Update`
- `UpdateSince`
- `Count`
- `Max`
- `Size`
- `Mean`
- `Min`
- `Percentile`
- `Percentiles`
- `Rate1`
- `Rate5`
- `Rate15`
- `RateMean`
- `StdDev`
- `Sum`
- `Variance`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"sync"
	"time"
)

// GetOrRegisterTimer returns an existing Timer or constructs and registers a
// new Timer.
// Be sure to unregister the meter from the registry once it is of no use to
// allow for garbage collection.
func GetOrRegisterTimer(name string, r Registry) *Timer {
	if r == nil {
		r = DefaultRegistry
	}
	return r.GetOrRegister(name, func() any { return NewTimer() }).(*Timer)
}

// NewCustomTimer constructs a new Timer from a Histogram and a Meter.
// Be sure to call Stop() once the timer is of no use to allow for garbage collection.
...
```