# config.go

## Architecture Metrics
- **Path:** `eth/ethconfig/config.go`
- **Extension:** `.go`
- **Size:** 9468 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 27
- **Out-Degree (Imports):** 16

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Config`
- `CreateConsensusEngine`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[consensus/beacon/consensus.go.md|consensus/beacon/consensus.go]]
- [[consensus/clique/clique.go.md|consensus/clique/clique.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[consensus/ethash/ethash.go.md|consensus/ethash/ethash.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/history/historymode.go.md|core/history/historymode.go]]
- [[core/txpool/blobpool/blobpool.go.md|core/txpool/blobpool/blobpool.go]]
- [[core/txpool/legacypool/legacypool.go.md|core/txpool/legacypool/legacypool.go]]
- [[eth/gasprice/gasprice.go.md|eth/gasprice/gasprice.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[log/format.go.md|log/format.go]]
- [[miner/miner.go.md|miner/miner.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[triedb/database.go.md|triedb/database.go]]
- [[triedb/pathdb/buffer.go.md|triedb/pathdb/buffer.go]]

## Imported By (Dependents)
- [[accounts/abi/bind/v2/lib_test.go.md|accounts/abi/bind/v2/lib_test.go]]
- [[cmd/devp2p/internal/ethtest/suite_test.go.md|cmd/devp2p/internal/ethtest/suite_test.go]]
- [[cmd/geth/config.go.md|cmd/geth/config.go]]
- [[cmd/utils/cmd.go.md|cmd/utils/cmd.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[console/console_test.go.md|console/console_test.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/catalyst/api.go.md|eth/catalyst/api.go]]
- [[eth/catalyst/api_test.go.md|eth/catalyst/api_test.go]]
- [[eth/catalyst/simulated_beacon_test.go.md|eth/catalyst/simulated_beacon_test.go]]
- [[eth/downloader/beaconsync.go.md|eth/downloader/beaconsync.go]]
- [[eth/downloader/downloader.go.md|eth/downloader/downloader.go]]
- [[eth/downloader/downloader_test.go.md|eth/downloader/downloader_test.go]]
- [[eth/downloader/events.go.md|eth/downloader/events.go]]
- [[eth/downloader/queue.go.md|eth/downloader/queue.go]]
- [[eth/downloader/syncmode.go.md|eth/downloader/syncmode.go]]
- [[eth/handler.go.md|eth/handler.go]]
- [[eth/handler_eth_test.go.md|eth/handler_eth_test.go]]
- [[eth/handler_test.go.md|eth/handler_test.go]]
- [[eth/sync_test.go.md|eth/sync_test.go]]
- [[eth/syncer/syncer.go.md|eth/syncer/syncer.go]]
- [[ethclient/ethclient_test.go.md|ethclient/ethclient_test.go]]
- [[ethclient/gethclient/gethclient_test.go.md|ethclient/gethclient/gethclient_test.go]]
- [[ethclient/simulated/backend.go.md|ethclient/simulated/backend.go]]
- [[ethclient/simulated/options.go.md|ethclient/simulated/options.go]]
- [[graphql/graphql_test.go.md|graphql/graphql_test.go]]
- [[miner/stress/main.go.md|miner/stress/main.go]]

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

// Package ethconfig contains the configuration of the ETH and LES protocols.
package ethconfig

import (
...
```