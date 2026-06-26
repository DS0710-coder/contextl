# utesting.go

## Architecture Metrics
- **Path:** `internal/utesting/utesting.go`
- **Extension:** `.go`
- **Size:** 8184 bytes
- **Centrality Score:** 0.0007
- **In-Degree (Imported By):** 13
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Test`
- `Result`
- `testOutput`
- `consoleOutput`
- `tapOutput`
- `indentWriter`
- `T`
- `MatchTests`
- `RunTests`
- `RunTAP`
- `run`
- `newConsoleOutput`
- `testStart`
- `Write`
- `testResult`
- `newTAP`
- `testStart`
- `Write`
- `testResult`
- `newIndentWriter`
- `Write`
- `flush`
- `CountFailures`
- `Run`
- `runTest`
- `Helper`
- `FailNow`
- `Fail`
- `Failed`
- `Log`
- `Logf`
- `Error`
- `Errorf`
- `Fatal`
- `Fatalf`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]

## Imported By (Dependents)
- [[cmd/devp2p/internal/ethtest/snap.go.md|cmd/devp2p/internal/ethtest/snap.go]]
- [[cmd/devp2p/internal/ethtest/snap2.go.md|cmd/devp2p/internal/ethtest/snap2.go]]
- [[cmd/devp2p/internal/ethtest/suite.go.md|cmd/devp2p/internal/ethtest/suite.go]]
- [[cmd/devp2p/internal/ethtest/suite_test.go.md|cmd/devp2p/internal/ethtest/suite_test.go]]
- [[cmd/devp2p/internal/ethtest/transaction.go.md|cmd/devp2p/internal/ethtest/transaction.go]]
- [[cmd/devp2p/internal/v4test/discv4tests.go.md|cmd/devp2p/internal/v4test/discv4tests.go]]
- [[cmd/devp2p/internal/v5test/discv5tests.go.md|cmd/devp2p/internal/v5test/discv5tests.go]]
- [[cmd/devp2p/runtest.go.md|cmd/devp2p/runtest.go]]
- [[cmd/workload/filtertest.go.md|cmd/workload/filtertest.go]]
- [[cmd/workload/historytest.go.md|cmd/workload/historytest.go]]
- [[cmd/workload/prooftest.go.md|cmd/workload/prooftest.go]]
- [[cmd/workload/testsuite.go.md|cmd/workload/testsuite.go]]
- [[cmd/workload/tracetest.go.md|cmd/workload/tracetest.go]]

## Source Code Snippet
```go
// Copyright 2020 The go-ethereum Authors
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

// Package utesting provides a standalone replacement for package testing.
//
// This package exists because package testing cannot easily be embedded into a
// standalone go program. It provides an API that mirrors the standard library
...
```