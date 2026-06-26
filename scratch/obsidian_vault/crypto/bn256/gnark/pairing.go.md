# pairing.go

## Architecture Metrics
- **Path:** `crypto/bn256/gnark/pairing.go`
- **Extension:** `.go`
- **Size:** 2040 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PairingCheck`
- `getInnerG1s`
- `getInnerG2s`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package bn256

import (
	"github.com/consensys/gnark-crypto/ecc/bn254"
)

// PairingCheck computes the following relation: ∏ᵢ e(Pᵢ, Qᵢ) =? 1
//
// To explain why gnark returns a (bool, error):
//
//   - If the function `e` does not return a result then internally
//     an error is returned.
//   - If `e` returns a result, then error will be nil,
//     but if this value is not `1` then the boolean value will be false
//
// We therefore check for an error, and return false if its non-nil and
// then return the value of the boolean if not.
func PairingCheck(a_ []*G1, b_ []*G2) bool {
	a := getInnerG1s(a_)
	b := getInnerG2s(b_)
...
```