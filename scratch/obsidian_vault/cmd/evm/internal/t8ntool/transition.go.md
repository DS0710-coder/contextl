# transition.go

## Architecture Metrics
- **Path:** `cmd/evm/internal/t8ntool/transition.go`
- **Extension:** `.go`
- **Size:** 22251 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 20

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `NumberedError`
- `input`
- `streamingAlloc`
- `NewError`
- `Error`
- `ExitCode`
- `Transition`
- `mergeUnmigratedBaseAlloc`
- `OnRoot`
- `OnAccount`
- `writeStreamedAlloc`
- `applyLondonChecks`
- `applyShanghaiChecks`
- `applyMergeChecks`
- `applyCancunChecks`
- `OnRoot`
- `OnAccount`
- `dumpAccountToTypesAccount`
- `newStreamingAlloc`
- `write`
- `OnRoot`
- `OnAccount`
- `Close`
- `saveFile`
- `dispatchOutput`
- `BinKey`
- `BinKeys`
- `BinTrieRoot`
- `genBinTrieFromAlloc`
- `BinaryCodeChunkKey`
- `BinaryCodeChunkCode`

## Imports (Dependencies)
- [[accounts/abi/bind/v2/auth.go.md|accounts/abi/bind/v2/auth.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[consensus/misc/eip1559/eip1559.go.md|consensus/misc/eip1559/eip1559.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/overlay/state_transition.go.md|core/overlay/state_transition.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/tracing/gen_balance_change_reason_stringer.go.md|core/tracing/gen_balance_change_reason_stringer.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[eth/tracers/api.go.md|eth/tracers/api.go]]
- [[eth/tracers/logger/logger.go.md|eth/tracers/logger/logger.go]]
- [[eth/tracers/native/4byte.go.md|eth/tracers/native/4byte.go]]
- [[log/format.go.md|log/format.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[tests/block_test.go.md|tests/block_test.go]]
- [[trie/bintrie/binary_node.go.md|trie/bintrie/binary_node.go]]
- [[triedb/database.go.md|triedb/database.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2020 The go-ethereum Authors
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

package t8ntool

import (
	"bufio"
...
```