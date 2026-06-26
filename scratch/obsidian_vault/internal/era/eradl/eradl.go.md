# eradl.go

## Architecture Metrics
- **Path:** `internal/era/eradl/eradl.go`
- **Extension:** `.go`
- **Size:** 3324 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Loader`
- `New`
- `DownloadAll`
- `DownloadBlockRange`
- `DownloadEpochRange`
- `download`

## Imports (Dependencies)
- [[internal/download/download.go.md|internal/download/download.go]]
- [[internal/era/era.go.md|internal/era/era.go]]

## Imported By (Dependents)
- [[cmd/geth/chaincmd.go.md|cmd/geth/chaincmd.go]]

## Source Code Snippet
```go
// Copyright 2025 The go-ethereum Authors
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

// Package eradl implements downloading of era1 files.
package eradl

import (
...
```