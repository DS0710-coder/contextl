# syncer.go

## Architecture Metrics
- **Path:** `eth/syncer/syncer.go`
- **Extension:** `.go`
- **Size:** 7337 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 10

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `syncReq`
- `Config`
- `Syncer`
- `API`
- `Register`
- `APIs`
- `run`
- `Start`
- `Stop`
- `Sync`
- `NewAPI`
- `Sync`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[beacon/params/params.go.md|beacon/params/params.go]]
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[eth/downloader/downloader.go.md|eth/downloader/downloader.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[log/format.go.md|log/format.go]]
- [[node/node.go.md|node/node.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
- [[cmd/geth/config.go.md|cmd/geth/config.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]

## Source Code Snippet
```go
// Copyright 2025 The go-ethereum Authors
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

package syncer

import (
	"errors"
...
```