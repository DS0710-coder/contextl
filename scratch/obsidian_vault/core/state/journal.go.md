# journal.go

## Architecture Metrics
- **Path:** `core/state/journal.go`
- **Extension:** `.go`
- **Size:** 18699 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `revision`
- `journalMutationState`
- `journalEntry`
- `journal`
- `createObjectChange`
- `createContractChange`
- `selfDestructChange`
- `balanceChange`
- `nonceChange`
- `storageChange`
- `codeChange`
- `refundChange`
- `addLogChange`
- `touchChange`
- `accessListAddAccountChange`
- `accessListAddSlotChange`
- `transientStorageChange`
- `add`
- `remove`
- `clearKind`
- `copy`
- `add`
- `remove`
- `stashBalance`
- `stashNonce`
- `stashCode`
- `mutationStateFor`
- `newJournal`
- `reset`
- `snapshot`
- `revertToSnapshot`
- `append`
- `revert`
- `ripemdMagic`
- `length`
- `copy`
- `logChange`
- `createObject`
- `createContract`
- `destruct`
- `storageChange`
- `transientStateChange`
- `refundChange`
- `balanceChange`
- `setCode`
- `nonceChange`
- `touchChange`
- `accessListAddAccount`
- `accessListAddSlot`
- `revert`
- `mutation`
- `copy`
- `revert`
- `mutation`
- `copy`
- `revert`
- `mutation`
- `copy`
- `revert`
- `mutation`
- `copy`
- `revert`
- `mutation`
- `copy`
- `revert`
- `mutation`
- `copy`
- `revert`
- `mutation`
- `copy`
- `revert`
- `mutation`
- `copy`
- `revert`
- `mutation`
- `copy`
- `revert`
- `mutation`
- `copy`
- `revert`
- `mutation`
- `copy`
- `revert`
- `mutation`
- `copy`
- `revert`
- `mutation`
- `copy`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]

## Imported By (Dependents)
*Not imported by any file*

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

package state

import (
	"fmt"
...
```