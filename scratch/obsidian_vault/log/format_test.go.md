# format_test.go

## Architecture Metrics
- **Path:** `log/format_test.go`
- **Extension:** `.go`
- **Size:** 383 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BenchmarkPrettyInt64Logfmt`
- `BenchmarkPrettyUint64Logfmt`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package log

import (
	"math/rand"
	"testing"
)

var sink []byte

func BenchmarkPrettyInt64Logfmt(b *testing.B) {
	buf := make([]byte, 100)
	b.ReportAllocs()
	for b.Loop() {
		sink = appendInt64(buf, rand.Int63())
	}
}

func BenchmarkPrettyUint64Logfmt(b *testing.B) {
	buf := make([]byte, 100)
	b.ReportAllocs()
...
```