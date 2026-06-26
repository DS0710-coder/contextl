# state_processor.go

## Architecture Metrics
- **Path:** `core/state_processor.go`
- **Extension:** `.go`
- **Size:** 19700 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 12

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `StateProcessor`
- `NewStateProcessor`
- `chainConfig`
- `Process`
- `PreExecution`
- `PostExecution`
- `ApplyTransactionWithEVM`
- `MakeReceipt`
- `ApplyTransaction`
- `systemCallGasBudget`
- `ProcessBeaconBlockRoot`
- `ProcessParentBlockHash`
- `ProcessWithdrawalQueue`
- `ProcessConsolidationQueue`
- `ProcessBuilderDepositQueue`
- `ProcessBuilderExitQueue`
- `processRequestsSystemCall`
- `ParseDepositLogs`
- `onSystemCallStart`
- `AssembleBlock`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[consensus/misc/dao.go.md|consensus/misc/dao.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[core/types.go.md|core/types.go]]
- [[core/types/bal/bal.go.md|core/types/bal/bal.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[internal/telemetry/telemetry.go.md|internal/telemetry/telemetry.go]]
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

package core

import (
	"context"
...
```