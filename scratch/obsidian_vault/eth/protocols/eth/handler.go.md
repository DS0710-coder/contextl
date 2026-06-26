# handler.go

## Architecture Metrics
- **Path:** `eth/protocols/eth/handler.go`
- **Extension:** `.go`
- **Size:** 9754 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Backend`
- `TxPool`
- `NodeInfo`
- `Decoder`
- `MakeProtocols`
- `nodeInfo`
- `Handle`
- `handleMessage`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/txpool/txpool.go.md|core/txpool/txpool.go]]
- [[core/types.go.md|core/types.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]
- [[node/api.go.md|node/api.go]]
- [[p2p/config.go.md|p2p/config.go]]
- [[p2p/enr/enr.go.md|p2p/enr/enr.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

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
	"fmt"
...
```