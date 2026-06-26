# gt.go

## Architecture Metrics
- **Path:** `crypto/bn256/gnark/gt.go`
- **Extension:** `.go`
- **Size:** 1625 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `GT`
- `Pair`
- `Unmarshal`
- `Marshal`
- `Exp`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package bn256

import (
	"fmt"
	"math/big"

	"github.com/consensys/gnark-crypto/ecc/bn254"
)

// GT is the affine representation of a GT field element.
//
// Note: GT is not explicitly used in mainline code.
// It is needed for fuzzing.
type GT struct {
	inner bn254.GT
}

// Pair compute the optimal Ate pairing between a G1 and
// G2 element.
//
...
```