# peer.go

## Architecture Metrics
- **Path:** `eth/protocols/eth/peer.go`
- **Extension:** `.go`
- **Size:** 21822 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 8

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `receiptRequest`
- `Peer`
- `knownCache`
- `NewPeer`
- `Close`
- `ID`
- `Version`
- `BlockRange`
- `KnownTransaction`
- `MarkTransaction`
- `SendTransactions`
- `AsyncSendTransactions`
- `sendPooledTransactionHashes`
- `AsyncSendPooledTransactionHashes`
- `ReplyPooledTransactionsRLP`
- `ReplyBlockHeadersRLP`
- `ReplyBlockBodiesRLP`
- `ReplyReceiptsRLP69`
- `ReplyReceiptsRLP70`
- `ReplyBlockAccessLists`
- `RequestBALs`
- `RequestOneHeader`
- `RequestHeadersByHash`
- `RequestHeadersByNumber`
- `RequestBodies`
- `RequestReceipts`
- `requestPartialReceipts`
- `bufferReceipts`
- `flushReceipts`
- `validateLastBlockReceipt`
- `RequestTxs`
- `SendBlockRangeUpdate`
- `newKnownCache`
- `Add`
- `Contains`
- `Cardinality`

## Imports (Dependencies)
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]
- [[p2p/config.go.md|p2p/config.go]]
- [[p2p/tracker/tracker.go.md|p2p/tracker/tracker.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2020 The go-ethereum Authors
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
	"errors"
...
```