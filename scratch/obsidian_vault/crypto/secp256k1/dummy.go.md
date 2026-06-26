# dummy.go

## Architecture Metrics
- **Path:** `crypto/secp256k1/dummy.go`
- **Extension:** `.go`
- **Size:** 811 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/dummy.go.md|crypto/secp256k1/libsecp256k1/include/dummy.go]]
- [[crypto/secp256k1/libsecp256k1/src/assumptions.h.md|crypto/secp256k1/libsecp256k1/src/assumptions.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/recovery/bench_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/recovery/bench_impl.h]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
//go:build dummy
// +build dummy

// This file is part of a workaround for `go mod vendor` which won't vendor
// C files if there's no Go file in the same directory.
// This would prevent the crypto/secp256k1/libsecp256k1/include/secp256k1.h file to be vendored.
//
// This Go file imports the c directory where there is another dummy.go file which
// is the second part of this workaround.
//
// These two files combined make it so `go mod vendor` behaves correctly.
//
// See this issue for reference: https://github.com/golang/go/issues/26366

package secp256k1

import (
	_ "github.com/ethereum/go-ethereum/crypto/secp256k1/libsecp256k1/include"
	_ "github.com/ethereum/go-ethereum/crypto/secp256k1/libsecp256k1/src"
	_ "github.com/ethereum/go-ethereum/crypto/secp256k1/libsecp256k1/src/modules/recovery"
...
```