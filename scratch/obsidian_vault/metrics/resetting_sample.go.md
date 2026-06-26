# resetting_sample.go

## Architecture Metrics
- **Path:** `metrics/resetting_sample.go`
- **Extension:** `.go`
- **Size:** 725 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `resettingSample`
- `ResettingSample`
- `Snapshot`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

// ResettingSample converts an ordinary sample into one that resets whenever its
// snapshot is retrieved. This will break for multi-monitor systems, but when only
// a single metric is being pushed out, this ensure that low-frequency events don't
// skew th charts indefinitely.
func ResettingSample(sample Sample) Sample {
	return &resettingSample{
		Sample: sample,
	}
}

// resettingSample is a simple wrapper around a sample that resets it upon the
// snapshot retrieval.
type resettingSample struct {
	Sample
}

// Snapshot returns a read-only copy of the sample with the original reset.
func (rs *resettingSample) Snapshot() *sampleSnapshot {
...
```