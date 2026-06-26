# register.go

## Architecture Metrics
- **Path:** `crypto/blake2b/register.go`
- **Extension:** `.go`
- **Size:** 628 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `init`

## Imports (Dependencies)
- [[crypto/crypto.go.md|crypto/crypto.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2017 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

//go:build go1.9
// +build go1.9

package blake2b

import (
	"crypto"
	"hash"
)

func init() {
	newHash256 := func() hash.Hash {
		h, _ := New256(nil)
		return h
	}
	newHash384 := func() hash.Hash {
...
```