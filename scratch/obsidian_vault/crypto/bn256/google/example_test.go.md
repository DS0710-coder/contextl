# example_test.go

## Architecture Metrics
- **Path:** `crypto/bn256/google/example_test.go`
- **Extension:** `.go`
- **Size:** 1163 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ExamplePair`

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

import (
	"crypto/rand"
)

func ExamplePair() {
	// This implements the tripartite Diffie-Hellman algorithm from "A One
	// Round Protocol for Tripartite Diffie-Hellman", A. Joux.
	// http://www.springerlink.com/content/cddc57yyva0hburb/fulltext.pdf

	// Each of three parties, a, b and c, generate a private value.
	a, _ := rand.Int(rand.Reader, Order)
	b, _ := rand.Int(rand.Reader, Order)
	c, _ := rand.Int(rand.Reader, Order)

...
```