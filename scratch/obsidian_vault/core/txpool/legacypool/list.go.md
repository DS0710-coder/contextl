# list.go

## Architecture Metrics
- **Path:** `core/txpool/legacypool/list.go`
- **Extension:** `.go`
- **Size:** 23285 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `SortedMap`
- `list`
- `priceHeap`
- `pricedList`
- `Len`
- `Less`
- `Swap`
- `Push`
- `Pop`
- `NewSortedMap`
- `Get`
- `Put`
- `Forward`
- `Filter`
- `reheap`
- `filter`
- `Cap`
- `Remove`
- `Ready`
- `Len`
- `flatten`
- `Flatten`
- `LastElement`
- `newList`
- `Contains`
- `Add`
- `Forward`
- `Filter`
- `Cap`
- `Remove`
- `Ready`
- `Len`
- `Empty`
- `Flatten`
- `LastElement`
- `subTotalCost`
- `Len`
- `Swap`
- `Less`
- `cmp`
- `Push`
- `Pop`
- `newPricedList`
- `Put`
- `Removed`
- `Underpriced`
- `underpricedFor`
- `Discard`
- `Reheap`
- `SetBaseFee`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[core/types.go.md|core/types.go]]

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

package legacypool

import (
	"container/heap"
...
```