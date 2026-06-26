# blockchain_repair_test.go

## Architecture Metrics
- **Path:** `core/blockchain_repair_test.go`
- **Extension:** `.go`
- **Size:** 65442 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `freezer`
- `TestShortRepair`
- `TestShortRepairWithSnapshots`
- `testShortRepair`
- `TestShortSnapSyncedRepair`
- `TestShortSnapSyncedRepairWithSnapshots`
- `testShortSnapSyncedRepair`
- `TestShortSnapSyncingRepair`
- `TestShortSnapSyncingRepairWithSnapshots`
- `testShortSnapSyncingRepair`
- `TestShortOldForkedRepair`
- `TestShortOldForkedRepairWithSnapshots`
- `testShortOldForkedRepair`
- `TestShortOldForkedSnapSyncedRepair`
- `TestShortOldForkedSnapSyncedRepairWithSnapshots`
- `testShortOldForkedSnapSyncedRepair`
- `TestShortOldForkedSnapSyncingRepair`
- `TestShortOldForkedSnapSyncingRepairWithSnapshots`
- `testShortOldForkedSnapSyncingRepair`
- `TestShortNewlyForkedRepair`
- `TestShortNewlyForkedRepairWithSnapshots`
- `testShortNewlyForkedRepair`
- `TestShortNewlyForkedSnapSyncedRepair`
- `TestShortNewlyForkedSnapSyncedRepairWithSnapshots`
- `testShortNewlyForkedSnapSyncedRepair`
- `TestShortNewlyForkedSnapSyncingRepair`
- `TestShortNewlyForkedSnapSyncingRepairWithSnapshots`
- `testShortNewlyForkedSnapSyncingRepair`
- `TestShortReorgedRepair`
- `TestShortReorgedRepairWithSnapshots`
- `testShortReorgedRepair`
- `TestShortReorgedSnapSyncedRepair`
- `TestShortReorgedSnapSyncedRepairWithSnapshots`
- `testShortReorgedSnapSyncedRepair`
- `TestShortReorgedSnapSyncingRepair`
- `TestShortReorgedSnapSyncingRepairWithSnapshots`
- `testShortReorgedSnapSyncingRepair`
- `TestLongShallowRepair`
- `TestLongShallowRepairWithSnapshots`
- `testLongShallowRepair`
- `TestLongDeepRepair`
- `TestLongDeepRepairWithSnapshots`
- `testLongDeepRepair`
- `TestLongSnapSyncedShallowRepair`
- `TestLongSnapSyncedShallowRepairWithSnapshots`
- `testLongSnapSyncedShallowRepair`
- `TestLongSnapSyncedDeepRepair`
- `TestLongSnapSyncedDeepRepairWithSnapshots`
- `testLongSnapSyncedDeepRepair`
- `TestLongSnapSyncingShallowRepair`
- `TestLongSnapSyncingShallowRepairWithSnapshots`
- `testLongSnapSyncingShallowRepair`
- `TestLongSnapSyncingDeepRepair`
- `TestLongSnapSyncingDeepRepairWithSnapshots`
- `testLongSnapSyncingDeepRepair`
- `TestLongOldForkedShallowRepair`
- `TestLongOldForkedShallowRepairWithSnapshots`
- `testLongOldForkedShallowRepair`
- `TestLongOldForkedDeepRepair`
- `TestLongOldForkedDeepRepairWithSnapshots`
- `testLongOldForkedDeepRepair`
- `TestLongOldForkedSnapSyncedShallowRepair`
- `TestLongOldForkedSnapSyncedShallowRepairWithSnapshots`
- `testLongOldForkedSnapSyncedShallowRepair`
- `TestLongOldForkedSnapSyncedDeepRepair`
- `TestLongOldForkedSnapSyncedDeepRepairWithSnapshots`
- `testLongOldForkedSnapSyncedDeepRepair`
- `TestLongOldForkedSnapSyncingShallowRepair`
- `TestLongOldForkedSnapSyncingShallowRepairWithSnapshots`
- `testLongOldForkedSnapSyncingShallowRepair`
- `TestLongOldForkedSnapSyncingDeepRepair`
- `TestLongOldForkedSnapSyncingDeepRepairWithSnapshots`
- `testLongOldForkedSnapSyncingDeepRepair`
- `TestLongNewerForkedShallowRepair`
- `TestLongNewerForkedShallowRepairWithSnapshots`
- `testLongNewerForkedShallowRepair`
- `TestLongNewerForkedDeepRepair`
- `TestLongNewerForkedDeepRepairWithSnapshots`
- `testLongNewerForkedDeepRepair`
- `TestLongNewerForkedSnapSyncedShallowRepair`
- `TestLongNewerForkedSnapSyncedShallowRepairWithSnapshots`
- `testLongNewerForkedSnapSyncedShallowRepair`
- `TestLongNewerForkedSnapSyncedDeepRepair`
- `TestLongNewerForkedSnapSyncedDeepRepairWithSnapshots`
- `testLongNewerForkedSnapSyncedDeepRepair`
- `TestLongNewerForkedSnapSyncingShallowRepair`
- `TestLongNewerForkedSnapSyncingShallowRepairWithSnapshots`
- `testLongNewerForkedSnapSyncingShallowRepair`
- `TestLongNewerForkedSnapSyncingDeepRepair`
- `TestLongNewerForkedSnapSyncingDeepRepairWithSnapshots`
- `testLongNewerForkedSnapSyncingDeepRepair`
- `TestLongReorgedShallowRepair`
- `TestLongReorgedShallowRepairWithSnapshots`
- `testLongReorgedShallowRepair`
- `TestLongReorgedDeepRepair`
- `TestLongReorgedDeepRepairWithSnapshots`
- `testLongReorgedDeepRepair`
- `TestLongReorgedSnapSyncedShallowRepair`
- `TestLongReorgedSnapSyncedShallowRepairWithSnapshots`
- `testLongReorgedSnapSyncedShallowRepair`
- `TestLongReorgedSnapSyncedDeepRepair`
- `TestLongReorgedSnapSyncedDeepRepairWithSnapshots`
- `testLongReorgedSnapSyncedDeepRepair`
- `TestLongReorgedSnapSyncingShallowRepair`
- `TestLongReorgedSnapSyncingShallowRepairWithSnapshots`
- `testLongReorgedSnapSyncingShallowRepair`
- `TestLongReorgedSnapSyncingDeepRepair`
- `TestLongReorgedSnapSyncingDeepRepairWithSnapshots`
- `testLongReorgedSnapSyncingDeepRepair`
- `testRepair`
- `testRepairWithScheme`
- `TestIssue23496`
- `testIssue23496`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[consensus/ethash/ethash.go.md|consensus/ethash/ethash.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/types.go.md|core/types.go]]
- [[ethdb/pebble/pebble.go.md|ethdb/pebble/pebble.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

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

// Tests that abnormal program termination (i.e.crash) and restart doesn't leave
// the database in some strange state with gaps in the chain, nor with block data
// dangling in the future.

...
```