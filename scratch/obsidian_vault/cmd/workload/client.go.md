# client.go

## Architecture Metrics
- **Path:** `cmd/workload/client.go`
- **Extension:** `.go`
- **Size:** 3504 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `client`
- `simpleBlock`
- `simpleTransaction`
- `makeClient`
- `getBlockByHash`
- `getBlockByNumber`
- `getTransactionByBlockHashAndIndex`
- `getTransactionByBlockNumberAndIndex`
- `getBlockTransactionCountByHash`
- `getBlockTransactionCountByNumber`
- `getBlockReceipts`

## Imports (Dependencies)
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/types.go.md|core/types.go]]
- [[ethclient/ethclient.go.md|ethclient/ethclient.go]]
- [[ethclient/gethclient/gethclient.go.md|ethclient/gethclient/gethclient.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2025 The go-ethereum Authors
// This file is part of go-ethereum.
//
// go-ethereum is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// go-ethereum is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with go-ethereum. If not, see <http://www.gnu.org/licenses/>.

package main

import (
	"context"
...
```