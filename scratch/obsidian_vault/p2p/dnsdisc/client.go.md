# client.go

## Architecture Metrics
- **Path:** `p2p/dnsdisc/client.go`
- **Extension:** `.go`
- **Size:** 10709 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Client`
- `Config`
- `Resolver`
- `randomIterator`
- `withDefaults`
- `NewClient`
- `SyncTree`
- `NewIterator`
- `resolveRoot`
- `parseAndVerifyRoot`
- `resolveEntry`
- `doResolveEntry`
- `newRandomIterator`
- `Node`
- `Close`
- `Next`
- `addTree`
- `nextNode`
- `pickTree`
- `syncableTrees`
- `waitForRootUpdates`
- `rebuildTrees`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/lru/lru.go.md|common/lru/lru.go]]
- [[common/mclock/mclock.go.md|common/mclock/mclock.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[log/format.go.md|log/format.go]]
- [[node/api.go.md|node/api.go]]
- [[p2p/enr/enr.go.md|p2p/enr/enr.go]]

## Imported By (Dependents)
- [[cmd/devp2p/dns_cloudflare.go.md|cmd/devp2p/dns_cloudflare.go]]
- [[cmd/devp2p/dns_route53.go.md|cmd/devp2p/dns_route53.go]]
- [[cmd/devp2p/dnscmd.go.md|cmd/devp2p/dnscmd.go]]
- [[eth/backend.go.md|eth/backend.go]]

## Source Code Snippet
```go
// Copyright 2019 The go-ethereum Authors
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

package dnsdisc

import (
	"bytes"
...
```