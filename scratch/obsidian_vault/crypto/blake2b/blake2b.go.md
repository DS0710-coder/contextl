# blake2b.go

## Architecture Metrics
- **Path:** `crypto/blake2b/blake2b.go`
- **Extension:** `.go`
- **Size:** 8238 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `digest`
- `Sum512`
- `Sum384`
- `Sum256`
- `New512`
- `New384`
- `New256`
- `New`
- `F`
- `newDigest`
- `checkSum`
- `hashBlocks`
- `MarshalBinary`
- `UnmarshalBinary`
- `BlockSize`
- `Size`
- `Reset`
- `Write`
- `Sum`
- `finalize`
- `appendUint64`
- `appendUint32`
- `consumeUint64`
- `consumeUint32`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[core/vm/contracts.go.md|core/vm/contracts.go]]

## Source Code Snippet
```go
// Copyright 2016 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

// Package blake2b implements the BLAKE2b hash algorithm defined by RFC 7693
// and the extendable output function (XOF) BLAKE2Xb.
//
// For a detailed specification of BLAKE2b see https://blake2.net/blake2.pdf
// and for BLAKE2Xb see https://blake2.net/blake2x.pdf
//
// If you aren't sure which function you need, use BLAKE2b (Sum512 or New512).
// If you need a secret-key MAC (message authentication code), use the New512
// function with a non-nil key.
//
// BLAKE2X is a construction to compute hash values larger than 64 bytes. It
// can produce hash values between 0 and 4 GiB.
package blake2b

import (
	"encoding/binary"
...
```