# backend.go

## Architecture Metrics
- **Path:** `ethclient/simulated/backend.go`
- **Extension:** `.go`
- **Size:** 6098 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 12

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Client`
- `simClient`
- `Backend`
- `NewBackend`
- `newWithNode`
- `Close`
- `Commit`
- `Rollback`
- `Fork`
- `AdjustTime`
- `Client`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/types.go.md|core/types.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[eth/catalyst/api.go.md|eth/catalyst/api.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/filters/api.go.md|eth/filters/api.go]]
- [[ethclient/ethclient.go.md|ethclient/ethclient.go]]
- [[node/node.go.md|node/node.go]]
- [[p2p/config.go.md|p2p/config.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
- [[accounts/abi/bind/backends/simulated.go.md|accounts/abi/bind/backends/simulated.go]]
- [[accounts/abi/bind/v2/lib_test.go.md|accounts/abi/bind/v2/lib_test.go]]
- [[accounts/abi/bind/v2/util_test.go.md|accounts/abi/bind/v2/util_test.go]]

## Source Code Snippet
```go
// Copyright 2023 The go-ethereum Authors
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

package simulated

import (
	"errors"
...
```