# sample_test.go

## Architecture Metrics
- **Path:** `metrics/sample_test.go`
- **Extension:** `.go`
- **Size:** 8344 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BenchmarkCompute1000`
- `BenchmarkCompute1000000`
- `BenchmarkExpDecaySample257`
- `BenchmarkExpDecaySample514`
- `BenchmarkExpDecaySample1028`
- `BenchmarkUniformSample257`
- `BenchmarkUniformSample514`
- `BenchmarkUniformSample1028`
- `TestExpDecaySample`
- `TestExpDecaySampleNanosecondRegression`
- `TestExpDecaySampleRescale`
- `TestExpDecaySampleSnapshot`
- `TestExpDecaySampleStatistics`
- `TestUniformSample`
- `TestUniformSampleIncludesTail`
- `TestUniformSampleSnapshot`
- `TestUniformSampleStatistics`
- `benchmarkSample`
- `testExpDecaySampleStatistics`
- `testUniformSampleStatistics`
- `TestUniformSampleConcurrentUpdateCount`
- `BenchmarkCalculatePercentiles`

## Imports (Dependencies)
- [[common/math/big.go.md|common/math/big.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"math"
	"math/rand"
	"testing"
	"time"
)

const epsilonPercentile = .00000000001

// Benchmark{Compute,Copy}{1000,1000000} demonstrate that, even for relatively
// expensive computations like Variance, the cost of copying the Sample, as
// approximated by a make and copy, is much greater than the cost of the
// computation for small samples and only slightly less for large samples.
func BenchmarkCompute1000(b *testing.B) {
	s := make([]int64, 1000)
	var sum int64
	for i := 0; i < len(s); i++ {
		s[i] = int64(i)
...
```