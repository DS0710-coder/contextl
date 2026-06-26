# sha3.go

## Architecture Metrics
- **Path:** `crypto/keccak/sha3.go`
- **Extension:** `.go`
- **Size:** 6667 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `state`
- `BlockSize`
- `Size`
- `Reset`
- `clone`
- `permute`
- `padAndPermute`
- `Write`
- `Read`
- `Sum`
- `MarshalBinary`
- `AppendBinary`
- `UnmarshalBinary`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2014 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package keccak

import (
	"crypto/subtle"
	"encoding/binary"
	"errors"
	"unsafe"

	"golang.org/x/sys/cpu"
)

// spongeDirection indicates the direction bytes are flowing through the sponge.
type spongeDirection int

const (
	// spongeAbsorbing indicates that the sponge is absorbing input.
...
```