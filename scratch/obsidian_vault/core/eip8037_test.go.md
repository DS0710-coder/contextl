# eip8037_test.go

## Architecture Metrics
- **Path:** `core/eip8037_test.go`
- **Extension:** `.go`
- **Size:** 24245 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `mkState`
- `amsterdamCoreEVM`
- `applyMsg`
- `assertBudgetSane`
- `assertPoolSane`
- `senderAlloc`
- `callTx`
- `createTx`
- `TestCreateTxIntrinsicChargesAccountUnconditionally`
- `TestCreateTxPreexistingDestRefill`
- `TestCreateTxRevertRefill`
- `TestCreateTxCollisionConsumesGasLeft`
- `TestValidationRegularGasAvailable`
- `TestValidationStateGasAvailable`
- `TestValidationStateGasOverflowAllowed`
- `TestValidationIntrinsicRegularCap`
- `clearSlots`
- `TestGasUsedBeforeRefund`
- `TestRefundCappedAt20Percent`
- `TestRefundCalldataFloorAfterRefund`
- `TestRefundFloorNegatesRefund`
- `TestBlockTracksTwoCounters`
- `TestBlockGasUsedIsMax`
- `TestBlockValidityAgainstMax`
- `TestBlockBaseFeeUsesMax`
- `TestReceiptCumulativeGasUsed`
- `signAuth`
- `setCodeTx`
- `TestAuthIntrinsicWorstCase`
- `TestAuthInvalidRefillFull`
- `TestAuthAccountExistsRefill`
- `TestAuthSetOnDelegatedRefillBase`
- `TestAuthSetNetNewNoRefill`
- `TestAuthClearRefillBase`
- `TestAuthClearSameTxDoubleRefill`
- `TestAuthDuplicateAuthorityOnce`
- `TestSystemCallGasLimit`
- `TestSystemCallExtraInReservoir`
- `TestSystemCallNotCountedInBlock`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[consensus/beacon/consensus.go.md|consensus/beacon/consensus.go]]
- [[consensus/ethash/ethash.go.md|consensus/ethash/ethash.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
*Not imported by any file*

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

// Transaction- and block-level tests for EIP-8037 (multidimensional state-gas
// metering). They apply whole transactions and inspect the 2D block gas pool
// (cumulativeRegular / cumulativeState) and the receipt/peak figures.

...
```