# instructions.go

## Architecture Metrics
- **Path:** `core/vm/instructions.go`
- **Extension:** `.go`
- **Size:** 36028 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `opAdd`
- `opSub`
- `opMul`
- `opDiv`
- `opSdiv`
- `opMod`
- `opSmod`
- `opExp`
- `opSignExtend`
- `opNot`
- `opLt`
- `opGt`
- `opSlt`
- `opSgt`
- `opEq`
- `opIszero`
- `opAnd`
- `opOr`
- `opXor`
- `opByte`
- `opAddmod`
- `opMulmod`
- `opSHL`
- `opSHR`
- `opSAR`
- `opKeccak256`
- `opAddress`
- `opBalance`
- `opOrigin`
- `opCaller`
- `opCallValue`
- `opCallDataLoad`
- `opCallDataSize`
- `opCallDataCopy`
- `opReturnDataSize`
- `opReturnDataCopy`
- `opExtCodeSize`
- `opCodeSize`
- `opCodeCopy`
- `opExtCodeCopy`
- `opExtCodeHash`
- `opGasprice`
- `opBlockhash`
- `opCoinbase`
- `opTimestamp`
- `opNumber`
- `opDifficulty`
- `opRandom`
- `opGasLimit`
- `opPop`
- `opMload`
- `opMstore`
- `opMstore8`
- `opSload`
- `opSstore`
- `opJump`
- `opJumpi`
- `opJumpdest`
- `opPc`
- `opMsize`
- `opGas`
- `opSwap1`
- `opSwap2`
- `opSwap3`
- `opSwap4`
- `opSwap5`
- `opSwap6`
- `opSwap7`
- `opSwap8`
- `opSwap9`
- `opSwap10`
- `opSwap11`
- `opSwap12`
- `opSwap13`
- `opSwap14`
- `opSwap15`
- `opSwap16`
- `opCreate`
- `opCreate2`
- `opCall`
- `opCallCode`
- `opDelegateCall`
- `opStaticCall`
- `opReturn`
- `opRevert`
- `opUndefined`
- `opStop`
- `opSelfdestruct`
- `opSelfdestruct6780`
- `decodeSingle`
- `decodePair`
- `opDupN`
- `opSwapN`
- `opExchange`
- `makeLog`
- `opPush1`
- `opPush2`
- `makePush`
- `makeDup`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

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

package vm

import (
	"math"
...
```