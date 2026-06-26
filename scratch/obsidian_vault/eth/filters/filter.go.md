# filter.go

## Architecture Metrics
- **Path:** `eth/filters/filter.go`
- **Extension:** `.go`
- **Size:** 21103 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 8

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Filter`
- `rangeLogsTestEvent`
- `searchSession`
- `ReceiptWithTx`
- `NewRangeFilter`
- `NewBlockFilter`
- `newFilter`
- `Logs`
- `newSearchSession`
- `updateChainView`
- `trimMatches`
- `searchInRange`
- `doSearchIteration`
- `rangeLogs`
- `indexedLogs`
- `unindexedLogs`
- `blockLogs`
- `checkMatches`
- `filterLogs`
- `bloomFilter`
- `filterReceipts`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/filtermaps/filtermaps.go.md|core/filtermaps/filtermaps.go]]
- [[core/history/historymode.go.md|core/history/historymode.go]]
- [[core/types.go.md|core/types.go]]
- [[log/format.go.md|log/format.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2014 The go-ethereum Authors
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