# transaction_args_test.go

## Architecture Metrics
- **Path:** `internal/ethapi/transaction_args_test.go`
- **Extension:** `.go`
- **Size:** 14741 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 13

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `test`
- `backendMock`
- `TestSetFeeDefaults`
- `newBackendMock`
- `setFork`
- `SuggestGasTipCap`
- `BlobBaseFee`
- `BaseFee`
- `CurrentHeader`
- `ChainConfig`
- `SyncProgress`
- `FeeHistory`
- `ChainDb`
- `AccountManager`
- `ExtRPCEnabled`
- `RPCGasCap`
- `RPCEVMTimeout`
- `RPCTxFeeCap`
- `UnprotectedAllowed`
- `SetHead`
- `HeaderByNumber`
- `HeaderByHash`
- `HeaderByNumberOrHash`
- `CurrentBlock`
- `BlockByNumber`
- `BlockByHash`
- `BlockByNumberOrHash`
- `GetBody`
- `StateAndHeaderByNumber`
- `StateAndHeaderByNumberOrHash`
- `Pending`
- `GetReceipts`
- `GetCanonicalReceipt`
- `GetLogs`
- `GetEVM`
- `SubscribeChainEvent`
- `SubscribeChainHeadEvent`
- `SendTx`
- `GetCanonicalTransaction`
- `TxIndexDone`
- `GetPoolTransactions`
- `GetPoolTransaction`
- `GetPoolNonce`
- `Stats`
- `TxPoolContent`
- `TxPoolContentFrom`
- `SubscribeNewTxsEvent`
- `SubscribeLogsEvent`
- `SubscribeRemovedLogsEvent`
- `Engine`
- `CurrentView`
- `NewMatcherBackend`
- `HistoryPruningCutoff`
- `HistoryRetention`

## Imports (Dependencies)
- [[accounts/accounts.go.md|accounts/accounts.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/filtermaps/filtermaps.go.md|core/filtermaps/filtermaps.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[event/event.go.md|event/event.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2022 The go-ethereum Authors
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

package ethapi

import (
	"context"
...
```