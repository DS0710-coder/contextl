# bitarray.go

## Architecture Metrics
- **Path:** `trie/bintrie/bitarray.go`
- **Extension:** `.go`
- **Size:** 5105 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BitArray`
- `NewBitArray`
- `Len`
- `Bytes`
- `AppendBit`
- `MSBs`
- `Equal`
- `SetBytes`
- `SetBit`
- `Copy`
- `Set`
- `KeyBytes`
- `PutKeyBytes`
- `maskTail`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2026 The go-ethereum Authors
// This file is part of go-ethereum.
//
// go-ethereum is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// go-ethereum is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with go-ethereum. If not, see <http://www.gnu.org/licenses/>.
package bintrie

// BitArray represents a trie path: the most significant `len` bits of a key,
// packed big-endian and MSB-first. Bit i (0 = most significant) lives at
// bytes[i/8] in mask 1<<(7-i%8). All bits at positions >= len are kept zero so
...
```