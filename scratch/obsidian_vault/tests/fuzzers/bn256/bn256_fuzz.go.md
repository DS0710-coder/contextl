# bn256_fuzz.go

## Architecture Metrics
- **Path:** `tests/fuzzers/bn256/bn256_fuzz.go`
- **Extension:** `.go`
- **Size:** 6866 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `getG1Points`
- `getG2Points`
- `fuzzAdd`
- `fuzzMul`
- `fuzzPair`
- `fuzzUnmarshalG1`
- `fuzzUnmarshalG2`
- `normalizeGTToGnark`

## Imports (Dependencies)
- [[crypto/bn256/cloudflare/bn256.go.md|crypto/bn256/cloudflare/bn256.go]]
- [[crypto/bn256/gnark/g1.go.md|crypto/bn256/gnark/g1.go]]
- [[crypto/bn256/google/bn256.go.md|crypto/bn256/google/bn256.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2018 The go-ethereum Authors
// This file is part of the go-ethereum library.
//
// The go-ethereum library is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// The go-ethereum library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public License
// along with the go-ethereum library. If not, see <http://www.gnu.org/licenses/>.

package bn256

import (
	"bytes"
...
```