# forkid.go

## Architecture Metrics
- **Path:** `core/forkid/forkid.go`
- **Extension:** `.go`
- **Size:** 11242 bytes
- **Centrality Score:** 0.0005
- **In-Degree (Imported By):** 7
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Blockchain`
- `ID`
- `NewID`
- `NewIDWithChain`
- `NewFilter`
- `NewStaticFilter`
- `newFilter`
- `checksumUpdate`
- `checksumToBytes`
- `gatherForks`

## Imports (Dependencies)
- [[common/math/big.go.md|common/math/big.go]]
- [[core/types.go.md|core/types.go]]
- [[log/format.go.md|log/format.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
- [[cmd/devp2p/internal/ethtest/chain.go.md|cmd/devp2p/internal/ethtest/chain.go]]
- [[cmd/devp2p/nodesetcmd.go.md|cmd/devp2p/nodesetcmd.go]]
- [[eth/protocols/eth/discovery.go.md|eth/protocols/eth/discovery.go]]
- [[eth/protocols/eth/handshake.go.md|eth/protocols/eth/handshake.go]]
- [[eth/protocols/eth/handshake_test.go.md|eth/protocols/eth/handshake_test.go]]
- [[eth/protocols/eth/protocol.go.md|eth/protocols/eth/protocol.go]]
- [[internal/ethapi/api.go.md|internal/ethapi/api.go]]

## Source Code Snippet
```go
// Copyright 2019 The go-ethereum Authors
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

// Package forkid implements EIP-2124 (https://eips.ethereum.org/EIPS/eip-2124).
package forkid

import (
...
```