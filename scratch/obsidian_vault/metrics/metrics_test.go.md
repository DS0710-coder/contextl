# metrics_test.go

## Architecture Metrics
- **Path:** `metrics/metrics_test.go`
- **Extension:** `.go`
- **Size:** 1203 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TestReadRuntimeValues`
- `BenchmarkMetrics`
- `Example`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"fmt"
	"sync"
	"testing"
	"time"
)

func TestReadRuntimeValues(t *testing.T) {
	var v runtimeStats
	readRuntimeStats(&v)
	t.Logf("%+v", v)
}

func BenchmarkMetrics(b *testing.B) {
	var (
		r  = NewRegistry()
		c  = NewRegisteredCounter("counter", r)
		cf = NewRegisteredCounterFloat64("counterfloat64", r)
...
```