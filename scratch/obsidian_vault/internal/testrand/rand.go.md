# rand.go

## Architecture Metrics
- **Path:** `internal/testrand/rand.go`
- **Extension:** `.go`
- **Size:** 1649 bytes
- **Centrality Score:** 0.0011
- **In-Degree (Imported By):** 21
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `initRand`
- `Bytes`
- `Hash`
- `Address`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]

## Imported By (Dependents)
- [[accounts/abi/abi_test.go.md|accounts/abi/abi_test.go]]
- [[cmd/workload/prooftestgen.go.md|cmd/workload/prooftestgen.go]]
- [[core/rawdb/ancienttest/testsuite.go.md|core/rawdb/ancienttest/testsuite.go]]
- [[core/state/reader_eip_7928_test.go.md|core/state/reader_eip_7928_test.go]]
- [[core/state/trie_prefetcher_test.go.md|core/state/trie_prefetcher_test.go]]
- [[core/txpool/blobpool/blobpool_test.go.md|core/txpool/blobpool/blobpool_test.go]]
- [[core/types/bal/bal_test.go.md|core/types/bal/bal_test.go]]
- [[eth/catalyst/api_test.go.md|eth/catalyst/api_test.go]]
- [[eth/protocols/snap/gentrie_test.go.md|eth/protocols/snap/gentrie_test.go]]
- [[eth/protocols/snap/sync_test.go.md|eth/protocols/snap/sync_test.go]]
- [[trie/node_test.go.md|trie/node_test.go]]
- [[trie/trie_test.go.md|trie/trie_test.go]]
- [[trie/trienode/node_test.go.md|trie/trienode/node_test.go]]
- [[triedb/pathdb/database_test.go.md|triedb/pathdb/database_test.go]]
- [[triedb/pathdb/difflayer_test.go.md|triedb/pathdb/difflayer_test.go]]
- [[triedb/pathdb/generate_test.go.md|triedb/pathdb/generate_test.go]]
- [[triedb/pathdb/history_reader_test.go.md|triedb/pathdb/history_reader_test.go]]
- [[triedb/pathdb/history_state_test.go.md|triedb/pathdb/history_state_test.go]]
- [[triedb/pathdb/history_trienode_test.go.md|triedb/pathdb/history_trienode_test.go]]
- [[triedb/pathdb/iterator_test.go.md|triedb/pathdb/iterator_test.go]]
- [[triedb/pathdb/nodes_test.go.md|triedb/pathdb/nodes_test.go]]

## Source Code Snippet
```go
// Copyright 2023 The go-ethereum Authors
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

package testrand

import (
	crand "crypto/rand"
...
```