# tracker.go

## Architecture Metrics
- **Path:** `p2p/tracker/tracker.go`
- **Extension:** `.go`
- **Size:** 8266 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 5
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Request`
- `Response`
- `Tracker`
- `New`
- `Track`
- `clean`
- `schedule`
- `Stop`
- `Fulfil`
- `trackedGauge`
- `lostMeter`
- `staleMeter`
- `waitHistogram`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[log/format.go.md|log/format.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]
- [[p2p/config.go.md|p2p/config.go]]

## Imported By (Dependents)
- [[eth/protocols/eth/dispatcher.go.md|eth/protocols/eth/dispatcher.go]]
- [[eth/protocols/eth/handlers.go.md|eth/protocols/eth/handlers.go]]
- [[eth/protocols/eth/peer.go.md|eth/protocols/eth/peer.go]]
- [[eth/protocols/snap/handlers.go.md|eth/protocols/snap/handlers.go]]
- [[eth/protocols/snap/peer.go.md|eth/protocols/snap/peer.go]]

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

package tracker

import (
	"container/list"
...
```