# runtime.go

## Architecture Metrics
- **Path:** `core/vm/runtime/runtime.go`
- **Extension:** `.go`
- **Size:** 7985 bytes
- **Centrality Score:** 0.0051
- **In-Degree (Imported By):** 55
- **Out-Degree (Imports):** 8

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Config`
- `setDefaults`
- `Execute`
- `Create`
- `Call`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
- [[accounts/abi/abigen/bind_test.go.md|accounts/abi/abigen/bind_test.go]]
- [[accounts/keystore/keystore.go.md|accounts/keystore/keystore.go]]
- [[accounts/keystore/keystore_test.go.md|accounts/keystore/keystore_test.go]]
- [[accounts/usbwallet/hub.go.md|accounts/usbwallet/hub.go]]
- [[cmd/evm/runner.go.md|cmd/evm/runner.go]]
- [[cmd/geth/accountcmd_test.go.md|cmd/geth/accountcmd_test.go]]
- [[cmd/geth/bintrie_convert.go.md|cmd/geth/bintrie_convert.go]]
- [[cmd/geth/chaincmd.go.md|cmd/geth/chaincmd.go]]
- [[cmd/geth/config.go.md|cmd/geth/config.go]]
- [[cmd/geth/consolecmd_test.go.md|cmd/geth/consolecmd_test.go]]
- [[cmd/geth/misccmd.go.md|cmd/geth/misccmd.go]]
- [[cmd/geth/snapshot.go.md|cmd/geth/snapshot.go]]
- [[cmd/utils/cmd.go.md|cmd/utils/cmd.go]]
- [[common/bitutil/bitutil.go.md|common/bitutil/bitutil.go]]
- [[common/debug.go.md|common/debug.go]]
- [[core/blockchain.go.md|core/blockchain.go]]
- [[core/rawdb/chain_iterator.go.md|core/rawdb/chain_iterator.go]]
- [[core/rawdb/database.go.md|core/rawdb/database.go]]
- [[core/sender_cacher.go.md|core/sender_cacher.go]]
- [[core/state/snapshot/conversion.go.md|core/state/snapshot/conversion.go]]
- [[core/state/state_sizer.go.md|core/state/state_sizer.go]]
- [[core/state_prefetcher.go.md|core/state_prefetcher.go]]
- [[core/vm/runtime/runtime_example_test.go.md|core/vm/runtime/runtime_example_test.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/filters/filter_system_test.go.md|eth/filters/filter_system_test.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[ethclient/gethclient/gethclient.go.md|ethclient/gethclient/gethclient.go]]
- [[ethdb/pebble/pebble.go.md|ethdb/pebble/pebble.go]]
- [[ethdb/pebble/pebble_v1.go.md|ethdb/pebble/pebble_v1.go]]
- [[ethdb/pebble/version.go.md|ethdb/pebble/version.go]]
- [[ethstats/ethstats.go.md|ethstats/ethstats.go]]
- [[internal/debug/api.go.md|internal/debug/api.go]]
- [[internal/debug/flags.go.md|internal/debug/flags.go]]
- [[internal/flags/flags_test.go.md|internal/flags/flags_test.go]]
- [[internal/utesting/utesting.go.md|internal/utesting/utesting.go]]
- [[internal/version/version.go.md|internal/version/version.go]]
- [[log/handler_glog.go.md|log/handler_glog.go]]
- [[log/logger.go.md|log/logger.go]]
- [[metrics/debug_test.go.md|metrics/debug_test.go]]
- [[metrics/influxdb/influxdb_test.go.md|metrics/influxdb/influxdb_test.go]]
- [[node/config.go.md|node/config.go]]
- [[node/config_test.go.md|node/config_test.go]]
- [[node/defaults.go.md|node/defaults.go]]
- [[p2p/enode/iter_test.go.md|p2p/enode/iter_test.go]]
- [[p2p/message_test.go.md|p2p/message_test.go]]
- [[p2p/nat/natupnp_test.go.md|p2p/nat/natupnp_test.go]]
- [[rlp/encode_test.go.md|rlp/encode_test.go]]
- [[rlp/rlpgen/gen_test.go.md|rlp/rlpgen/gen_test.go]]
- [[rpc/client_test.go.md|rpc/client_test.go]]
- [[rpc/service.go.md|rpc/service.go]]
- [[tests/init_test.go.md|tests/init_test.go]]
- [[trie/bintrie/store_commit.go.md|trie/bintrie/store_commit.go]]
- [[trie/secure_trie_test.go.md|trie/secure_trie_test.go]]
- [[triedb/internal/conversion.go.md|triedb/internal/conversion.go]]
- [[triedb/pathdb/history_indexer.go.md|triedb/pathdb/history_indexer.go]]

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

package runtime

import (
	"math"
...
```