# gasprice_test.go

## Architecture Metrics
- **Path:** `eth/gasprice/gasprice_test.go`
- **Extension:** `.go`
- **Size:** 8341 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 12

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `testBackend`
- `HeaderByNumber`
- `BlockByNumber`
- `GetReceipts`
- `Pending`
- `ChainConfig`
- `SubscribeChainHeadEvent`
- `teardown`
- `newTestBackend`
- `CurrentHeader`
- `GetBlockByNumber`
- `TestSuggestTipCap`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[consensus/beacon/consensus.go.md|consensus/beacon/consensus.go]]
- [[consensus/ethash/ethash.go.md|consensus/ethash/ethash.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[crypto/kzg4844/kzg4844.go.md|crypto/kzg4844/kzg4844.go]]
- [[event/event.go.md|event/event.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rpc/client.go.md|rpc/client.go]]

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

package gasprice

import (
	"context"
...
```