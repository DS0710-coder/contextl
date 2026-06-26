# jsre.go

## Architecture Metrics
- **Path:** `internal/jsre/jsre.go`
- **Extension:** `.go`
- **Size:** 10532 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `JSRE`
- `Call`
- `jsTimer`
- `evalReq`
- `New`
- `randomSource`
- `runEventLoop`
- `Do`
- `Stop`
- `Exec`
- `Run`
- `Set`
- `MakeCallback`
- `Evaluate`
- `Interrupt`
- `Compile`
- `loadScript`
- `compileAndRun`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]

## Imported By (Dependents)
- [[console/bridge.go.md|console/bridge.go]]
- [[console/console.go.md|console/console.go]]
- [[console/console_test.go.md|console/console_test.go]]

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

// Package jsre provides execution environment for JavaScript.
package jsre

import (
...
```