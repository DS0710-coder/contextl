# legacypool_test.go

## Architecture Metrics
- **Path:** `core/txpool/legacypool/legacypool_test.go`
- **Extension:** `.go`
- **Size:** 105838 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 12

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `testBlockChain`
- `unsignedAuth`
- `reserver`
- `testChain`
- `init`
- `newTestBlockChain`
- `Config`
- `CurrentBlock`
- `GetBlock`
- `StateAt`
- `Genesis`
- `SubscribeChainHeadEvent`
- `transaction`
- `pricedTransaction`
- `pricedDataTransaction`
- `dynamicFeeTx`
- `setCodeTx`
- `pricedSetCodeTx`
- `pricedSetCodeTxWithAuth`
- `setupPool`
- `newReserver`
- `Hold`
- `Release`
- `Has`
- `setupPoolWithConfig`
- `validatePoolInternals`
- `validateEvents`
- `deriveSender`
- `State`
- `TestStateChangeDuringReset`
- `testAddBalance`
- `testSetNonce`
- `TestInvalidTransactions`
- `TestQueue`
- `TestQueue2`
- `TestNegativeValue`
- `TestTipAboveFeeCap`
- `TestVeryHighValues`
- `TestChainFork`
- `TestDoubleNonce`
- `TestMissingNonce`
- `TestNonceRecovery`
- `TestDropping`
- `TestPostponing`
- `TestGapFilling`
- `TestQueueAccountLimiting`
- `TestQueueGlobalLimiting`
- `TestQueueTimeLimiting`
- `TestPendingLimiting`
- `TestPendingGlobalLimiting`
- `TestAllowedTxSize`
- `TestCapClearsFromAll`
- `TestPendingMinimumAllowance`
- `TestRepricing`
- `TestMinGasPriceEnforced`
- `TestRepricingDynamicFee`
- `TestUnderpricing`
- `TestStableUnderpricing`
- `TestUnderpricingDynamicFee`
- `TestDualHeapEviction`
- `TestDeduplication`
- `TestReplacement`
- `TestReplacementDynamicFee`
- `TestStatusCheck`
- `TestSlotCount`
- `TestSetCodeTransactions`
- `TestSetCodeTransactionsReorg`
- `BenchmarkPendingDemotion100`
- `BenchmarkPendingDemotion1000`
- `BenchmarkPendingDemotion10000`
- `benchmarkPendingDemotion`
- `BenchmarkFuturePromotion100`
- `BenchmarkFuturePromotion1000`
- `BenchmarkFuturePromotion10000`
- `benchmarkFuturePromotion`
- `BenchmarkBatchInsert100`
- `BenchmarkBatchInsert1000`
- `BenchmarkBatchInsert10000`
- `benchmarkBatchInsert`
- `BenchmarkMultiAccountBatchInsert`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[core/txpool/txpool.go.md|core/txpool/txpool.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[event/event.go.md|event/event.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[trie/trie.go.md|trie/trie.go]]

## Imported By (Dependents)
*Not imported by any file*

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

package legacypool

import (
	"crypto/ecdsa"
...
```