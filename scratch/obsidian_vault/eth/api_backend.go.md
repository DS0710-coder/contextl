# api_backend.go

## Architecture Metrics
- **Path:** `eth/api_backend.go`
- **Extension:** `.go`
- **Size:** 18256 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 21

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `EthAPIBackend`
- `ChainConfig`
- `CurrentBlock`
- `SetHead`
- `HeaderByNumber`
- `HeaderByNumberOrHash`
- `HeaderByHash`
- `BlockByNumber`
- `BlockByHash`
- `GetBody`
- `BlockByNumberOrHash`
- `Pending`
- `StateAndHeaderByNumber`
- `StateAndHeaderByNumberOrHash`
- `HistoryPruningCutoff`
- `HistoryRetention`
- `GetReceipts`
- `GetCanonicalReceipt`
- `GetLogs`
- `GetEVM`
- `SubscribeRemovedLogsEvent`
- `SubscribeChainEvent`
- `SubscribeChainHeadEvent`
- `SubscribeNewPayloadEvent`
- `SubscribeLogsEvent`
- `SendTx`
- `GetPoolTransactions`
- `GetPoolTransaction`
- `GetCanonicalTransaction`
- `TxIndexDone`
- `GetPoolNonce`
- `Stats`
- `TxPoolContent`
- `TxPoolContentFrom`
- `TxPool`
- `SubscribeNewTxsEvent`
- `SyncProgress`
- `SuggestGasTipCap`
- `FeeHistory`
- `BaseFee`
- `BlobBaseFee`
- `ChainDb`
- `AccountManager`
- `ExtRPCEnabled`
- `UnprotectedAllowed`
- `RPCGasCap`
- `RPCEVMTimeout`
- `RPCTxFeeCap`
- `CurrentView`
- `NewMatcherBackend`
- `Engine`
- `CurrentHeader`
- `StateAtBlock`
- `StateAtTransaction`
- `RPCTxSyncDefaultTimeout`
- `RPCTxSyncMaxTimeout`

## Imports (Dependencies)
- [[accounts/accounts.go.md|accounts/accounts.go]]
- [[common/big.go.md|common/big.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[consensus/misc/eip1559/eip1559.go.md|consensus/misc/eip1559/eip1559.go]]
- [[consensus/misc/eip4844/eip4844.go.md|consensus/misc/eip4844/eip4844.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/filtermaps/filtermaps.go.md|core/filtermaps/filtermaps.go]]
- [[core/history/historymode.go.md|core/history/historymode.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/txpool/locals/errors.go.md|core/txpool/locals/errors.go]]
- [[core/txpool/txpool.go.md|core/txpool/txpool.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[eth/gasprice/gasprice.go.md|eth/gasprice/gasprice.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[event/event.go.md|event/event.go]]
- [[internal/ethapi/addrlock.go.md|internal/ethapi/addrlock.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rpc/client.go.md|rpc/client.go]]

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
	"context"
...
```