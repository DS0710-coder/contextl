# chaincmd.go

## Architecture Metrics
- **Path:** `cmd/geth/chaincmd.go`
- **Extension:** `.go`
- **Size:** 27491 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 21

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `initGenesis`
- `dumpGenesis`
- `importChain`
- `exportChain`
- `importHistory`
- `exportHistory`
- `importPreimages`
- `parseDumpConfig`
- `dump`
- `hashish`
- `pruneHistory`
- `downloadEra`
- `parseRange`

## Imports (Dependencies)
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[cmd/utils/cmd.go.md|cmd/utils/cmd.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/history/historymode.go.md|core/history/historymode.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[internal/debug/api.go.md|internal/debug/api.go]]
- [[internal/era/era.go.md|internal/era/era.go]]
- [[internal/era/eradl/eradl.go.md|internal/era/eradl/eradl.go]]
- [[internal/era/execdb/builder.go.md|internal/era/execdb/builder.go]]
- [[internal/era/onedb/builder.go.md|internal/era/onedb/builder.go]]
- [[internal/flags/flags.go.md|internal/flags/flags.go]]
- [[log/format.go.md|log/format.go]]
- [[node/node.go.md|node/node.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2015 The go-ethereum Authors
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