# big.go

## Architecture Metrics
- **Path:** `common/math/big.go`
- **Extension:** `.go`
- **Size:** 4985 bytes
- **Centrality Score:** 0.0172
- **In-Degree (Imported By):** 152
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NewHexOrDecimal256`
- `UnmarshalJSON`
- `UnmarshalText`
- `MarshalText`
- `NewDecimal256`
- `UnmarshalText`
- `MarshalText`
- `String`
- `ParseBig256`
- `MustParseBig256`
- `BigPow`
- `PaddedBigBytes`
- `ReadBits`
- `U256`
- `U256Bytes`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[accounts/abi/abi_test.go.md|accounts/abi/abi_test.go]]
- [[accounts/abi/pack.go.md|accounts/abi/pack.go]]
- [[accounts/abi/pack_test.go.md|accounts/abi/pack_test.go]]
- [[accounts/abi/topics.go.md|accounts/abi/topics.go]]
- [[accounts/abi/topics_test.go.md|accounts/abi/topics_test.go]]
- [[accounts/abi/unpack.go.md|accounts/abi/unpack.go]]
- [[accounts/abi/unpack_test.go.md|accounts/abi/unpack_test.go]]
- [[accounts/hd.go.md|accounts/hd.go]]
- [[accounts/keystore/passphrase.go.md|accounts/keystore/passphrase.go]]
- [[accounts/usbwallet/trezor.go.md|accounts/usbwallet/trezor.go]]
- [[beacon/light/committee_chain.go.md|beacon/light/committee_chain.go]]
- [[beacon/light/request/server.go.md|beacon/light/request/server.go]]
- [[beacon/params/config.go.md|beacon/params/config.go]]
- [[cmd/evm/internal/t8ntool/block.go.md|cmd/evm/internal/t8ntool/block.go]]
- [[cmd/evm/internal/t8ntool/execution.go.md|cmd/evm/internal/t8ntool/execution.go]]
- [[cmd/evm/internal/t8ntool/gen_execresult.go.md|cmd/evm/internal/t8ntool/gen_execresult.go]]
- [[cmd/evm/internal/t8ntool/gen_header.go.md|cmd/evm/internal/t8ntool/gen_header.go]]
- [[cmd/evm/internal/t8ntool/gen_stenv.go.md|cmd/evm/internal/t8ntool/gen_stenv.go]]
- [[cmd/geth/bintrie_convert_test.go.md|cmd/geth/bintrie_convert_test.go]]
- [[cmd/geth/dbcmd.go.md|cmd/geth/dbcmd.go]]
- [[cmd/geth/logtestcmd_active.go.md|cmd/geth/logtestcmd_active.go]]
- [[cmd/rlpdump/main.go.md|cmd/rlpdump/main.go]]
- [[cmd/utils/cmd.go.md|cmd/utils/cmd.go]]
- [[cmd/workload/filtertestgen.go.md|cmd/workload/filtertestgen.go]]
- [[common/lru/blob_lru.go.md|common/lru/blob_lru.go]]
- [[common/math/integer_test.go.md|common/math/integer_test.go]]
- [[common/types_test.go.md|common/types_test.go]]
- [[consensus/ethash/consensus_test.go.md|consensus/ethash/consensus_test.go]]
- [[consensus/misc/eip4844/eip4844.go.md|consensus/misc/eip4844/eip4844.go]]
- [[core/bench_test.go.md|core/bench_test.go]]
- [[core/blockchain_test.go.md|core/blockchain_test.go]]
- [[core/filtermaps/indexer.go.md|core/filtermaps/indexer.go]]
- [[core/filtermaps/map_renderer.go.md|core/filtermaps/map_renderer.go]]
- [[core/filtermaps/math.go.md|core/filtermaps/math.go]]
- [[core/forkid/forkid.go.md|core/forkid/forkid.go]]
- [[core/forkid/forkid_test.go.md|core/forkid/forkid_test.go]]
- [[core/gaspool.go.md|core/gaspool.go]]
- [[core/gen_genesis.go.md|core/gen_genesis.go]]
- [[core/genesis.go.md|core/genesis.go]]
- [[core/rawdb/freezer.go.md|core/rawdb/freezer.go]]
- [[core/rawdb/freezer_batch.go.md|core/rawdb/freezer_batch.go]]
- [[core/rawdb/freezer_memory.go.md|core/rawdb/freezer_memory.go]]
- [[core/rawdb/freezer_meta.go.md|core/rawdb/freezer_meta.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/state/access_events_test.go.md|core/state/access_events_test.go]]
- [[core/state/pruner/pruner.go.md|core/state/pruner/pruner.go]]
- [[core/state/snapshot/context.go.md|core/state/snapshot/context.go]]
- [[core/state/snapshot/conversion.go.md|core/state/snapshot/conversion.go]]
- [[core/state/snapshot/difflayer.go.md|core/state/snapshot/difflayer.go]]
- [[core/state/statedb_fuzz_test.go.md|core/state/statedb_fuzz_test.go]]
- [[core/state/statedb_test.go.md|core/state/statedb_test.go]]
- [[core/state_processor_test.go.md|core/state_processor_test.go]]
- [[core/state_transition.go.md|core/state_transition.go]]
- [[core/txpool/blobpool/blobpool.go.md|core/txpool/blobpool/blobpool.go]]
- [[core/txpool/blobpool/blobpool_test.go.md|core/txpool/blobpool/blobpool_test.go]]
- [[core/txpool/blobpool/evictheap.go.md|core/txpool/blobpool/evictheap.go]]
- [[core/txpool/blobpool/priority.go.md|core/txpool/blobpool/priority.go]]
- [[core/txpool/legacypool/legacypool.go.md|core/txpool/legacypool/legacypool.go]]
- [[core/txpool/legacypool/list.go.md|core/txpool/legacypool/list.go]]
- [[core/txpool/validation_test.go.md|core/txpool/validation_test.go]]
- [[core/types/account.go.md|core/types/account.go]]
- [[core/types/bal/bal_test.go.md|core/types/bal/bal_test.go]]
- [[core/types/block_test.go.md|core/types/block_test.go]]
- [[core/types/gen_account.go.md|core/types/gen_account.go]]
- [[core/types/hashing.go.md|core/types/hashing.go]]
- [[core/types/receipt_test.go.md|core/types/receipt_test.go]]
- [[core/vm/common.go.md|core/vm/common.go]]
- [[core/vm/contracts.go.md|core/vm/contracts.go]]
- [[core/vm/eip8037_test.go.md|core/vm/eip8037_test.go]]
- [[core/vm/eips.go.md|core/vm/eips.go]]
- [[core/vm/errors.go.md|core/vm/errors.go]]
- [[core/vm/gas_table.go.md|core/vm/gas_table.go]]
- [[core/vm/gas_table_test.go.md|core/vm/gas_table_test.go]]
- [[core/vm/instructions.go.md|core/vm/instructions.go]]
- [[core/vm/instructions_test.go.md|core/vm/instructions_test.go]]
- [[core/vm/interpreter.go.md|core/vm/interpreter.go]]
- [[core/vm/interpreter_test.go.md|core/vm/interpreter_test.go]]
- [[core/vm/operations_acl.go.md|core/vm/operations_acl.go]]
- [[core/vm/operations_verkle.go.md|core/vm/operations_verkle.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[crypto/secp256k1/curve.go.md|crypto/secp256k1/curve.go]]
- [[crypto/secp256k1/scalar_mult_cgo.go.md|crypto/secp256k1/scalar_mult_cgo.go]]
- [[crypto/signature_cgo.go.md|crypto/signature_cgo.go]]
- [[crypto/signature_test.go.md|crypto/signature_test.go]]
- [[eth/api_backend_test.go.md|eth/api_backend_test.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/catalyst/simulated_beacon.go.md|eth/catalyst/simulated_beacon.go]]
- [[eth/downloader/skeleton_test.go.md|eth/downloader/skeleton_test.go]]
- [[eth/fetcher/tx_fetcher.go.md|eth/fetcher/tx_fetcher.go]]
- [[eth/filters/filter.go.md|eth/filters/filter.go]]
- [[eth/gasprice/feehistory.go.md|eth/gasprice/feehistory.go]]
- [[eth/gasprice/gasprice_test.go.md|eth/gasprice/gasprice_test.go]]
- [[eth/handler.go.md|eth/handler.go]]
- [[eth/protocols/eth/handler_test.go.md|eth/protocols/eth/handler_test.go]]
- [[eth/protocols/eth/handlers.go.md|eth/protocols/eth/handlers.go]]
- [[eth/protocols/snap/sync.go.md|eth/protocols/snap/sync.go]]
- [[eth/tracers/internal/tracetest/util.go.md|eth/tracers/internal/tracetest/util.go]]
- [[eth/tracers/logger/gen_callframe.go.md|eth/tracers/logger/gen_callframe.go]]
- [[eth/tracers/logger/gen_structlog.go.md|eth/tracers/logger/gen_structlog.go]]
- [[eth/tracers/logger/logger.go.md|eth/tracers/logger/logger.go]]
- [[eth/tracers/logger/logger_json.go.md|eth/tracers/logger/logger_json.go]]
- [[internal/ethapi/api.go.md|internal/ethapi/api.go]]
- [[internal/ethapi/simulate.go.md|internal/ethapi/simulate.go]]
- [[internal/ethapi/transaction_args.go.md|internal/ethapi/transaction_args.go]]
- [[internal/flags/flags.go.md|internal/flags/flags.go]]
- [[log/logger.go.md|log/logger.go]]
- [[metrics/counter_float64.go.md|metrics/counter_float64.go]]
- [[metrics/ewma.go.md|metrics/ewma.go]]
- [[metrics/ewma_test.go.md|metrics/ewma_test.go]]
- [[metrics/gauge_float64.go.md|metrics/gauge_float64.go]]
- [[metrics/meter.go.md|metrics/meter.go]]
- [[metrics/runtimehistogram.go.md|metrics/runtimehistogram.go]]
- [[metrics/runtimehistogram_test.go.md|metrics/runtimehistogram_test.go]]
- [[metrics/sample.go.md|metrics/sample.go]]
- [[metrics/sample_test.go.md|metrics/sample_test.go]]
- [[metrics/timer_test.go.md|metrics/timer_test.go]]
- [[p2p/discover/table_reval.go.md|p2p/discover/table_reval.go]]
- [[p2p/discover/v4wire/v4wire.go.md|p2p/discover/v4wire/v4wire.go]]
- [[p2p/discover/v5wire/crypto.go.md|p2p/discover/v5wire/crypto.go]]
- [[p2p/enode/idscheme.go.md|p2p/enode/idscheme.go]]
- [[p2p/enode/urlv4.go.md|p2p/enode/urlv4.go]]
- [[p2p/msgrate/msgrate.go.md|p2p/msgrate/msgrate.go]]
- [[p2p/nat/natupnp.go.md|p2p/nat/natupnp.go]]
- [[params/config.go.md|params/config.go]]
- [[params/config_test.go.md|params/config_test.go]]
- [[rlp/decode_test.go.md|rlp/decode_test.go]]
- [[rlp/encbuffer.go.md|rlp/encbuffer.go]]
- [[rlp/encode_test.go.md|rlp/encode_test.go]]
- [[rpc/http.go.md|rpc/http.go]]
- [[rpc/types.go.md|rpc/types.go]]
- [[rpc/types_test.go.md|rpc/types_test.go]]
- [[signer/core/apitypes/signed_data_internal_test.go.md|signer/core/apitypes/signed_data_internal_test.go]]
- [[signer/core/apitypes/types.go.md|signer/core/apitypes/types.go]]
- [[tests/block_test_util.go.md|tests/block_test_util.go]]
- [[tests/difficulty_test_util.go.md|tests/difficulty_test_util.go]]
- [[tests/gen_btheader.go.md|tests/gen_btheader.go]]
- [[tests/gen_difficultytest.go.md|tests/gen_difficultytest.go]]
- [[tests/gen_stauthorization.go.md|tests/gen_stauthorization.go]]
- [[tests/gen_stenv.go.md|tests/gen_stenv.go]]
- [[tests/gen_sttransaction.go.md|tests/gen_sttransaction.go]]
- [[tests/state_test_util.go.md|tests/state_test_util.go]]
- [[tests/transaction_test_util.go.md|tests/transaction_test_util.go]]
- [[triedb/internal/conversion.go.md|triedb/internal/conversion.go]]
- [[triedb/pathdb/context.go.md|triedb/pathdb/context.go]]
- [[triedb/pathdb/history_index.go.md|triedb/pathdb/history_index.go]]
- [[triedb/pathdb/history_index_block.go.md|triedb/pathdb/history_index_block.go]]
- [[triedb/pathdb/history_index_block_test.go.md|triedb/pathdb/history_index_block_test.go]]
- [[triedb/pathdb/history_index_pruner_test.go.md|triedb/pathdb/history_index_pruner_test.go]]
- [[triedb/pathdb/history_index_test.go.md|triedb/pathdb/history_index_test.go]]
- [[triedb/pathdb/history_reader.go.md|triedb/pathdb/history_reader.go]]
- [[triedb/pathdb/history_trienode.go.md|triedb/pathdb/history_trienode.go]]

## Source Code Snippet
```go
// Copyright 2017 The go-ethereum Authors
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

// Package math provides integer math utilities.
package math

import (
...
```