# hexutil.go

## Architecture Metrics
- **Path:** `common/hexutil/hexutil.go`
- **Extension:** `.go`
- **Size:** 6008 bytes
- **Centrality Score:** 0.0115
- **In-Degree (Imported By):** 154
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `decError`
- `Error`
- `Decode`
- `MustDecode`
- `Encode`
- `DecodeUint64`
- `MustDecodeUint64`
- `EncodeUint64`
- `init`
- `DecodeBig`
- `MustDecodeBig`
- `EncodeBig`
- `has0xPrefix`
- `checkNumber`
- `decodeNibble`
- `mapError`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[accounts/abi/bind/v2/base_test.go.md|accounts/abi/bind/v2/base_test.go]]
- [[accounts/accounts_test.go.md|accounts/accounts_test.go]]
- [[accounts/external/backend.go.md|accounts/external/backend.go]]
- [[accounts/usbwallet/ledger.go.md|accounts/usbwallet/ledger.go]]
- [[accounts/usbwallet/trezor.go.md|accounts/usbwallet/trezor.go]]
- [[beacon/blsync/engineclient.go.md|beacon/blsync/engineclient.go]]
- [[beacon/engine/ed_codec.go.md|beacon/engine/ed_codec.go]]
- [[beacon/engine/epe_decode.go.md|beacon/engine/epe_decode.go]]
- [[beacon/engine/epe_test.go.md|beacon/engine/epe_test.go]]
- [[beacon/engine/pa_codec.go.md|beacon/engine/pa_codec.go]]
- [[beacon/engine/types.go.md|beacon/engine/types.go]]
- [[beacon/light/api/light_api.go.md|beacon/light/api/light_api.go]]
- [[beacon/merkle/merkle.go.md|beacon/merkle/merkle.go]]
- [[beacon/params/config.go.md|beacon/params/config.go]]
- [[beacon/types/committee.go.md|beacon/types/committee.go]]
- [[beacon/types/gen_syncaggregate_json.go.md|beacon/types/gen_syncaggregate_json.go]]
- [[cmd/devp2p/internal/ethtest/chain.go.md|cmd/devp2p/internal/ethtest/chain.go]]
- [[cmd/devp2p/internal/ethtest/suite_test.go.md|cmd/devp2p/internal/ethtest/suite_test.go]]
- [[cmd/evm/internal/t8ntool/block.go.md|cmd/evm/internal/t8ntool/block.go]]
- [[cmd/evm/internal/t8ntool/execution.go.md|cmd/evm/internal/t8ntool/execution.go]]
- [[cmd/evm/internal/t8ntool/gen_execresult.go.md|cmd/evm/internal/t8ntool/gen_execresult.go]]
- [[cmd/evm/internal/t8ntool/gen_header.go.md|cmd/evm/internal/t8ntool/gen_header.go]]
- [[cmd/evm/internal/t8ntool/transaction.go.md|cmd/evm/internal/t8ntool/transaction.go]]
- [[cmd/evm/internal/t8ntool/transition.go.md|cmd/evm/internal/t8ntool/transition.go]]
- [[cmd/evm/internal/t8ntool/tx_iterator.go.md|cmd/evm/internal/t8ntool/tx_iterator.go]]
- [[cmd/fetchpayload/main.go.md|cmd/fetchpayload/main.go]]
- [[cmd/geth/chaincmd.go.md|cmd/geth/chaincmd.go]]
- [[cmd/geth/dbcmd.go.md|cmd/geth/dbcmd.go]]
- [[cmd/keeper/getpayload_example.go.md|cmd/keeper/getpayload_example.go]]
- [[cmd/rlpdump/rlpdump_test.go.md|cmd/rlpdump/rlpdump_test.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[cmd/workload/client.go.md|cmd/workload/client.go]]
- [[cmd/workload/historytest.go.md|cmd/workload/historytest.go]]
- [[common/bitutil/compress_test.go.md|common/bitutil/compress_test.go]]
- [[common/bytes.go.md|common/bytes.go]]
- [[common/hexutil/json_example_test.go.md|common/hexutil/json_example_test.go]]
- [[common/types.go.md|common/types.go]]
- [[consensus/clique/clique.go.md|consensus/clique/clique.go]]
- [[console/bridge.go.md|console/bridge.go]]
- [[core/gen_genesis.go.md|core/gen_genesis.go]]
- [[core/genesis.go.md|core/genesis.go]]
- [[core/state/dump.go.md|core/state/dump.go]]
- [[core/state/snapshot/generate.go.md|core/state/snapshot/generate.go]]
- [[core/stateless/encoding.go.md|core/stateless/encoding.go]]
- [[core/stateless/encoding_test.go.md|core/stateless/encoding_test.go]]
- [[core/types/account.go.md|core/types/account.go]]
- [[core/types/bal/bal_encoding.go.md|core/types/bal/bal_encoding.go]]
- [[core/types/bal/gen_account_access_json.go.md|core/types/bal/gen_account_access_json.go]]
- [[core/types/bal/gen_encoding_account_nonce_json.go.md|core/types/bal/gen_encoding_account_nonce_json.go]]
- [[core/types/bal/gen_encoding_balance_change_json.go.md|core/types/bal/gen_encoding_balance_change_json.go]]
- [[core/types/bal/gen_encoding_code_change_json.go.md|core/types/bal/gen_encoding_code_change_json.go]]
- [[core/types/bal/gen_encoding_slot_changes_json.go.md|core/types/bal/gen_encoding_slot_changes_json.go]]
- [[core/types/bal/gen_encoding_storage_write_json.go.md|core/types/bal/gen_encoding_storage_write_json.go]]
- [[core/types/block.go.md|core/types/block.go]]
- [[core/types/block_test.go.md|core/types/block_test.go]]
- [[core/types/bloom9.go.md|core/types/bloom9.go]]
- [[core/types/gen_account.go.md|core/types/gen_account.go]]
- [[core/types/gen_authorization.go.md|core/types/gen_authorization.go]]
- [[core/types/gen_header_json.go.md|core/types/gen_header_json.go]]
- [[core/types/gen_log_json.go.md|core/types/gen_log_json.go]]
- [[core/types/gen_receipt_json.go.md|core/types/gen_receipt_json.go]]
- [[core/types/gen_withdrawal_json.go.md|core/types/gen_withdrawal_json.go]]
- [[core/types/hashing_test.go.md|core/types/hashing_test.go]]
- [[core/types/log.go.md|core/types/log.go]]
- [[core/types/log_test.go.md|core/types/log_test.go]]
- [[core/types/receipt.go.md|core/types/receipt.go]]
- [[core/types/transaction_marshalling.go.md|core/types/transaction_marshalling.go]]
- [[core/types/tx_setcode.go.md|core/types/tx_setcode.go]]
- [[core/types/withdrawal.go.md|core/types/withdrawal.go]]
- [[core/vm/gas_table_test.go.md|core/vm/gas_table_test.go]]
- [[crypto/crypto_test.go.md|crypto/crypto_test.go]]
- [[crypto/kzg4844/kzg4844.go.md|crypto/kzg4844/kzg4844.go]]
- [[crypto/kzg4844/kzg4844_ckzg_cgo.go.md|crypto/kzg4844/kzg4844_ckzg_cgo.go]]
- [[crypto/signature_test.go.md|crypto/signature_test.go]]
- [[eth/api_debug.go.md|eth/api_debug.go]]
- [[eth/api_miner.go.md|eth/api_miner.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/catalyst/api.go.md|eth/catalyst/api.go]]
- [[eth/catalyst/api_test.go.md|eth/catalyst/api_test.go]]
- [[eth/catalyst/api_testing.go.md|eth/catalyst/api_testing.go]]
- [[eth/catalyst/api_testing_test.go.md|eth/catalyst/api_testing_test.go]]
- [[eth/catalyst/witness.go.md|eth/catalyst/witness.go]]
- [[eth/filters/api.go.md|eth/filters/api.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[eth/tracers/api_test.go.md|eth/tracers/api_test.go]]
- [[eth/tracers/internal/tracetest/calltrace_test.go.md|eth/tracers/internal/tracetest/calltrace_test.go]]
- [[eth/tracers/internal/tracetest/erc7562_tracer_test.go.md|eth/tracers/internal/tracetest/erc7562_tracer_test.go]]
- [[eth/tracers/internal/tracetest/flat_calltrace_test.go.md|eth/tracers/internal/tracetest/flat_calltrace_test.go]]
- [[eth/tracers/internal/tracetest/supply_test.go.md|eth/tracers/internal/tracetest/supply_test.go]]
- [[eth/tracers/js/goja.go.md|eth/tracers/js/goja.go]]
- [[eth/tracers/live/gen_supplyinfoburn.go.md|eth/tracers/live/gen_supplyinfoburn.go]]
- [[eth/tracers/live/gen_supplyinfoissuance.go.md|eth/tracers/live/gen_supplyinfoissuance.go]]
- [[eth/tracers/live/supply.go.md|eth/tracers/live/supply.go]]
- [[eth/tracers/logger/gen_callframe.go.md|eth/tracers/logger/gen_callframe.go]]
- [[eth/tracers/logger/gen_structlog.go.md|eth/tracers/logger/gen_structlog.go]]
- [[eth/tracers/logger/logger.go.md|eth/tracers/logger/logger.go]]
- [[eth/tracers/logger/logger_json.go.md|eth/tracers/logger/logger_json.go]]
- [[eth/tracers/native/call.go.md|eth/tracers/native/call.go]]
- [[eth/tracers/native/call_flat.go.md|eth/tracers/native/call_flat.go]]
- [[eth/tracers/native/erc7562.go.md|eth/tracers/native/erc7562.go]]
- [[eth/tracers/native/gen_account_json.go.md|eth/tracers/native/gen_account_json.go]]
- [[eth/tracers/native/gen_callframe_json.go.md|eth/tracers/native/gen_callframe_json.go]]
- [[eth/tracers/native/gen_callframewithopcodes_json.go.md|eth/tracers/native/gen_callframewithopcodes_json.go]]
- [[eth/tracers/native/gen_flatcallaction_json.go.md|eth/tracers/native/gen_flatcallaction_json.go]]
- [[eth/tracers/native/gen_flatcallresult_json.go.md|eth/tracers/native/gen_flatcallresult_json.go]]
- [[eth/tracers/native/keccak256_preimage.go.md|eth/tracers/native/keccak256_preimage.go]]
- [[eth/tracers/native/keccak256_preimage_test.go.md|eth/tracers/native/keccak256_preimage_test.go]]
- [[eth/tracers/native/prestate.go.md|eth/tracers/native/prestate.go]]
- [[ethclient/ethclient.go.md|ethclient/ethclient.go]]
- [[ethclient/gen_simulate_block_result.go.md|ethclient/gen_simulate_block_result.go]]
- [[ethclient/gen_simulate_call_result.go.md|ethclient/gen_simulate_call_result.go]]
- [[ethclient/gethclient/gen_callframe_json.go.md|ethclient/gethclient/gen_callframe_json.go]]
- [[ethclient/gethclient/gen_calllog_json.go.md|ethclient/gethclient/gen_calllog_json.go]]
- [[ethclient/gethclient/gethclient.go.md|ethclient/gethclient/gethclient.go]]
- [[ethdb/remotedb/remotedb.go.md|ethdb/remotedb/remotedb.go]]
- [[graphql/graphql.go.md|graphql/graphql.go]]
- [[interfaces.go.md|interfaces.go]]
- [[internal/ethapi/api.go.md|internal/ethapi/api.go]]
- [[internal/ethapi/api_test.go.md|internal/ethapi/api_test.go]]
- [[internal/ethapi/capabilities.go.md|internal/ethapi/capabilities.go]]
- [[internal/ethapi/capabilities_test.go.md|internal/ethapi/capabilities_test.go]]
- [[internal/ethapi/dbapi.go.md|internal/ethapi/dbapi.go]]
- [[internal/ethapi/errors.go.md|internal/ethapi/errors.go]]
- [[internal/ethapi/override/override.go.md|internal/ethapi/override/override.go]]
- [[internal/ethapi/override/override_test.go.md|internal/ethapi/override/override_test.go]]
- [[internal/ethapi/simulate.go.md|internal/ethapi/simulate.go]]
- [[internal/ethapi/simulate_test.go.md|internal/ethapi/simulate_test.go]]
- [[internal/ethapi/transaction_args.go.md|internal/ethapi/transaction_args.go]]
- [[internal/ethapi/transaction_args_test.go.md|internal/ethapi/transaction_args_test.go]]
- [[miner/miner.go.md|miner/miner.go]]
- [[miner/payload_building.go.md|miner/payload_building.go]]
- [[node/api.go.md|node/api.go]]
- [[node/node.go.md|node/node.go]]
- [[node/node_auth_test.go.md|node/node_auth_test.go]]
- [[p2p/discover/v5wire/crypto_test.go.md|p2p/discover/v5wire/crypto_test.go]]
- [[p2p/discover/v5wire/encoding_test.go.md|p2p/discover/v5wire/encoding_test.go]]
- [[p2p/discover/v5wire/msg.go.md|p2p/discover/v5wire/msg.go]]
- [[p2p/dnsdisc/client_test.go.md|p2p/dnsdisc/client_test.go]]
- [[p2p/dnsdisc/tree_test.go.md|p2p/dnsdisc/tree_test.go]]
- [[p2p/rlpx/buffer_test.go.md|p2p/rlpx/buffer_test.go]]
- [[rlp/iterator_test.go.md|rlp/iterator_test.go]]
- [[rpc/client_example_test.go.md|rpc/client_example_test.go]]
- [[rpc/types.go.md|rpc/types.go]]
- [[signer/core/apitypes/signed_data_internal_test.go.md|signer/core/apitypes/signed_data_internal_test.go]]
- [[signer/core/apitypes/types.go.md|signer/core/apitypes/types.go]]
- [[signer/fourbyte/validation_test.go.md|signer/fourbyte/validation_test.go]]
- [[tests/block_test_util.go.md|tests/block_test_util.go]]
- [[tests/gen_btheader.go.md|tests/gen_btheader.go]]
- [[tests/gen_sttransaction.go.md|tests/gen_sttransaction.go]]
- [[tests/state_test_util.go.md|tests/state_test_util.go]]
- [[tests/transaction_test_util.go.md|tests/transaction_test_util.go]]
- [[trie/sync.go.md|trie/sync.go]]
- [[triedb/pathdb/generate.go.md|triedb/pathdb/generate.go]]
- [[triedb/pathdb/reader.go.md|triedb/pathdb/reader.go]]

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

/*
Package hexutil implements hex encoding with 0x prefix.
This encoding is used by the Ethereum RPC API to transport binary data in JSON payloads.

...
```