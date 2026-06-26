# log.go

## Architecture Metrics
- **Path:** `metrics/log.go`
- **Extension:** `.go`
- **Size:** 3160 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Logger`
- `Log`
- `LogScaled`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"time"
)

type Logger interface {
	Printf(format string, v ...interface{})
}

func Log(r Registry, freq time.Duration, l Logger) {
	LogScaled(r, freq, time.Nanosecond, l)
}

// LogScaled outputs each metric in the given registry periodically using the given
// logger. Print timings in `scale` units (eg time.Millisecond) rather than nanos.
func LogScaled(r Registry, freq time.Duration, scale time.Duration, l Logger) {
	du := float64(scale)
	duSuffix := scale.String()[1:]

...
```