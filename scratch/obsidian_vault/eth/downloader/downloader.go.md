# downloader.go

## Architecture Metrics
- **Path:** `eth/downloader/downloader.go`
- **Extension:** `.go`
- **Size:** 46495 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 13

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `headerTask`
- `Downloader`
- `BlockChain`
- `New`
- `Progress`
- `RegisterPeer`
- `UnregisterPeer`
- `synchronise`
- `getMode`
- `ConfigSyncMode`
- `SubscribeSyncEvents`
- `syncToHead`
- `spawnSync`
- `cancel`
- `Cancel`
- `Terminate`
- `fetchBodies`
- `fetchReceipts`
- `processHeaders`
- `processFullSyncContent`
- `importBlockResults`
- `processSnapSyncContent`
- `splitAroundPivot`
- `commitSnapSyncData`
- `commitPivotBlock`
- `DeliverSnapPacket`
- `RegisterSnapPeer`
- `SnapSyncVersion`
- `UnregisterSnapPeer`
- `readHeaderRange`
- `reportSnapSyncProgress`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/state/snapshot/snapshot.go.md|core/state/snapshot/snapshot.go]]
- [[core/types.go.md|core/types.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/protocols/snap/bal_apply.go.md|eth/protocols/snap/bal_apply.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[event/event.go.md|event/event.go]]
- [[log/format.go.md|log/format.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[triedb/database.go.md|triedb/database.go]]

## Imported By (Dependents)
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/handler.go.md|eth/handler.go]]
- [[eth/syncer/syncer.go.md|eth/syncer/syncer.go]]
- [[miner/stress/main.go.md|miner/stress/main.go]]

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

// Package downloader contains the manual full chain synchronisation.
package downloader

import (
...
```