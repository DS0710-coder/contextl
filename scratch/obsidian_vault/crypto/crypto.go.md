# crypto.go

## Architecture Metrics
- **Path:** `crypto/crypto.go`
- **Extension:** `.go`
- **Size:** 8056 bytes
- **Centrality Score:** 0.0141
- **In-Degree (Imported By):** 241
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `EllipticCurve`
- `KeccakState`
- `HashData`
- `CreateAddress`
- `CreateAddress2`
- `ToECDSA`
- `ToECDSAUnsafe`
- `toECDSA`
- `FromECDSA`
- `UnmarshalPubkey`
- `FromECDSAPub`
- `HexToECDSA`
- `LoadECDSA`
- `readASCII`
- `checkKeyFileEnd`
- `SaveECDSA`
- `GenerateKey`
- `ValidateSignatureValues`
- `PubkeyToAddress`
- `zeroBytes`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

## Imported By (Dependents)
- [[accounts/abi/abi.go.md|accounts/abi/abi.go]]
- [[accounts/abi/abi_test.go.md|accounts/abi/abi_test.go]]
- [[accounts/abi/abigen/bindv2_test.go.md|accounts/abi/abigen/bindv2_test.go]]
- [[accounts/abi/bind/old.go.md|accounts/abi/bind/old.go]]
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[accounts/abi/bind/v2/base_test.go.md|accounts/abi/bind/v2/base_test.go]]
- [[accounts/abi/bind/v2/dep_tree_test.go.md|accounts/abi/bind/v2/dep_tree_test.go]]
- [[accounts/abi/bind/v2/generate_test.go.md|accounts/abi/bind/v2/generate_test.go]]
- [[accounts/abi/bind/v2/lib.go.md|accounts/abi/bind/v2/lib.go]]
- [[accounts/abi/bind/v2/lib_test.go.md|accounts/abi/bind/v2/lib_test.go]]
- [[accounts/abi/bind/v2/util_test.go.md|accounts/abi/bind/v2/util_test.go]]
- [[accounts/abi/error.go.md|accounts/abi/error.go]]
- [[accounts/abi/event.go.md|accounts/abi/event.go]]
- [[accounts/abi/event_test.go.md|accounts/abi/event_test.go]]
- [[accounts/abi/method.go.md|accounts/abi/method.go]]
- [[accounts/abi/topics.go.md|accounts/abi/topics.go]]
- [[accounts/abi/topics_test.go.md|accounts/abi/topics_test.go]]
- [[accounts/keystore/key.go.md|accounts/keystore/key.go]]
- [[accounts/keystore/keystore.go.md|accounts/keystore/keystore.go]]
- [[accounts/keystore/keystore_test.go.md|accounts/keystore/keystore_test.go]]
- [[accounts/keystore/passphrase.go.md|accounts/keystore/passphrase.go]]
- [[accounts/keystore/plain_test.go.md|accounts/keystore/plain_test.go]]
- [[accounts/keystore/presale.go.md|accounts/keystore/presale.go]]
- [[accounts/keystore/wallet.go.md|accounts/keystore/wallet.go]]
- [[accounts/scwallet/securechannel.go.md|accounts/scwallet/securechannel.go]]
- [[accounts/scwallet/wallet.go.md|accounts/scwallet/wallet.go]]
- [[accounts/usbwallet/ledger.go.md|accounts/usbwallet/ledger.go]]
- [[accounts/usbwallet/wallet.go.md|accounts/usbwallet/wallet.go]]
- [[cmd/abigen/main.go.md|cmd/abigen/main.go]]
- [[cmd/devp2p/discv4cmd.go.md|cmd/devp2p/discv4cmd.go]]
- [[cmd/devp2p/internal/ethtest/chain.go.md|cmd/devp2p/internal/ethtest/chain.go]]
- [[cmd/devp2p/internal/ethtest/conn.go.md|cmd/devp2p/internal/ethtest/conn.go]]
- [[cmd/devp2p/internal/ethtest/snap.go.md|cmd/devp2p/internal/ethtest/snap.go]]
- [[cmd/devp2p/internal/ethtest/snap2.go.md|cmd/devp2p/internal/ethtest/snap2.go]]
- [[cmd/devp2p/internal/ethtest/suite.go.md|cmd/devp2p/internal/ethtest/suite.go]]
- [[cmd/devp2p/internal/v4test/discv4tests.go.md|cmd/devp2p/internal/v4test/discv4tests.go]]
- [[cmd/devp2p/internal/v4test/framework.go.md|cmd/devp2p/internal/v4test/framework.go]]
- [[cmd/devp2p/internal/v5test/framework.go.md|cmd/devp2p/internal/v5test/framework.go]]
- [[cmd/devp2p/keycmd.go.md|cmd/devp2p/keycmd.go]]
- [[cmd/devp2p/rlpxcmd.go.md|cmd/devp2p/rlpxcmd.go]]
- [[cmd/ethkey/generate.go.md|cmd/ethkey/generate.go]]
- [[cmd/ethkey/inspect.go.md|cmd/ethkey/inspect.go]]
- [[cmd/ethkey/message.go.md|cmd/ethkey/message.go]]
- [[cmd/evm/internal/t8ntool/block.go.md|cmd/evm/internal/t8ntool/block.go]]
- [[cmd/evm/internal/t8ntool/transition.go.md|cmd/evm/internal/t8ntool/transition.go]]
- [[cmd/evm/internal/t8ntool/tx_iterator.go.md|cmd/evm/internal/t8ntool/tx_iterator.go]]
- [[cmd/geth/accountcmd.go.md|cmd/geth/accountcmd.go]]
- [[cmd/geth/chaincmd.go.md|cmd/geth/chaincmd.go]]
- [[cmd/geth/config.go.md|cmd/geth/config.go]]
- [[cmd/geth/dbcmd.go.md|cmd/geth/dbcmd.go]]
- [[cmd/geth/snapshot.go.md|cmd/geth/snapshot.go]]
- [[cmd/utils/cmd.go.md|cmd/utils/cmd.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[cmd/utils/history_test.go.md|cmd/utils/history_test.go]]
- [[cmd/workload/filtertest.go.md|cmd/workload/filtertest.go]]
- [[cmd/workload/historytestgen.go.md|cmd/workload/historytestgen.go]]
- [[cmd/workload/prooftest.go.md|cmd/workload/prooftest.go]]
- [[cmd/workload/prooftestgen.go.md|cmd/workload/prooftestgen.go]]
- [[cmd/workload/tracetest.go.md|cmd/workload/tracetest.go]]
- [[cmd/workload/tracetestgen.go.md|cmd/workload/tracetestgen.go]]
- [[consensus/clique/clique.go.md|consensus/clique/clique.go]]
- [[consensus/clique/clique_test.go.md|consensus/clique/clique_test.go]]
- [[consensus/clique/snapshot_test.go.md|consensus/clique/snapshot_test.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/bench_test.go.md|core/bench_test.go]]
- [[core/bintrie_witness_test.go.md|core/bintrie_witness_test.go]]
- [[core/block_validator_test.go.md|core/block_validator_test.go]]
- [[core/blockchain_test.go.md|core/blockchain_test.go]]
- [[core/chain_makers_test.go.md|core/chain_makers_test.go]]
- [[core/eip8037_test.go.md|core/eip8037_test.go]]
- [[core/eth_transfer_logs_test.go.md|core/eth_transfer_logs_test.go]]
- [[core/genesis.go.md|core/genesis.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/rawdb/accessors_chain_test.go.md|core/rawdb/accessors_chain_test.go]]
- [[core/rawdb/accessors_indexes.go.md|core/rawdb/accessors_indexes.go]]
- [[core/rawdb/accessors_trie.go.md|core/rawdb/accessors_trie.go]]
- [[core/rawdb/database.go.md|core/rawdb/database.go]]
- [[core/rawdb/schema.go.md|core/rawdb/schema.go]]
- [[core/rlp_test.go.md|core/rlp_test.go]]
- [[core/state/database_history.go.md|core/state/database_history.go]]
- [[core/state/database_iterator_test.go.md|core/state/database_iterator_test.go]]
- [[core/state/database_mpt.go.md|core/state/database_mpt.go]]
- [[core/state/iterator_test.go.md|core/state/iterator_test.go]]
- [[core/state/journal.go.md|core/state/journal.go]]
- [[core/state/reader.go.md|core/state/reader.go]]
- [[core/state/snapshot/difflayer_test.go.md|core/state/snapshot/difflayer_test.go]]
- [[core/state/snapshot/generate_test.go.md|core/state/snapshot/generate_test.go]]
- [[core/state/state_object.go.md|core/state/state_object.go]]
- [[core/state/state_sizer.go.md|core/state/state_sizer.go]]
- [[core/state/state_test.go.md|core/state/state_test.go]]
- [[core/state/statedb.go.md|core/state/statedb.go]]
- [[core/state/statedb_fuzz_test.go.md|core/state/statedb_fuzz_test.go]]
- [[core/state/statedb_hooked.go.md|core/state/statedb_hooked.go]]
- [[core/state/statedb_test.go.md|core/state/statedb_test.go]]
- [[core/state/stateupdate.go.md|core/state/stateupdate.go]]
- [[core/state/sync_test.go.md|core/state/sync_test.go]]
- [[core/state/trie_prefetcher_test.go.md|core/state/trie_prefetcher_test.go]]
- [[core/state_processor.go.md|core/state_processor.go]]
- [[core/state_processor_test.go.md|core/state_processor_test.go]]
- [[core/stateless/database.go.md|core/stateless/database.go]]
- [[core/tracing/journal_test.go.md|core/tracing/journal_test.go]]
- [[core/txindexer_test.go.md|core/txindexer_test.go]]
- [[core/txpool/blobpool/blobpool_test.go.md|core/txpool/blobpool/blobpool_test.go]]
- [[core/txpool/blobpool/cache_test.go.md|core/txpool/blobpool/cache_test.go]]
- [[core/txpool/legacypool/legacypool2_test.go.md|core/txpool/legacypool/legacypool2_test.go]]
- [[core/txpool/legacypool/legacypool_test.go.md|core/txpool/legacypool/legacypool_test.go]]
- [[core/txpool/legacypool/list_test.go.md|core/txpool/legacypool/list_test.go]]
- [[core/txpool/locals/tx_tracker_test.go.md|core/txpool/locals/tx_tracker_test.go]]
- [[core/txpool/txorder/ordering_test.go.md|core/txpool/txorder/ordering_test.go]]
- [[core/txpool/validation_test.go.md|core/txpool/validation_test.go]]
- [[core/types/bal/bal_encoding.go.md|core/types/bal/bal_encoding.go]]
- [[core/types/block_test.go.md|core/types/block_test.go]]
- [[core/types/bloom9.go.md|core/types/bloom9.go]]
- [[core/types/bloom9_test.go.md|core/types/bloom9_test.go]]
- [[core/types/hashes.go.md|core/types/hashes.go]]
- [[core/types/hashing.go.md|core/types/hashing.go]]
- [[core/types/hashing_test.go.md|core/types/hashing_test.go]]
- [[core/types/receipt.go.md|core/types/receipt.go]]
- [[core/types/transaction.go.md|core/types/transaction.go]]
- [[core/types/transaction_signing.go.md|core/types/transaction_signing.go]]
- [[core/types/transaction_signing_test.go.md|core/types/transaction_signing_test.go]]
- [[core/types/transaction_test.go.md|core/types/transaction_test.go]]
- [[core/types/tx_blob_test.go.md|core/types/tx_blob_test.go]]
- [[core/types/tx_setcode.go.md|core/types/tx_setcode.go]]
- [[core/types/types_test.go.md|core/types/types_test.go]]
- [[core/vm/analysis_legacy_test.go.md|core/vm/analysis_legacy_test.go]]
- [[core/vm/contracts.go.md|core/vm/contracts.go]]
- [[core/vm/eip8037_test.go.md|core/vm/eip8037_test.go]]
- [[core/vm/evm.go.md|core/vm/evm.go]]
- [[core/vm/instructions.go.md|core/vm/instructions.go]]
- [[core/vm/instructions_test.go.md|core/vm/instructions_test.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[crypto/blake2b/register.go.md|crypto/blake2b/register.go]]
- [[crypto/ecies/ecies.go.md|crypto/ecies/ecies.go]]
- [[crypto/ecies/ecies_test.go.md|crypto/ecies/ecies_test.go]]
- [[crypto/ecies/params.go.md|crypto/ecies/params.go]]
- [[eth/api_backend_test.go.md|eth/api_backend_test.go]]
- [[eth/api_debug.go.md|eth/api_debug.go]]
- [[eth/api_debug_test.go.md|eth/api_debug_test.go]]
- [[eth/catalyst/api_benchmark_test.go.md|eth/catalyst/api_benchmark_test.go]]
- [[eth/catalyst/api_test.go.md|eth/catalyst/api_test.go]]
- [[eth/catalyst/api_testing_test.go.md|eth/catalyst/api_testing_test.go]]
- [[eth/catalyst/simulated_beacon_test.go.md|eth/catalyst/simulated_beacon_test.go]]
- [[eth/downloader/testchain_test.go.md|eth/downloader/testchain_test.go]]
- [[eth/fetcher/tx_fetcher_test.go.md|eth/fetcher/tx_fetcher_test.go]]
- [[eth/filters/filter_system_test.go.md|eth/filters/filter_system_test.go]]
- [[eth/filters/filter_test.go.md|eth/filters/filter_test.go]]
- [[eth/gasprice/gasprice_test.go.md|eth/gasprice/gasprice_test.go]]
- [[eth/handler_test.go.md|eth/handler_test.go]]
- [[eth/protocols/eth/handler_test.go.md|eth/protocols/eth/handler_test.go]]
- [[eth/protocols/eth/handlers.go.md|eth/protocols/eth/handlers.go]]
- [[eth/protocols/snap/bal_apply.go.md|eth/protocols/snap/bal_apply.go]]
- [[eth/protocols/snap/bal_apply_test.go.md|eth/protocols/snap/bal_apply_test.go]]
- [[eth/protocols/snap/gentrie_test.go.md|eth/protocols/snap/gentrie_test.go]]
- [[eth/protocols/snap/sync.go.md|eth/protocols/snap/sync.go]]
- [[eth/protocols/snap/sync_test.go.md|eth/protocols/snap/sync_test.go]]
- [[eth/protocols/snap/syncv2.go.md|eth/protocols/snap/syncv2.go]]
- [[eth/protocols/snap/syncv2_test.go.md|eth/protocols/snap/syncv2_test.go]]
- [[eth/tracers/api_test.go.md|eth/tracers/api_test.go]]
- [[eth/tracers/internal/tracetest/calltrace_test.go.md|eth/tracers/internal/tracetest/calltrace_test.go]]
- [[eth/tracers/internal/tracetest/selfdestruct_state_test.go.md|eth/tracers/internal/tracetest/selfdestruct_state_test.go]]
- [[eth/tracers/internal/tracetest/supply_test.go.md|eth/tracers/internal/tracetest/supply_test.go]]
- [[eth/tracers/js/goja.go.md|eth/tracers/js/goja.go]]
- [[eth/tracers/native/keccak256_preimage.go.md|eth/tracers/native/keccak256_preimage.go]]
- [[eth/tracers/native/keccak256_preimage_test.go.md|eth/tracers/native/keccak256_preimage_test.go]]
- [[eth/tracers/native/prestate.go.md|eth/tracers/native/prestate.go]]
- [[eth/tracers/tracers_test.go.md|eth/tracers/tracers_test.go]]
- [[ethclient/ethclient_test.go.md|ethclient/ethclient_test.go]]
- [[ethclient/gethclient/gethclient_test.go.md|ethclient/gethclient/gethclient_test.go]]
- [[ethclient/simulated/backend_test.go.md|ethclient/simulated/backend_test.go]]
- [[graphql/graphql_test.go.md|graphql/graphql_test.go]]
- [[internal/ethapi/api.go.md|internal/ethapi/api.go]]
- [[internal/ethapi/api_test.go.md|internal/ethapi/api_test.go]]
- [[miner/miner_test.go.md|miner/miner_test.go]]
- [[miner/payload_building_test.go.md|miner/payload_building_test.go]]
- [[miner/stress/main.go.md|miner/stress/main.go]]
- [[node/api.go.md|node/api.go]]
- [[node/config.go.md|node/config.go]]
- [[node/config_test.go.md|node/config_test.go]]
- [[node/node_test.go.md|node/node_test.go]]
- [[p2p/discover/table_test.go.md|p2p/discover/table_test.go]]
- [[p2p/discover/table_util_test.go.md|p2p/discover/table_util_test.go]]
- [[p2p/discover/v4_lookup_test.go.md|p2p/discover/v4_lookup_test.go]]
- [[p2p/discover/v4_udp.go.md|p2p/discover/v4_udp.go]]
- [[p2p/discover/v4wire/v4wire.go.md|p2p/discover/v4wire/v4wire.go]]
- [[p2p/discover/v4wire/v4wire_test.go.md|p2p/discover/v4wire/v4wire_test.go]]
- [[p2p/discover/v5wire/crypto.go.md|p2p/discover/v5wire/crypto.go]]
- [[p2p/discover/v5wire/crypto_test.go.md|p2p/discover/v5wire/crypto_test.go]]
- [[p2p/discover/v5wire/encoding_test.go.md|p2p/discover/v5wire/encoding_test.go]]
- [[p2p/discover/v5wire/session.go.md|p2p/discover/v5wire/session.go]]
- [[p2p/dnsdisc/client.go.md|p2p/dnsdisc/client.go]]
- [[p2p/dnsdisc/client_test.go.md|p2p/dnsdisc/client_test.go]]
- [[p2p/dnsdisc/tree.go.md|p2p/dnsdisc/tree.go]]
- [[p2p/enode/idscheme.go.md|p2p/enode/idscheme.go]]
- [[p2p/enode/idscheme_test.go.md|p2p/enode/idscheme_test.go]]
- [[p2p/enode/localnode_test.go.md|p2p/enode/localnode_test.go]]
- [[p2p/enode/urlv4.go.md|p2p/enode/urlv4.go]]
- [[p2p/enode/urlv4_test.go.md|p2p/enode/urlv4_test.go]]
- [[p2p/rlpx/rlpx.go.md|p2p/rlpx/rlpx.go]]
- [[p2p/rlpx/rlpx_oracle_poc_test.go.md|p2p/rlpx/rlpx_oracle_poc_test.go]]
- [[p2p/rlpx/rlpx_test.go.md|p2p/rlpx/rlpx_test.go]]
- [[p2p/server.go.md|p2p/server.go]]
- [[p2p/server_test.go.md|p2p/server_test.go]]
- [[p2p/transport_test.go.md|p2p/transport_test.go]]
- [[signer/core/apitypes/signed_data_internal_test.go.md|signer/core/apitypes/signed_data_internal_test.go]]
- [[signer/core/apitypes/types.go.md|signer/core/apitypes/types.go]]
- [[tests/state_test_util.go.md|tests/state_test_util.go]]
- [[trie/hasher.go.md|trie/hasher.go]]
- [[trie/inspect.go.md|trie/inspect.go]]
- [[trie/inspect_test.go.md|trie/inspect_test.go]]
- [[trie/iterator_test.go.md|trie/iterator_test.go]]
- [[trie/node.go.md|trie/node.go]]
- [[trie/node_test.go.md|trie/node_test.go]]
- [[trie/proof.go.md|trie/proof.go]]
- [[trie/proof_test.go.md|trie/proof_test.go]]
- [[trie/secure_trie.go.md|trie/secure_trie.go]]
- [[trie/secure_trie_test.go.md|trie/secure_trie_test.go]]
- [[trie/stacktrie_fuzzer_test.go.md|trie/stacktrie_fuzzer_test.go]]
- [[trie/stacktrie_partial_test.go.md|trie/stacktrie_partial_test.go]]
- [[trie/stacktrie_test.go.md|trie/stacktrie_test.go]]
- [[trie/sync.go.md|trie/sync.go]]
- [[trie/sync_test.go.md|trie/sync_test.go]]
- [[trie/trie_test.go.md|trie/trie_test.go]]
- [[trie/trienode/node_test.go.md|trie/trienode/node_test.go]]
- [[trie/trienode/proof.go.md|trie/trienode/proof.go]]
- [[triedb/generate.go.md|triedb/generate.go]]
- [[triedb/generate_test.go.md|triedb/generate_test.go]]
- [[triedb/pathdb/database.go.md|triedb/pathdb/database.go]]
- [[triedb/pathdb/database_test.go.md|triedb/pathdb/database_test.go]]
- [[triedb/pathdb/difflayer_test.go.md|triedb/pathdb/difflayer_test.go]]
- [[triedb/pathdb/disklayer.go.md|triedb/pathdb/disklayer.go]]
- [[triedb/pathdb/execute.go.md|triedb/pathdb/execute.go]]
- [[triedb/pathdb/generate.go.md|triedb/pathdb/generate.go]]
- [[triedb/pathdb/generate_test.go.md|triedb/pathdb/generate_test.go]]
- [[triedb/pathdb/history_index_test.go.md|triedb/pathdb/history_index_test.go]]
- [[triedb/pathdb/history_inspect.go.md|triedb/pathdb/history_inspect.go]]
- [[triedb/pathdb/history_state.go.md|triedb/pathdb/history_state.go]]
- [[triedb/pathdb/history_trienode_test.go.md|triedb/pathdb/history_trienode_test.go]]
- [[triedb/pathdb/nodes.go.md|triedb/pathdb/nodes.go]]
- [[triedb/pathdb/nodes_test.go.md|triedb/pathdb/nodes_test.go]]
- [[triedb/pathdb/reader.go.md|triedb/pathdb/reader.go]]

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

package crypto

import (
	"bufio"
...
```