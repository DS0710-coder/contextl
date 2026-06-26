# decode.go

## Architecture Metrics
- **Path:** `rlp/decode.go`
- **Extension:** `.go`
- **Size:** 32480 bytes
- **Centrality Score:** 0.0168
- **In-Degree (Imported By):** 200
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Decoder`
- `decodeError`
- `ByteReader`
- `Stream`
- `Decode`
- `DecodeBytes`
- `Error`
- `wrapStreamError`
- `addErrorContext`
- `makeDecoder`
- `decodeRawValue`
- `decodeUint`
- `decodeBool`
- `decodeString`
- `decodeBigIntNoPtr`
- `decodeBigInt`
- `decodeU256NoPtr`
- `decodeU256`
- `makeListDecoder`
- `decodeListSlice`
- `decodeSliceElems`
- `decodeListArray`
- `decodeByteSlice`
- `decodeByteArray`
- `makeStructDecoder`
- `zeroFields`
- `makePtrDecoder`
- `makeSimplePtrDecoder`
- `makeNilPtrDecoder`
- `decodeInterface`
- `decodeDecoder`
- `String`
- `NewStream`
- `NewListStream`
- `Bytes`
- `ReadBytes`
- `Raw`
- `Uint`
- `Uint64`
- `Uint32`
- `Uint16`
- `Uint8`
- `uint`
- `Bool`
- `List`
- `ListEnd`
- `MoreDataInList`
- `BigInt`
- `decodeBigInt`
- `ReadUint256`
- `Decode`
- `Reset`
- `Kind`
- `readKind`
- `readUint`
- `readFull`
- `readByte`
- `willRead`
- `listLimit`
- `Read`
- `ReadByte`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[rlp/internal/rlpstruct/rlpstruct.go.md|rlp/internal/rlpstruct/rlpstruct.go]]

## Imported By (Dependents)
- [[accounts/abi/bind/v2/base_test.go.md|accounts/abi/bind/v2/base_test.go]]
- [[accounts/usbwallet/ledger.go.md|accounts/usbwallet/ledger.go]]
- [[beacon/light/canonical.go.md|beacon/light/canonical.go]]
- [[cmd/devp2p/enrcmd.go.md|cmd/devp2p/enrcmd.go]]
- [[cmd/devp2p/internal/ethtest/chain.go.md|cmd/devp2p/internal/ethtest/chain.go]]
- [[cmd/devp2p/internal/ethtest/conn.go.md|cmd/devp2p/internal/ethtest/conn.go]]
- [[cmd/devp2p/internal/ethtest/protocol.go.md|cmd/devp2p/internal/ethtest/protocol.go]]
- [[cmd/devp2p/internal/ethtest/snap.go.md|cmd/devp2p/internal/ethtest/snap.go]]
- [[cmd/devp2p/internal/ethtest/snap2.go.md|cmd/devp2p/internal/ethtest/snap2.go]]
- [[cmd/devp2p/internal/ethtest/suite.go.md|cmd/devp2p/internal/ethtest/suite.go]]
- [[cmd/devp2p/internal/ethtest/transaction.go.md|cmd/devp2p/internal/ethtest/transaction.go]]
- [[cmd/devp2p/nodesetcmd.go.md|cmd/devp2p/nodesetcmd.go]]
- [[cmd/devp2p/rlpxcmd.go.md|cmd/devp2p/rlpxcmd.go]]
- [[cmd/evm/internal/t8ntool/block.go.md|cmd/evm/internal/t8ntool/block.go]]
- [[cmd/evm/internal/t8ntool/execution.go.md|cmd/evm/internal/t8ntool/execution.go]]
- [[cmd/evm/internal/t8ntool/transaction.go.md|cmd/evm/internal/t8ntool/transaction.go]]
- [[cmd/evm/internal/t8ntool/tx_iterator.go.md|cmd/evm/internal/t8ntool/tx_iterator.go]]
- [[cmd/fetchpayload/main.go.md|cmd/fetchpayload/main.go]]
- [[cmd/geth/bintrie_convert.go.md|cmd/geth/bintrie_convert.go]]
- [[cmd/geth/dbcmd.go.md|cmd/geth/dbcmd.go]]
- [[cmd/geth/snapshot.go.md|cmd/geth/snapshot.go]]
- [[cmd/keeper/getpayload_example.go.md|cmd/keeper/getpayload_example.go]]
- [[cmd/keeper/main.go.md|cmd/keeper/main.go]]
- [[cmd/rlpdump/main.go.md|cmd/rlpdump/main.go]]
- [[cmd/utils/cmd.go.md|cmd/utils/cmd.go]]
- [[cmd/utils/export_test.go.md|cmd/utils/export_test.go]]
- [[cmd/workload/filtertest.go.md|cmd/workload/filtertest.go]]
- [[cmd/workload/historytestgen.go.md|cmd/workload/historytestgen.go]]
- [[consensus/clique/clique.go.md|consensus/clique/clique.go]]
- [[consensus/ethash/consensus.go.md|consensus/ethash/consensus.go]]
- [[core/blockchain.go.md|core/blockchain.go]]
- [[core/blockchain_reader.go.md|core/blockchain_reader.go]]
- [[core/filtermaps/indexer_test.go.md|core/filtermaps/indexer_test.go]]
- [[core/forkid/forkid_test.go.md|core/forkid/forkid_test.go]]
- [[core/genesis.go.md|core/genesis.go]]
- [[core/headerchain.go.md|core/headerchain.go]]
- [[core/mkalloc.go.md|core/mkalloc.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/rawdb/accessors_chain_test.go.md|core/rawdb/accessors_chain_test.go]]
- [[core/rawdb/accessors_indexes.go.md|core/rawdb/accessors_indexes.go]]
- [[core/rawdb/accessors_indexes_test.go.md|core/rawdb/accessors_indexes_test.go]]
- [[core/rawdb/accessors_metadata.go.md|core/rawdb/accessors_metadata.go]]
- [[core/rawdb/accessors_sync.go.md|core/rawdb/accessors_sync.go]]
- [[core/rawdb/chain_iterator.go.md|core/rawdb/chain_iterator.go]]
- [[core/rawdb/eradb/eradb.go.md|core/rawdb/eradb/eradb.go]]
- [[core/rawdb/eradb/eradb_test.go.md|core/rawdb/eradb/eradb_test.go]]
- [[core/rawdb/freezer_batch.go.md|core/rawdb/freezer_batch.go]]
- [[core/rawdb/freezer_memory.go.md|core/rawdb/freezer_memory.go]]
- [[core/rawdb/freezer_meta.go.md|core/rawdb/freezer_meta.go]]
- [[core/rawdb/freezer_meta_test.go.md|core/rawdb/freezer_meta_test.go]]
- [[core/rawdb/freezer_test.go.md|core/rawdb/freezer_test.go]]
- [[core/rlp_test.go.md|core/rlp_test.go]]
- [[core/state/database_history.go.md|core/state/database_history.go]]
- [[core/state/database_iterator.go.md|core/state/database_iterator.go]]
- [[core/state/iterator.go.md|core/state/iterator.go]]
- [[core/state/pruner/pruner.go.md|core/state/pruner/pruner.go]]
- [[core/state/reader.go.md|core/state/reader.go]]
- [[core/state/snapshot/conversion.go.md|core/state/snapshot/conversion.go]]
- [[core/state/snapshot/difflayer.go.md|core/state/snapshot/difflayer.go]]
- [[core/state/snapshot/disklayer.go.md|core/state/snapshot/disklayer.go]]
- [[core/state/snapshot/disklayer_test.go.md|core/state/snapshot/disklayer_test.go]]
- [[core/state/snapshot/generate.go.md|core/state/snapshot/generate.go]]
- [[core/state/snapshot/generate_test.go.md|core/state/snapshot/generate_test.go]]
- [[core/state/snapshot/journal.go.md|core/state/snapshot/journal.go]]
- [[core/state/snapshot/snapshot.go.md|core/state/snapshot/snapshot.go]]
- [[core/state/snapshot/snapshot_test.go.md|core/state/snapshot/snapshot_test.go]]
- [[core/state/statedb_fuzz_test.go.md|core/state/statedb_fuzz_test.go]]
- [[core/state/statedb_test.go.md|core/state/statedb_test.go]]
- [[core/state/stateupdate.go.md|core/state/stateupdate.go]]
- [[core/state/sync.go.md|core/state/sync.go]]
- [[core/state/sync_test.go.md|core/state/sync_test.go]]
- [[core/stateless/encoding.go.md|core/stateless/encoding.go]]
- [[core/txpool/blobpool/blobpool.go.md|core/txpool/blobpool/blobpool.go]]
- [[core/txpool/blobpool/blobpool_test.go.md|core/txpool/blobpool/blobpool_test.go]]
- [[core/txpool/blobpool/limbo.go.md|core/txpool/blobpool/limbo.go]]
- [[core/txpool/legacypool/legacypool.go.md|core/txpool/legacypool/legacypool.go]]
- [[core/txpool/locals/journal.go.md|core/txpool/locals/journal.go]]
- [[core/types/bal/bal_encoding.go.md|core/types/bal/bal_encoding.go]]
- [[core/types/bal/bal_encoding_rlp_generated.go.md|core/types/bal/bal_encoding_rlp_generated.go]]
- [[core/types/bal/bal_test.go.md|core/types/bal/bal_test.go]]
- [[core/types/block.go.md|core/types/block.go]]
- [[core/types/block_test.go.md|core/types/block_test.go]]
- [[core/types/gen_account_rlp.go.md|core/types/gen_account_rlp.go]]
- [[core/types/gen_header_rlp.go.md|core/types/gen_header_rlp.go]]
- [[core/types/gen_log_rlp.go.md|core/types/gen_log_rlp.go]]
- [[core/types/gen_withdrawal_rlp.go.md|core/types/gen_withdrawal_rlp.go]]
- [[core/types/hashing.go.md|core/types/hashing.go]]
- [[core/types/hashing_test.go.md|core/types/hashing_test.go]]
- [[core/types/receipt.go.md|core/types/receipt.go]]
- [[core/types/receipt_test.go.md|core/types/receipt_test.go]]
- [[core/types/rlp_fuzzer_test.go.md|core/types/rlp_fuzzer_test.go]]
- [[core/types/state_account.go.md|core/types/state_account.go]]
- [[core/types/transaction.go.md|core/types/transaction.go]]
- [[core/types/transaction_signing_test.go.md|core/types/transaction_signing_test.go]]
- [[core/types/transaction_test.go.md|core/types/transaction_test.go]]
- [[core/types/tx_access_list.go.md|core/types/tx_access_list.go]]
- [[core/types/tx_blob.go.md|core/types/tx_blob.go]]
- [[core/types/tx_dynamic_fee.go.md|core/types/tx_dynamic_fee.go]]
- [[core/types/tx_setcode.go.md|core/types/tx_setcode.go]]
- [[core/types/types_test.go.md|core/types/types_test.go]]
- [[core/types/withdrawal.go.md|core/types/withdrawal.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[eth/api_debug.go.md|eth/api_debug.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/catalyst/api.go.md|eth/catalyst/api.go]]
- [[eth/catalyst/api_benchmark_test.go.md|eth/catalyst/api_benchmark_test.go]]
- [[eth/catalyst/witness.go.md|eth/catalyst/witness.go]]
- [[eth/downloader/downloader.go.md|eth/downloader/downloader.go]]
- [[eth/downloader/downloader_test.go.md|eth/downloader/downloader_test.go]]
- [[eth/downloader/queue.go.md|eth/downloader/queue.go]]
- [[eth/downloader/queue_test.go.md|eth/downloader/queue_test.go]]
- [[eth/handler_test.go.md|eth/handler_test.go]]
- [[eth/protocols/eth/discovery.go.md|eth/protocols/eth/discovery.go]]
- [[eth/protocols/eth/handler_test.go.md|eth/protocols/eth/handler_test.go]]
- [[eth/protocols/eth/handlers.go.md|eth/protocols/eth/handlers.go]]
- [[eth/protocols/eth/peer.go.md|eth/protocols/eth/peer.go]]
- [[eth/protocols/eth/protocol.go.md|eth/protocols/eth/protocol.go]]
- [[eth/protocols/eth/protocol_test.go.md|eth/protocols/eth/protocol_test.go]]
- [[eth/protocols/eth/receipt.go.md|eth/protocols/eth/receipt.go]]
- [[eth/protocols/eth/receipt_test.go.md|eth/protocols/eth/receipt_test.go]]
- [[eth/protocols/snap/bal_apply.go.md|eth/protocols/snap/bal_apply.go]]
- [[eth/protocols/snap/bal_apply_test.go.md|eth/protocols/snap/bal_apply_test.go]]
- [[eth/protocols/snap/discovery.go.md|eth/protocols/snap/discovery.go]]
- [[eth/protocols/snap/handler_fuzzing_test.go.md|eth/protocols/snap/handler_fuzzing_test.go]]
- [[eth/protocols/snap/handler_test.go.md|eth/protocols/snap/handler_test.go]]
- [[eth/protocols/snap/handlers.go.md|eth/protocols/snap/handlers.go]]
- [[eth/protocols/snap/peer.go.md|eth/protocols/snap/peer.go]]
- [[eth/protocols/snap/protocol.go.md|eth/protocols/snap/protocol.go]]
- [[eth/protocols/snap/sync.go.md|eth/protocols/snap/sync.go]]
- [[eth/protocols/snap/sync_test.go.md|eth/protocols/snap/sync_test.go]]
- [[eth/protocols/snap/syncer.go.md|eth/protocols/snap/syncer.go]]
- [[eth/protocols/snap/syncv2.go.md|eth/protocols/snap/syncv2.go]]
- [[eth/protocols/snap/syncv2_test.go.md|eth/protocols/snap/syncv2_test.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[eth/tracers/internal/tracetest/flat_calltrace_test.go.md|eth/tracers/internal/tracetest/flat_calltrace_test.go]]
- [[graphql/graphql.go.md|graphql/graphql.go]]
- [[internal/era/execdb/builder.go.md|internal/era/execdb/builder.go]]
- [[internal/era/execdb/era_test.go.md|internal/era/execdb/era_test.go]]
- [[internal/era/execdb/iterator.go.md|internal/era/execdb/iterator.go]]
- [[internal/era/execdb/reader.go.md|internal/era/execdb/reader.go]]
- [[internal/era/onedb/builder.go.md|internal/era/onedb/builder.go]]
- [[internal/era/onedb/builder_test.go.md|internal/era/onedb/builder_test.go]]
- [[internal/era/onedb/iterator.go.md|internal/era/onedb/iterator.go]]
- [[internal/era/onedb/reader.go.md|internal/era/onedb/reader.go]]
- [[internal/era/proof.go.md|internal/era/proof.go]]
- [[internal/ethapi/api.go.md|internal/ethapi/api.go]]
- [[miner/payload_building.go.md|miner/payload_building.go]]
- [[p2p/discover/v4wire/v4wire.go.md|p2p/discover/v4wire/v4wire.go]]
- [[p2p/discover/v4wire/v4wire_test.go.md|p2p/discover/v4wire/v4wire_test.go]]
- [[p2p/discover/v5_udp_test.go.md|p2p/discover/v5_udp_test.go]]
- [[p2p/discover/v5wire/encoding.go.md|p2p/discover/v5wire/encoding.go]]
- [[p2p/discover/v5wire/msg.go.md|p2p/discover/v5wire/msg.go]]
- [[p2p/dnsdisc/tree.go.md|p2p/dnsdisc/tree.go]]
- [[p2p/enode/idscheme.go.md|p2p/enode/idscheme.go]]
- [[p2p/enode/idscheme_test.go.md|p2p/enode/idscheme_test.go]]
- [[p2p/enode/node.go.md|p2p/enode/node.go]]
- [[p2p/enode/node_test.go.md|p2p/enode/node_test.go]]
- [[p2p/enode/nodedb.go.md|p2p/enode/nodedb.go]]
- [[p2p/enr/enr.go.md|p2p/enr/enr.go]]
- [[p2p/enr/enr_test.go.md|p2p/enr/enr_test.go]]
- [[p2p/enr/entries.go.md|p2p/enr/entries.go]]
- [[p2p/message.go.md|p2p/message.go]]
- [[p2p/peer.go.md|p2p/peer.go]]
- [[p2p/rlpx/rlpx.go.md|p2p/rlpx/rlpx.go]]
- [[p2p/rlpx/rlpx_test.go.md|p2p/rlpx/rlpx_test.go]]
- [[p2p/transport.go.md|p2p/transport.go]]
- [[rlp/encbuffer_example_test.go.md|rlp/encbuffer_example_test.go]]
- [[rlp/encoder_example_test.go.md|rlp/encoder_example_test.go]]
- [[tests/block_test_util.go.md|tests/block_test_util.go]]
- [[tests/rlp_test_util.go.md|tests/rlp_test_util.go]]
- [[tests/state_test_util.go.md|tests/state_test_util.go]]
- [[trie/hasher.go.md|trie/hasher.go]]
- [[trie/inspect.go.md|trie/inspect.go]]
- [[trie/inspect_test.go.md|trie/inspect_test.go]]
- [[trie/node.go.md|trie/node.go]]
- [[trie/node_enc.go.md|trie/node_enc.go]]
- [[trie/node_test.go.md|trie/node_test.go]]
- [[trie/secure_trie.go.md|trie/secure_trie.go]]
- [[trie/stacktrie_partial_test.go.md|trie/stacktrie_partial_test.go]]
- [[trie/trie_test.go.md|trie/trie_test.go]]
- [[trie/trienode/proof.go.md|trie/trienode/proof.go]]
- [[triedb/generate.go.md|triedb/generate.go]]
- [[triedb/generate_test.go.md|triedb/generate_test.go]]
- [[triedb/hashdb/database.go.md|triedb/hashdb/database.go]]
- [[triedb/internal/conversion.go.md|triedb/internal/conversion.go]]
- [[triedb/pathdb/database_test.go.md|triedb/pathdb/database_test.go]]
- [[triedb/pathdb/execute.go.md|triedb/pathdb/execute.go]]
- [[triedb/pathdb/generate.go.md|triedb/pathdb/generate.go]]
- [[triedb/pathdb/generate_test.go.md|triedb/pathdb/generate_test.go]]
- [[triedb/pathdb/history_indexer.go.md|triedb/pathdb/history_indexer.go]]
- [[triedb/pathdb/history_reader.go.md|triedb/pathdb/history_reader.go]]
- [[triedb/pathdb/history_state_test.go.md|triedb/pathdb/history_state_test.go]]
- [[triedb/pathdb/iterator_test.go.md|triedb/pathdb/iterator_test.go]]
- [[triedb/pathdb/journal.go.md|triedb/pathdb/journal.go]]
- [[triedb/pathdb/nodes.go.md|triedb/pathdb/nodes.go]]
- [[triedb/pathdb/nodes_test.go.md|triedb/pathdb/nodes_test.go]]
- [[triedb/pathdb/reader.go.md|triedb/pathdb/reader.go]]
- [[triedb/pathdb/states.go.md|triedb/pathdb/states.go]]
- [[triedb/pathdb/states_test.go.md|triedb/pathdb/states_test.go]]

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

package rlp

import (
	"bufio"
...
```