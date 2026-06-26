# miner.go

## Architecture Metrics
- **Path:** `miner/miner.go`
- **Extension:** `.go`
- **Size:** 6563 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 10
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Backend`
- `Config`
- `Miner`
- `New`
- `Pending`
- `SetExtra`
- `SetPrioAddresses`
- `SetGasCeil`
- `SetGasTip`
- `BuildPayload`
- `getPending`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/txpool/txpool.go.md|core/txpool/txpool.go]]
- [[core/types.go.md|core/types.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[console/console_test.go.md|console/console_test.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/catalyst/api.go.md|eth/catalyst/api.go]]
- [[eth/catalyst/api_test.go.md|eth/catalyst/api_test.go]]
- [[eth/catalyst/api_testing.go.md|eth/catalyst/api_testing.go]]
- [[eth/catalyst/queue.go.md|eth/catalyst/queue.go]]
- [[eth/catalyst/simulated_beacon_test.go.md|eth/catalyst/simulated_beacon_test.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/ethconfig/gen_config.go.md|eth/ethconfig/gen_config.go]]

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

// Package miner implements Ethereum block creation and mining.
package miner

import (
...
```