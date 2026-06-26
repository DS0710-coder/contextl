# queue.go

## Architecture Metrics
- **Path:** `eth/downloader/queue.go`
- **Extension:** `.go`
- **Size:** 25254 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `fetchRequest`
- `fetchResult`
- `queue`
- `newFetchResult`
- `body`
- `SetBodyDone`
- `AllDone`
- `SetReceiptsDone`
- `Done`
- `newQueue`
- `Reset`
- `Close`
- `PendingBodies`
- `PendingReceipts`
- `InFlightBlocks`
- `InFlightReceipts`
- `Idle`
- `Schedule`
- `Results`
- `Stats`
- `stats`
- `ReserveBodies`
- `ReserveReceipts`
- `reserveHeaders`
- `Revoke`
- `ExpireBodies`
- `ExpireReceipts`
- `expire`
- `DeliverBodies`
- `DeliverReceipts`
- `deliver`
- `Prepare`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/prque/prque.go.md|common/prque/prque.go]]
- [[core/types.go.md|core/types.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[log/format.go.md|log/format.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

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

// Contains the block download scheduler to collect download tasks and schedule
// them in an ordered, and throttled way.

package downloader
...
```