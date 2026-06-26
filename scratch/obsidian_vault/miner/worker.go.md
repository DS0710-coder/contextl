# worker.go

## Architecture Metrics
- **Path:** `miner/worker.go`
- **Extension:** `.go`
- **Size:** 23867 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 14

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `environment`
- `newPayloadResult`
- `generateParams`
- `maxBlobsPerBlock`
- `txFitsSize`
- `discard`
- `generateWork`
- `prepareWork`
- `makeEnv`
- `commitTransaction`
- `commitBlobTransaction`
- `applyTransaction`
- `commitTransactions`
- `fillTransactions`
- `totalFees`
- `signalToErr`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[consensus/misc/eip1559/eip1559.go.md|consensus/misc/eip1559/eip1559.go]]
- [[consensus/misc/eip4844/eip4844.go.md|consensus/misc/eip4844/eip4844.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/stateless.go.md|core/stateless.go]]
- [[core/txpool/txorder/ordering.go.md|core/txpool/txorder/ordering.go]]
- [[core/txpool/txpool.go.md|core/txpool/txpool.go]]
- [[core/types.go.md|core/types.go]]
- [[core/types/bal/bal.go.md|core/types/bal/bal.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[internal/telemetry/telemetry.go.md|internal/telemetry/telemetry.go]]
- [[log/format.go.md|log/format.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2015 The go-ethereum Authors
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

package miner

import (
	"context"
...
```