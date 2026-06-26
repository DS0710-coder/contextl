# addrlock.go

## Architecture Metrics
- **Path:** `internal/ethapi/addrlock.go`
- **Extension:** `.go`
- **Size:** 1758 bytes
- **Centrality Score:** 0.0005
- **In-Degree (Imported By):** 11
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `AddrLocker`
- `lock`
- `LockAddr`
- `UnlockAddr`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]

## Imported By (Dependents)
- [[cmd/era/main.go.md|cmd/era/main.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[eth/api_backend.go.md|eth/api_backend.go]]
- [[eth/api_debug.go.md|eth/api_debug.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/filters/api.go.md|eth/filters/api.go]]
- [[eth/filters/filter_system_test.go.md|eth/filters/filter_system_test.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[eth/tracers/api_test.go.md|eth/tracers/api_test.go]]
- [[graphql/graphql.go.md|graphql/graphql.go]]
- [[graphql/service.go.md|graphql/service.go]]

## Source Code Snippet
```go
// Copyright 2017 The go-ethereum Authors
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

package ethapi

import (
	"sync"
...
```