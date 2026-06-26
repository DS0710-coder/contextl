# runtimehistogram.go

## Architecture Metrics
- **Path:** `metrics/runtimehistogram.go`
- **Extension:** `.go`
- **Size:** 7850 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `runtimeHistogram`
- `runtimeHistogramSnapshot`
- `floatsAscendingKeepingIndex`
- `floatsByIndex`
- `getOrRegisterRuntimeHistogram`
- `newRuntimeHistogram`
- `RuntimeHistogramFromData`
- `update`
- `Clear`
- `Update`
- `Snapshot`
- `newRuntimeHistogramSnapshot`
- `calc`
- `Count`
- `Size`
- `Mean`
- `midpoint`
- `StdDev`
- `Variance`
- `Percentile`
- `Percentiles`
- `computePercentiles`
- `Max`
- `Min`
- `Sum`
- `Len`
- `Less`
- `Swap`
- `Len`
- `Less`
- `Swap`

## Imports (Dependencies)
- [[common/math/big.go.md|common/math/big.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"math"
	"runtime/metrics"
	"sort"
	"sync/atomic"
)

func getOrRegisterRuntimeHistogram(name string, scale float64, r Registry) *runtimeHistogram {
	if r == nil {
		r = DefaultRegistry
	}
	return r.GetOrRegister(name, func() any { return newRuntimeHistogram(scale) }).(*runtimeHistogram)
}

// runtimeHistogram wraps a runtime/metrics histogram.
type runtimeHistogram struct {
	v           atomic.Pointer[metrics.Float64Histogram]
	scaleFactor float64
...
```