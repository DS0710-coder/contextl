# bitutil.go

## Architecture Metrics
- **Path:** `common/bitutil/bitutil.go`
- **Extension:** `.go`
- **Size:** 3882 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 5
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `XORBytes`
- `ANDBytes`
- `fastANDBytes`
- `safeANDBytes`
- `ORBytes`
- `fastORBytes`
- `safeORBytes`
- `TestBytes`
- `fastTestBytes`
- `safeTestBytes`

## Imports (Dependencies)
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]

## Imported By (Dependents)
- [[core/types/bloom9.go.md|core/types/bloom9.go]]
- [[core/vm/contracts.go.md|core/vm/contracts.go]]
- [[crypto/bn256/gnark/g1.go.md|crypto/bn256/gnark/g1.go]]
- [[crypto/bn256/gnark/g2.go.md|crypto/bn256/gnark/g2.go]]
- [[p2p/transport.go.md|p2p/transport.go]]

## Source Code Snippet
```go
// Copyright 2013 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Adapted from: https://go.dev/src/crypto/subtle/xor_generic.go

// Package bitutil implements fast bitwise operations.
package bitutil

import (
	"crypto/subtle"
	"runtime"
	"unsafe"
)

const wordSize = int(unsafe.Sizeof(uintptr(0)))
const supportsUnaligned = runtime.GOARCH == "386" || runtime.GOARCH == "amd64" || runtime.GOARCH == "ppc64" || runtime.GOARCH == "ppc64le" || runtime.GOARCH == "s390x"

// XORBytes xors the bytes in a and b. The destination is assumed to have enough
// space. Returns the number of bytes xor'd.
...
```