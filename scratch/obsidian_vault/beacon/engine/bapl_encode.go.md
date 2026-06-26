# bapl_encode.go

## Architecture Metrics
- **Path:** `beacon/engine/bapl_encode.go`
- **Extension:** `.go`
- **Size:** 1896 bytes
- **Centrality Score:** 0.0005
- **In-Degree (Imported By):** 11
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `MarshalJSON`
- `marshalBlobAndProofV1`
- `MarshalJSON`
- `marshalBlobAndProofV2`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[beacon/blsync/engineclient.go.md|beacon/blsync/engineclient.go]]
- [[eth/catalyst/api.go.md|eth/catalyst/api.go]]
- [[eth/catalyst/api_benchmark_test.go.md|eth/catalyst/api_benchmark_test.go]]
- [[eth/catalyst/api_test.go.md|eth/catalyst/api_test.go]]
- [[eth/catalyst/api_testing.go.md|eth/catalyst/api_testing.go]]
- [[eth/catalyst/api_testing_test.go.md|eth/catalyst/api_testing_test.go]]
- [[eth/catalyst/queue.go.md|eth/catalyst/queue.go]]
- [[eth/catalyst/simulated_beacon.go.md|eth/catalyst/simulated_beacon.go]]
- [[eth/catalyst/witness.go.md|eth/catalyst/witness.go]]
- [[miner/payload_building.go.md|miner/payload_building.go]]
- [[miner/payload_building_test.go.md|miner/payload_building_test.go]]

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

package engine

import (
	"github.com/fjl/jsonw"
...
```