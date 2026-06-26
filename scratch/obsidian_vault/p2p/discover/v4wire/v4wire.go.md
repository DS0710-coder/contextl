# v4wire.go

## Architecture Metrics
- **Path:** `p2p/discover/v4wire/v4wire.go`
- **Extension:** `.go`
- **Size:** 8611 bytes
- **Centrality Score:** 0.0005
- **In-Degree (Imported By):** 7
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Ping`
- `Pong`
- `Findnode`
- `Neighbors`
- `ENRRequest`
- `ENRResponse`
- `Node`
- `Endpoint`
- `Packet`
- `ID`
- `NewEndpoint`
- `Name`
- `Kind`
- `Name`
- `Kind`
- `Name`
- `Kind`
- `Name`
- `Kind`
- `Name`
- `Kind`
- `Name`
- `Kind`
- `Expired`
- `Decode`
- `Encode`
- `recoverNodeKey`
- `EncodePubkey`
- `DecodePubkey`

## Imports (Dependencies)
- [[common/math/big.go.md|common/math/big.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[node/api.go.md|node/api.go]]
- [[p2p/enr/enr.go.md|p2p/enr/enr.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
- [[cmd/devp2p/internal/v4test/discv4tests.go.md|cmd/devp2p/internal/v4test/discv4tests.go]]
- [[cmd/devp2p/internal/v4test/framework.go.md|cmd/devp2p/internal/v4test/framework.go]]
- [[p2p/discover/table_util_test.go.md|p2p/discover/table_util_test.go]]
- [[p2p/discover/v4_lookup_test.go.md|p2p/discover/v4_lookup_test.go]]
- [[p2p/discover/v4_udp.go.md|p2p/discover/v4_udp.go]]
- [[p2p/discover/v4_udp_test.go.md|p2p/discover/v4_udp_test.go]]
- [[p2p/discover/v5_udp_test.go.md|p2p/discover/v5_udp_test.go]]

## Source Code Snippet
```go
// Copyright 2020 The go-ethereum Authors
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

// Package v4wire implements the Discovery v4 Wire Protocol.
package v4wire

import (
...
```