# accessors_chain.go

## Architecture Metrics
- **Path:** `core/rawdb/accessors_chain.go`
- **Extension:** `.go`
- **Size:** 32218 bytes
- **Centrality Score:** 0.0066
- **In-Degree (Imported By):** 179
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NumberHash`
- `receiptLogs`
- `badBlock`
- `ReadCanonicalHash`
- `WriteCanonicalHash`
- `DeleteCanonicalHash`
- `ReadAllHashes`
- `ReadHeaderNumber`
- `WriteHeaderNumber`
- `DeleteHeaderNumber`
- `ReadHeadHeaderHash`
- `WriteHeadHeaderHash`
- `ReadHeadBlockHash`
- `WriteHeadBlockHash`
- `ReadHeadFastBlockHash`
- `WriteHeadFastBlockHash`
- `ReadFinalizedBlockHash`
- `WriteFinalizedBlockHash`
- `ReadLastPivotNumber`
- `WriteLastPivotNumber`
- `ReadTxIndexTail`
- `WriteTxIndexTail`
- `DeleteTxIndexTail`
- `ReadHeaderRange`
- `ReadHeaderRLP`
- `HasHeader`
- `ReadHeader`
- `WriteHeader`
- `DeleteHeader`
- `deleteHeaderWithoutNumber`
- `isCanon`
- `ReadBodyRLP`
- `ReadCanonicalBodyRLP`
- `WriteBodyRLP`
- `HasBody`
- `ReadBody`
- `WriteBody`
- `DeleteBody`
- `HasReceipts`
- `ReadReceiptsRLP`
- `ReadCanonicalReceiptsRLP`
- `ReadRawReceipts`
- `ReadReceipts`
- `WriteReceipts`
- `WriteRawReceipts`
- `DeleteReceipts`
- `HasAccessList`
- `ReadAccessListRLP`
- `ReadAccessList`
- `WriteAccessList`
- `WriteAccessListRLP`
- `DeleteAccessList`
- `DecodeRLP`
- `ReadLogs`
- `ReadBlock`
- `WriteBlock`
- `WriteAncientBlocks`
- `writeAncientBlock`
- `WriteAncientHeaderChain`
- `DeleteBlock`
- `DeleteBlockWithoutNumber`
- `ReadBadBlock`
- `ReadAllBadBlocks`
- `WriteBadBlock`
- `ReadHeadHeader`
- `ReadHeadBlock`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[consensus/misc/eip4844/eip4844.go.md|consensus/misc/eip4844/eip4844.go]]
- [[core/types.go.md|core/types.go]]
- [[core/types/bal/bal.go.md|core/types/bal/bal.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[log/format.go.md|log/format.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
- [[beacon/light/committee_chain.go.md|beacon/light/committee_chain.go]]
- [[cmd/evm/blockrunner.go.md|cmd/evm/blockrunner.go]]
- [[cmd/evm/internal/t8ntool/execution.go.md|cmd/evm/internal/t8ntool/execution.go]]
- [[cmd/evm/internal/t8ntool/transition.go.md|cmd/evm/internal/t8ntool/transition.go]]
- [[cmd/evm/runner.go.md|cmd/evm/runner.go]]
- [[cmd/evm/staterunner.go.md|cmd/evm/staterunner.go]]
- [[cmd/geth/bintrie_convert.go.md|cmd/geth/bintrie_convert.go]]
- [[cmd/geth/bintrie_convert_test.go.md|cmd/geth/bintrie_convert_test.go]]
- [[cmd/geth/chaincmd.go.md|cmd/geth/chaincmd.go]]
- [[cmd/geth/dbcmd.go.md|cmd/geth/dbcmd.go]]
- [[cmd/geth/snapshot.go.md|cmd/geth/snapshot.go]]
- [[cmd/utils/cmd.go.md|cmd/utils/cmd.go]]
- [[cmd/utils/export_test.go.md|cmd/utils/export_test.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[cmd/utils/history_test.go.md|cmd/utils/history_test.go]]
- [[consensus/clique/clique_test.go.md|consensus/clique/clique_test.go]]
- [[consensus/clique/snapshot.go.md|consensus/clique/snapshot.go]]
- [[consensus/clique/snapshot_test.go.md|consensus/clique/snapshot_test.go]]
- [[core/bench_test.go.md|core/bench_test.go]]
- [[core/bintrie_witness_test.go.md|core/bintrie_witness_test.go]]
- [[core/block_validator_test.go.md|core/block_validator_test.go]]
- [[core/blockchain.go.md|core/blockchain.go]]
- [[core/blockchain_reader.go.md|core/blockchain_reader.go]]
- [[core/blockchain_repair_test.go.md|core/blockchain_repair_test.go]]
- [[core/blockchain_sethead_test.go.md|core/blockchain_sethead_test.go]]
- [[core/blockchain_snapshot_test.go.md|core/blockchain_snapshot_test.go]]
- [[core/blockchain_test.go.md|core/blockchain_test.go]]
- [[core/chain_makers.go.md|core/chain_makers.go]]
- [[core/chain_makers_test.go.md|core/chain_makers_test.go]]
- [[core/dao_test.go.md|core/dao_test.go]]
- [[core/filtermaps/filtermaps.go.md|core/filtermaps/filtermaps.go]]
- [[core/filtermaps/indexer_test.go.md|core/filtermaps/indexer_test.go]]
- [[core/genesis.go.md|core/genesis.go]]
- [[core/genesis_test.go.md|core/genesis_test.go]]
- [[core/headerchain.go.md|core/headerchain.go]]
- [[core/headerchain_test.go.md|core/headerchain_test.go]]
- [[core/overlay/state_transition.go.md|core/overlay/state_transition.go]]
- [[core/state/database.go.md|core/state/database.go]]
- [[core/state/database_code.go.md|core/state/database_code.go]]
- [[core/state/database_iterator_test.go.md|core/state/database_iterator_test.go]]
- [[core/state/database_mpt.go.md|core/state/database_mpt.go]]
- [[core/state/database_ubt.go.md|core/state/database_ubt.go]]
- [[core/state/iterator_test.go.md|core/state/iterator_test.go]]
- [[core/state/pruner/bloom.go.md|core/state/pruner/bloom.go]]
- [[core/state/pruner/pruner.go.md|core/state/pruner/pruner.go]]
- [[core/state/snapshot/context.go.md|core/state/snapshot/context.go]]
- [[core/state/snapshot/conversion.go.md|core/state/snapshot/conversion.go]]
- [[core/state/snapshot/disklayer.go.md|core/state/snapshot/disklayer.go]]
- [[core/state/snapshot/disklayer_test.go.md|core/state/snapshot/disklayer_test.go]]
- [[core/state/snapshot/generate.go.md|core/state/snapshot/generate.go]]
- [[core/state/snapshot/generate_test.go.md|core/state/snapshot/generate_test.go]]
- [[core/state/snapshot/holdable_iterator_test.go.md|core/state/snapshot/holdable_iterator_test.go]]
- [[core/state/snapshot/iterator.go.md|core/state/snapshot/iterator.go]]
- [[core/state/snapshot/iterator_test.go.md|core/state/snapshot/iterator_test.go]]
- [[core/state/snapshot/journal.go.md|core/state/snapshot/journal.go]]
- [[core/state/snapshot/snapshot.go.md|core/state/snapshot/snapshot.go]]
- [[core/state/snapshot/snapshot_test.go.md|core/state/snapshot/snapshot_test.go]]
- [[core/state/snapshot/utils.go.md|core/state/snapshot/utils.go]]
- [[core/state/state_sizer.go.md|core/state/state_sizer.go]]
- [[core/state/state_sizer_test.go.md|core/state/state_sizer_test.go]]
- [[core/state/state_test.go.md|core/state/state_test.go]]
- [[core/state/statedb_fuzz_test.go.md|core/state/statedb_fuzz_test.go]]
- [[core/state/statedb_test.go.md|core/state/statedb_test.go]]
- [[core/state/sync_test.go.md|core/state/sync_test.go]]
- [[core/state/trie_prefetcher_test.go.md|core/state/trie_prefetcher_test.go]]
- [[core/state_processor_test.go.md|core/state_processor_test.go]]
- [[core/stateless/database.go.md|core/stateless/database.go]]
- [[core/txindexer.go.md|core/txindexer.go]]
- [[core/txindexer_test.go.md|core/txindexer_test.go]]
- [[core/txpool/locals/tx_tracker_test.go.md|core/txpool/locals/tx_tracker_test.go]]
- [[eth/api_backend.go.md|eth/api_backend.go]]
- [[eth/api_backend_test.go.md|eth/api_backend_test.go]]
- [[eth/api_debug.go.md|eth/api_debug.go]]
- [[eth/api_debug_test.go.md|eth/api_debug_test.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/catalyst/api.go.md|eth/catalyst/api.go]]
- [[eth/downloader/beaconsync.go.md|eth/downloader/beaconsync.go]]
- [[eth/downloader/downloader.go.md|eth/downloader/downloader.go]]
- [[eth/downloader/downloader_test.go.md|eth/downloader/downloader_test.go]]
- [[eth/downloader/skeleton.go.md|eth/downloader/skeleton.go]]
- [[eth/downloader/skeleton_test.go.md|eth/downloader/skeleton_test.go]]
- [[eth/downloader/syncmode.go.md|eth/downloader/syncmode.go]]
- [[eth/downloader/testchain_test.go.md|eth/downloader/testchain_test.go]]
- [[eth/filters/filter_system_test.go.md|eth/filters/filter_system_test.go]]
- [[eth/filters/filter_test.go.md|eth/filters/filter_test.go]]
- [[eth/handler.go.md|eth/handler.go]]
- [[eth/handler_eth_test.go.md|eth/handler_eth_test.go]]
- [[eth/handler_test.go.md|eth/handler_test.go]]
- [[eth/protocols/eth/handler_test.go.md|eth/protocols/eth/handler_test.go]]
- [[eth/protocols/snap/bal_apply.go.md|eth/protocols/snap/bal_apply.go]]
- [[eth/protocols/snap/bal_apply_test.go.md|eth/protocols/snap/bal_apply_test.go]]
- [[eth/protocols/snap/gentrie.go.md|eth/protocols/snap/gentrie.go]]
- [[eth/protocols/snap/gentrie_test.go.md|eth/protocols/snap/gentrie_test.go]]
- [[eth/protocols/snap/handler_fuzzing_test.go.md|eth/protocols/snap/handler_fuzzing_test.go]]
- [[eth/protocols/snap/handler_test.go.md|eth/protocols/snap/handler_test.go]]
- [[eth/protocols/snap/handlers.go.md|eth/protocols/snap/handlers.go]]
- [[eth/protocols/snap/progress_test.go.md|eth/protocols/snap/progress_test.go]]
- [[eth/protocols/snap/sync.go.md|eth/protocols/snap/sync.go]]
- [[eth/protocols/snap/sync_test.go.md|eth/protocols/snap/sync_test.go]]
- [[eth/protocols/snap/syncv2.go.md|eth/protocols/snap/syncv2.go]]
- [[eth/protocols/snap/syncv2_test.go.md|eth/protocols/snap/syncv2_test.go]]
- [[eth/state_accessor.go.md|eth/state_accessor.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[eth/tracers/api_test.go.md|eth/tracers/api_test.go]]
- [[eth/tracers/internal/tracetest/calltrace_test.go.md|eth/tracers/internal/tracetest/calltrace_test.go]]
- [[eth/tracers/internal/tracetest/erc7562_tracer_test.go.md|eth/tracers/internal/tracetest/erc7562_tracer_test.go]]
- [[eth/tracers/internal/tracetest/flat_calltrace_test.go.md|eth/tracers/internal/tracetest/flat_calltrace_test.go]]
- [[eth/tracers/internal/tracetest/prestate_test.go.md|eth/tracers/internal/tracetest/prestate_test.go]]
- [[eth/tracers/internal/tracetest/selfdestruct_state_test.go.md|eth/tracers/internal/tracetest/selfdestruct_state_test.go]]
- [[eth/tracers/internal/tracetest/supply_test.go.md|eth/tracers/internal/tracetest/supply_test.go]]
- [[eth/tracers/tracers_test.go.md|eth/tracers/tracers_test.go]]
- [[graphql/graphql_test.go.md|graphql/graphql_test.go]]
- [[internal/ethapi/api_test.go.md|internal/ethapi/api_test.go]]
- [[internal/ethapi/capabilities.go.md|internal/ethapi/capabilities.go]]
- [[internal/ethapi/capabilities_test.go.md|internal/ethapi/capabilities_test.go]]
- [[internal/ethapi/override/override_test.go.md|internal/ethapi/override/override_test.go]]
- [[internal/shutdowncheck/shutdown_tracker.go.md|internal/shutdowncheck/shutdown_tracker.go]]
- [[miner/miner_test.go.md|miner/miner_test.go]]
- [[miner/payload_building_test.go.md|miner/payload_building_test.go]]
- [[node/database.go.md|node/database.go]]
- [[node/node.go.md|node/node.go]]
- [[tests/block_test.go.md|tests/block_test.go]]
- [[tests/block_test_util.go.md|tests/block_test_util.go]]
- [[tests/fuzzers/rangeproof/rangeproof-fuzzer.go.md|tests/fuzzers/rangeproof/rangeproof-fuzzer.go]]
- [[tests/state_test.go.md|tests/state_test.go]]
- [[tests/state_test_util.go.md|tests/state_test_util.go]]
- [[trie/database_test.go.md|trie/database_test.go]]
- [[trie/inspect.go.md|trie/inspect.go]]
- [[trie/inspect_test.go.md|trie/inspect_test.go]]
- [[trie/iterator_test.go.md|trie/iterator_test.go]]
- [[trie/proof_test.go.md|trie/proof_test.go]]
- [[trie/secure_trie_test.go.md|trie/secure_trie_test.go]]
- [[trie/stacktrie_fuzzer_test.go.md|trie/stacktrie_fuzzer_test.go]]
- [[trie/stacktrie_test.go.md|trie/stacktrie_test.go]]
- [[trie/sync.go.md|trie/sync.go]]
- [[trie/sync_test.go.md|trie/sync_test.go]]
- [[trie/tracer_test.go.md|trie/tracer_test.go]]
- [[trie/trie_test.go.md|trie/trie_test.go]]
- [[triedb/database.go.md|triedb/database.go]]
- [[triedb/generate.go.md|triedb/generate.go]]
- [[triedb/generate_test.go.md|triedb/generate_test.go]]
- [[triedb/hashdb/database.go.md|triedb/hashdb/database.go]]
- [[triedb/internal/conversion.go.md|triedb/internal/conversion.go]]
- [[triedb/internal/holdable_iterator_test.go.md|triedb/internal/holdable_iterator_test.go]]
- [[triedb/pathdb/buffer.go.md|triedb/pathdb/buffer.go]]
- [[triedb/pathdb/context.go.md|triedb/pathdb/context.go]]
- [[triedb/pathdb/database.go.md|triedb/pathdb/database.go]]
- [[triedb/pathdb/database_test.go.md|triedb/pathdb/database_test.go]]
- [[triedb/pathdb/difflayer_test.go.md|triedb/pathdb/difflayer_test.go]]
- [[triedb/pathdb/disklayer.go.md|triedb/pathdb/disklayer.go]]
- [[triedb/pathdb/flush.go.md|triedb/pathdb/flush.go]]
- [[triedb/pathdb/generate.go.md|triedb/pathdb/generate.go]]
- [[triedb/pathdb/generate_test.go.md|triedb/pathdb/generate_test.go]]
- [[triedb/pathdb/history.go.md|triedb/pathdb/history.go]]
- [[triedb/pathdb/history_index.go.md|triedb/pathdb/history_index.go]]
- [[triedb/pathdb/history_index_iterator_test.go.md|triedb/pathdb/history_index_iterator_test.go]]
- [[triedb/pathdb/history_index_pruner.go.md|triedb/pathdb/history_index_pruner.go]]
- [[triedb/pathdb/history_index_pruner_test.go.md|triedb/pathdb/history_index_pruner_test.go]]
- [[triedb/pathdb/history_index_test.go.md|triedb/pathdb/history_index_test.go]]
- [[triedb/pathdb/history_indexer.go.md|triedb/pathdb/history_indexer.go]]
- [[triedb/pathdb/history_indexer_state.go.md|triedb/pathdb/history_indexer_state.go]]
- [[triedb/pathdb/history_indexer_test.go.md|triedb/pathdb/history_indexer_test.go]]
- [[triedb/pathdb/history_inspect.go.md|triedb/pathdb/history_inspect.go]]
- [[triedb/pathdb/history_reader.go.md|triedb/pathdb/history_reader.go]]
- [[triedb/pathdb/history_reader_test.go.md|triedb/pathdb/history_reader_test.go]]
- [[triedb/pathdb/history_state.go.md|triedb/pathdb/history_state.go]]
- [[triedb/pathdb/history_state_test.go.md|triedb/pathdb/history_state_test.go]]
- [[triedb/pathdb/history_trienode.go.md|triedb/pathdb/history_trienode.go]]
- [[triedb/pathdb/history_trienode_test.go.md|triedb/pathdb/history_trienode_test.go]]
- [[triedb/pathdb/iterator.go.md|triedb/pathdb/iterator.go]]
- [[triedb/pathdb/iterator_test.go.md|triedb/pathdb/iterator_test.go]]
- [[triedb/pathdb/journal.go.md|triedb/pathdb/journal.go]]
- [[triedb/pathdb/layertree_test.go.md|triedb/pathdb/layertree_test.go]]
- [[triedb/pathdb/nodes.go.md|triedb/pathdb/nodes.go]]
- [[triedb/pathdb/reader.go.md|triedb/pathdb/reader.go]]
- [[triedb/pathdb/states.go.md|triedb/pathdb/states.go]]
- [[triedb/pathdb/verifier.go.md|triedb/pathdb/verifier.go]]
- [[triedb/preimages.go.md|triedb/preimages.go]]
- [[triedb/preimages_test.go.md|triedb/preimages_test.go]]

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

package rawdb

import (
	"bytes"
...
```