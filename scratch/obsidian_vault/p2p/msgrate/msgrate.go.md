# msgrate.go

## Architecture Metrics
- **Path:** `p2p/msgrate/msgrate.go`
- **Extension:** `.go`
- **Size:** 18418 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Tracker`
- `Trackers`
- `NewTracker`
- `Capacity`
- `roundCapacity`
- `Update`
- `NewTrackers`
- `Track`
- `Untrack`
- `MedianRoundTrip`
- `medianRoundTrip`
- `MeanCapacities`
- `meanCapacities`
- `TargetRoundTrip`
- `TargetTimeout`
- `targetTimeout`
- `tune`
- `detune`
- `Capacity`
- `Update`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
- [[eth/downloader/peer.go.md|eth/downloader/peer.go]]
- [[eth/protocols/snap/sync.go.md|eth/protocols/snap/sync.go]]
- [[eth/protocols/snap/syncv2.go.md|eth/protocols/snap/syncv2.go]]

## Source Code Snippet
```go
// Copyright 2021 The go-ethereum Authors
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

// Package msgrate allows estimating the throughput of peers for more balanced syncs.
package msgrate

import (
...
```