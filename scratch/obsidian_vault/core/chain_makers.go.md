# chain_makers.go

## Architecture Metrics
- **Path:** `core/chain_makers.go`
- **Extension:** `.go`
- **Size:** 23253 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 13

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BlockGen`
- `chainMaker`
- `SetCoinbase`
- `SetExtra`
- `SetNonce`
- `SetDifficulty`
- `SetPoS`
- `Difficulty`
- `SetParentBeaconRoot`
- `addTx`
- `AddTx`
- `AddTxWithChain`
- `AddTxWithVMConfig`
- `GetBalance`
- `AddUncheckedTx`
- `Number`
- `Timestamp`
- `BaseFee`
- `Gas`
- `Signer`
- `AddUncheckedReceipt`
- `TxNonce`
- `AddUncle`
- `AddWithdrawal`
- `nextWithdrawalIndex`
- `PrevBlock`
- `OffsetTime`
- `ConsensusLayerRequests`
- `collectRequests`
- `GenerateChain`
- `GenerateChainWithGenesis`
- `makeHeader`
- `makeHeaderChain`
- `makeHeaderChainWithGenesis`
- `makeBlockChain`
- `makeBlockChainWithGenesis`
- `newChainMaker`
- `add`
- `blockByNumber`
- `Config`
- `Engine`
- `CurrentHeader`
- `GetHeaderByNumber`
- `GetHeaderByHash`
- `GetHeader`
- `GetBlock`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[consensus/misc/dao.go.md|consensus/misc/dao.go]]
- [[consensus/misc/eip1559/eip1559.go.md|consensus/misc/eip1559/eip1559.go]]
- [[consensus/misc/eip4844/eip4844.go.md|consensus/misc/eip4844/eip4844.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/types.go.md|core/types.go]]
- [[core/types/bal/bal.go.md|core/types/bal/bal.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[triedb/database.go.md|triedb/database.go]]

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

package core

import (
	"context"
...
```