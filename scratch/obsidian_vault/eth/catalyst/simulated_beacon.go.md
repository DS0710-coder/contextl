# simulated_beacon.go

## Architecture Metrics
- **Path:** `eth/catalyst/simulated_beacon.go`
- **Extension:** `.go`
- **Size:** 13612 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 15

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `withdrawalQueue`
- `newWithdrawalsEvent`
- `SimulatedBeacon`
- `add`
- `pop`
- `subscribe`
- `payloadVersion`
- `NewSimulatedBeacon`
- `setFeeRecipient`
- `Start`
- `Stop`
- `sealBlock`
- `loop`
- `finalizedBlockHash`
- `setCurrentState`
- `Commit`
- `Rollback`
- `Fork`
- `AdjustTime`
- `RegisterSimulatedBeaconAPIs`

## Imports (Dependencies)
- [[beacon/engine/bapl_encode.go.md|beacon/engine/bapl_encode.go]]
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[core/txpool/txpool.go.md|core/txpool/txpool.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/kzg4844/kzg4844.go.md|crypto/kzg4844/kzg4844.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[event/event.go.md|event/event.go]]
- [[internal/telemetry/telemetry.go.md|internal/telemetry/telemetry.go]]
- [[log/format.go.md|log/format.go]]
- [[node/node.go.md|node/node.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[params/forks/forks.go.md|params/forks/forks.go]]
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

package catalyst

import (
	"context"
...
```