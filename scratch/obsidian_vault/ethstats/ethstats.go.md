# ethstats.go

## Architecture Metrics
- **Path:** `ethstats/ethstats.go`
- **Extension:** `.go`
- **Size:** 25840 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 13

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `backend`
- `fullNodeBackend`
- `Service`
- `connWrapper`
- `nodeInfo`
- `authMsg`
- `blockStats`
- `txStats`
- `newPayloadStats`
- `pendStats`
- `nodeStats`
- `newConnectionWrapper`
- `WriteJSON`
- `ReadJSON`
- `Close`
- `parseEthstatsURL`
- `New`
- `Start`
- `Stop`
- `loop`
- `readLoop`
- `login`
- `report`
- `reportLatency`
- `MarshalJSON`
- `reportNewPayload`
- `reportBlock`
- `assembleBlockStats`
- `reportHistory`
- `reportPending`
- `reportStats`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/mclock/mclock.go.md|common/mclock/mclock.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[event/event.go.md|event/event.go]]
- [[log/format.go.md|log/format.go]]
- [[node/node.go.md|node/node.go]]
- [[p2p/config.go.md|p2p/config.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]

## Source Code Snippet
```go
// Copyright 2016 The go-ethereum Authors
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

// Package ethstats implements the network stats reporting service.
package ethstats

import (
...
```