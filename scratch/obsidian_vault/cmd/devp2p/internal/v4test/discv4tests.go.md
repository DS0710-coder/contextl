# discv4tests.go

## Architecture Metrics
- **Path:** `cmd/devp2p/internal/v4test/discv4tests.go`
- **Extension:** `.go`
- **Size:** 16305 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `pingWithJunk`
- `pingWrongType`
- `Name`
- `Kind`
- `Name`
- `Kind`
- `futureExpiration`
- `BasicPing`
- `checkPingPong`
- `checkPong`
- `PingWrongTo`
- `PingWrongFrom`
- `PingExtraData`
- `PingExtraDataWrongFrom`
- `PingPastExpiration`
- `WrongPacketType`
- `BondThenPingWithWrongFrom`
- `FindnodeWithoutEndpointProof`
- `BasicFindnode`
- `UnsolicitedNeighbors`
- `FindnodePastExpiration`
- `bond`
- `FindnodeAmplificationInvalidPongHash`
- `FindnodeAmplificationWrongIP`
- `ENRRequest`

## Imports (Dependencies)
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[internal/utesting/utesting.go.md|internal/utesting/utesting.go]]
- [[node/api.go.md|node/api.go]]
- [[p2p/discover/v4wire/v4wire.go.md|p2p/discover/v4wire/v4wire.go]]

## Imported By (Dependents)
- [[cmd/devp2p/discv4cmd.go.md|cmd/devp2p/discv4cmd.go]]
- [[cmd/devp2p/runtest.go.md|cmd/devp2p/runtest.go]]

## Source Code Snippet
```go
// Copyright 2020 The go-ethereum Authors
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

package v4test

import (
	"bytes"
...
```