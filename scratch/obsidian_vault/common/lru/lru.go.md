# lru.go

## Architecture Metrics
- **Path:** `common/lru/lru.go`
- **Extension:** `.go`
- **Size:** 2539 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 19
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Cache`
- `NewCache`
- `Add`
- `Contains`
- `Get`
- `Len`
- `Peek`
- `Purge`
- `Remove`
- `Keys`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]

## Imported By (Dependents)
- [[beacon/blsync/block_sync.go.md|beacon/blsync/block_sync.go]]
- [[beacon/light/canonical.go.md|beacon/light/canonical.go]]
- [[beacon/light/committee_chain.go.md|beacon/light/committee_chain.go]]
- [[cmd/workload/filtertestfuzz.go.md|cmd/workload/filtertestfuzz.go]]
- [[consensus/clique/clique.go.md|consensus/clique/clique.go]]
- [[consensus/clique/snapshot.go.md|consensus/clique/snapshot.go]]
- [[core/blockchain.go.md|core/blockchain.go]]
- [[core/filtermaps/filtermaps.go.md|core/filtermaps/filtermaps.go]]
- [[core/filtermaps/map_renderer.go.md|core/filtermaps/map_renderer.go]]
- [[core/headerchain.go.md|core/headerchain.go]]
- [[core/jumpdest.go.md|core/jumpdest.go]]
- [[core/rawdb/eradb/eradb.go.md|core/rawdb/eradb/eradb.go]]
- [[core/state/database_code.go.md|core/state/database_code.go]]
- [[core/stateless.go.md|core/stateless.go]]
- [[eth/fetcher/tx_fetcher.go.md|eth/fetcher/tx_fetcher.go]]
- [[eth/filters/filter_system.go.md|eth/filters/filter_system.go]]
- [[eth/gasprice/gasprice.go.md|eth/gasprice/gasprice.go]]
- [[p2p/discover/v5wire/session.go.md|p2p/discover/v5wire/session.go]]
- [[p2p/dnsdisc/client.go.md|p2p/dnsdisc/client.go]]

## Source Code Snippet
```go
// Copyright 2022 The go-ethereum Authors
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

package lru

import "sync"

...
```