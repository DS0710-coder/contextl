# trie.go

## Architecture Metrics
- **Path:** `trie/trie.go`
- **Extension:** `.go`
- **Size:** 25400 bytes
- **Centrality Score:** 0.0022
- **In-Degree (Imported By):** 71
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Trie`
- `newFlag`
- `Copy`
- `New`
- `NewEmpty`
- `MustNodeIterator`
- `NodeIterator`
- `NodeIteratorWithPrefix`
- `NodeIteratorWithRange`
- `MustGet`
- `Get`
- `get`
- `Prefetch`
- `MustGetNode`
- `GetNode`
- `getNode`
- `MustUpdate`
- `Update`
- `update`
- `insert`
- `MustDelete`
- `Delete`
- `delete`
- `copyNode`
- `resolve`
- `resolveAndTrack`
- `deletedNodes`
- `Hash`
- `Commit`
- `hashRoot`
- `Witness`
- `reset`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]
- [[log/format.go.md|log/format.go]]
- [[node/api.go.md|node/api.go]]
- [[triedb/database.go.md|triedb/database.go]]

## Imported By (Dependents)
- [[beacon/engine/types.go.md|beacon/engine/types.go]]
- [[beacon/types/exec_payload.go.md|beacon/types/exec_payload.go]]
- [[cmd/devp2p/internal/ethtest/snap.go.md|cmd/devp2p/internal/ethtest/snap.go]]
- [[cmd/devp2p/internal/ethtest/suite.go.md|cmd/devp2p/internal/ethtest/suite.go]]
- [[cmd/era/main.go.md|cmd/era/main.go]]
- [[cmd/evm/internal/t8ntool/execution.go.md|cmd/evm/internal/t8ntool/execution.go]]
- [[cmd/geth/bintrie_convert.go.md|cmd/geth/bintrie_convert.go]]
- [[cmd/geth/dbcmd.go.md|cmd/geth/dbcmd.go]]
- [[cmd/geth/snapshot.go.md|cmd/geth/snapshot.go]]
- [[cmd/utils/history_test.go.md|cmd/utils/history_test.go]]
- [[core/block_validator.go.md|core/block_validator.go]]
- [[core/blockchain_test.go.md|core/blockchain_test.go]]
- [[core/genesis.go.md|core/genesis.go]]
- [[core/state/database.go.md|core/state/database.go]]
- [[core/state/database_history.go.md|core/state/database_history.go]]
- [[core/state/database_iterator.go.md|core/state/database_iterator.go]]
- [[core/state/database_iterator_test.go.md|core/state/database_iterator_test.go]]
- [[core/state/database_mpt.go.md|core/state/database_mpt.go]]
- [[core/state/iterator.go.md|core/state/iterator.go]]
- [[core/state/pruner/pruner.go.md|core/state/pruner/pruner.go]]
- [[core/state/reader.go.md|core/state/reader.go]]
- [[core/state/snapshot/conversion.go.md|core/state/snapshot/conversion.go]]
- [[core/state/snapshot/generate.go.md|core/state/snapshot/generate.go]]
- [[core/state/snapshot/generate_test.go.md|core/state/snapshot/generate_test.go]]
- [[core/state/state_object.go.md|core/state/state_object.go]]
- [[core/state/statedb.go.md|core/state/statedb.go]]
- [[core/state/statedb_fuzz_test.go.md|core/state/statedb_fuzz_test.go]]
- [[core/state/statedb_test.go.md|core/state/statedb_test.go]]
- [[core/state/sync.go.md|core/state/sync.go]]
- [[core/state/sync_test.go.md|core/state/sync_test.go]]
- [[core/state_processor.go.md|core/state_processor.go]]
- [[core/state_processor_test.go.md|core/state_processor_test.go]]
- [[core/stateless.go.md|core/stateless.go]]
- [[core/stateless/stats.go.md|core/stateless/stats.go]]
- [[core/txpool/blobpool/blobpool_test.go.md|core/txpool/blobpool/blobpool_test.go]]
- [[core/txpool/legacypool/legacypool_test.go.md|core/txpool/legacypool/legacypool_test.go]]
- [[core/types/hashing_test.go.md|core/types/hashing_test.go]]
- [[eth/api_debug.go.md|eth/api_debug.go]]
- [[eth/catalyst/api_test.go.md|eth/catalyst/api_test.go]]
- [[eth/downloader/downloader_test.go.md|eth/downloader/downloader_test.go]]
- [[eth/downloader/queue_test.go.md|eth/downloader/queue_test.go]]
- [[eth/protocols/eth/handler_test.go.md|eth/protocols/eth/handler_test.go]]
- [[eth/protocols/eth/handlers.go.md|eth/protocols/eth/handlers.go]]
- [[eth/protocols/eth/receipt_test.go.md|eth/protocols/eth/receipt_test.go]]
- [[eth/protocols/snap/gentrie.go.md|eth/protocols/snap/gentrie.go]]
- [[eth/protocols/snap/gentrie_test.go.md|eth/protocols/snap/gentrie_test.go]]
- [[eth/protocols/snap/handlers.go.md|eth/protocols/snap/handlers.go]]
- [[eth/protocols/snap/sync.go.md|eth/protocols/snap/sync.go]]
- [[eth/protocols/snap/sync_test.go.md|eth/protocols/snap/sync_test.go]]
- [[eth/protocols/snap/syncv2.go.md|eth/protocols/snap/syncv2.go]]
- [[eth/protocols/snap/syncv2_test.go.md|eth/protocols/snap/syncv2_test.go]]
- [[eth/state_accessor.go.md|eth/state_accessor.go]]
- [[miner/miner_test.go.md|miner/miner_test.go]]
- [[tests/fuzzers/rangeproof/rangeproof-fuzzer.go.md|tests/fuzzers/rangeproof/rangeproof-fuzzer.go]]
- [[trie/bintrie/format_test.go.md|trie/bintrie/format_test.go]]
- [[trie/bintrie/iterator.go.md|trie/bintrie/iterator.go]]
- [[trie/bintrie/iterator_test.go.md|trie/bintrie/iterator_test.go]]
- [[trie/bintrie/recorder_test.go.md|trie/bintrie/recorder_test.go]]
- [[trie/bintrie/trie.go.md|trie/bintrie/trie.go]]
- [[trie/bintrie/trie_test.go.md|trie/bintrie/trie_test.go]]
- [[trie/transitiontrie/transition.go.md|trie/transitiontrie/transition.go]]
- [[triedb/generate.go.md|triedb/generate.go]]
- [[triedb/generate_test.go.md|triedb/generate_test.go]]
- [[triedb/hashdb/database.go.md|triedb/hashdb/database.go]]
- [[triedb/internal/conversion.go.md|triedb/internal/conversion.go]]
- [[triedb/pathdb/database_test.go.md|triedb/pathdb/database_test.go]]
- [[triedb/pathdb/execute.go.md|triedb/pathdb/execute.go]]
- [[triedb/pathdb/generate.go.md|triedb/pathdb/generate.go]]
- [[triedb/pathdb/generate_test.go.md|triedb/pathdb/generate_test.go]]
- [[triedb/pathdb/nodes.go.md|triedb/pathdb/nodes.go]]
- [[triedb/pathdb/verifier.go.md|triedb/pathdb/verifier.go]]

## Source Code Snippet
```go
// Copyright 2014 The go-ethereum Authors
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

// Package trie implements Merkle Patricia Tries.
package trie

import (
...
```