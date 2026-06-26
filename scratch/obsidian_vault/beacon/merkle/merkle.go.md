# merkle.go

## Architecture Metrics
- **Path:** `beacon/merkle/merkle.go`
- **Extension:** `.go`
- **Size:** 2124 bytes
- **Centrality Score:** 0.0006
- **In-Degree (Imported By):** 6
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `UnmarshalJSON`
- `VerifyProof`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]

## Imported By (Dependents)
- [[beacon/light/api/light_api.go.md|beacon/light/api/light_api.go]]
- [[beacon/light/test_helpers.go.md|beacon/light/test_helpers.go]]
- [[beacon/params/config.go.md|beacon/params/config.go]]
- [[beacon/types/exec_header.go.md|beacon/types/exec_header.go]]
- [[beacon/types/header.go.md|beacon/types/header.go]]
- [[beacon/types/light_sync.go.md|beacon/types/light_sync.go]]

## Source Code Snippet
```go
// Copyright 2022 The go-ethereum Authors
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

// Package merkle implements proof verifications in binary merkle trees.
package merkle

import (
...
```