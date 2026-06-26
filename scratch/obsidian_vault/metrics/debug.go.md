# debug.go

## Architecture Metrics
- **Path:** `metrics/debug.go`
- **Extension:** `.go`
- **Size:** 2691 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `CaptureDebugGCStats`
- `CaptureDebugGCStatsOnce`
- `RegisterDebugGCStats`
- `init`

## Imports (Dependencies)
- [[internal/debug/api.go.md|internal/debug/api.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"runtime/debug"
	"time"
)

var (
	debugMetrics struct {
		GCStats struct {
			LastGC *Gauge
			NumGC  *Gauge
			Pause  Histogram
			//PauseQuantiles Histogram
			PauseTotal *Gauge
		}
		ReadGCStats *Timer
	}
	gcStats debug.GCStats
)
...
```