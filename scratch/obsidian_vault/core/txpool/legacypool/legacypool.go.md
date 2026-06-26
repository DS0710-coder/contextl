# legacypool.go

## Architecture Metrics
- **Path:** `core/txpool/legacypool/legacypool.go`
- **Extension:** `.go`
- **Size:** 65215 bytes
- **Centrality Score:** 0.0006
- **In-Degree (Imported By):** 13
- **Out-Degree (Imports):** 14

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BlockChain`
- `Config`
- `LegacyPool`
- `txpoolResetRequest`
- `accountSet`
- `lookup`
- `sanitize`
- `New`
- `Filter`
- `FilterType`
- `Init`
- `loop`
- `Close`
- `Reset`
- `SubscribeTransactions`
- `SetGasTip`
- `Nonce`
- `Stats`
- `stats`
- `Content`
- `ContentFrom`
- `Pending`
- `ValidateTxBasics`
- `validateTx`
- `checkDelegationLimit`
- `validateAuth`
- `add`
- `isGapped`
- `enqueueTx`
- `promoteTx`
- `addRemotes`
- `addRemote`
- `addRemotesSync`
- `addRemoteSync`
- `Add`
- `addTxsLocked`
- `Status`
- `Get`
- `get`
- `GetRLP`
- `GetMetadata`
- `Has`
- `removeTx`
- `requestReset`
- `requestPromoteExecutables`
- `queueTxEvent`
- `scheduleReorgLoop`
- `runReorg`
- `reset`
- `promoteExecutables`
- `truncatePending`
- `truncateQueue`
- `demoteUnexecutables`
- `newAccountSet`
- `add`
- `addTx`
- `flatten`
- `merge`
- `newLookup`
- `Range`
- `Get`
- `Count`
- `Slots`
- `Add`
- `Remove`
- `Clear`
- `TxsBelowTip`
- `addAuthorities`
- `removeAuthorities`
- `hasAuth`
- `numSlots`
- `Clear`
- `HasPendingAuth`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[common/prque/prque.go.md|common/prque/prque.go]]
- [[consensus/misc/eip1559/eip1559.go.md|consensus/misc/eip1559/eip1559.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/txpool/txpool.go.md|core/txpool/txpool.go]]
- [[core/types.go.md|core/types.go]]
- [[event/event.go.md|event/event.go]]
- [[log/format.go.md|log/format.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[core/txpool/locals/errors.go.md|core/txpool/locals/errors.go]]
- [[core/txpool/locals/tx_tracker.go.md|core/txpool/locals/tx_tracker.go]]
- [[core/txpool/locals/tx_tracker_test.go.md|core/txpool/locals/tx_tracker_test.go]]
- [[eth/api_backend_test.go.md|eth/api_backend_test.go]]
- [[eth/api_debug_test.go.md|eth/api_debug_test.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/ethconfig/gen_config.go.md|eth/ethconfig/gen_config.go]]
- [[eth/protocols/eth/handler_test.go.md|eth/protocols/eth/handler_test.go]]
- [[miner/miner_test.go.md|miner/miner_test.go]]
- [[miner/payload_building_test.go.md|miner/payload_building_test.go]]
- [[miner/stress/main.go.md|miner/stress/main.go]]

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

// Package legacypool implements the normal EVM execution transaction pool.
package legacypool

import (
...
```