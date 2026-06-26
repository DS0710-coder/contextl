# dbcmd.go

## Architecture Metrics
- **Path:** `cmd/geth/dbcmd.go`
- **Extension:** `.go`
- **Size:** 32707 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 17

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `preimageIterator`
- `snapshotIterator`
- `codeIterator`
- `removeDB`
- `removeFolder`
- `confirmAndRemoveDB`
- `inspect`
- `checkStateContent`
- `inspectTrie`
- `showDBStats`
- `dbStats`
- `dbCompact`
- `dbPebbleUpgrade`
- `dbGet`
- `dbDelete`
- `dbPut`
- `dbDumpTrie`
- `freezerInspect`
- `importLDBdata`
- `Next`
- `Release`
- `Next`
- `Release`
- `Next`
- `Release`
- `exportChaindata`
- `showMetaData`
- `inspectAccount`
- `inspectStorage`
- `inspectHistory`

## Imports (Dependencies)
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[cmd/utils/cmd.go.md|cmd/utils/cmd.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[console/prompt/prompter.go.md|console/prompt/prompter.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/state/snapshot/snapshot.go.md|core/state/snapshot/snapshot.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[ethdb/pebble/pebble.go.md|ethdb/pebble/pebble.go]]
- [[internal/tablewriter/database_tablewriter.go.md|internal/tablewriter/database_tablewriter.go]]
- [[log/format.go.md|log/format.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[trie/trie.go.md|trie/trie.go]]
- [[triedb/database.go.md|triedb/database.go]]

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
	"bytes"
...
```