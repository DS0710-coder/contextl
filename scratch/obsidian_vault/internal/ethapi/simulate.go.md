# simulate.go

## Architecture Metrics
- **Path:** `internal/ethapi/simulate.go`
- **Extension:** `.go`
- **Size:** 21198 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 14

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `simBlock`
- `simCallResult`
- `simBlockResult`
- `simOpts`
- `simChainHeadReader`
- `gasBudget`
- `simulator`
- `simBackend`
- `MarshalJSON`
- `MarshalJSON`
- `Config`
- `CurrentHeader`
- `GetHeader`
- `GetHeaderByNumber`
- `GetHeaderByHash`
- `newGasBudget`
- `cap`
- `consume`
- `execute`
- `processBlock`
- `repairLogs`
- `sanitizeCall`
- `activePrecompiles`
- `sanitizeChain`
- `makeHeaders`
- `newSimulatedChainContext`
- `Engine`
- `HeaderByNumber`
- `ChainConfig`
- `HeaderByHash`
- `CurrentHeader`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[consensus/misc/eip1559/eip1559.go.md|consensus/misc/eip1559/eip1559.go]]
- [[consensus/misc/eip4844/eip4844.go.md|consensus/misc/eip4844/eip4844.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/types.go.md|core/types.go]]
- [[core/types/bal/bal.go.md|core/types/bal/bal.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[internal/ethapi/override/override.go.md|internal/ethapi/override/override.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
*Not imported by any file*

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

package ethapi

import (
	"context"
...
```