# gfp.go

## Architecture Metrics
- **Path:** `crypto/bn256/cloudflare/gfp.go`
- **Extension:** `.go`
- **Size:** 1563 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `newGFp`
- `String`
- `Set`
- `Invert`
- `Marshal`
- `Unmarshal`
- `montEncode`
- `montDecode`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package bn256

import (
	"errors"
	"fmt"
)

type gfP [4]uint64

func newGFp(x int64) (out *gfP) {
	if x >= 0 {
		out = &gfP{uint64(x)}
	} else {
		out = &gfP{uint64(-x)}
		gfpNeg(out, out)
	}

	montEncode(out, out)
	return out
}
...
```