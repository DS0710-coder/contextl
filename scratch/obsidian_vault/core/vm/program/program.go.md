# program.go

## Architecture Metrics
- **Path:** `core/vm/program/program.go`
- **Extension:** `.go`
- **Size:** 13147 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Program`
- `New`
- `add`
- `doPush`
- `Append`
- `Bytes`
- `SetBytes`
- `Hex`
- `Op`
- `Push`
- `Push0`
- `ExtcodeCopy`
- `Call`
- `DelegateCall`
- `StaticCall`
- `CallCode`
- `Label`
- `Jumpdest`
- `Jump`
- `JumpIf`
- `Size`
- `InputAddressToStack`
- `Mstore`
- `MstoreSmall`
- `MemToStorage`
- `ReturnViaCodeCopy`
- `Sstore`
- `Tstore`
- `Return`
- `ReturnData`
- `Create2`
- `Create2ThenCall`
- `Selfdestruct`

## Imports (Dependencies)
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]

## Imported By (Dependents)
- [[core/blockchain_test.go.md|core/blockchain_test.go]]
- [[core/vm/runtime/runtime_test.go.md|core/vm/runtime/runtime_test.go]]

## Source Code Snippet
```go
// Copyright 2024 The go-ethereum Authors
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

// package program is a utility to create EVM bytecode for testing, but _not_ for production. As such:
//
// - There are not package guarantees. We might iterate heavily on this package, and do backwards-incompatible changes without warning
// - There are no quality-guarantees. These utilities may produce evm-code that is non-functional. YMMV.
...
```