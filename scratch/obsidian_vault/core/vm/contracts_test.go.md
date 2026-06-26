# contracts_test.go

## Architecture Metrics
- **Path:** `core/vm/contracts_test.go`
- **Extension:** `.go`
- **Size:** 24612 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `precompiledTest`
- `precompiledFailureTest`
- `testPrecompiled`
- `testPrecompiledOOG`
- `testPrecompiledFailure`
- `benchmarkPrecompiled`
- `BenchmarkPrecompiledEcrecover`
- `BenchmarkPrecompiledSha256`
- `BenchmarkPrecompiledRipeMD`
- `BenchmarkPrecompiledIdentity`
- `TestPrecompiledModExp`
- `BenchmarkPrecompiledModExp`
- `TestPrecompiledModExpEip2565`
- `BenchmarkPrecompiledModExpEip2565`
- `TestPrecompiledModExpEip7883`
- `BenchmarkPrecompiledModExpEip7883`
- `TestPrecompiledBn256Add`
- `BenchmarkPrecompiledBn256Add`
- `TestPrecompiledModExpOOG`
- `TestPrecompiledBn256ScalarMul`
- `BenchmarkPrecompiledBn256ScalarMul`
- `TestPrecompiledBn256Pairing`
- `BenchmarkPrecompiledBn256Pairing`
- `TestPrecompiledBlake2F`
- `BenchmarkPrecompiledBlake2F`
- `TestPrecompileBlake2FMalformedInput`
- `TestPrecompiledEcrecover`
- `testJson`
- `testJsonFail`
- `benchJson`
- `TestPrecompiledBLS12381G1Add`
- `TestPrecompiledBLS12381G1Mul`
- `TestPrecompiledBLS12381G1MultiExp`
- `TestPrecompiledBLS12381G2Add`
- `TestPrecompiledBLS12381G2Mul`
- `TestPrecompiledBLS12381G2MultiExp`
- `TestPrecompiledBLS12381Pairing`
- `TestPrecompiledBLS12381MapG1`
- `TestPrecompiledBLS12381MapG2`
- `TestPrecompiledPointEvaluation`
- `BenchmarkPrecompiledPointEvaluation`
- `BenchmarkPrecompiledBLS12381G1Add`
- `BenchmarkPrecompiledBLS12381G1MultiExp`
- `BenchmarkPrecompiledBLS12381G2Add`
- `BenchmarkPrecompiledBLS12381G2MultiExp`
- `BenchmarkPrecompiledBLS12381Pairing`
- `BenchmarkPrecompiledBLS12381MapG1`
- `BenchmarkPrecompiledBLS12381MapG2`
- `TestPrecompiledBLS12381G1AddFail`
- `TestPrecompiledBLS12381G1MulFail`
- `TestPrecompiledBLS12381G1MultiExpFail`
- `TestPrecompiledBLS12381G2AddFail`
- `TestPrecompiledBLS12381G2MulFail`
- `TestPrecompiledBLS12381G2MultiExpFail`
- `TestPrecompiledBLS12381PairingFail`
- `TestPrecompiledBLS12381MapG1Fail`
- `TestPrecompiledBLS12381MapG2Fail`
- `loadJson`
- `loadJsonFail`
- `BenchmarkPrecompiledBLS12381G1MultiExpWorstCase`
- `BenchmarkPrecompiledBLS12381G2MultiExpWorstCase`
- `BenchmarkPrecompiledP256Verify`
- `TestPrecompiledP256Verify`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
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