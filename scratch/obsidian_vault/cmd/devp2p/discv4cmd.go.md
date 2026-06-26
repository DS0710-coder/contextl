# discv4cmd.go

## Architecture Metrics
- **Path:** `cmd/devp2p/discv4cmd.go`
- **Extension:** `.go`
- **Size:** 10418 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `discv4API`
- `discv4Ping`
- `discv4Listen`
- `discv4RequestRecord`
- `discv4Resolve`
- `discv4ResolveJSON`
- `discv4Crawl`
- `discv4Test`
- `startV4`
- `makeDiscoveryConfig`
- `parseExtAddr`
- `listen`
- `parseBootnodes`
- `LookupRandom`
- `Buckets`
- `Self`

## Imports (Dependencies)
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[cmd/devp2p/internal/v4test/discv4tests.go.md|cmd/devp2p/internal/v4test/discv4tests.go]]
- [[common/big.go.md|common/big.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[log/format.go.md|log/format.go]]
- [[node/api.go.md|node/api.go]]
- [[p2p/discover/common.go.md|p2p/discover/common.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2019 The go-ethereum Authors
// This file is part of go-ethereum.
//
// go-ethereum is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// go-ethereum is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with go-ethereum. If not, see <http://www.gnu.org/licenses/>.

package main

import (
	"errors"
...
```