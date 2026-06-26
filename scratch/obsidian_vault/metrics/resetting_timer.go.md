# resetting_timer.go

## Architecture Metrics
- **Path:** `metrics/resetting_timer.go`
- **Extension:** `.go`
- **Size:** 3480 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ResettingTimer`
- `ResettingTimerSnapshot`
- `GetOrRegisterResettingTimer`
- `NewRegisteredResettingTimer`
- `NewResettingTimer`
- `Snapshot`
- `Time`
- `Update`
- `UpdateSince`
- `Count`
- `Percentiles`
- `Mean`
- `Max`
- `Min`
- `calc`

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

// GetOrRegisterResettingTimer returns an existing ResettingTimer or constructs and registers a
// new ResettingTimer.
func GetOrRegisterResettingTimer(name string, r Registry) *ResettingTimer {
	if r == nil {
		r = DefaultRegistry
	}
	return r.GetOrRegister(name, func() any { return NewResettingTimer() }).(*ResettingTimer)
}

// NewRegisteredResettingTimer constructs and registers a new ResettingTimer.
func NewRegisteredResettingTimer(name string, r Registry) *ResettingTimer {
	c := NewResettingTimer()
	if nil == r {
...
```