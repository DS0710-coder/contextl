# eips.go

## Architecture Metrics
- **Path:** `core/vm/eips.go`
- **Extension:** `.go`
- **Size:** 17283 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `EnableEIP`
- `ValidEip`
- `ActivateableEips`
- `enable1884`
- `opSelfBalance`
- `enable1344`
- `opChainID`
- `enable2200`
- `enable2929`
- `enable3529`
- `enable3198`
- `enable1153`
- `opTload`
- `opTstore`
- `opBaseFee`
- `enable3855`
- `opPush0`
- `enable3860`
- `enable5656`
- `opMcopy`
- `opBlobHash`
- `opBlobBaseFee`
- `opCLZ`
- `enable4844`
- `enable7939`
- `enable7516`
- `enable6780`
- `enable8024`
- `opExtCodeCopyEIP4762`
- `opPush1EIP4762`
- `makePushEIP4762`
- `enable4762`
- `enable7702`
- `opSlotNum`
- `enable7843`
- `enable8037`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2019 The go-ethereum Authors
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

package vm

import (
	"fmt"
...
```