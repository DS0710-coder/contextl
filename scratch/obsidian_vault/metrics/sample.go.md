# sample.go

## Architecture Metrics
- **Path:** `metrics/sample.go`
- **Extension:** `.go`
- **Size:** 10134 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Sample`
- `sampleSnapshot`
- `ExpDecaySample`
- `UniformSample`
- `expDecaySample`
- `expDecaySampleHeap`
- `newSampleSnapshotPrecalculated`
- `newSampleSnapshot`
- `Count`
- `Max`
- `Mean`
- `Min`
- `Percentile`
- `Percentiles`
- `Size`
- `StdDev`
- `Sum`
- `Values`
- `Variance`
- `NewExpDecaySample`
- `SetRand`
- `Clear`
- `Snapshot`
- `Update`
- `update`
- `SamplePercentile`
- `CalculatePercentiles`
- `SampleVariance`
- `NewUniformSample`
- `SetRand`
- `Clear`
- `Snapshot`
- `Update`
- `newExpDecaySampleHeap`
- `Clear`
- `Push`
- `Pop`
- `Size`
- `Values`
- `up`
- `down`

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
	"math/rand"
	"slices"
	"sync"
	"time"
)

const rescaleThreshold = time.Hour

// Sample maintains a statistically-significant selection of values from
// a stream.
type Sample interface {
	Snapshot() *sampleSnapshot
	Clear()
	Update(int64)
}

...
```