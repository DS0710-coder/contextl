# database.go

## Architecture Metrics
- **Path:** `triedb/database.go`
- **Extension:** `.go`
- **Size:** 14515 bytes
- **Centrality Score:** 0.0023
- **In-Degree (Imported By):** 66
- **Out-Degree (Imports):** 8

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Config`
- `backend`
- `Database`
- `NewDatabase`
- `NodeReader`
- `StateReader`
- `HistoricStateReader`
- `HistoricNodeReader`
- `Update`
- `Commit`
- `Size`
- `Scheme`
- `Close`
- `WritePreimages`
- `Preimage`
- `InsertPreimage`
- `PreimageEnabled`
- `Cap`
- `Reference`
- `Dereference`
- `Recover`
- `Recoverable`
- `Disable`
- `Enable`
- `AdoptSyncedState`
- `Journal`
- `VerifyState`
- `AccountIterator`
- `StorageIterator`
- `IndexProgress`
- `IsUBT`
- `Disk`
- `SnapshotCompleted`
- `BinTrieGroupDepth`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[log/format.go.md|log/format.go]]
- [[node/api.go.md|node/api.go]]
- [[triedb/database.go.md|triedb/database.go]]
- [[triedb/hashdb/database.go.md|triedb/hashdb/database.go]]
- [[triedb/pathdb/buffer.go.md|triedb/pathdb/buffer.go]]

## Imported By (Dependents)
- [[cmd/evm/internal/t8ntool/execution.go.md|cmd/evm/internal/t8ntool/execution.go]]
- [[cmd/evm/internal/t8ntool/transition.go.md|cmd/evm/internal/t8ntool/transition.go]]
- [[cmd/evm/runner.go.md|cmd/evm/runner.go]]
- [[cmd/geth/bintrie_convert.go.md|cmd/geth/bintrie_convert.go]]
- [[cmd/geth/bintrie_convert_test.go.md|cmd/geth/bintrie_convert_test.go]]
- [[cmd/geth/dbcmd.go.md|cmd/geth/dbcmd.go]]
- [[cmd/geth/snapshot.go.md|cmd/geth/snapshot.go]]
- [[cmd/utils/cmd.go.md|cmd/utils/cmd.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[cmd/utils/history_test.go.md|cmd/utils/history_test.go]]
- [[core/bintrie_witness_test.go.md|core/bintrie_witness_test.go]]
- [[core/blockchain.go.md|core/blockchain.go]]
- [[core/blockchain_reader.go.md|core/blockchain_reader.go]]
- [[core/blockchain_sethead_test.go.md|core/blockchain_sethead_test.go]]
- [[core/chain_makers.go.md|core/chain_makers.go]]
- [[core/chain_makers_test.go.md|core/chain_makers_test.go]]
- [[core/genesis.go.md|core/genesis.go]]
- [[core/genesis_test.go.md|core/genesis_test.go]]
- [[core/headerchain_test.go.md|core/headerchain_test.go]]
- [[core/state/database.go.md|core/state/database.go]]
- [[core/state/database_history.go.md|core/state/database_history.go]]
- [[core/state/database_iterator.go.md|core/state/database_iterator.go]]
- [[core/state/database_mpt.go.md|core/state/database_mpt.go]]
- [[core/state/database_ubt.go.md|core/state/database_ubt.go]]
- [[core/state/pruner/pruner.go.md|core/state/pruner/pruner.go]]
- [[core/state/reader.go.md|core/state/reader.go]]
- [[core/state/snapshot/disklayer.go.md|core/state/snapshot/disklayer.go]]
- [[core/state/snapshot/generate.go.md|core/state/snapshot/generate.go]]
- [[core/state/snapshot/generate_test.go.md|core/state/snapshot/generate_test.go]]
- [[core/state/snapshot/journal.go.md|core/state/snapshot/journal.go]]
- [[core/state/snapshot/snapshot.go.md|core/state/snapshot/snapshot.go]]
- [[core/state/state_sizer.go.md|core/state/state_sizer.go]]
- [[core/state/state_sizer_test.go.md|core/state/state_sizer_test.go]]
- [[core/state/state_test.go.md|core/state/state_test.go]]
- [[core/state/statedb_fuzz_test.go.md|core/state/statedb_fuzz_test.go]]
- [[core/state/statedb_test.go.md|core/state/statedb_test.go]]
- [[core/state/sync_test.go.md|core/state/sync_test.go]]
- [[core/state/trie_prefetcher_test.go.md|core/state/trie_prefetcher_test.go]]
- [[core/stateless.go.md|core/stateless.go]]
- [[eth/api_debug_test.go.md|eth/api_debug_test.go]]
- [[eth/downloader/downloader.go.md|eth/downloader/downloader.go]]
- [[eth/downloader/testchain_test.go.md|eth/downloader/testchain_test.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/filters/filter_system_test.go.md|eth/filters/filter_system_test.go]]
- [[eth/filters/filter_test.go.md|eth/filters/filter_test.go]]
- [[eth/protocols/snap/handlers.go.md|eth/protocols/snap/handlers.go]]
- [[eth/protocols/snap/sync_test.go.md|eth/protocols/snap/sync_test.go]]
- [[eth/protocols/snap/syncv2.go.md|eth/protocols/snap/syncv2.go]]
- [[eth/protocols/snap/syncv2_test.go.md|eth/protocols/snap/syncv2_test.go]]
- [[eth/state_accessor.go.md|eth/state_accessor.go]]
- [[internal/ethapi/override/override_test.go.md|internal/ethapi/override/override_test.go]]
- [[miner/miner_test.go.md|miner/miner_test.go]]
- [[tests/block_test_util.go.md|tests/block_test_util.go]]
- [[tests/fuzzers/rangeproof/rangeproof-fuzzer.go.md|tests/fuzzers/rangeproof/rangeproof-fuzzer.go]]
- [[tests/state_test_util.go.md|tests/state_test_util.go]]
- [[trie/bintrie/trie.go.md|trie/bintrie/trie.go]]
- [[trie/database_test.go.md|trie/database_test.go]]
- [[trie/inspect.go.md|trie/inspect.go]]
- [[trie/secure_trie.go.md|trie/secure_trie.go]]
- [[trie/trie.go.md|trie/trie.go]]
- [[trie/trie_reader.go.md|trie/trie_reader.go]]
- [[triedb/database.go.md|triedb/database.go]]
- [[triedb/hashdb/database.go.md|triedb/hashdb/database.go]]
- [[triedb/pathdb/execute.go.md|triedb/pathdb/execute.go]]
- [[triedb/pathdb/generate.go.md|triedb/pathdb/generate.go]]
- [[triedb/pathdb/reader.go.md|triedb/pathdb/reader.go]]

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

package triedb

import (
	"errors"
...
```