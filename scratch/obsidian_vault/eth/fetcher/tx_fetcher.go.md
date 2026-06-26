# tx_fetcher.go

## Architecture Metrics
- **Path:** `eth/fetcher/tx_fetcher.go`
- **Extension:** `.go`
- **Size:** 40533 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 8

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `txAnnounce`
- `txMetadata`
- `txMetadataWithSeq`
- `txRequest`
- `txDelivery`
- `txDrop`
- `TxFetcher`
- `announcement`
- `NewTxFetcher`
- `NewTxFetcherForTests`
- `Notify`
- `isKnownUnderpriced`
- `Enqueue`
- `Drop`
- `Start`
- `Stop`
- `loop`
- `rescheduleWait`
- `rescheduleTimeout`
- `scheduleFetches`
- `forEachPeer`
- `forEachAnnounce`
- `rotateStrings`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/lru/lru.go.md|common/lru/lru.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[common/mclock/mclock.go.md|common/mclock/mclock.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/txpool/txpool.go.md|core/txpool/txpool.go]]
- [[core/types.go.md|core/types.go]]
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2019 The go-ethereum Authors
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

package fetcher

import (
	"errors"
...
```