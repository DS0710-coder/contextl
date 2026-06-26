# api_server.go

## Architecture Metrics
- **Path:** `beacon/light/api/api_server.go`
- **Extension:** `.go`
- **Size:** 4544 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ApiServer`
- `NewApiServer`
- `Subscribe`
- `SendRequest`
- `Unsubscribe`
- `Name`

## Imports (Dependencies)
- [[beacon/light/request/scheduler.go.md|beacon/light/request/scheduler.go]]
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[beacon/types/beacon_block.go.md|beacon/types/beacon_block.go]]
- [[common/big.go.md|common/big.go]]
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
- [[beacon/blsync/client.go.md|beacon/blsync/client.go]]
- [[metrics/influxdb/influxdbv2.go.md|metrics/influxdb/influxdbv2.go]]

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

package api

import (
	"reflect"
...
```