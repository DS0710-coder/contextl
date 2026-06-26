# bench_test.go

## Architecture Metrics
- **Path:** `core/bench_test.go`
- **Extension:** `.go`
- **Size:** 10296 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BenchmarkInsertChain_empty_memdb`
- `BenchmarkInsertChain_empty_diskdb`
- `BenchmarkInsertChain_valueTx_memdb`
- `BenchmarkInsertChain_valueTx_diskdb`
- `BenchmarkInsertChain_valueTx_100kB_memdb`
- `BenchmarkInsertChain_valueTx_100kB_diskdb`
- `BenchmarkInsertChain_uncles_memdb`
- `BenchmarkInsertChain_uncles_diskdb`
- `BenchmarkInsertChain_ring200_memdb`
- `BenchmarkInsertChain_ring200_diskdb`
- `BenchmarkInsertChain_ring1000_memdb`
- `BenchmarkInsertChain_ring1000_diskdb`
- `genValueTx`
- `init`
- `genTxRing`
- `genUncles`
- `benchInsertChain`
- `BenchmarkChainRead_header_10k`
- `BenchmarkChainRead_full_10k`
- `BenchmarkChainRead_header_100k`
- `BenchmarkChainRead_full_100k`
- `BenchmarkChainRead_header_500k`
- `BenchmarkChainRead_full_500k`
- `BenchmarkChainWrite_header_10k`
- `BenchmarkChainWrite_full_10k`
- `BenchmarkChainWrite_header_100k`
- `BenchmarkChainWrite_full_100k`
- `BenchmarkChainWrite_header_500k`
- `BenchmarkChainWrite_full_500k`
- `makeChainForBench`
- `benchWriteChain`
- `benchReadChain`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[consensus/ethash/ethash.go.md|consensus/ethash/ethash.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[ethdb/pebble/pebble.go.md|ethdb/pebble/pebble.go]]
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

package core

import (
	"crypto/ecdsa"
...
```