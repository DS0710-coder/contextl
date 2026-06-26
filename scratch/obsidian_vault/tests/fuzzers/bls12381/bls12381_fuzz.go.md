# bls12381_fuzz.go

## Architecture Metrics
- **Path:** `tests/fuzzers/bls12381/bls12381_fuzz.go`
- **Extension:** `.go`
- **Size:** 9659 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `fuzzG1SubgroupChecks`
- `fuzzG2SubgroupChecks`
- `fuzzCrossPairing`
- `massageBLST`
- `fuzzCrossG1Add`
- `fuzzCrossG2Add`
- `fuzzCrossG1MultiExp`
- `fuzzCrossG2MultiExp`
- `getG1Points`
- `getG2Points`
- `randomScalar`
- `multiExpG1Gnark`
- `multiExpG2Gnark`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]

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

//go:build cgo
// +build cgo

package bls
...
```