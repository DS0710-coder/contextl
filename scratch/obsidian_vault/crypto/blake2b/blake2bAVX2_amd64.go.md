# blake2bAVX2_amd64.go

## Architecture Metrics
- **Path:** `crypto/blake2b/blake2bAVX2_amd64.go`
- **Extension:** `.go`
- **Size:** 985 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `init`
- `fAVX2`
- `fAVX`
- `fSSE4`
- `f`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2016 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

//go:build go1.7 && amd64 && !gccgo && !appengine
// +build go1.7,amd64,!gccgo,!appengine

package blake2b

import "golang.org/x/sys/cpu"

func init() {
	useAVX2 = cpu.X86.HasAVX2
	useAVX = cpu.X86.HasAVX
	useSSE4 = cpu.X86.HasSSE41
}

//go:noescape
func fAVX2(h *[8]uint64, m *[16]uint64, c0, c1 uint64, flag uint64, rounds uint64)

...
```