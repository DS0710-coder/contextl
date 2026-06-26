# t8n_test.go

## Architecture Metrics
- **Path:** `cmd/evm/t8n_test.go`
- **Extension:** `.go`
- **Size:** 23597 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `testT8n`
- `t8nInput`
- `t8nOutput`
- `t9nInput`
- `b11rInput`
- `TestMain`
- `get`
- `get`
- `TestT8n`
- `lineIterator`
- `get`
- `TestT9n`
- `get`
- `TestB11r`
- `TestEvmRun`
- `TestEvmRunRegEx`
- `cmpJson`
- `TestEVMTracing`

## Imports (Dependencies)
- [[cmd/evm/internal/t8ntool/block.go.md|cmd/evm/internal/t8ntool/block.go]]
- [[internal/cmdtest/test_cmd.go.md|internal/cmdtest/test_cmd.go]]
- [[internal/reexec/reexec.go.md|internal/reexec/reexec.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2021 The go-ethereum Authors
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
	"bufio"
...
```