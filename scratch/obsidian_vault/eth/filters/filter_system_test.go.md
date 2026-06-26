# filter_system_test.go

## Architecture Metrics
- **Path:** `eth/filters/filter_system_test.go`
- **Extension:** `.go`
- **Size:** 30169 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 14

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `testBackend`
- `testcase`
- `ChainConfig`
- `CurrentHeader`
- `CurrentBlock`
- `ChainDb`
- `GetCanonicalHash`
- `GetHeader`
- `GetReceiptsByHash`
- `GetRawReceipts`
- `HeaderByNumber`
- `HeaderByHash`
- `GetBody`
- `GetReceipts`
- `GetLogs`
- `SubscribeNewTxsEvent`
- `SubscribeRemovedLogsEvent`
- `SubscribeLogsEvent`
- `SubscribeChainEvent`
- `CurrentView`
- `NewMatcherBackend`
- `startFilterMaps`
- `stopFilterMaps`
- `setPending`
- `HistoryPruningCutoff`
- `newTestFilterSystem`
- `TestBlockSubscription`
- `TestPendingTxFilter`
- `TestPendingTxFilterFullTx`
- `TestLogFilterCreation`
- `TestInvalidLogFilterCreation`
- `TestInvalidGetLogsRequest`
- `TestInvalidGetRangeLogsRequest`
- `TestExceedLogQueryLimit`
- `TestLogFilter`
- `TestPendingTxFilterDeadlock`
- `TestTransactionReceiptsSubscription`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[consensus/ethash/ethash.go.md|consensus/ethash/ethash.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/filtermaps/filtermaps.go.md|core/filtermaps/filtermaps.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[event/event.go.md|event/event.go]]
- [[internal/ethapi/addrlock.go.md|internal/ethapi/addrlock.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rpc/client.go.md|rpc/client.go]]
- [[triedb/database.go.md|triedb/database.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2016 The go-ethereum Authors
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

package filters

import (
	"context"
...
```