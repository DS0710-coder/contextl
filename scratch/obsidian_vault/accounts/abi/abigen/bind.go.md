# bind.go

## Architecture Metrics
- **Path:** `accounts/abi/abigen/bind.go`
- **Extension:** `.go`
- **Size:** 14901 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `isKeyWord`
- `Bind`
- `bindBasicType`
- `bindType`
- `bindTopicType`
- `bindStructType`
- `alias`
- `decapitalise`
- `structured`
- `hasStruct`

## Imports (Dependencies)
- [[accounts/abi/abi.go.md|accounts/abi/abi.go]]
- [[log/format.go.md|log/format.go]]

## Imported By (Dependents)
- [[accounts/abi/bind/old.go.md|accounts/abi/bind/old.go]]
- [[accounts/abi/bind/v2/generate_test.go.md|accounts/abi/bind/v2/generate_test.go]]
- [[cmd/abigen/main.go.md|cmd/abigen/main.go]]

## Source Code Snippet
```go
// Copyright 2016 The go-ethereum Authors
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

// Package abigen generates Ethereum contract Go bindings.
//
// Detailed usage document and tutorial available on the go-ethereum Wiki page:
// https://geth.ethereum.org/docs/developers/dapp-developer/native-bindings
...
```