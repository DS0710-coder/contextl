# txpool.go

## Architecture Metrics
- **Path:** `core/txpool/txpool.go`
- **Extension:** `.go`
- **Size:** 16774 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 27
- **Out-Degree (Imports):** 8

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BlockChain`
- `TxPool`
- `New`
- `Close`
- `loop`
- `SetGasTip`
- `Has`
- `Get`
- `GetRLP`
- `GetMetadata`
- `Add`
- `Pending`
- `SubscribeTransactions`
- `PoolNonce`
- `Nonce`
- `Stats`
- `Content`
- `ContentFrom`
- `Status`
- `Sync`
- `Clear`
- `FilterType`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/types.go.md|core/types.go]]
- [[event/event.go.md|event/event.go]]
- [[log/format.go.md|log/format.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
- [[core/txpool/blobpool/blobpool.go.md|core/txpool/blobpool/blobpool.go]]
- [[core/txpool/blobpool/blobpool_test.go.md|core/txpool/blobpool/blobpool_test.go]]
- [[core/txpool/blobpool/cache.go.md|core/txpool/blobpool/cache.go]]
- [[core/txpool/legacypool/legacypool.go.md|core/txpool/legacypool/legacypool.go]]
- [[core/txpool/legacypool/legacypool_test.go.md|core/txpool/legacypool/legacypool_test.go]]
- [[core/txpool/legacypool/queue.go.md|core/txpool/legacypool/queue.go]]
- [[core/txpool/locals/errors.go.md|core/txpool/locals/errors.go]]
- [[core/txpool/locals/tx_tracker.go.md|core/txpool/locals/tx_tracker.go]]
- [[core/txpool/locals/tx_tracker_test.go.md|core/txpool/locals/tx_tracker_test.go]]
- [[core/txpool/txorder/ordering.go.md|core/txpool/txorder/ordering.go]]
- [[core/txpool/txorder/ordering_test.go.md|core/txpool/txorder/ordering_test.go]]
- [[eth/api_backend.go.md|eth/api_backend.go]]
- [[eth/api_backend_test.go.md|eth/api_backend_test.go]]
- [[eth/api_debug_test.go.md|eth/api_debug_test.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/catalyst/simulated_beacon.go.md|eth/catalyst/simulated_beacon.go]]
- [[eth/fetcher/tx_fetcher.go.md|eth/fetcher/tx_fetcher.go]]
- [[eth/fetcher/tx_fetcher_test.go.md|eth/fetcher/tx_fetcher_test.go]]
- [[eth/handler.go.md|eth/handler.go]]
- [[eth/handler_test.go.md|eth/handler_test.go]]
- [[eth/protocols/eth/handler.go.md|eth/protocols/eth/handler.go]]
- [[eth/protocols/eth/handler_test.go.md|eth/protocols/eth/handler_test.go]]
- [[eth/sync.go.md|eth/sync.go]]
- [[miner/miner.go.md|miner/miner.go]]
- [[miner/miner_test.go.md|miner/miner_test.go]]
- [[miner/payload_building_test.go.md|miner/payload_building_test.go]]
- [[miner/worker.go.md|miner/worker.go]]

## Source Code Snippet
```go
// Copyright 2014 The go-ethereum Authors
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

package txpool

import (
	"errors"
...
```