# syncv2_test.go

## Architecture Metrics
- **Path:** `eth/protocols/snap/syncv2_test.go`
- **Extension:** `.go`
- **Size:** 110866 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 12

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `testPeerV2`
- `pivotMove`
- `balBlock`
- `newTestPeerV2`
- `setStorageTries`
- `ID`
- `Log`
- `Stats`
- `RequestAccountRange`
- `RequestStorageRanges`
- `RequestByteCodes`
- `RequestTrieNodes`
- `RequestAccessLists`
- `createAccountRequestResponseV2`
- `createStorageRequestResponseV2`
- `createStorageRequestResponseAlwaysProveV2`
- `defaultAccountRequestHandlerV2`
- `defaultStorageRequestHandlerV2`
- `defaultCodeRequestHandlerV2`
- `defaultAccessListRequestHandler`
- `emptyRequestAccountRangeFnV2`
- `nonResponsiveRequestAccountRangeFnV2`
- `emptyStorageRequestHandlerV2`
- `nonResponsiveStorageRequestHandlerV2`
- `proofHappyStorageRequestHandlerV2`
- `corruptCodeRequestHandlerV2`
- `cappedCodeRequestHandlerV2`
- `starvingStorageRequestHandlerV2`
- `starvingAccountRequestHandlerV2`
- `corruptAccountRequestHandlerV2`
- `corruptStorageRequestHandlerV2`
- `noProofStorageRequestHandlerV2`
- `TestSyncBloatedProofV2`
- `testSyncBloatedProofV2`
- `setupSyncerV2`
- `mkPivot`
- `makeAccessListHeaders`
- `TestSyncV2`
- `testSyncV2`
- `TestSyncV2FrozenPivot`
- `testSyncV2FrozenPivot`
- `verifyAdoptedSyncedState`
- `TestSyncTinyTriePanicV2`
- `testSyncTinyTriePanicV2`
- `TestMultiSyncV2`
- `testMultiSyncV2`
- `TestSyncWithStorageV2`
- `testSyncWithStorageV2`
- `TestMultiSyncManyUselessV2`
- `testMultiSyncManyUselessV2`
- `TestMultiSyncManyUselessWithLowTimeoutV2`
- `testMultiSyncManyUselessWithLowTimeoutV2`
- `TestMultiSyncManyUnresponsiveV2`
- `testMultiSyncManyUnresponsiveV2`
- `TestSyncBoundaryAccountTrieV2`
- `testSyncBoundaryAccountTrieV2`
- `TestSyncNoStorageAndOneCappedPeerV2`
- `testSyncNoStorageAndOneCappedPeerV2`
- `TestSyncNoStorageAndOneCodeCorruptPeerV2`
- `testSyncNoStorageAndOneCodeCorruptPeerV2`
- `TestSyncNoStorageAndOneAccountCorruptPeerV2`
- `testSyncNoStorageAndOneAccountCorruptPeerV2`
- `TestSyncNoStorageAndOneCodeCappedPeerV2`
- `testSyncNoStorageAndOneCodeCappedPeerV2`
- `TestSyncBoundaryStorageTrieV2`
- `testSyncBoundaryStorageTrieV2`
- `TestSyncWithStorageAndOneCappedPeerV2`
- `testSyncWithStorageAndOneCappedPeerV2`
- `TestSyncWithStorageAndCorruptPeerV2`
- `testSyncWithStorageAndCorruptPeerV2`
- `TestSyncWithStorageAndNonProvingPeerV2`
- `testSyncWithStorageAndNonProvingPeerV2`
- `TestSyncWithStorageMisbehavingProveV2`
- `testSyncWithStorageMisbehavingProveV2`
- `TestSyncWithUnevenStorageV2`
- `testSyncWithUnevenStorageV2`
- `makeAccountTrieWithAddresses`
- `TestIsPivotReorged`
- `TestSyncDetectsPivotReorged`
- `TestInterruptedDownloadRecovery`
- `testInterruptedDownloadRecovery`
- `TestSyncPersistsPivotDuringDownload`
- `TestPivotMovement`
- `TestPivotMovementRepeated`
- `testPivotMovement`
- `TestCatchUpPersistsIncrementally`
- `testCatchUpPersistsIncrementally`
- `TestCatchUpWindowed`
- `testCatchUpWindowed`
- `TestSyncStatusMarkedCompleteAfterCompletion`
- `testSyncStatusMarkedCompleteAfterCompletion`
- `TestSyncSkipsIfAlreadyComplete`
- `TestInterruptedGenerationRecovery`
- `TestPruneStaleState`
- `TestResumeWipesUncoveredState`
- `testResumeWipesUncoveredState`
- `TestFetchAccessListsMultiplePeers`
- `TestFetchAccessListsPeerTimeout`
- `TestFetchAccessListsPeerRejection`
- `TestFetchAccessListsCancel`
- `TestFetchAccessListsPeerDrop`
- `TestFetchAccessListsShortResponse`
- `TestFetchAccessListsEmptyPlaceholder`
- `TestFetchAccessListsRejectsBadBAL`
- `TestCatchUpRetriesOnBadBAL`
- `makeStorageTrieFromSlots`
- `makeStateWithStorageContract`
- `TestCatchUpAppliesStorageBALs`
- `testCatchUpAppliesStorageBALs`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/types.go.md|core/types.go]]
- [[core/types/bal/bal.go.md|core/types/bal/bal.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[log/format.go.md|log/format.go]]
- [[node/api.go.md|node/api.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[trie/trie.go.md|trie/trie.go]]
- [[triedb/database.go.md|triedb/database.go]]

## Imported By (Dependents)
*Not imported by any file*

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

package snap

import (
	"bytes"
...
```