# nat.go

## Architecture Metrics
- **Path:** `p2p/nat/nat.go`
- **Extension:** `.go`
- **Size:** 8071 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 5
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Interface`
- `autodisc`
- `Parse`
- `Map`
- `ExternalIP`
- `String`
- `MarshalText`
- `AddMapping`
- `DeleteMapping`
- `Any`
- `UPnP`
- `PMP`
- `startautodisc`
- `AddMapping`
- `DeleteMapping`
- `ExternalIP`
- `String`
- `MarshalText`
- `wait`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[node/defaults.go.md|node/defaults.go]]
- [[p2p/config.go.md|p2p/config.go]]
- [[p2p/config_toml.go.md|p2p/config_toml.go]]
- [[p2p/server_nat.go.md|p2p/server_nat.go]]

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

// Package nat provides access to common network port mapping protocols.
package nat

import (
...
```