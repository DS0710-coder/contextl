# gfp_decl.go

## Architecture Metrics
- **Path:** `crypto/bn256/cloudflare/gfp_decl.go`
- **Extension:** `.go`
- **Size:** 501 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `gfpNeg`
- `gfpAdd`
- `gfpSub`
- `gfpMul`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
//go:build (amd64 && !generic) || (arm64 && !generic)
// +build amd64,!generic arm64,!generic

package bn256

// This file contains forward declarations for the architecture-specific
// assembly implementations of these functions, provided that they exist.

import (
	"golang.org/x/sys/cpu"
)

//nolint:unused
var hasBMI2 = cpu.X86.HasBMI2

//go:noescape
func gfpNeg(c, a *gfP)

//go:noescape
func gfpAdd(c, a, b *gfP)
...
```