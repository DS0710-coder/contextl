# meter.go

## Architecture Metrics
- **Path:** `metrics/meter.go`
- **Extension:** `.go`
- **Size:** 4575 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `MeterSnapshot`
- `Meter`
- `meterTicker`
- `GetOrRegisterMeter`
- `NewMeter`
- `NewInactiveMeter`
- `NewRegisteredMeter`
- `Count`
- `Rate1`
- `Rate5`
- `Rate15`
- `RateMean`
- `newMeter`
- `Stop`
- `Mark`
- `Snapshot`
- `tick`
- `add`
- `remove`
- `loop`
- `startMeterTickerLoop`

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

// GetOrRegisterMeter returns an existing Meter or constructs and registers a
// new Meter.
// Be sure to unregister the meter from the registry once it is of no use to
// allow for garbage collection.
func GetOrRegisterMeter(name string, r Registry) *Meter {
	if r == nil {
		r = DefaultRegistry
	}
	return r.GetOrRegister(name, func() any { return NewMeter() }).(*Meter)
}

...
```