# cmd.go

## Architecture Metrics
- **Path:** `cmd/utils/cmd.go`
- **Extension:** `.go`
- **Size:** 28565 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 17
- **Out-Degree (Imports):** 18

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `StateIterator`
- `hashAndPreimageSize`
- `exportHeader`
- `ChainDataIterator`
- `Fatalf`
- `StartNode`
- `monitorFreeDiskSpace`
- `ImportChain`
- `readList`
- `ImportHistory`
- `missingBlocks`
- `ExportChain`
- `ExportAppendChain`
- `ExportHistory`
- `ImportPreimages`
- `ExportPreimages`
- `NewStateIterator`
- `AccountIterator`
- `StorageIterator`
- `ExportSnapshotPreimages`
- `ImportLDBData`
- `ExportChaindata`

## Imports (Dependencies)
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/state/snapshot/snapshot.go.md|core/state/snapshot/snapshot.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/runtime/runtime.go.md|core/vm/runtime/runtime.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[internal/debug/api.go.md|internal/debug/api.go]]
- [[internal/era/era.go.md|internal/era/era.go]]
- [[log/format.go.md|log/format.go]]
- [[node/node.go.md|node/node.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[triedb/database.go.md|triedb/database.go]]

## Imported By (Dependents)
- [[accounts/abi/bind/v2/generate_test.go.md|accounts/abi/bind/v2/generate_test.go]]
- [[cmd/abigen/main.go.md|cmd/abigen/main.go]]
- [[cmd/blsync/main.go.md|cmd/blsync/main.go]]
- [[cmd/ethkey/changepassword.go.md|cmd/ethkey/changepassword.go]]
- [[cmd/ethkey/generate.go.md|cmd/ethkey/generate.go]]
- [[cmd/ethkey/inspect.go.md|cmd/ethkey/inspect.go]]
- [[cmd/ethkey/message.go.md|cmd/ethkey/message.go]]
- [[cmd/ethkey/utils.go.md|cmd/ethkey/utils.go]]
- [[cmd/evm/runner.go.md|cmd/evm/runner.go]]
- [[cmd/geth/accountcmd.go.md|cmd/geth/accountcmd.go]]
- [[cmd/geth/bintrie_convert.go.md|cmd/geth/bintrie_convert.go]]
- [[cmd/geth/chaincmd.go.md|cmd/geth/chaincmd.go]]
- [[cmd/geth/config.go.md|cmd/geth/config.go]]
- [[cmd/geth/consolecmd.go.md|cmd/geth/consolecmd.go]]
- [[cmd/geth/dbcmd.go.md|cmd/geth/dbcmd.go]]
- [[cmd/geth/main.go.md|cmd/geth/main.go]]
- [[cmd/geth/snapshot.go.md|cmd/geth/snapshot.go]]

## Source Code Snippet
```go
// Copyright 2014 The go-ethereum Authors
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

// Package utils contains internal helper functions for go-ethereum commands.
package utils

import (
...
```