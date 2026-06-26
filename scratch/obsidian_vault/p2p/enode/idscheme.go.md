# idscheme.go

## Architecture Metrics
- **Path:** `p2p/enode/idscheme.go`
- **Extension:** `.go`
- **Size:** 4223 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `V4ID`
- `v4CompatID`
- `NullID`
- `SignV4`
- `Verify`
- `NodeAddr`
- `ENRKey`
- `EncodeRLP`
- `DecodeRLP`
- `ENRKey`
- `Verify`
- `signV4Compat`
- `Verify`
- `NodeAddr`
- `SignNull`

## Imports (Dependencies)
- [[common/math/big.go.md|common/math/big.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[crypto/keccak.go.md|crypto/keccak.go]]
- [[p2p/enr/enr.go.md|p2p/enr/enr.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

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

package enode

import (
	"crypto/ecdsa"
...
```