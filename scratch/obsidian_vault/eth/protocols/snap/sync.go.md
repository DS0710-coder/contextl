# sync.go

## Architecture Metrics
- **Path:** `eth/protocols/snap/sync.go`
- **Extension:** `.go`
- **Size:** 116575 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 14

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `accountRequest`
- `accountResponse`
- `bytecodeRequest`
- `bytecodeResponse`
- `storageRequest`
- `storageResponse`
- `trienodeHealRequest`
- `trienodeHealResponse`
- `bytecodeHealRequest`
- `bytecodeHealResponse`
- `accountTask`
- `storageTask`
- `healTask`
- `syncProgress`
- `syncPending`
- `SyncPeer`
- `syncer`
- `capacitySort`
- `healRequestSort`
- `activeSubTasks`
- `newSyncer`
- `Register`
- `Unregister`
- `Sync`
- `loadSyncStatus`
- `saveSyncStatus`
- `Progress`
- `cleanAccountTasks`
- `cleanStorageTasks`
- `assignAccountTasks`
- `assignBytecodeTasks`
- `assignStorageTasks`
- `assignTrienodeHealTasks`
- `assignBytecodeHealTasks`
- `revertRequests`
- `scheduleRevertAccountRequest`
- `revertAccountRequest`
- `scheduleRevertBytecodeRequest`
- `revertBytecodeRequest`
- `scheduleRevertStorageRequest`
- `revertStorageRequest`
- `scheduleRevertTrienodeHealRequest`
- `revertTrienodeHealRequest`
- `scheduleRevertBytecodeHealRequest`
- `revertBytecodeHealRequest`
- `processAccountResponse`
- `processBytecodeResponse`
- `processStorageResponse`
- `processTrienodeHealResponse`
- `commitHealer`
- `processBytecodeHealResponse`
- `forwardAccountTask`
- `OnAccounts`
- `OnByteCodes`
- `onByteCodes`
- `OnStorage`
- `OnTrieNodes`
- `onHealByteCodes`
- `onHealState`
- `report`
- `reportSyncProgress`
- `reportHealProgress`
- `estimateRemainingSlots`
- `Len`
- `Less`
- `Swap`
- `Len`
- `Less`
- `Swap`
- `Merge`
- `sortByAccountPath`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[event/event.go.md|event/event.go]]
- [[log/format.go.md|log/format.go]]
- [[node/api.go.md|node/api.go]]
- [[p2p/msgrate/msgrate.go.md|p2p/msgrate/msgrate.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[trie/trie.go.md|trie/trie.go]]

## Imported By (Dependents)
*Not imported by any file*

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

package snap

import (
	"bytes"
...
```