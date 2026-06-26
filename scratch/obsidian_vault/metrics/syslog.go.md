# syslog.go

## Architecture Metrics
- **Path:** `metrics/syslog.go`
- **Extension:** `.go`
- **Size:** 2201 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Syslog`

## Imports (Dependencies)
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
//go:build !windows
// +build !windows

package metrics

import (
	"fmt"
	"log/syslog"
	"time"
)

// Syslog outputs each metric in the given registry to syslog periodically using
// the given syslogger.
func Syslog(r Registry, d time.Duration, w *syslog.Writer) {
	for range time.Tick(d) {
		r.Each(func(name string, i interface{}) {
			switch metric := i.(type) {
			case *Counter:
				w.Info(fmt.Sprintf("counter %s: count: %d", name, metric.Snapshot().Count()))
			case *CounterFloat64:
...
```