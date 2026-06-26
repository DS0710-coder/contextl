# blobpool.go

## Architecture Metrics
- **Path:** `core/txpool/blobpool/blobpool.go`
- **Extension:** `.go`
- **Size:** 90658 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 7
- **Out-Degree (Imports):** 15

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `blobTxMeta`
- `blobTxForPool`
- `BlobPool`
- `Sidecar`
- `TxSize`
- `ToTx`
- `newBlobTxForPool`
- `encodeForNetwork`
- `newBlobTxMeta`
- `New`
- `Filter`
- `FilterType`
- `Init`
- `Close`
- `parseTransaction`
- `trackTransaction`
- `recheck`
- `offload`
- `Reset`
- `vhashesByTx`
- `getByVhash`
- `reorg`
- `reinject`
- `SetGasTip`
- `ValidateTxBasics`
- `checkDelegationLimit`
- `validateTx`
- `Has`
- `getRLP`
- `Get`
- `GetRLP`
- `GetMetadata`
- `getBlobs`
- `availableBlobs`
- `Add`
- `add`
- `addLocked`
- `drop`
- `Pending`
- `updateStorageMetrics`
- `updateLimboMetrics`
- `SubscribeTransactions`
- `Nonce`
- `gappedAllowance`
- `evictGapped`
- `isAnnouncable`
- `Stats`
- `Content`
- `ContentFrom`
- `Status`
- `Clear`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[consensus/misc/eip1559/eip1559.go.md|consensus/misc/eip1559/eip1559.go]]
- [[consensus/misc/eip4844/eip4844.go.md|consensus/misc/eip4844/eip4844.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/txpool/txpool.go.md|core/txpool/txpool.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/kzg4844/kzg4844.go.md|crypto/kzg4844/kzg4844.go]]
- [[event/event.go.md|event/event.go]]
- [[log/format.go.md|log/format.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[eth/api_backend_test.go.md|eth/api_backend_test.go]]
- [[eth/api_debug_test.go.md|eth/api_debug_test.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/ethconfig/gen_config.go.md|eth/ethconfig/gen_config.go]]
- [[eth/protocols/eth/handler_test.go.md|eth/protocols/eth/handler_test.go]]

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

// Package blobpool implements the EIP-4844 blob transaction pool.
package blobpool

import (
...
```