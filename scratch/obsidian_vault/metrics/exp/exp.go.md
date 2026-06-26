# exp.go

## Architecture Metrics
- **Path:** `metrics/exp/exp.go`
- **Extension:** `.go`
- **Size:** 6755 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `exp`
- `expHandler`
- `Exp`
- `ExpHandler`
- `Setup`
- `getInt`
- `getFloat`
- `getInfo`
- `publishCounter`
- `publishCounterFloat64`
- `publishGauge`
- `publishGaugeFloat64`
- `publishGaugeInfo`
- `publishHistogram`
- `publishMeter`
- `publishTimer`
- `publishResettingTimer`
- `syncToExpvar`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[log/format.go.md|log/format.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]
- [[metrics/prometheus/prometheus.go.md|metrics/prometheus/prometheus.go]]

## Imported By (Dependents)
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[internal/debug/flags.go.md|internal/debug/flags.go]]

## Source Code Snippet
```go
// Hook go-metrics into expvar
// on any /debug/metrics request, load all vars from the registry into expvar, and execute regular expvar handler

package exp

import (
	"expvar"
	"fmt"
	"net/http"
	"sync"

	"github.com/ethereum/go-ethereum/log"
	"github.com/ethereum/go-ethereum/metrics"
	"github.com/ethereum/go-ethereum/metrics/prometheus"
)

type exp struct {
	expvarLock sync.Mutex // expvar panics if you try to register the same var twice, so we must probe it safely
	registry   metrics.Registry
}
...
```