# api_admin.go

## Architecture Metrics
- **Path:** `eth/api_admin.go`
- **Extension:** `.go`
- **Size:** 4068 bytes
- **Centrality Score:** 0.0014
- **In-Degree (Imported By):** 40
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `AdminAPI`
- `NewAdminAPI`
- `ExportChain`
- `hasAllBlocks`
- `ImportChain`

## Imports (Dependencies)
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/types.go.md|core/types.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
- [[cmd/devp2p/internal/ethtest/chain.go.md|cmd/devp2p/internal/ethtest/chain.go]]
- [[cmd/devp2p/internal/ethtest/chain_test.go.md|cmd/devp2p/internal/ethtest/chain_test.go]]
- [[cmd/devp2p/internal/ethtest/conn.go.md|cmd/devp2p/internal/ethtest/conn.go]]
- [[cmd/devp2p/internal/ethtest/suite.go.md|cmd/devp2p/internal/ethtest/suite.go]]
- [[cmd/devp2p/internal/ethtest/suite_test.go.md|cmd/devp2p/internal/ethtest/suite_test.go]]
- [[cmd/devp2p/internal/ethtest/transaction.go.md|cmd/devp2p/internal/ethtest/transaction.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[console/console_test.go.md|console/console_test.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/catalyst/api.go.md|eth/catalyst/api.go]]
- [[eth/catalyst/api_benchmark_test.go.md|eth/catalyst/api_benchmark_test.go]]
- [[eth/catalyst/api_test.go.md|eth/catalyst/api_test.go]]
- [[eth/catalyst/api_testing.go.md|eth/catalyst/api_testing.go]]
- [[eth/catalyst/simulated_beacon.go.md|eth/catalyst/simulated_beacon.go]]
- [[eth/catalyst/simulated_beacon_test.go.md|eth/catalyst/simulated_beacon_test.go]]
- [[eth/downloader/downloader_test.go.md|eth/downloader/downloader_test.go]]
- [[eth/downloader/fetchers.go.md|eth/downloader/fetchers.go]]
- [[eth/downloader/fetchers_concurrent.go.md|eth/downloader/fetchers_concurrent.go]]
- [[eth/downloader/fetchers_concurrent_bodies.go.md|eth/downloader/fetchers_concurrent_bodies.go]]
- [[eth/downloader/fetchers_concurrent_receipts.go.md|eth/downloader/fetchers_concurrent_receipts.go]]
- [[eth/downloader/peer.go.md|eth/downloader/peer.go]]
- [[eth/downloader/queue.go.md|eth/downloader/queue.go]]
- [[eth/downloader/queue_test.go.md|eth/downloader/queue_test.go]]
- [[eth/downloader/skeleton.go.md|eth/downloader/skeleton.go]]
- [[eth/downloader/skeleton_test.go.md|eth/downloader/skeleton_test.go]]
- [[eth/handler.go.md|eth/handler.go]]
- [[eth/handler_eth.go.md|eth/handler_eth.go]]
- [[eth/handler_eth_test.go.md|eth/handler_eth_test.go]]
- [[eth/handler_test.go.md|eth/handler_test.go]]
- [[eth/peer.go.md|eth/peer.go]]
- [[eth/peerset.go.md|eth/peerset.go]]
- [[eth/sync.go.md|eth/sync.go]]
- [[eth/sync_test.go.md|eth/sync_test.go]]
- [[eth/syncer/syncer.go.md|eth/syncer/syncer.go]]
- [[ethclient/ethclient_test.go.md|ethclient/ethclient_test.go]]
- [[ethclient/gethclient/gethclient_test.go.md|ethclient/gethclient/gethclient_test.go]]
- [[ethclient/simulated/backend.go.md|ethclient/simulated/backend.go]]
- [[ethstats/ethstats.go.md|ethstats/ethstats.go]]
- [[graphql/graphql_test.go.md|graphql/graphql_test.go]]
- [[miner/stress/main.go.md|miner/stress/main.go]]

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

package eth

import (
	"compress/gzip"
...
```