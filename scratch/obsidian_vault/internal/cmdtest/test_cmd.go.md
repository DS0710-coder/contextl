# test_cmd.go

## Architecture Metrics
- **Path:** `internal/cmdtest/test_cmd.go`
- **Extension:** `.go`
- **Size:** 7915 bytes
- **Centrality Score:** 0.0005
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `TestCmd`
- `testlogger`
- `runeTee`
- `NewTestCmd`
- `Run`
- `InputLine`
- `SetTemplateFunc`
- `Expect`
- `Output`
- `matchExactOutput`
- `ExpectRegexp`
- `ExpectExit`
- `WaitExit`
- `Interrupt`
- `ExitStatus`
- `StderrText`
- `CloseStdin`
- `Kill`
- `withKillTimeout`
- `Write`
- `Read`
- `ReadRune`
- `ReadByte`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[internal/reexec/reexec.go.md|internal/reexec/reexec.go]]

## Imported By (Dependents)
- [[cmd/ethkey/run_test.go.md|cmd/ethkey/run_test.go]]
- [[cmd/evm/t8n_test.go.md|cmd/evm/t8n_test.go]]
- [[cmd/geth/run_test.go.md|cmd/geth/run_test.go]]

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

package cmdtest

import (
	"bufio"
...
```