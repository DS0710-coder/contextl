# event.go

## Architecture Metrics
- **Path:** `event/event.go`
- **Extension:** `.go`
- **Size:** 5332 bytes
- **Centrality Score:** 0.0024
- **In-Degree (Imported By):** 46
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TypeMuxEvent`
- `TypeMux`
- `TypeMuxSubscription`
- `Subscribe`
- `Post`
- `Stop`
- `del`
- `find`
- `posdelete`
- `newsub`
- `Chan`
- `Unsubscribe`
- `Closed`
- `closewait`
- `deliver`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]

## Imported By (Dependents)
- [[accounts/abi/bind/v2/base.go.md|accounts/abi/bind/v2/base.go]]
- [[accounts/abi/bind/v2/lib.go.md|accounts/abi/bind/v2/lib.go]]
- [[accounts/accounts.go.md|accounts/accounts.go]]
- [[accounts/external/backend.go.md|accounts/external/backend.go]]
- [[accounts/keystore/keystore.go.md|accounts/keystore/keystore.go]]
- [[accounts/keystore/keystore_test.go.md|accounts/keystore/keystore_test.go]]
- [[accounts/manager.go.md|accounts/manager.go]]
- [[accounts/scwallet/hub.go.md|accounts/scwallet/hub.go]]
- [[accounts/usbwallet/hub.go.md|accounts/usbwallet/hub.go]]
- [[beacon/blsync/block_sync.go.md|beacon/blsync/block_sync.go]]
- [[beacon/blsync/client.go.md|beacon/blsync/client.go]]
- [[core/blockchain.go.md|core/blockchain.go]]
- [[core/blockchain_reader.go.md|core/blockchain_reader.go]]
- [[core/txindexer.go.md|core/txindexer.go]]
- [[core/txpool/blobpool/blobpool.go.md|core/txpool/blobpool/blobpool.go]]
- [[core/txpool/legacypool/legacypool.go.md|core/txpool/legacypool/legacypool.go]]
- [[core/txpool/legacypool/legacypool2_test.go.md|core/txpool/legacypool/legacypool2_test.go]]
- [[core/txpool/legacypool/legacypool_test.go.md|core/txpool/legacypool/legacypool_test.go]]
- [[core/txpool/subpool.go.md|core/txpool/subpool.go]]
- [[core/txpool/txpool.go.md|core/txpool/txpool.go]]
- [[eth/api_backend.go.md|eth/api_backend.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/catalyst/simulated_beacon.go.md|eth/catalyst/simulated_beacon.go]]
- [[eth/downloader/downloader.go.md|eth/downloader/downloader.go]]
- [[eth/downloader/peer.go.md|eth/downloader/peer.go]]
- [[eth/filters/filter_system.go.md|eth/filters/filter_system.go]]
- [[eth/filters/filter_system_test.go.md|eth/filters/filter_system_test.go]]
- [[eth/gasprice/gasprice.go.md|eth/gasprice/gasprice.go]]
- [[eth/gasprice/gasprice_test.go.md|eth/gasprice/gasprice_test.go]]
- [[eth/handler.go.md|eth/handler.go]]
- [[eth/handler_eth_test.go.md|eth/handler_eth_test.go]]
- [[eth/handler_test.go.md|eth/handler_test.go]]
- [[eth/protocols/snap/sync.go.md|eth/protocols/snap/sync.go]]
- [[eth/protocols/snap/syncv2.go.md|eth/protocols/snap/syncv2.go]]
- [[ethstats/ethstats.go.md|ethstats/ethstats.go]]
- [[event/example_feed_test.go.md|event/example_feed_test.go]]
- [[event/example_scope_test.go.md|event/example_scope_test.go]]
- [[event/example_subscription_test.go.md|event/example_subscription_test.go]]
- [[internal/ethapi/api_test.go.md|internal/ethapi/api_test.go]]
- [[internal/ethapi/backend.go.md|internal/ethapi/backend.go]]
- [[internal/ethapi/transaction_args_test.go.md|internal/ethapi/transaction_args_test.go]]
- [[miner/miner_test.go.md|miner/miner_test.go]]
- [[p2p/discover/table.go.md|p2p/discover/table.go]]
- [[p2p/message.go.md|p2p/message.go]]
- [[p2p/peer.go.md|p2p/peer.go]]
- [[p2p/server.go.md|p2p/server.go]]

## Source Code Snippet
```go
// Copyright 2014 The go-ethereum Authors
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

// Package event deals with subscriptions to real-time events.
package event

import (
...
```