# writer.go

## Architecture Metrics
- **Path:** `metrics/writer.go`
- **Extension:** `.go`
- **Size:** 3673 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `namedMetric`
- `Write`
- `WriteOnce`
- `cmp`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"fmt"
	"io"
	"slices"
	"strings"
	"time"
)

// Write sorts writes each metric in the given registry periodically to the
// given io.Writer.
func Write(r Registry, d time.Duration, w io.Writer) {
	for range time.Tick(d) {
		WriteOnce(r, w)
	}
}

// WriteOnce sorts and writes metrics in the given registry to the given
// io.Writer.
...
```