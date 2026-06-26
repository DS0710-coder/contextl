# blockchain.go

## Architecture Metrics
- **Path:** `core/blockchain.go`
- **Extension:** `.go`
- **Size:** 119038 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 28

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BlockChainConfig`
- `txLookup`
- `BlockChain`
- `blockProcessingResult`
- `ExecuteConfig`
- `prewarmReader`
- `DefaultConfig`
- `WithArchive`
- `WithStateScheme`
- `WithNoAsyncFlush`
- `triedbConfig`
- `NewBlockChain`
- `setupSnapshot`
- `empty`
- `loadLastState`
- `initializeHistoryPruning`
- `SetHead`
- `SetHeadWithTimestamp`
- `sendChainHeadEvent`
- `SetFinalized`
- `SetSafe`
- `rewindHashHead`
- `rewindPathHead`
- `rewindHead`
- `setHeadBeyondRoot`
- `SnapSyncStart`
- `SnapSyncComplete`
- `Reset`
- `ResetWithGenesisBlock`
- `Export`
- `ExportN`
- `writeHeadBlock`
- `stopWithoutSaving`
- `Stop`
- `InterruptInsert`
- `insertStopped`
- `InsertReceiptChain`
- `writeBlockWithoutState`
- `writeKnownBlock`
- `writeBlockWithState`
- `writeBlockAndSetHead`
- `InsertChain`
- `insertChain`
- `Witness`
- `Stats`
- `ProcessBlock`
- `insertSideChain`
- `recoverAncestors`
- `collectLogs`
- `collectReceiptsAndLogs`
- `reorg`
- `InsertBlockWithoutSetHead`
- `SetCanonical`
- `skipBlock`
- `reportBadBlock`
- `logForkReadiness`
- `summarizeBadBlock`
- `InsertHeaderChain`
- `InsertHeadersBeforeCutoff`
- `SetBlockValidatorAndProcessorForTesting`
- `SetTrieFlushInterval`
- `GetTrieFlushInterval`
- `StateSizer`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/lru/lru.go.md|common/lru/lru.go]]
- [[common/mclock/mclock.go.md|common/mclock/mclock.go]]
- [[common/prque/prque.go.md|common/prque/prque.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[consensus/misc/eip4844/eip4844.go.md|consensus/misc/eip4844/eip4844.go]]
- [[core/history/historymode.go.md|core/history/historymode.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/state/snapshot/snapshot.go.md|core/state/snapshot/snapshot.go]]
- [[core/stateless.go.md|core/stateless.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[event/event.go.md|event/event.go]]
- [[internal/syncx/mutex.go.md|internal/syncx/mutex.go]]
- [[internal/telemetry/telemetry.go.md|internal/telemetry/telemetry.go]]
- [[internal/version/version.go.md|internal/version/version.go]]
- [[log/format.go.md|log/format.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[triedb/database.go.md|triedb/database.go]]
- [[triedb/hashdb/database.go.md|triedb/hashdb/database.go]]
- [[triedb/pathdb/buffer.go.md|triedb/pathdb/buffer.go]]

## Imported By (Dependents)
*Not imported by any file*

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

// Package core implements the Ethereum consensus protocol.
package core

import (
...
```