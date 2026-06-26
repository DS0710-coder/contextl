# api.go

## Architecture Metrics
- **Path:** `eth/filters/api.go`
- **Extension:** `.go`
- **Size:** 22038 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 6
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `invalidParamsError`
- `filter`
- `FilterAPI`
- `input`
- `input`
- `Error`
- `ErrorCode`
- `invalidParamsErr`
- `NewFilterAPI`
- `timeoutLoop`
- `NewPendingTransactionFilter`
- `NewPendingTransactions`
- `NewBlockFilter`
- `NewHeads`
- `Logs`
- `UnmarshalJSON`
- `TransactionReceipts`
- `NewFilter`
- `GetLogs`
- `UninstallFilter`
- `GetFilterLogs`
- `GetFilterChanges`
- `returnHashes`
- `returnLogs`
- `UnmarshalJSON`
- `decodeAddress`
- `decodeTopic`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/history/historymode.go.md|core/history/historymode.go]]
- [[core/types.go.md|core/types.go]]
- [[internal/ethapi/addrlock.go.md|internal/ethapi/addrlock.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[ethclient/gethclient/gethclient_test.go.md|ethclient/gethclient/gethclient_test.go]]
- [[ethclient/simulated/backend.go.md|ethclient/simulated/backend.go]]
- [[graphql/graphql.go.md|graphql/graphql.go]]
- [[graphql/graphql_test.go.md|graphql/graphql_test.go]]
- [[graphql/service.go.md|graphql/service.go]]

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

package filters

import (
	"context"
...
```