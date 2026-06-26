# backend.go

## Architecture Metrics
- **Path:** `eth/backend.go`
- **Extension:** `.go`
- **Size:** 21172 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 39

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Ethereum`
- `New`
- `makeExtraData`
- `APIs`
- `ResetWithGenesisBlock`
- `Miner`
- `AccountManager`
- `BlockChain`
- `TxPool`
- `BlobTxPool`
- `BlobCache`
- `Engine`
- `ChainDb`
- `IsListening`
- `Downloader`
- `Synced`
- `SetSynced`
- `ArchiveMode`
- `Protocols`
- `Start`
- `newChainView`
- `updateFilterMapsHeads`
- `setupDiscovery`
- `Stop`

## Imports (Dependencies)
- [[accounts/accounts.go.md|accounts/accounts.go]]
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/filtermaps/filtermaps.go.md|core/filtermaps/filtermaps.go]]
- [[core/history/historymode.go.md|core/history/historymode.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/state/pruner/pruner.go.md|core/state/pruner/pruner.go]]
- [[core/txpool/blobpool/blobpool.go.md|core/txpool/blobpool/blobpool.go]]
- [[core/txpool/legacypool/legacypool.go.md|core/txpool/legacypool/legacypool.go]]
- [[core/txpool/locals/errors.go.md|core/txpool/locals/errors.go]]
- [[core/txpool/txpool.go.md|core/txpool/txpool.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[eth/downloader/downloader.go.md|eth/downloader/downloader.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/gasprice/gasprice.go.md|eth/gasprice/gasprice.go]]
- [[eth/protocols/snap/bal_apply.go.md|eth/protocols/snap/bal_apply.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[event/event.go.md|event/event.go]]
- [[internal/ethapi/addrlock.go.md|internal/ethapi/addrlock.go]]
- [[internal/shutdowncheck/shutdown_tracker.go.md|internal/shutdowncheck/shutdown_tracker.go]]
- [[internal/version/version.go.md|internal/version/version.go]]
- [[log/format.go.md|log/format.go]]
- [[miner/miner.go.md|miner/miner.go]]
- [[node/api.go.md|node/api.go]]
- [[node/node.go.md|node/node.go]]
- [[p2p/config.go.md|p2p/config.go]]
- [[p2p/dnsdisc/client.go.md|p2p/dnsdisc/client.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[rpc/client.go.md|rpc/client.go]]
- [[version/version.go.md|version/version.go]]

## Imported By (Dependents)
*Not imported by any file*

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

// Package eth implements the Ethereum protocol.
package eth

import (
...
```