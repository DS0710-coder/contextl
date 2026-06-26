# api_test.go

## Architecture Metrics
- **Path:** `eth/tracers/api_test.go`
- **Extension:** `.go`
- **Size:** 62868 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 18

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `testBackend`
- `stateTracer`
- `tracedOpcodeLog`
- `tracedOpcodeResult`
- `res`
- `Account`
- `newTestBackend`
- `HeaderByHash`
- `HeaderByNumber`
- `BlockByHash`
- `BlockByNumber`
- `GetCanonicalTransaction`
- `TxIndexDone`
- `RPCGasCap`
- `ChainConfig`
- `Engine`
- `ChainDb`
- `CurrentHeader`
- `teardown`
- `StateAtBlock`
- `StateAtTransaction`
- `newStateTracer`
- `TestStateHooks`
- `TestTraceCall`
- `TestTraceTransaction`
- `TestTraceBlock`
- `TestTracingWithOverrides`
- `TestTraceTransactionRefundAndStorageSnapshots`
- `TestTraceTransactionFailureReturnValues`
- `newAccounts`
- `newRPCBalance`
- `newRPCBytes`
- `newStates`
- `TestTraceChain`
- `newTestMergedBackend`
- `TestTraceBlockWithBasefee`
- `TestStandardTraceBlockToFile`
- `TestTraceBadBlock`
- `TestIntermediateRoots`
- `TestStandardTraceBadBlockToFile`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[consensus/beacon/consensus.go.md|consensus/beacon/consensus.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[consensus/ethash/ethash.go.md|consensus/ethash/ethash.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[eth/tracers/logger/logger.go.md|eth/tracers/logger/logger.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[internal/ethapi/addrlock.go.md|internal/ethapi/addrlock.go]]
- [[internal/ethapi/override/override.go.md|internal/ethapi/override/override.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2021 The go-ethereum Authors
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

package tracers

import (
	"context"
...
```