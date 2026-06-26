# batch.go

## Architecture Metrics
- **Path:** `ethdb/batch.go`
- **Extension:** `.go`
- **Size:** 2854 bytes
- **Centrality Score:** 0.0079
- **In-Degree (Imported By):** 150
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Batch`
- `Batcher`
- `HookedBatch`
- `Put`
- `Delete`
- `DeleteRange`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[beacon/light/canonical.go.md|beacon/light/canonical.go]]
- [[beacon/light/committee_chain.go.md|beacon/light/committee_chain.go]]
- [[cmd/evm/internal/t8ntool/execution.go.md|cmd/evm/internal/t8ntool/execution.go]]
- [[cmd/geth/bintrie_convert.go.md|cmd/geth/bintrie_convert.go]]
- [[cmd/geth/chaincmd.go.md|cmd/geth/chaincmd.go]]
- [[cmd/geth/dbcmd.go.md|cmd/geth/dbcmd.go]]
- [[cmd/utils/cmd.go.md|cmd/utils/cmd.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[consensus/clique/clique.go.md|consensus/clique/clique.go]]
- [[consensus/clique/snapshot.go.md|consensus/clique/snapshot.go]]
- [[core/bench_test.go.md|core/bench_test.go]]
- [[core/blockchain.go.md|core/blockchain.go]]
- [[core/blockchain_snapshot_test.go.md|core/blockchain_snapshot_test.go]]
- [[core/blockchain_test.go.md|core/blockchain_test.go]]
- [[core/chain_makers.go.md|core/chain_makers.go]]
- [[core/filtermaps/filtermaps.go.md|core/filtermaps/filtermaps.go]]
- [[core/filtermaps/indexer_test.go.md|core/filtermaps/indexer_test.go]]
- [[core/genesis.go.md|core/genesis.go]]
- [[core/genesis_test.go.md|core/genesis_test.go]]
- [[core/headerchain.go.md|core/headerchain.go]]
- [[core/overlay/state_transition.go.md|core/overlay/state_transition.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/rawdb/accessors_history.go.md|core/rawdb/accessors_history.go]]
- [[core/rawdb/accessors_indexes.go.md|core/rawdb/accessors_indexes.go]]
- [[core/rawdb/accessors_indexes_test.go.md|core/rawdb/accessors_indexes_test.go]]
- [[core/rawdb/accessors_metadata.go.md|core/rawdb/accessors_metadata.go]]
- [[core/rawdb/accessors_overlay.go.md|core/rawdb/accessors_overlay.go]]
- [[core/rawdb/accessors_snapshot.go.md|core/rawdb/accessors_snapshot.go]]
- [[core/rawdb/accessors_state.go.md|core/rawdb/accessors_state.go]]
- [[core/rawdb/accessors_sync.go.md|core/rawdb/accessors_sync.go]]
- [[core/rawdb/accessors_trie.go.md|core/rawdb/accessors_trie.go]]
- [[core/rawdb/ancient_scheme.go.md|core/rawdb/ancient_scheme.go]]
- [[core/rawdb/ancient_utils.go.md|core/rawdb/ancient_utils.go]]
- [[core/rawdb/ancienttest/testsuite.go.md|core/rawdb/ancienttest/testsuite.go]]
- [[core/rawdb/chain_freezer.go.md|core/rawdb/chain_freezer.go]]
- [[core/rawdb/chain_iterator.go.md|core/rawdb/chain_iterator.go]]
- [[core/rawdb/chain_iterator_test.go.md|core/rawdb/chain_iterator_test.go]]
- [[core/rawdb/database.go.md|core/rawdb/database.go]]
- [[core/rawdb/freezer.go.md|core/rawdb/freezer.go]]
- [[core/rawdb/freezer_memory.go.md|core/rawdb/freezer_memory.go]]
- [[core/rawdb/freezer_memory_test.go.md|core/rawdb/freezer_memory_test.go]]
- [[core/rawdb/freezer_resettable.go.md|core/rawdb/freezer_resettable.go]]
- [[core/rawdb/freezer_resettable_test.go.md|core/rawdb/freezer_resettable_test.go]]
- [[core/rawdb/freezer_test.go.md|core/rawdb/freezer_test.go]]
- [[core/rawdb/key_length_iterator.go.md|core/rawdb/key_length_iterator.go]]
- [[core/rawdb/table.go.md|core/rawdb/table.go]]
- [[core/rawdb/table_test.go.md|core/rawdb/table_test.go]]
- [[core/state/database.go.md|core/state/database.go]]
- [[core/state/database_code.go.md|core/state/database_code.go]]
- [[core/state/pruner/pruner.go.md|core/state/pruner/pruner.go]]
- [[core/state/snapshot/context.go.md|core/state/snapshot/context.go]]
- [[core/state/snapshot/conversion.go.md|core/state/snapshot/conversion.go]]
- [[core/state/snapshot/disklayer.go.md|core/state/snapshot/disklayer.go]]
- [[core/state/snapshot/generate.go.md|core/state/snapshot/generate.go]]
- [[core/state/snapshot/generate_test.go.md|core/state/snapshot/generate_test.go]]
- [[core/state/snapshot/holdable_iterator.go.md|core/state/snapshot/holdable_iterator.go]]
- [[core/state/snapshot/iterator.go.md|core/state/snapshot/iterator.go]]
- [[core/state/snapshot/journal.go.md|core/state/snapshot/journal.go]]
- [[core/state/snapshot/snapshot.go.md|core/state/snapshot/snapshot.go]]
- [[core/state/snapshot/utils.go.md|core/state/snapshot/utils.go]]
- [[core/state/state_sizer.go.md|core/state/state_sizer.go]]
- [[core/state/sync.go.md|core/state/sync.go]]
- [[core/state/sync_test.go.md|core/state/sync_test.go]]
- [[core/stateless/database.go.md|core/stateless/database.go]]
- [[core/txindexer.go.md|core/txindexer.go]]
- [[core/txindexer_test.go.md|core/txindexer_test.go]]
- [[core/txpool/locals/tx_tracker_test.go.md|core/txpool/locals/tx_tracker_test.go]]
- [[eth/api_backend.go.md|eth/api_backend.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/downloader/downloader.go.md|eth/downloader/downloader.go]]
- [[eth/downloader/downloader_test.go.md|eth/downloader/downloader_test.go]]
- [[eth/downloader/skeleton.go.md|eth/downloader/skeleton.go]]
- [[eth/downloader/skeleton_test.go.md|eth/downloader/skeleton_test.go]]
- [[eth/downloader/syncmode.go.md|eth/downloader/syncmode.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/filters/filter_system.go.md|eth/filters/filter_system.go]]
- [[eth/filters/filter_system_test.go.md|eth/filters/filter_system_test.go]]
- [[eth/handler.go.md|eth/handler.go]]
- [[eth/handler_test.go.md|eth/handler_test.go]]
- [[eth/protocols/eth/handler_test.go.md|eth/protocols/eth/handler_test.go]]
- [[eth/protocols/snap/bal_apply.go.md|eth/protocols/snap/bal_apply.go]]
- [[eth/protocols/snap/gentrie.go.md|eth/protocols/snap/gentrie.go]]
- [[eth/protocols/snap/gentrie_test.go.md|eth/protocols/snap/gentrie_test.go]]
- [[eth/protocols/snap/sync.go.md|eth/protocols/snap/sync.go]]
- [[eth/protocols/snap/sync_test.go.md|eth/protocols/snap/sync_test.go]]
- [[eth/protocols/snap/syncer.go.md|eth/protocols/snap/syncer.go]]
- [[eth/protocols/snap/syncv2.go.md|eth/protocols/snap/syncv2.go]]
- [[eth/protocols/snap/syncv2_test.go.md|eth/protocols/snap/syncv2_test.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[eth/tracers/api_test.go.md|eth/tracers/api_test.go]]
- [[ethdb/dbtest/testsuite.go.md|ethdb/dbtest/testsuite.go]]
- [[ethdb/leveldb/leveldb.go.md|ethdb/leveldb/leveldb.go]]
- [[ethdb/leveldb/leveldb_test.go.md|ethdb/leveldb/leveldb_test.go]]
- [[ethdb/memorydb/memorydb.go.md|ethdb/memorydb/memorydb.go]]
- [[ethdb/memorydb/memorydb_test.go.md|ethdb/memorydb/memorydb_test.go]]
- [[ethdb/pebble/pebble.go.md|ethdb/pebble/pebble.go]]
- [[ethdb/pebble/pebble_test.go.md|ethdb/pebble/pebble_test.go]]
- [[ethdb/pebble/pebble_v1.go.md|ethdb/pebble/pebble_v1.go]]
- [[ethdb/remotedb/remotedb.go.md|ethdb/remotedb/remotedb.go]]
- [[internal/ethapi/api_test.go.md|internal/ethapi/api_test.go]]
- [[internal/ethapi/backend.go.md|internal/ethapi/backend.go]]
- [[internal/ethapi/transaction_args_test.go.md|internal/ethapi/transaction_args_test.go]]
- [[internal/shutdowncheck/shutdown_tracker.go.md|internal/shutdowncheck/shutdown_tracker.go]]
- [[miner/payload_building_test.go.md|miner/payload_building_test.go]]
- [[node/database.go.md|node/database.go]]
- [[node/node.go.md|node/node.go]]
- [[node/node_test.go.md|node/node_test.go]]
- [[tests/state_test_util.go.md|tests/state_test_util.go]]
- [[trie/bintrie/trie.go.md|trie/bintrie/trie.go]]
- [[trie/database_test.go.md|trie/database_test.go]]
- [[trie/inspect.go.md|trie/inspect.go]]
- [[trie/proof.go.md|trie/proof.go]]
- [[trie/sync.go.md|trie/sync.go]]
- [[trie/sync_test.go.md|trie/sync_test.go]]
- [[trie/transitiontrie/transition.go.md|trie/transitiontrie/transition.go]]
- [[trie/trie_test.go.md|trie/trie_test.go]]
- [[trie/trienode/proof.go.md|trie/trienode/proof.go]]
- [[triedb/database.go.md|triedb/database.go]]
- [[triedb/generate.go.md|triedb/generate.go]]
- [[triedb/generate_test.go.md|triedb/generate_test.go]]
- [[triedb/hashdb/database.go.md|triedb/hashdb/database.go]]
- [[triedb/internal/conversion.go.md|triedb/internal/conversion.go]]
- [[triedb/internal/holdable_iterator.go.md|triedb/internal/holdable_iterator.go]]
- [[triedb/internal/holdable_iterator_test.go.md|triedb/internal/holdable_iterator_test.go]]
- [[triedb/pathdb/buffer.go.md|triedb/pathdb/buffer.go]]
- [[triedb/pathdb/context.go.md|triedb/pathdb/context.go]]
- [[triedb/pathdb/database.go.md|triedb/pathdb/database.go]]
- [[triedb/pathdb/database_test.go.md|triedb/pathdb/database_test.go]]
- [[triedb/pathdb/disklayer.go.md|triedb/pathdb/disklayer.go]]
- [[triedb/pathdb/flush.go.md|triedb/pathdb/flush.go]]
- [[triedb/pathdb/generate.go.md|triedb/pathdb/generate.go]]
- [[triedb/pathdb/generate_test.go.md|triedb/pathdb/generate_test.go]]
- [[triedb/pathdb/history.go.md|triedb/pathdb/history.go]]
- [[triedb/pathdb/history_index.go.md|triedb/pathdb/history_index.go]]
- [[triedb/pathdb/history_index_iterator_test.go.md|triedb/pathdb/history_index_iterator_test.go]]
- [[triedb/pathdb/history_index_pruner.go.md|triedb/pathdb/history_index_pruner.go]]
- [[triedb/pathdb/history_index_pruner_test.go.md|triedb/pathdb/history_index_pruner_test.go]]
- [[triedb/pathdb/history_indexer.go.md|triedb/pathdb/history_indexer.go]]
- [[triedb/pathdb/history_indexer_state.go.md|triedb/pathdb/history_indexer_state.go]]
- [[triedb/pathdb/history_inspect.go.md|triedb/pathdb/history_inspect.go]]
- [[triedb/pathdb/history_reader.go.md|triedb/pathdb/history_reader.go]]
- [[triedb/pathdb/history_state.go.md|triedb/pathdb/history_state.go]]
- [[triedb/pathdb/history_state_test.go.md|triedb/pathdb/history_state_test.go]]
- [[triedb/pathdb/history_trienode.go.md|triedb/pathdb/history_trienode.go]]
- [[triedb/pathdb/iterator.go.md|triedb/pathdb/iterator.go]]
- [[triedb/pathdb/journal.go.md|triedb/pathdb/journal.go]]
- [[triedb/pathdb/nodes.go.md|triedb/pathdb/nodes.go]]
- [[triedb/pathdb/states.go.md|triedb/pathdb/states.go]]
- [[triedb/pathdb/verifier.go.md|triedb/pathdb/verifier.go]]
- [[triedb/preimages.go.md|triedb/preimages.go]]

## Source Code Snippet
```go
// Copyright 2018 The go-ethereum Authors
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

package ethdb

// IdealBatchSize defines the size of the data batches should ideally add in one
// write.
...
```