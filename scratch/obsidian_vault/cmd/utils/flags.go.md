# flags.go

## Architecture Metrics
- **Path:** `cmd/utils/flags.go`
- **Extension:** `.go`
- **Size:** 89081 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 43

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `MakeDataDir`
- `setNodeKey`
- `setNodeUserIdent`
- `setBootstrapNodes`
- `mustParseBootnodes`
- `setBootstrapNodesV5`
- `setListenAddress`
- `setNAT`
- `SplitAndTrim`
- `setHTTP`
- `setGraphQL`
- `setWS`
- `setIPC`
- `MakeDatabaseHandles`
- `setEtherbase`
- `SetP2PConfig`
- `SetNodeConfig`
- `setSmartCard`
- `setOpenTelemetry`
- `SetDataDir`
- `setGPO`
- `setTxPool`
- `setBlobPool`
- `setMiner`
- `setRequiredBlocks`
- `SetEthConfig`
- `MakeBeaconLightConfig`
- `SetDNSDiscoveryDefaults`
- `RegisterEthService`
- `RegisterEthStatsService`
- `RegisterGraphQLService`
- `RegisterFilterAPI`
- `RegisterSyncOverrideService`
- `SetupMetrics`
- `SplitTagsFlag`
- `MakeChainDatabase`
- `tryMakeReadOnlyDatabase`
- `IsNetworkPreset`
- `DialRPCWithHeaders`
- `MakeGenesis`
- `MakeChain`
- `MakeConsolePreloads`
- `MakeTrieDatabase`

## Imports (Dependencies)
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[accounts/accounts.go.md|accounts/accounts.go]]
- [[accounts/keystore/keystore.go.md|accounts/keystore/keystore.go]]
- [[beacon/params/params.go.md|beacon/params/params.go]]
- [[common/big.go.md|common/big.go]]
- [[common/fdlimit/fdlimit_bsd.go.md|common/fdlimit/fdlimit_bsd.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/txpool/blobpool/blobpool.go.md|core/txpool/blobpool/blobpool.go]]
- [[core/txpool/legacypool/legacypool.go.md|core/txpool/legacypool/legacypool.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[crypto/kzg4844/kzg4844.go.md|crypto/kzg4844/kzg4844.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/filters/api.go.md|eth/filters/api.go]]
- [[eth/gasprice/gasprice.go.md|eth/gasprice/gasprice.go]]
- [[eth/syncer/syncer.go.md|eth/syncer/syncer.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[ethdb/remotedb/remotedb.go.md|ethdb/remotedb/remotedb.go]]
- [[ethstats/ethstats.go.md|ethstats/ethstats.go]]
- [[graphql/graphql.go.md|graphql/graphql.go]]
- [[internal/debug/api.go.md|internal/debug/api.go]]
- [[internal/ethapi/addrlock.go.md|internal/ethapi/addrlock.go]]
- [[internal/flags/flags.go.md|internal/flags/flags.go]]
- [[internal/memlimit/probe.go.md|internal/memlimit/probe.go]]
- [[log/format.go.md|log/format.go]]
- [[metrics/exp/exp.go.md|metrics/exp/exp.go]]
- [[metrics/influxdb/influxdb.go.md|metrics/influxdb/influxdb.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]
- [[miner/miner.go.md|miner/miner.go]]
- [[node/api.go.md|node/api.go]]
- [[node/node.go.md|node/node.go]]
- [[p2p/config.go.md|p2p/config.go]]
- [[p2p/nat/nat.go.md|p2p/nat/nat.go]]
- [[p2p/netutil/addrutil.go.md|p2p/netutil/addrutil.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rpc/client.go.md|rpc/client.go]]
- [[triedb/database.go.md|triedb/database.go]]
- [[triedb/hashdb/database.go.md|triedb/hashdb/database.go]]
- [[triedb/pathdb/buffer.go.md|triedb/pathdb/buffer.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2015 The go-ethereum Authors
// This file is part of go-ethereum.
//
// go-ethereum is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// go-ethereum is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with go-ethereum. If not, see <http://www.gnu.org/licenses/>.

// Package utils contains internal helper functions for go-ethereum commands.
package utils

import (
...
```