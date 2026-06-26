# contracts.go

## Architecture Metrics
- **Path:** `core/vm/contracts.go`
- **Extension:** `.go`
- **Size:** 46699 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 10

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PrecompiledContract`
- `ecrecover`
- `sha256hash`
- `ripemd160hash`
- `dataCopy`
- `bigModExp`
- `bn256AddIstanbul`
- `bn256AddByzantium`
- `bn256ScalarMulIstanbul`
- `bn256ScalarMulByzantium`
- `bn256PairingIstanbul`
- `bn256PairingByzantium`
- `blake2F`
- `bls12381G1Add`
- `bls12381G1MultiExp`
- `bls12381G2Add`
- `bls12381G2MultiExp`
- `bls12381Pairing`
- `bls12381MapG1`
- `bls12381MapG2`
- `kzgPointEvaluation`
- `p256Verify`
- `init`
- `activePrecompiledContracts`
- `ActivePrecompiledContracts`
- `ActivePrecompiles`
- `RunPrecompiledContract`
- `RequiredGas`
- `Run`
- `Name`
- `RequiredGas`
- `Run`
- `Name`
- `RequiredGas`
- `Run`
- `Name`
- `RequiredGas`
- `Run`
- `Name`
- `byzantiumMultComplexity`
- `berlinMultComplexity`
- `osakaMultComplexity`
- `modexpIterationCount`
- `byzantiumModexpGas`
- `berlinModexpGas`
- `osakaModexpGas`
- `RequiredGas`
- `Run`
- `Name`
- `newCurvePoint`
- `newTwistPoint`
- `runBn256Add`
- `RequiredGas`
- `Run`
- `Name`
- `RequiredGas`
- `Run`
- `Name`
- `runBn256ScalarMul`
- `RequiredGas`
- `Run`
- `Name`
- `RequiredGas`
- `Run`
- `Name`
- `runBn256Pairing`
- `RequiredGas`
- `Run`
- `Name`
- `RequiredGas`
- `Run`
- `Name`
- `RequiredGas`
- `Run`
- `Name`
- `RequiredGas`
- `Run`
- `Name`
- `RequiredGas`
- `Run`
- `Name`
- `RequiredGas`
- `Run`
- `Name`
- `RequiredGas`
- `Run`
- `Name`
- `RequiredGas`
- `Run`
- `Name`
- `decodePointG1`
- `decodePointG2`
- `decodeBLS12381FieldElement`
- `encodePointG1`
- `encodePointG2`
- `RequiredGas`
- `Run`
- `Name`
- `RequiredGas`
- `Run`
- `Name`
- `RequiredGas`
- `Run`
- `Name`
- `kZGToVersionedHash`
- `RequiredGas`
- `Run`
- `Name`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/bitutil/bitutil.go.md|common/bitutil/bitutil.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[crypto/blake2b/blake2b.go.md|crypto/blake2b/blake2b.go]]
- [[crypto/bn256/bn256_fast.go.md|crypto/bn256/bn256_fast.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[crypto/kzg4844/kzg4844.go.md|crypto/kzg4844/kzg4844.go]]
- [[crypto/secp256r1/verifier.go.md|crypto/secp256r1/verifier.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2014 The go-ethereum Authors
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
	"crypto/sha256"
...
```