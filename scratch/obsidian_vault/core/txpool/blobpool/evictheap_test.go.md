# evictheap_test.go

## Architecture Metrics
- **Path:** `core/txpool/blobpool/evictheap_test.go`
- **Extension:** `.go`
- **Size:** 11958 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `verifyHeapInternals`
- `TestPriceHeapSorting`
- `BenchmarkPriceHeapReinit1MB`
- `BenchmarkPriceHeapReinit10MB`
- `BenchmarkPriceHeapReinit100MB`
- `BenchmarkPriceHeapReinit1GB`
- `BenchmarkPriceHeapReinit10GB`
- `BenchmarkPriceHeapReinit25GB`
- `BenchmarkPriceHeapReinit50GB`
- `BenchmarkPriceHeapReinit100GB`
- `benchmarkPriceHeapReinit`
- `BenchmarkPriceHeapOverflow1MB`
- `BenchmarkPriceHeapOverflow10MB`
- `BenchmarkPriceHeapOverflow100MB`
- `BenchmarkPriceHeapOverflow1GB`
- `BenchmarkPriceHeapOverflow10GB`
- `BenchmarkPriceHeapOverflow25GB`
- `BenchmarkPriceHeapOverflow50GB`
- `BenchmarkPriceHeapOverflow100GB`
- `benchmarkPriceHeapOverflow`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2023 The go-ethereum Authors
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

package blobpool

import (
	"container/heap"
...
```