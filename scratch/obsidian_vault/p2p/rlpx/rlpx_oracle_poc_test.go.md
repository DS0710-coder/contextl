# rlpx_oracle_poc_test.go

## Architecture Metrics
- **Path:** `p2p/rlpx/rlpx_oracle_poc_test.go`
- **Extension:** `.go`
- **Size:** 1272 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TestHandshakeECIESInvalidCurveOracle`

## Imports (Dependencies)
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[crypto/ecies/ecies.go.md|crypto/ecies/ecies.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package rlpx

import (
	"bytes"
	"errors"
	"testing"

	"github.com/ethereum/go-ethereum/crypto"
	"github.com/ethereum/go-ethereum/crypto/ecies"
)

func TestHandshakeECIESInvalidCurveOracle(t *testing.T) {
	initKey, err := crypto.GenerateKey()
	if err != nil {
		t.Fatal(err)
	}
	respKey, err := crypto.GenerateKey()
	if err != nil {
		t.Fatal(err)
	}
...
```