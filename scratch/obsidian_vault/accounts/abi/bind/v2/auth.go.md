# auth.go

## Architecture Metrics
- **Path:** `accounts/abi/bind/v2/auth.go`
- **Extension:** `.go`
- **Size:** 3331 bytes
- **Centrality Score:** 0.0047
- **In-Degree (Imported By):** 83
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NewKeyStoreTransactor`
- `NewKeyedTransactor`
- `NewClefTransactor`

## Imports (Dependencies)
- [[accounts/accounts.go.md|accounts/accounts.go]]
- [[accounts/external/backend.go.md|accounts/external/backend.go]]
- [[accounts/keystore/keystore.go.md|accounts/keystore/keystore.go]]
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]

## Imported By (Dependents)
- [[accounts/abi/bind/old.go.md|accounts/abi/bind/old.go]]
- [[accounts/abi/bind/v2/base_test.go.md|accounts/abi/bind/v2/base_test.go]]
- [[accounts/abi/bind/v2/internal/contracts/db/bindings.go.md|accounts/abi/bind/v2/internal/contracts/db/bindings.go]]
- [[accounts/abi/bind/v2/internal/contracts/events/bindings.go.md|accounts/abi/bind/v2/internal/contracts/events/bindings.go]]
- [[accounts/abi/bind/v2/internal/contracts/nested_libraries/bindings.go.md|accounts/abi/bind/v2/internal/contracts/nested_libraries/bindings.go]]
- [[accounts/abi/bind/v2/internal/contracts/solc_errors/bindings.go.md|accounts/abi/bind/v2/internal/contracts/solc_errors/bindings.go]]
- [[accounts/abi/bind/v2/internal/contracts/uint256arrayreturn/bindings.go.md|accounts/abi/bind/v2/internal/contracts/uint256arrayreturn/bindings.go]]
- [[accounts/abi/bind/v2/lib_test.go.md|accounts/abi/bind/v2/lib_test.go]]
- [[accounts/abi/bind/v2/util_test.go.md|accounts/abi/bind/v2/util_test.go]]
- [[accounts/keystore/account_cache.go.md|accounts/keystore/account_cache.go]]
- [[accounts/keystore/file_cache.go.md|accounts/keystore/file_cache.go]]
- [[cmd/abigen/main.go.md|cmd/abigen/main.go]]
- [[cmd/blsync/main.go.md|cmd/blsync/main.go]]
- [[cmd/devp2p/discv4cmd.go.md|cmd/devp2p/discv4cmd.go]]
- [[cmd/devp2p/discv5cmd.go.md|cmd/devp2p/discv5cmd.go]]
- [[cmd/devp2p/dns_cloudflare.go.md|cmd/devp2p/dns_cloudflare.go]]
- [[cmd/devp2p/dns_route53.go.md|cmd/devp2p/dns_route53.go]]
- [[cmd/devp2p/dnscmd.go.md|cmd/devp2p/dnscmd.go]]
- [[cmd/devp2p/enrcmd.go.md|cmd/devp2p/enrcmd.go]]
- [[cmd/devp2p/keycmd.go.md|cmd/devp2p/keycmd.go]]
- [[cmd/devp2p/main.go.md|cmd/devp2p/main.go]]
- [[cmd/devp2p/nodesetcmd.go.md|cmd/devp2p/nodesetcmd.go]]
- [[cmd/devp2p/rlpxcmd.go.md|cmd/devp2p/rlpxcmd.go]]
- [[cmd/devp2p/runtest.go.md|cmd/devp2p/runtest.go]]
- [[cmd/era/main.go.md|cmd/era/main.go]]
- [[cmd/ethkey/changepassword.go.md|cmd/ethkey/changepassword.go]]
- [[cmd/ethkey/generate.go.md|cmd/ethkey/generate.go]]
- [[cmd/ethkey/inspect.go.md|cmd/ethkey/inspect.go]]
- [[cmd/ethkey/main.go.md|cmd/ethkey/main.go]]
- [[cmd/ethkey/message.go.md|cmd/ethkey/message.go]]
- [[cmd/ethkey/utils.go.md|cmd/ethkey/utils.go]]
- [[cmd/evm/blockrunner.go.md|cmd/evm/blockrunner.go]]
- [[cmd/evm/internal/t8ntool/block.go.md|cmd/evm/internal/t8ntool/block.go]]
- [[cmd/evm/internal/t8ntool/flags.go.md|cmd/evm/internal/t8ntool/flags.go]]
- [[cmd/evm/internal/t8ntool/transaction.go.md|cmd/evm/internal/t8ntool/transaction.go]]
- [[cmd/evm/internal/t8ntool/transition.go.md|cmd/evm/internal/t8ntool/transition.go]]
- [[cmd/evm/internal/t8ntool/utils.go.md|cmd/evm/internal/t8ntool/utils.go]]
- [[cmd/evm/main.go.md|cmd/evm/main.go]]
- [[cmd/evm/reporter.go.md|cmd/evm/reporter.go]]
- [[cmd/evm/runner.go.md|cmd/evm/runner.go]]
- [[cmd/evm/staterunner.go.md|cmd/evm/staterunner.go]]
- [[cmd/geth/accountcmd.go.md|cmd/geth/accountcmd.go]]
- [[cmd/geth/bintrie_convert.go.md|cmd/geth/bintrie_convert.go]]
- [[cmd/geth/chaincmd.go.md|cmd/geth/chaincmd.go]]
- [[cmd/geth/config.go.md|cmd/geth/config.go]]
- [[cmd/geth/consolecmd.go.md|cmd/geth/consolecmd.go]]
- [[cmd/geth/dbcmd.go.md|cmd/geth/dbcmd.go]]
- [[cmd/geth/logtestcmd_active.go.md|cmd/geth/logtestcmd_active.go]]
- [[cmd/geth/logtestcmd_inactive.go.md|cmd/geth/logtestcmd_inactive.go]]
- [[cmd/geth/main.go.md|cmd/geth/main.go]]
- [[cmd/geth/misccmd.go.md|cmd/geth/misccmd.go]]
- [[cmd/geth/snapshot.go.md|cmd/geth/snapshot.go]]
- [[cmd/utils/cmd.go.md|cmd/utils/cmd.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[cmd/utils/flags_legacy.go.md|cmd/utils/flags_legacy.go]]
- [[cmd/workload/client.go.md|cmd/workload/client.go]]
- [[cmd/workload/filtertestfuzz.go.md|cmd/workload/filtertestfuzz.go]]
- [[cmd/workload/filtertestgen.go.md|cmd/workload/filtertestgen.go]]
- [[cmd/workload/filtertestperf.go.md|cmd/workload/filtertestperf.go]]
- [[cmd/workload/historytestgen.go.md|cmd/workload/historytestgen.go]]
- [[cmd/workload/main.go.md|cmd/workload/main.go]]
- [[cmd/workload/prooftest.go.md|cmd/workload/prooftest.go]]
- [[cmd/workload/prooftestgen.go.md|cmd/workload/prooftestgen.go]]
- [[cmd/workload/testsuite.go.md|cmd/workload/testsuite.go]]
- [[cmd/workload/tracetest.go.md|cmd/workload/tracetest.go]]
- [[cmd/workload/tracetestgen.go.md|cmd/workload/tracetestgen.go]]
- [[consensus/ethash/consensus.go.md|consensus/ethash/consensus.go]]
- [[core/state/pruner/bloom.go.md|core/state/pruner/bloom.go]]
- [[core/state/snapshot/difflayer.go.md|core/state/snapshot/difflayer.go]]
- [[eth/protocols/eth/peer.go.md|eth/protocols/eth/peer.go]]
- [[ethdb/pebble/pebble.go.md|ethdb/pebble/pebble.go]]
- [[ethdb/pebble/pebble_test.go.md|ethdb/pebble/pebble_test.go]]
- [[ethdb/pebble/version.go.md|ethdb/pebble/version.go]]
- [[ethdb/pebble/version_test.go.md|ethdb/pebble/version_test.go]]
- [[internal/debug/flags.go.md|internal/debug/flags.go]]
- [[internal/debug/pyroscope.go.md|internal/debug/pyroscope.go]]
- [[internal/flags/categories.go.md|internal/flags/categories.go]]
- [[internal/flags/flags.go.md|internal/flags/flags.go]]
- [[internal/flags/helpers.go.md|internal/flags/helpers.go]]
- [[metrics/influxdb/influxdb_test.go.md|metrics/influxdb/influxdb_test.go]]
- [[metrics/influxdb/influxdbv1.go.md|metrics/influxdb/influxdbv1.go]]
- [[metrics/influxdb/influxdbv2.go.md|metrics/influxdb/influxdbv2.go]]
- [[rpc/websocket.go.md|rpc/websocket.go]]

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

package bind

import (
	"context"
...
```