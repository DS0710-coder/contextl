# native_format_test.go

## Architecture Metrics
- **Path:** `crypto/bn256/gnark/native_format_test.go`
- **Extension:** `.go`
- **Size:** 937 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TestNativeGnarkFormatIncompatibility`
- `TestSerRoundTrip`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package bn256

import (
	"testing"

	"github.com/consensys/gnark-crypto/ecc/bn254"
)

func TestNativeGnarkFormatIncompatibility(t *testing.T) {
	// Use official gnark serialization
	_, _, g1Gen, _ := bn254.Generators()
	wrongSer := g1Gen.Bytes()

	var evmG1 G1
	_, err := evmG1.Unmarshal(wrongSer[:])
	if err == nil {
		t.Fatalf("points serialized using the official bn254 serialization algorithm, should not work with the evm format")
	}
}

...
```