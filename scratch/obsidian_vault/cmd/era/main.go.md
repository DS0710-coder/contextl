# main.go

## Architecture Metrics
- **Path:** `cmd/era/main.go`
- **Extension:** `.go`
- **Size:** 11254 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 10

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `init`
- `main`
- `block`
- `info`
- `open`
- `openByPath`
- `verify`
- `checkAccumulator`
- `readHashes`

## Imports (Dependencies)
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]
- [[internal/era/era.go.md|internal/era/era.go]]
- [[internal/era/execdb/builder.go.md|internal/era/execdb/builder.go]]
- [[internal/era/onedb/builder.go.md|internal/era/onedb/builder.go]]
- [[internal/ethapi/addrlock.go.md|internal/ethapi/addrlock.go]]
- [[internal/flags/flags.go.md|internal/flags/flags.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[trie/trie.go.md|trie/trie.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2023 The go-ethereum Authors
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

package main

import (
	"encoding/json"
...
```