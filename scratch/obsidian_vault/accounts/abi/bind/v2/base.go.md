# base.go

## Architecture Metrics
- **Path:** `accounts/abi/bind/v2/base.go`
- **Extension:** `.go`
- **Size:** 19618 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `CallOpts`
- `TransactOpts`
- `FilterOpts`
- `WatchOpts`
- `MetaData`
- `BoundContract`
- `ParseABI`
- `NewBoundContract`
- `Address`
- `Call`
- `CallRaw`
- `call`
- `Transact`
- `RawTransact`
- `RawCreationTransact`
- `Transfer`
- `createDynamicTx`
- `createLegacyTx`
- `estimateGasLimit`
- `getNonce`
- `transact`
- `FilterLogs`
- `WatchLogs`
- `UnpackLog`
- `UnpackLogIntoMap`
- `ensureContext`

## Imports (Dependencies)
- [[accounts/abi/abi.go.md|accounts/abi/abi.go]]
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]
- [[event/event.go.md|event/event.go]]

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

package bind

import (
	"context"
...
```