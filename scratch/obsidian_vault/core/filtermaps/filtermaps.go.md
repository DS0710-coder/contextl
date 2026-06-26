# filtermaps.go

## Architecture Metrics
- **Path:** `core/filtermaps/filtermaps.go`
- **Extension:** `.go`
- **Size:** 35542 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 9
- **Out-Degree (Imports):** 8

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `FilterMaps`
- `filterMapsRange`
- `lastBlockOfMap`
- `Config`
- `fastCopy`
- `fullCopy`
- `Equal`
- `hasIndexedBlocks`
- `NewFilterMaps`
- `Start`
- `Stop`
- `checkRevertRange`
- `reset`
- `isShuttingDown`
- `init`
- `removeBloomBits`
- `safeDeleteWithLogs`
- `setRange`
- `getLogByLvIndex`
- `getFilterMap`
- `getFilterMapRows`
- `getFilterMapRowsOfGroup`
- `storeFilterMapRows`
- `storeFilterMapRowsOfGroup`
- `mapRowIndex`
- `getBlockLvPointer`
- `storeBlockLvPointer`
- `deleteBlockLvPointer`
- `getLastBlockOfMap`
- `storeLastBlockOfMap`
- `deleteLastBlockOfMap`
- `deleteTailEpoch`
- `exportCheckpoints`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/lru/lru.go.md|common/lru/lru.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/types.go.md|core/types.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[log/format.go.md|log/format.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]

## Imported By (Dependents)
- [[eth/api_backend.go.md|eth/api_backend.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/filters/filter.go.md|eth/filters/filter.go]]
- [[eth/filters/filter_system.go.md|eth/filters/filter_system.go]]
- [[eth/filters/filter_system_test.go.md|eth/filters/filter_system_test.go]]
- [[eth/filters/filter_test.go.md|eth/filters/filter_test.go]]
- [[internal/ethapi/api_test.go.md|internal/ethapi/api_test.go]]
- [[internal/ethapi/backend.go.md|internal/ethapi/backend.go]]
- [[internal/ethapi/transaction_args_test.go.md|internal/ethapi/transaction_args_test.go]]

## Source Code Snippet
```go
// Copyright 2024 The go-ethereum Authors
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

package filtermaps

import (
	"errors"
...
```