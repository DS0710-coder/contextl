# historymode.go

## Architecture Metrics
- **Path:** `core/history/historymode.go`
- **Extension:** `.go`
- **Size:** 4665 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 10
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PrunePoint`
- `HistoryPolicy`
- `PrunedHistoryError`
- `IsValid`
- `String`
- `MarshalText`
- `UnmarshalText`
- `NewPolicy`
- `Error`
- `ErrorCode`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
- [[cmd/geth/chaincmd.go.md|cmd/geth/chaincmd.go]]
- [[cmd/workload/testsuite.go.md|cmd/workload/testsuite.go]]
- [[core/blockchain.go.md|core/blockchain.go]]
- [[eth/api_backend.go.md|eth/api_backend.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/ethconfig/gen_config.go.md|eth/ethconfig/gen_config.go]]
- [[eth/filters/api.go.md|eth/filters/api.go]]
- [[eth/filters/filter.go.md|eth/filters/filter.go]]
- [[eth/filters/filter_system.go.md|eth/filters/filter_system.go]]

## Source Code Snippet
```go
// Copyright 2025 The go-ethereum Authors
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

package history

import (
	"fmt"
...
```