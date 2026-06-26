# handler.go

## Architecture Metrics
- **Path:** `eth/handler.go`
- **Extension:** `.go`
- **Size:** 22927 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 18

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `txPool`
- `handlerConfig`
- `handler`
- `blockRangeState`
- `broadcastChoice`
- `broadcastPeer`
- `newHandler`
- `protoTracker`
- `incHandlers`
- `decHandlers`
- `runEthPeer`
- `runSnapExtension`
- `removePeer`
- `unregisterPeer`
- `Start`
- `Stop`
- `BroadcastTransactions`
- `txBroadcastLoop`
- `enableSyncedFeatures`
- `newBlockRangeState`
- `blockRangeLoop`
- `blockRangeWhileSnapSyncing`
- `broadcastBlockRange`
- `update`
- `shouldSend`
- `stop`
- `currentRange`
- `newBroadcastChoiceKey`
- `newBroadcastChoice`
- `choosePeers`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/txpool/txpool.go.md|core/txpool/txpool.go]]
- [[core/types.go.md|core/types.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[eth/downloader/downloader.go.md|eth/downloader/downloader.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/fetcher/metrics.go.md|eth/fetcher/metrics.go]]
- [[eth/protocols/snap/bal_apply.go.md|eth/protocols/snap/bal_apply.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[event/event.go.md|event/event.go]]
- [[log/format.go.md|log/format.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]
- [[node/api.go.md|node/api.go]]
- [[p2p/config.go.md|p2p/config.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2015 The go-ethereum Authors
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

package eth

import (
	"cmp"
...
```