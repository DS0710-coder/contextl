# telemetry.go

## Architecture Metrics
- **Path:** `internal/telemetry/telemetry.go`
- **Extension:** `.go`
- **Size:** 5844 bytes
- **Centrality Score:** 0.0005
- **In-Degree (Imported By):** 9
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `RPCInfo`
- `StringAttribute`
- `Int64Attribute`
- `IntAttribute`
- `BoolAttribute`
- `StartSpan`
- `StartSpanWithTracer`
- `TracerFromContext`
- `StartCallServerSpan`
- `StartBatchServerSpan`
- `StartBatchCallSpan`
- `startSpan`
- `endSpan`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[core/blockchain.go.md|core/blockchain.go]]
- [[core/state_processor.go.md|core/state_processor.go]]
- [[core/txpool/blobpool/cache.go.md|core/txpool/blobpool/cache.go]]
- [[eth/catalyst/api.go.md|eth/catalyst/api.go]]
- [[eth/catalyst/simulated_beacon.go.md|eth/catalyst/simulated_beacon.go]]
- [[miner/payload_building.go.md|miner/payload_building.go]]
- [[miner/worker.go.md|miner/worker.go]]
- [[rpc/handler.go.md|rpc/handler.go]]
- [[rpc/http.go.md|rpc/http.go]]

## Source Code Snippet
```go
// Copyright 2026 The go-ethereum Authors
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

package telemetry

import (
	"context"
...
```