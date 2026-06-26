# bal_test.go

## Architecture Metrics
- **Path:** `core/bal_test.go`
- **Extension:** `.go`
- **Size:** 49023 bytes
- **Centrality Score:** 0.0032
- **In-Degree (Imported By):** 103
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `balTestEnv`
- `balChainConfig`
- `newBALTestEnv`
- `run`
- `findAccount`
- `hasSlotIn`
- `hasStorageWrite`
- `assertPresent`
- `assertAbsent`
- `assertEmpty`
- `tx`
- `TestBALTxSenderAndRecipient`
- `TestBALZeroValueRecipient`
- `TestBALEmptyBlockExcludesCoinbase`
- `TestBALCoinbaseTipCapturesBalance`
- `TestBALSystemAddressExcluded`
- `TestBALSystemAddressIncludedWhenTouched`
- `TestBALPrecompileInvokedFromContractIncluded`
- `TestBALPrecompileCalledNoValueIncluded`
- `TestBALPrecompileValueTransferRecordsBalance`
- `TestBALBalanceProbeOnNonExistent`
- `TestBALExtCodeSizeProbeOnNonExistent`
- `TestBALExtCodeHashProbeOnNonExistent`
- `TestBALExtCodeCopyProbeOnNonExistent`
- `TestBALAccessListNotAutoPromoted`
- `makeStubCaller`
- `TestBALCallTargetWithEmptyChangeSet`
- `TestBALCallCodeTargetIncluded`
- `TestBALDelegateCallTargetIncluded`
- `TestBALStaticCallTargetIncluded`
- `TestBALRevertedTxStillIncluded`
- `TestBALSenderRecordedOnRevert`
- `TestBALStorageWriteRecorded`
- `TestBALStorageSloadOnly`
- `TestBALStorageReadThenWriteOnlyInWrites`
- `TestBALNoOpSSTOREDemotesToRead`
- `TestBALStorageWriteZeroIsAWrite`
- `TestBALCreateDeploysCode`
- `TestBALCreateEmptyRuntimeNoCodeEntry`
- `TestBALCreateInitRevertEmptyChangeSet`
- `TestBALCreateInitOOGEmptyChangeSet`
- `TestBALCreateAddressCollisionStillIncluded`
- `TestBALInEVMCreatePreAccessAbortDestinationExcluded`
- `TestBALInEVMCreateDeploysContract`
- `TestBALSelfDestructBeneficiaryWithZeroBalance`
- `TestBALSelfDestructBeneficiaryWithValueTransfer`
- `TestBALSelfDestructPreExistingContract`
- `TestBALMidTxBalanceRoundTrip`
- `TestBALSystemContractsPresent`
- `TestBALWithdrawalZeroAmountIncluded`
- `TestBALWithdrawalNonZeroAmountRecordsBalance`
- `TestBALAuthorityIncludedOnSetCodeTx`
- `TestBALDelegationTargetNotIncludedOnAuthOnly`
- `newSetCodeTx`
- `TestBALAuthFailedBeforeLoadExcluded`
- `TestBALAuthFailedAfterLoadEmptyChangeSet`
- `TestBALMultipleAuthsOnlyLoadedIncluded`
- `TestBALAuthCodeRoundTripNoCodeEntry`
- `TestBALAuthCodeOverwrittenFinalRecorded`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[consensus/beacon/consensus.go.md|consensus/beacon/consensus.go]]
- [[consensus/ethash/ethash.go.md|consensus/ethash/ethash.go]]
- [[core/types.go.md|core/types.go]]
- [[core/types/bal/bal.go.md|core/types/bal/bal.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
- [[cmd/devp2p/internal/ethtest/chain.go.md|cmd/devp2p/internal/ethtest/chain.go]]
- [[cmd/devp2p/nodesetcmd.go.md|cmd/devp2p/nodesetcmd.go]]
- [[cmd/evm/blockrunner.go.md|cmd/evm/blockrunner.go]]
- [[cmd/evm/internal/t8ntool/execution.go.md|cmd/evm/internal/t8ntool/execution.go]]
- [[cmd/evm/internal/t8ntool/transaction.go.md|cmd/evm/internal/t8ntool/transaction.go]]
- [[cmd/evm/internal/t8ntool/transition.go.md|cmd/evm/internal/t8ntool/transition.go]]
- [[cmd/evm/runner.go.md|cmd/evm/runner.go]]
- [[cmd/geth/bintrie_convert_test.go.md|cmd/geth/bintrie_convert_test.go]]
- [[cmd/geth/chaincmd.go.md|cmd/geth/chaincmd.go]]
- [[cmd/geth/snapshot.go.md|cmd/geth/snapshot.go]]
- [[cmd/keeper/main.go.md|cmd/keeper/main.go]]
- [[cmd/utils/cmd.go.md|cmd/utils/cmd.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[cmd/utils/history_test.go.md|cmd/utils/history_test.go]]
- [[consensus/clique/clique_test.go.md|consensus/clique/clique_test.go]]
- [[consensus/clique/snapshot_test.go.md|consensus/clique/snapshot_test.go]]
- [[console/console_test.go.md|console/console_test.go]]
- [[core/filtermaps/indexer_test.go.md|core/filtermaps/indexer_test.go]]
- [[core/forkid/forkid_test.go.md|core/forkid/forkid_test.go]]
- [[core/mkalloc.go.md|core/mkalloc.go]]
- [[core/txpool/blobpool/blobpool.go.md|core/txpool/blobpool/blobpool.go]]
- [[core/txpool/blobpool/blobpool_test.go.md|core/txpool/blobpool/blobpool_test.go]]
- [[core/txpool/legacypool/legacypool.go.md|core/txpool/legacypool/legacypool.go]]
- [[core/txpool/legacypool/legacypool_test.go.md|core/txpool/legacypool/legacypool_test.go]]
- [[core/txpool/locals/tx_tracker_test.go.md|core/txpool/locals/tx_tracker_test.go]]
- [[core/txpool/subpool.go.md|core/txpool/subpool.go]]
- [[core/txpool/txpool.go.md|core/txpool/txpool.go]]
- [[core/txpool/validation.go.md|core/txpool/validation.go]]
- [[core/txpool/validation_test.go.md|core/txpool/validation_test.go]]
- [[core/vm/runtime/env.go.md|core/vm/runtime/env.go]]
- [[core/vm/runtime/runtime_test.go.md|core/vm/runtime/runtime_test.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[eth/api_backend.go.md|eth/api_backend.go]]
- [[eth/api_backend_test.go.md|eth/api_backend_test.go]]
- [[eth/api_debug.go.md|eth/api_debug.go]]
- [[eth/api_debug_test.go.md|eth/api_debug_test.go]]
- [[eth/backend.go.md|eth/backend.go]]
- [[eth/catalyst/api.go.md|eth/catalyst/api.go]]
- [[eth/catalyst/api_benchmark_test.go.md|eth/catalyst/api_benchmark_test.go]]
- [[eth/catalyst/api_test.go.md|eth/catalyst/api_test.go]]
- [[eth/catalyst/simulated_beacon_api.go.md|eth/catalyst/simulated_beacon_api.go]]
- [[eth/catalyst/simulated_beacon_test.go.md|eth/catalyst/simulated_beacon_test.go]]
- [[eth/catalyst/witness.go.md|eth/catalyst/witness.go]]
- [[eth/downloader/api.go.md|eth/downloader/api.go]]
- [[eth/downloader/downloader_test.go.md|eth/downloader/downloader_test.go]]
- [[eth/downloader/queue_test.go.md|eth/downloader/queue_test.go]]
- [[eth/downloader/testchain_test.go.md|eth/downloader/testchain_test.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/ethconfig/gen_config.go.md|eth/ethconfig/gen_config.go]]
- [[eth/fetcher/tx_fetcher.go.md|eth/fetcher/tx_fetcher.go]]
- [[eth/filters/filter.go.md|eth/filters/filter.go]]
- [[eth/filters/filter_system.go.md|eth/filters/filter_system.go]]
- [[eth/filters/filter_system_test.go.md|eth/filters/filter_system_test.go]]
- [[eth/filters/filter_test.go.md|eth/filters/filter_test.go]]
- [[eth/gasestimator/gasestimator.go.md|eth/gasestimator/gasestimator.go]]
- [[eth/gasprice/gasprice.go.md|eth/gasprice/gasprice.go]]
- [[eth/gasprice/gasprice_test.go.md|eth/gasprice/gasprice_test.go]]
- [[eth/handler.go.md|eth/handler.go]]
- [[eth/handler_eth.go.md|eth/handler_eth.go]]
- [[eth/handler_eth_test.go.md|eth/handler_eth_test.go]]
- [[eth/handler_snap.go.md|eth/handler_snap.go]]
- [[eth/handler_test.go.md|eth/handler_test.go]]
- [[eth/protocols/eth/discovery.go.md|eth/protocols/eth/discovery.go]]
- [[eth/protocols/eth/handler.go.md|eth/protocols/eth/handler.go]]
- [[eth/protocols/eth/handler_test.go.md|eth/protocols/eth/handler_test.go]]
- [[eth/protocols/eth/handlers.go.md|eth/protocols/eth/handlers.go]]
- [[eth/protocols/snap/handler.go.md|eth/protocols/snap/handler.go]]
- [[eth/protocols/snap/handler_fuzzing_test.go.md|eth/protocols/snap/handler_fuzzing_test.go]]
- [[eth/protocols/snap/handler_test.go.md|eth/protocols/snap/handler_test.go]]
- [[eth/protocols/snap/handlers.go.md|eth/protocols/snap/handlers.go]]
- [[eth/state_accessor.go.md|eth/state_accessor.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[eth/tracers/api_test.go.md|eth/tracers/api_test.go]]
- [[eth/tracers/internal/tracetest/calltrace_test.go.md|eth/tracers/internal/tracetest/calltrace_test.go]]
- [[eth/tracers/internal/tracetest/erc7562_tracer_test.go.md|eth/tracers/internal/tracetest/erc7562_tracer_test.go]]
- [[eth/tracers/internal/tracetest/flat_calltrace_test.go.md|eth/tracers/internal/tracetest/flat_calltrace_test.go]]
- [[eth/tracers/internal/tracetest/prestate_test.go.md|eth/tracers/internal/tracetest/prestate_test.go]]
- [[eth/tracers/internal/tracetest/selfdestruct_state_test.go.md|eth/tracers/internal/tracetest/selfdestruct_state_test.go]]
- [[eth/tracers/internal/tracetest/supply_test.go.md|eth/tracers/internal/tracetest/supply_test.go]]
- [[eth/tracers/internal/tracetest/util.go.md|eth/tracers/internal/tracetest/util.go]]
- [[eth/tracers/tracers_test.go.md|eth/tracers/tracers_test.go]]
- [[ethclient/ethclient_test.go.md|ethclient/ethclient_test.go]]
- [[ethclient/gethclient/gethclient_test.go.md|ethclient/gethclient/gethclient_test.go]]
- [[ethclient/simulated/backend.go.md|ethclient/simulated/backend.go]]
- [[ethclient/simulated/options_test.go.md|ethclient/simulated/options_test.go]]
- [[ethstats/ethstats.go.md|ethstats/ethstats.go]]
- [[graphql/graphql_test.go.md|graphql/graphql_test.go]]
- [[internal/ethapi/api.go.md|internal/ethapi/api.go]]
- [[internal/ethapi/api_test.go.md|internal/ethapi/api_test.go]]
- [[internal/ethapi/backend.go.md|internal/ethapi/backend.go]]
- [[internal/ethapi/errors.go.md|internal/ethapi/errors.go]]
- [[internal/ethapi/simulate.go.md|internal/ethapi/simulate.go]]
- [[internal/ethapi/transaction_args.go.md|internal/ethapi/transaction_args.go]]
- [[internal/ethapi/transaction_args_test.go.md|internal/ethapi/transaction_args_test.go]]
- [[miner/miner.go.md|miner/miner.go]]
- [[miner/miner_test.go.md|miner/miner_test.go]]
- [[miner/payload_building_test.go.md|miner/payload_building_test.go]]
- [[miner/stress/main.go.md|miner/stress/main.go]]
- [[miner/worker.go.md|miner/worker.go]]
- [[tests/block_test_util.go.md|tests/block_test_util.go]]
- [[tests/state_test.go.md|tests/state_test.go]]
- [[tests/state_test_util.go.md|tests/state_test_util.go]]
- [[tests/transaction_test_util.go.md|tests/transaction_test_util.go]]

## Source Code Snippet
```go
// Copyright 2026 The go-ethereum Authors
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

package core

import (
	"bytes"
...
```