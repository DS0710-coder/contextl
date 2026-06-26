# setup.go

## Architecture Metrics
- **Path:** `internal/telemetry/tracesetup/setup.go`
- **Extension:** `.go`
- **Size:** 6213 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Service`
- `Start`
- `Stop`
- `SetupTelemetry`

## Imports (Dependencies)
- [[internal/version/version.go.md|internal/version/version.go]]
- [[log/format.go.md|log/format.go]]
- [[node/node.go.md|node/node.go]]
- [[rpc/client.go.md|rpc/client.go]]

## Imported By (Dependents)
- [[cmd/geth/config.go.md|cmd/geth/config.go]]

## Source Code Snippet
```go
// Copyright 2026 The go-ethereum Authors
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

package tracesetup

import (
	"context"
...
```