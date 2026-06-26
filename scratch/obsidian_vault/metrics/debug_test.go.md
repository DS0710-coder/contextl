# debug_test.go

## Architecture Metrics
- **Path:** `metrics/debug_test.go`
- **Extension:** `.go`
- **Size:** 849 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BenchmarkDebugGCStats`
- `TestDebugGCStatsBlocking`
- `testDebugGCStatsBlocking`

## Imports (Dependencies)
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[internal/debug/api.go.md|internal/debug/api.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"runtime"
	"runtime/debug"
	"testing"
	"time"
)

func BenchmarkDebugGCStats(b *testing.B) {
	r := NewRegistry()
	RegisterDebugGCStats(r)
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		CaptureDebugGCStatsOnce(r)
	}
}

func TestDebugGCStatsBlocking(t *testing.T) {
	if g := runtime.GOMAXPROCS(0); g < 2 {
...
```