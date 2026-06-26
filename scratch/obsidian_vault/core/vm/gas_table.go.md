# gas_table.go

## Architecture Metrics
- **Path:** `core/vm/gas_table.go`
- **Extension:** `.go`
- **Size:** 28182 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `memoryGasCost`
- `memoryCopierGas`
- `gasSStore`
- `gasSStoreEIP2200`
- `makeGasLog`
- `gasKeccak256`
- `pureMemoryGascost`
- `gasCreate`
- `gasCreate2`
- `gasCreateEip3860`
- `gasCreate2Eip3860`
- `gasExpFrontier`
- `gasExpEIP158`
- `makeCallVariantGasCost`
- `gasCallIntrinsic`
- `gasCallCodeIntrinsic`
- `gasDelegateCallIntrinsic`
- `gasStaticCallIntrinsic`
- `gasSelfdestruct`
- `gasCreateEip8037`
- `gasCreate2Eip8037`
- `regularGasCall8037`
- `stateGasCall8037`
- `gasSelfdestruct8037`
- `gasSStore8037`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
*Not imported by any file*

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

package vm

import (
	"errors"
...
```