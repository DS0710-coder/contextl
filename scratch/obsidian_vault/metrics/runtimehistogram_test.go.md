# runtimehistogram_test.go

## Architecture Metrics
- **Path:** `metrics/runtimehistogram_test.go`
- **Extension:** `.go`
- **Size:** 8822 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `runtimeHistogramTest`
- `TestRuntimeHistogramStats`
- `approxEqual`
- `TestRuntimeHistogramStatsPercentileOrder`
- `BenchmarkRuntimeHistogramSnapshotRead`

## Imports (Dependencies)
- [[common/math/big.go.md|common/math/big.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"bytes"
	"encoding/gob"
	"fmt"
	"math"
	"reflect"
	"runtime/metrics"
	"testing"
	"time"
)

var _ Histogram = (*runtimeHistogram)(nil)

type runtimeHistogramTest struct {
	h metrics.Float64Histogram

	Count       int64
	Min         int64
...
```