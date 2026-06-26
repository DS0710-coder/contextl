# filter_system.go

## Architecture Metrics
- **Path:** `eth/filters/filter_system.go`
- **Extension:** `.go`
- **Size:** 16667 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 12

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Config`
- `Backend`
- `FilterSystem`
- `logCacheElem`
- `subscription`
- `EventSystem`
- `Subscription`
- `withDefaults`
- `NewFilterSystem`
- `cachedLogElem`
- `cachedGetBody`
- `NewEventSystem`
- `Err`
- `Unsubscribe`
- `subscribe`
- `SubscribeLogs`
- `subscribeLogs`
- `SubscribeNewHeads`
- `SubscribePendingTxs`
- `SubscribeTransactionReceipts`
- `handleLogs`
- `handleTxsEvent`
- `handleChainEvent`
- `eventLoop`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/lru/lru.go.md|common/lru/lru.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/filtermaps/filtermaps.go.md|core/filtermaps/filtermaps.go]]
- [[core/history/historymode.go.md|core/history/historymode.go]]
- [[core/types.go.md|core/types.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[event/event.go.md|event/event.go]]
- [[log/format.go.md|log/format.go]]
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

// Package filters implements an ethereum filtering system for block,
// transactions and log events.
package filters

...
```