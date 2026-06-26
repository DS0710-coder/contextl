# blockchain_reader.go

## Architecture Metrics
- **Path:** `core/blockchain_reader.go`
- **Extension:** `.go`
- **Size:** 19994 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 12

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `CurrentHeader`
- `CurrentBlock`
- `CurrentSnapBlock`
- `CurrentFinalBlock`
- `CurrentSafeBlock`
- `HasHeader`
- `GetHeader`
- `GetHeaderByHash`
- `GetHeaderByNumber`
- `GetBlockNumber`
- `GetHeadersFrom`
- `GetBody`
- `GetBodyRLP`
- `HasBlock`
- `HasFastBlock`
- `GetBlock`
- `GetBlockByHash`
- `GetBlockByNumber`
- `GetBlocksFromHash`
- `GetCanonicalReceipt`
- `GetReceiptsByHash`
- `GetRawReceipts`
- `GetReceiptsRLP`
- `GetAccessListRLP`
- `GetUnclesInChain`
- `GetCanonicalHash`
- `GetAncestor`
- `GetCanonicalTransaction`
- `TxIndexDone`
- `HasState`
- `HasBlockAndState`
- `stateRecoverable`
- `ContractCodeWithPrefix`
- `State`
- `StateAt`
- `StateAtForkBoundary`
- `HistoricState`
- `Config`
- `Engine`
- `Snapshots`
- `Validator`
- `Processor`
- `GasLimit`
- `Genesis`
- `GetVMConfig`
- `TxIndexProgress`
- `StateIndexProgress`
- `HistoryPruningCutoff`
- `TrieDB`
- `CodeDB`
- `HeaderChain`
- `SubscribeRemovedLogsEvent`
- `SubscribeChainEvent`
- `SubscribeChainHeadEvent`
- `SubscribeLogsEvent`
- `SubscribeBlockProcessingEvent`
- `SubscribeNewPayloadEvent`
- `SendNewPayloadEvent`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[consensus/misc/eip4844/eip4844.go.md|consensus/misc/eip4844/eip4844.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/state/snapshot/snapshot.go.md|core/state/snapshot/snapshot.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[event/event.go.md|event/event.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[triedb/database.go.md|triedb/database.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2021 The go-ethereum Authors
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

package core

import (
	"errors"
...
```