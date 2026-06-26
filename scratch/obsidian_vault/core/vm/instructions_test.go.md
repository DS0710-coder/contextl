# instructions_test.go

## Architecture Metrics
- **Path:** `core/vm/instructions_test.go`
- **Extension:** `.go`
- **Size:** 41913 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TwoOperandTestcase`
- `twoOperandParams`
- `testcase`
- `testcase`
- `testcase`
- `init`
- `testTwoOperandOp`
- `TestByteOp`
- `TestSHL`
- `TestSHR`
- `TestSAR`
- `TestAddMod`
- `TestWriteExpectedValues`
- `TestJsonTestcases`
- `opBenchmark`
- `BenchmarkOpAdd64`
- `BenchmarkOpAdd128`
- `BenchmarkOpAdd256`
- `BenchmarkOpSub64`
- `BenchmarkOpSub128`
- `BenchmarkOpSub256`
- `BenchmarkOpMul`
- `BenchmarkOpDiv256`
- `BenchmarkOpDiv128`
- `BenchmarkOpDiv64`
- `BenchmarkOpSdiv`
- `BenchmarkOpMod`
- `BenchmarkOpSmod`
- `BenchmarkOpExp`
- `BenchmarkOpSignExtend`
- `BenchmarkOpLt`
- `BenchmarkOpGt`
- `BenchmarkOpSlt`
- `BenchmarkOpSgt`
- `BenchmarkOpEq`
- `BenchmarkOpEq2`
- `BenchmarkOpAnd`
- `BenchmarkOpOr`
- `BenchmarkOpXor`
- `BenchmarkOpByte`
- `BenchmarkOpAddmod`
- `BenchmarkOpMulmod`
- `BenchmarkOpSHL`
- `BenchmarkOpSHR`
- `BenchmarkOpSAR`
- `BenchmarkOpIsZero`
- `TestOpMstore`
- `BenchmarkOpMstore`
- `TestOpTstore`
- `BenchmarkOpKeccak256`
- `TestCreate2Addresses`
- `TestRandom`
- `TestBlobHash`
- `TestOpMCopy`
- `TestPush`
- `TestOpCLZ`
- `TestEIP8024_Execution`
- `ptrToByte`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
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
	"bytes"
...
```