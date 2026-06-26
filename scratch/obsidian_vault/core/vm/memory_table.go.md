# memory_table.go

## Architecture Metrics
- **Path:** `core/vm/memory_table.go`
- **Extension:** `.go`
- **Size:** 3290 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `memoryKeccak256`
- `memoryCallDataCopy`
- `memoryReturnDataCopy`
- `memoryCodeCopy`
- `memoryExtCodeCopy`
- `memoryMLoad`
- `memoryMStore8`
- `memoryMStore`
- `memoryMcopy`
- `memoryCreate`
- `memoryCreate2`
- `memoryCall`
- `memoryDelegateCall`
- `memoryStaticCall`
- `memoryReturn`
- `memoryRevert`
- `memoryLog`

## Imports (Dependencies)
*No internal imports*

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

func memoryKeccak256(stack *Stack) (uint64, bool) {
	return calcMemSize64(stack.back(0), stack.back(1))
...
```