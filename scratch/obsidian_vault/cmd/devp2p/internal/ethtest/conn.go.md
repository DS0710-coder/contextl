# conn.go

## Architecture Metrics
- **Path:** `cmd/devp2p/internal/ethtest/conn.go`
- **Extension:** `.go`
- **Size:** 12210 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Conn`
- `dial`
- `dialAs`
- `dialSnap`
- `dialSnap2`
- `Read`
- `ReadMsg`
- `Write`
- `ReadEth`
- `ReadSnap`
- `dialAndPeer`
- `peer`
- `handshake`
- `negotiateEthProtocol`
- `statusExchange`

## Imports (Dependencies)
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[eth/protocols/snap/bal_apply.go.md|eth/protocols/snap/bal_apply.go]]
- [[p2p/config.go.md|p2p/config.go]]
- [[p2p/rlpx/rlpx.go.md|p2p/rlpx/rlpx.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2023 The go-ethereum Authors
// This file is part of go-ethereum.
//
// go-ethereum is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// go-ethereum is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with go-ethereum. If not, see <http://www.gnu.org/licenses/>.

package ethtest

import (
	"crypto/ecdsa"
...
```