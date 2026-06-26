# histogram.go

## Architecture Metrics
- **Path:** `metrics/histogram.go`
- **Extension:** `.go`
- **Size:** 1953 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `HistogramSnapshot`
- `Histogram`
- `StandardHistogram`
- `GetOrRegisterHistogram`
- `GetOrRegisterHistogramLazy`
- `NewHistogram`
- `NewRegisteredHistogram`
- `Clear`
- `Snapshot`
- `Update`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

type HistogramSnapshot interface {
	Count() int64
	Max() int64
	Mean() float64
	Min() int64
	Percentile(float64) float64
	Percentiles([]float64) []float64
	Size() int
	StdDev() float64
	Sum() int64
	Variance() float64
}

// Histogram calculates distribution statistics from a series of int64 values.
type Histogram interface {
	Clear()
	Update(int64)
	Snapshot() HistogramSnapshot
...
```