# node.go

## Architecture Metrics
- **Path:** `node/node.go`
- **Extension:** `.go`
- **Size:** 23469 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 27
- **Out-Degree (Imports):** 10

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Node`
- `closeTrackingDB`
- `New`
- `Start`
- `Close`
- `doClose`
- `openEndpoints`
- `stopServices`
- `openDataDir`
- `closeDataDir`
- `ObtainJWTSecret`
- `obtainJWTSecret`
- `startRPC`
- `wsServerForPort`
- `stopRPC`
- `startInProc`
- `stopInProc`
- `Wait`
- `RegisterLifecycle`
- `RegisterProtocols`
- `RegisterAPIs`
- `getAPIs`
- `RegisterHandler`
- `Attach`
- `RPCHandler`
- `Config`
- `Server`
- `DataDir`
- `InstanceDir`
- `KeyStoreDir`
- `AccountManager`
- `IPCEndpoint`
- `HTTPEndpoint`
- `WSEndpoint`
- `HTTPAuthEndpoint`
- `WSAuthEndpoint`
- `OpenDatabaseWithOptions`
- `OpenDatabase`
- `OpenDatabaseWithFreezer`
- `ResolvePath`
- `ResolveAncient`
- `Close`
- `wrapDatabase`
- `closeDatabases`

## Imports (Dependencies)
- [[accounts/accounts.go.md|accounts/accounts.go]]
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[ethdb/memorydb/memorydb.go.md|ethdb/memorydb/memorydb.go]]
- [[log/format.go.md|log/format.go]]
- [[p2p/config.go.md|p2p/config.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
- [[accounts/abi/bind/v2/lib_test.go.md|accounts/abi/bind/v2/lib_test.go]]
- [[cmd/blsync/main.go.md|cmd/blsync/main.go]]
- [[cmd/devp2p/internal/ethtest/suite_test.go.md|cmd/devp2p/internal/ethtest/suite_test.go]]
- [[cmd/geth/chaincmd.go.md|cmd/geth/chaincmd.go]]
- [[cmd/geth/config.go.md|cmd/geth/config.go]]
- [[cmd/geth/main.go.md|cmd/geth/main.go]]
- [[cmd/utils/cmd.go.md|cmd/utils/cmd.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[console/console_test.go.md|console/console_test.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/catalyst/api.go.md|eth/catalyst/api.go]]
- [[eth/catalyst/api_benchmark_test.go.md|eth/catalyst/api_benchmark_test.go]]
- [[eth/catalyst/api_test.go.md|eth/catalyst/api_test.go]]
- [[eth/catalyst/simulated_beacon.go.md|eth/catalyst/simulated_beacon.go]]
- [[eth/catalyst/simulated_beacon_test.go.md|eth/catalyst/simulated_beacon_test.go]]
- [[eth/syncer/syncer.go.md|eth/syncer/syncer.go]]
- [[ethclient/ethclient_test.go.md|ethclient/ethclient_test.go]]
- [[ethclient/example_test.go.md|ethclient/example_test.go]]
- [[ethclient/gethclient/gethclient_test.go.md|ethclient/gethclient/gethclient_test.go]]
- [[ethclient/simulated/backend.go.md|ethclient/simulated/backend.go]]
- [[ethclient/simulated/options.go.md|ethclient/simulated/options.go]]
- [[ethstats/ethstats.go.md|ethstats/ethstats.go]]
- [[graphql/graphql_test.go.md|graphql/graphql_test.go]]
- [[graphql/service.go.md|graphql/service.go]]
- [[internal/telemetry/tracesetup/setup.go.md|internal/telemetry/tracesetup/setup.go]]
- [[miner/stress/main.go.md|miner/stress/main.go]]
- [[node/node_example_test.go.md|node/node_example_test.go]]

## Source Code Snippet
```go
// Copyright 2015 The go-ethereum Authors
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

package node

import (
	crand "crypto/rand"
...
```