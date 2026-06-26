# blockchain_sethead_test.go

## Architecture Metrics
- **Path:** `core/blockchain_sethead_test.go`
- **Extension:** `.go`
- **Size:** 71426 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `rewindTest`
- `freezer`
- `dump`
- `TestShortSetHead`
- `TestShortSetHeadWithSnapshots`
- `testShortSetHead`
- `TestShortSnapSyncedSetHead`
- `TestShortSnapSyncedSetHeadWithSnapshots`
- `testShortSnapSyncedSetHead`
- `TestShortSnapSyncingSetHead`
- `TestShortSnapSyncingSetHeadWithSnapshots`
- `testShortSnapSyncingSetHead`
- `TestShortOldForkedSetHead`
- `TestShortOldForkedSetHeadWithSnapshots`
- `testShortOldForkedSetHead`
- `TestShortOldForkedSnapSyncedSetHead`
- `TestShortOldForkedSnapSyncedSetHeadWithSnapshots`
- `testShortOldForkedSnapSyncedSetHead`
- `TestShortOldForkedSnapSyncingSetHead`
- `TestShortOldForkedSnapSyncingSetHeadWithSnapshots`
- `testShortOldForkedSnapSyncingSetHead`
- `TestShortNewlyForkedSetHead`
- `TestShortNewlyForkedSetHeadWithSnapshots`
- `testShortNewlyForkedSetHead`
- `TestShortNewlyForkedSnapSyncedSetHead`
- `TestShortNewlyForkedSnapSyncedSetHeadWithSnapshots`
- `testShortNewlyForkedSnapSyncedSetHead`
- `TestShortNewlyForkedSnapSyncingSetHead`
- `TestShortNewlyForkedSnapSyncingSetHeadWithSnapshots`
- `testShortNewlyForkedSnapSyncingSetHead`
- `TestShortReorgedSetHead`
- `TestShortReorgedSetHeadWithSnapshots`
- `testShortReorgedSetHead`
- `TestShortReorgedSnapSyncedSetHead`
- `TestShortReorgedSnapSyncedSetHeadWithSnapshots`
- `testShortReorgedSnapSyncedSetHead`
- `TestShortReorgedSnapSyncingSetHead`
- `TestShortReorgedSnapSyncingSetHeadWithSnapshots`
- `testShortReorgedSnapSyncingSetHead`
- `TestLongShallowSetHead`
- `TestLongShallowSetHeadWithSnapshots`
- `testLongShallowSetHead`
- `TestLongDeepSetHead`
- `TestLongDeepSetHeadWithSnapshots`
- `testLongDeepSetHead`
- `TestLongSnapSyncedShallowSetHead`
- `TestLongSnapSyncedShallowSetHeadWithSnapshots`
- `testLongSnapSyncedShallowSetHead`
- `TestLongSnapSyncedDeepSetHead`
- `TestLongSnapSyncedDeepSetHeadWithSnapshots`
- `testLongSnapSyncedDeepSetHead`
- `TestLongSnapSyncingShallowSetHead`
- `TestLongSnapSyncingShallowSetHeadWithSnapshots`
- `testLongSnapSyncingShallowSetHead`
- `TestLongSnapSyncingDeepSetHead`
- `TestLongSnapSyncingDeepSetHeadWithSnapshots`
- `testLongSnapSyncingDeepSetHead`
- `TestLongOldForkedShallowSetHead`
- `TestLongOldForkedShallowSetHeadWithSnapshots`
- `testLongOldForkedShallowSetHead`
- `TestLongOldForkedDeepSetHead`
- `TestLongOldForkedDeepSetHeadWithSnapshots`
- `testLongOldForkedDeepSetHead`
- `TestLongOldForkedSnapSyncedShallowSetHead`
- `TestLongOldForkedSnapSyncedShallowSetHeadWithSnapshots`
- `testLongOldForkedSnapSyncedShallowSetHead`
- `TestLongOldForkedSnapSyncedDeepSetHead`
- `TestLongOldForkedSnapSyncedDeepSetHeadWithSnapshots`
- `testLongOldForkedSnapSyncedDeepSetHead`
- `TestLongOldForkedSnapSyncingShallowSetHead`
- `TestLongOldForkedSnapSyncingShallowSetHeadWithSnapshots`
- `testLongOldForkedSnapSyncingShallowSetHead`
- `TestLongOldForkedSnapSyncingDeepSetHead`
- `TestLongOldForkedSnapSyncingDeepSetHeadWithSnapshots`
- `testLongOldForkedSnapSyncingDeepSetHead`
- `TestLongNewerForkedShallowSetHead`
- `TestLongNewerForkedShallowSetHeadWithSnapshots`
- `testLongNewerForkedShallowSetHead`
- `TestLongNewerForkedDeepSetHead`
- `TestLongNewerForkedDeepSetHeadWithSnapshots`
- `testLongNewerForkedDeepSetHead`
- `TestLongNewerForkedSnapSyncedShallowSetHead`
- `TestLongNewerForkedSnapSyncedShallowSetHeadWithSnapshots`
- `testLongNewerForkedSnapSyncedShallowSetHead`
- `TestLongNewerForkedSnapSyncedDeepSetHead`
- `TestLongNewerForkedSnapSyncedDeepSetHeadWithSnapshots`
- `testLongNewerForkedSnapSyncedDeepSetHead`
- `TestLongNewerForkedSnapSyncingShallowSetHead`
- `TestLongNewerForkedSnapSyncingShallowSetHeadWithSnapshots`
- `testLongNewerForkedSnapSyncingShallowSetHead`
- `TestLongNewerForkedSnapSyncingDeepSetHead`
- `TestLongNewerForkedSnapSyncingDeepSetHeadWithSnapshots`
- `testLongNewerForkedSnapSyncingDeepSetHead`
- `TestLongReorgedShallowSetHead`
- `TestLongReorgedShallowSetHeadWithSnapshots`
- `testLongReorgedShallowSetHead`
- `TestLongReorgedDeepSetHead`
- `TestLongReorgedDeepSetHeadWithSnapshots`
- `testLongReorgedDeepSetHead`
- `TestLongReorgedSnapSyncedShallowSetHead`
- `TestLongReorgedSnapSyncedShallowSetHeadWithSnapshots`
- `testLongReorgedSnapSyncedShallowSetHead`
- `TestLongReorgedSnapSyncedDeepSetHead`
- `TestLongReorgedSnapSyncedDeepSetHeadWithSnapshots`
- `testLongReorgedSnapSyncedDeepSetHead`
- `TestLongReorgedSnapSyncingShallowSetHead`
- `TestLongReorgedSnapSyncingShallowSetHeadWithSnapshots`
- `testLongReorgedSnapSyncingShallowSetHead`
- `TestLongReorgedSnapSyncingDeepSetHead`
- `TestLongReorgedSnapSyncingDeepSetHeadWithSnapshots`
- `testLongReorgedSnapSyncingDeepSetHead`
- `testSetHead`
- `testSetHeadWithScheme`
- `verifyNoGaps`
- `verifyCutoff`
- `uint64ptr`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[consensus/ethash/ethash.go.md|consensus/ethash/ethash.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/types.go.md|core/types.go]]
- [[ethdb/pebble/pebble.go.md|ethdb/pebble/pebble.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[triedb/database.go.md|triedb/database.go]]
- [[triedb/hashdb/database.go.md|triedb/hashdb/database.go]]
- [[triedb/pathdb/buffer.go.md|triedb/pathdb/buffer.go]]

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

// Tests that setting the chain head backwards doesn't leave the database in some
// strange state with gaps in the chain, nor with block data dangling in the future.

package core
...
```