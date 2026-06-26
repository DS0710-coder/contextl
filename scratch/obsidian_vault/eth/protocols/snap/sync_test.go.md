# sync_test.go

## Architecture Metrics
- **Path:** `eth/protocols/snap/sync_test.go`
- **Extension:** `.go`
- **Size:** 61302 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 14

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `testPeer`
- `kv`
- `TestHashing`
- `BenchmarkHashing`
- `newTestPeer`
- `setStorageTries`
- `ID`
- `Log`
- `Stats`
- `RequestAccountRange`
- `RequestTrieNodes`
- `RequestStorageRanges`
- `RequestByteCodes`
- `defaultTrieRequestHandler`
- `defaultAccountRequestHandler`
- `createAccountRequestResponse`
- `defaultStorageRequestHandler`
- `defaultCodeRequestHandler`
- `createStorageRequestResponse`
- `createStorageRequestResponseAlwaysProve`
- `emptyRequestAccountRangeFn`
- `nonResponsiveRequestAccountRangeFn`
- `emptyTrieRequestHandler`
- `nonResponsiveTrieRequestHandler`
- `emptyStorageRequestHandler`
- `nonResponsiveStorageRequestHandler`
- `proofHappyStorageRequestHandler`
- `corruptCodeRequestHandler`
- `cappedCodeRequestHandler`
- `starvingStorageRequestHandler`
- `starvingAccountRequestHandler`
- `corruptAccountRequestHandler`
- `corruptStorageRequestHandler`
- `noProofStorageRequestHandler`
- `TestSyncBloatedProof`
- `testSyncBloatedProof`
- `setupSyncer`
- `TestSync`
- `testSync`
- `TestSyncTinyTriePanic`
- `testSyncTinyTriePanic`
- `TestMultiSync`
- `testMultiSync`
- `TestSyncWithStorage`
- `testSyncWithStorage`
- `TestMultiSyncManyUseless`
- `testMultiSyncManyUseless`
- `TestMultiSyncManyUselessWithLowTimeout`
- `testMultiSyncManyUselessWithLowTimeout`
- `TestMultiSyncManyUnresponsive`
- `testMultiSyncManyUnresponsive`
- `checkStall`
- `TestSyncBoundaryAccountTrie`
- `testSyncBoundaryAccountTrie`
- `TestSyncNoStorageAndOneCappedPeer`
- `testSyncNoStorageAndOneCappedPeer`
- `TestSyncNoStorageAndOneCodeCorruptPeer`
- `testSyncNoStorageAndOneCodeCorruptPeer`
- `TestSyncNoStorageAndOneAccountCorruptPeer`
- `testSyncNoStorageAndOneAccountCorruptPeer`
- `TestSyncNoStorageAndOneCodeCappedPeer`
- `testSyncNoStorageAndOneCodeCappedPeer`
- `TestSyncBoundaryStorageTrie`
- `testSyncBoundaryStorageTrie`
- `TestSyncWithStorageAndOneCappedPeer`
- `testSyncWithStorageAndOneCappedPeer`
- `TestSyncWithStorageAndCorruptPeer`
- `testSyncWithStorageAndCorruptPeer`
- `TestSyncWithStorageAndNonProvingPeer`
- `testSyncWithStorageAndNonProvingPeer`
- `TestSyncWithStorageMisbehavingProve`
- `testSyncWithStorageMisbehavingProve`
- `TestSyncWithUnevenStorage`
- `testSyncWithUnevenStorage`
- `cmp`
- `key32`
- `getCodeHash`
- `getCodeByHash`
- `makeAccountTrieNoStorage`
- `makeBoundaryAccountTrie`
- `makeAccountTrieWithStorageWithUniqueStorage`
- `makeAccountTrieWithStorage`
- `makeStorageTrieWithSeed`
- `makeBoundaryStorageTrie`
- `makeUnevenStorageTrie`
- `verifyTrie`
- `TestSyncAccountPerformance`
- `testSyncAccountPerformance`
- `TestSlotEstimation`
- `newDbConfig`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[crypto/keccak.go.md|crypto/keccak.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[internal/testrand/rand.go.md|internal/testrand/rand.go]]
- [[log/format.go.md|log/format.go]]
- [[node/api.go.md|node/api.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[trie/trie.go.md|trie/trie.go]]
- [[triedb/database.go.md|triedb/database.go]]
- [[triedb/pathdb/buffer.go.md|triedb/pathdb/buffer.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2021 The go-ethereum Authors
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

package snap

import (
	"bytes"
...
```