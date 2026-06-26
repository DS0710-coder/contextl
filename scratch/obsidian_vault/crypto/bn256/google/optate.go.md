# optate.go

## Architecture Metrics
- **Path:** `crypto/bn256/google/optate.go`
- **Extension:** `.go`
- **Size:** 8673 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `lineFunctionAdd`
- `lineFunctionDouble`
- `mulLine`
- `miller`
- `finalExponentiation`
- `optimalAte`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2012 The Go Authors. All rights reserved.
// Use of this source code is governed by a BSD-style
// license that can be found in the LICENSE file.

package bn256

func lineFunctionAdd(r, p *twistPoint, q *curvePoint, r2 *gfP2, pool *bnPool) (a, b, c *gfP2, rOut *twistPoint) {
	// See the mixed addition algorithm from "Faster Computation of the
	// Tate Pairing", http://arxiv.org/pdf/0904.0854v3.pdf

	B := newGFp2(pool).Mul(p.x, r.t, pool)

	D := newGFp2(pool).Add(p.y, r.z)
	D.Square(D, pool)
	D.Sub(D, r2)
	D.Sub(D, r.t)
	D.Mul(D, r.t, pool)

	H := newGFp2(pool).Sub(B, r.x)
	I := newGFp2(pool).Square(H, pool)
...
```