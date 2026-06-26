# client.go

## Architecture Metrics
- **Path:** `rpc/client.go`
- **Extension:** `.go`
- **Size:** 22723 bytes
- **Centrality Score:** 0.0040
- **In-Degree (Imported By):** 69
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BatchElem`
- `Client`
- `clientContextKey`
- `clientConn`
- `readOp`
- `requestOp`
- `newClientConn`
- `close`
- `wait`
- `Dial`
- `DialContext`
- `DialOptions`
- `ClientFromContext`
- `newClient`
- `initClient`
- `RegisterName`
- `nextID`
- `SupportedModules`
- `Close`
- `SetHeader`
- `Call`
- `CallContext`
- `BatchCall`
- `BatchCallContext`
- `Notify`
- `EthSubscribe`
- `Subscribe`
- `SupportsSubscriptions`
- `newMessage`
- `send`
- `sendBatch`
- `write`
- `writeBatch`
- `reconnect`
- `dispatch`
- `drainRead`
- `read`

## Imports (Dependencies)
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
- [[accounts/external/backend.go.md|accounts/external/backend.go]]
- [[beacon/blsync/client.go.md|beacon/blsync/client.go]]
- [[beacon/blsync/engineclient.go.md|beacon/blsync/engineclient.go]]
- [[beacon/engine/errors.go.md|beacon/engine/errors.go]]
- [[cmd/blsync/main.go.md|cmd/blsync/main.go]]
- [[cmd/devp2p/discv4cmd.go.md|cmd/devp2p/discv4cmd.go]]
- [[cmd/fetchpayload/main.go.md|cmd/fetchpayload/main.go]]
- [[cmd/geth/config.go.md|cmd/geth/config.go]]
- [[cmd/geth/run_test.go.md|cmd/geth/run_test.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[cmd/workload/client.go.md|cmd/workload/client.go]]
- [[cmd/workload/filtertest.go.md|cmd/workload/filtertest.go]]
- [[cmd/workload/filtertestfuzz.go.md|cmd/workload/filtertestfuzz.go]]
- [[cmd/workload/filtertestgen.go.md|cmd/workload/filtertestgen.go]]
- [[cmd/workload/testsuite.go.md|cmd/workload/testsuite.go]]
- [[console/bridge.go.md|console/bridge.go]]
- [[console/console.go.md|console/console.go]]
- [[eth/api_backend.go.md|eth/api_backend.go]]
- [[eth/api_debug.go.md|eth/api_debug.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/catalyst/api.go.md|eth/catalyst/api.go]]
- [[eth/catalyst/api_benchmark_test.go.md|eth/catalyst/api_benchmark_test.go]]
- [[eth/catalyst/api_test.go.md|eth/catalyst/api_test.go]]
- [[eth/catalyst/api_testing.go.md|eth/catalyst/api_testing.go]]
- [[eth/catalyst/simulated_beacon.go.md|eth/catalyst/simulated_beacon.go]]
- [[eth/downloader/api.go.md|eth/downloader/api.go]]
- [[eth/filters/api.go.md|eth/filters/api.go]]
- [[eth/filters/api_test.go.md|eth/filters/api_test.go]]
- [[eth/filters/filter.go.md|eth/filters/filter.go]]
- [[eth/filters/filter_system.go.md|eth/filters/filter_system.go]]
- [[eth/filters/filter_system_test.go.md|eth/filters/filter_system_test.go]]
- [[eth/filters/filter_test.go.md|eth/filters/filter_test.go]]
- [[eth/gasprice/feehistory.go.md|eth/gasprice/feehistory.go]]
- [[eth/gasprice/feehistory_test.go.md|eth/gasprice/feehistory_test.go]]
- [[eth/gasprice/gasprice.go.md|eth/gasprice/gasprice.go]]
- [[eth/gasprice/gasprice_test.go.md|eth/gasprice/gasprice_test.go]]
- [[eth/syncer/syncer.go.md|eth/syncer/syncer.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[eth/tracers/api_test.go.md|eth/tracers/api_test.go]]
- [[ethclient/ethclient.go.md|ethclient/ethclient.go]]
- [[ethclient/ethclient_test.go.md|ethclient/ethclient_test.go]]
- [[ethclient/gethclient/gethclient.go.md|ethclient/gethclient/gethclient.go]]
- [[ethclient/gethclient/gethclient_test.go.md|ethclient/gethclient/gethclient_test.go]]
- [[ethclient/simulated/backend.go.md|ethclient/simulated/backend.go]]
- [[ethdb/remotedb/remotedb.go.md|ethdb/remotedb/remotedb.go]]
- [[ethstats/ethstats.go.md|ethstats/ethstats.go]]
- [[graphql/graphql.go.md|graphql/graphql.go]]
- [[graphql/service.go.md|graphql/service.go]]
- [[internal/ethapi/api.go.md|internal/ethapi/api.go]]
- [[internal/ethapi/api_test.go.md|internal/ethapi/api_test.go]]
- [[internal/ethapi/backend.go.md|internal/ethapi/backend.go]]
- [[internal/ethapi/simulate.go.md|internal/ethapi/simulate.go]]
- [[internal/ethapi/transaction_args.go.md|internal/ethapi/transaction_args.go]]
- [[internal/ethapi/transaction_args_test.go.md|internal/ethapi/transaction_args_test.go]]
- [[internal/telemetry/tracesetup/setup.go.md|internal/telemetry/tracesetup/setup.go]]
- [[node/api.go.md|node/api.go]]
- [[node/api_test.go.md|node/api_test.go]]
- [[node/config.go.md|node/config.go]]
- [[node/defaults.go.md|node/defaults.go]]
- [[node/endpoints.go.md|node/endpoints.go]]
- [[node/jwt_auth.go.md|node/jwt_auth.go]]
- [[node/node.go.md|node/node.go]]
- [[node/node_auth_test.go.md|node/node_auth_test.go]]
- [[node/node_test.go.md|node/node_test.go]]
- [[node/rpcstack.go.md|node/rpcstack.go]]
- [[node/rpcstack_test.go.md|node/rpcstack_test.go]]
- [[node/utils_test.go.md|node/utils_test.go]]
- [[rpc/client_example_test.go.md|rpc/client_example_test.go]]
- [[rpc/client_opt_test.go.md|rpc/client_opt_test.go]]

## Source Code Snippet
```go
// Copyright 2016 The go-ethereum Authors
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

package rpc

import (
	"context"
...
```