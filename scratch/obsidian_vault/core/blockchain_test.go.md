# blockchain_test.go

## Architecture Metrics
- **Path:** `core/blockchain_test.go`
- **Extension:** `.go`
- **Size:** 172199 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 17

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `expectation`
- `newCanonical`
- `newGwei`
- `testFork`
- `testBlockChainImport`
- `testHeaderChainImport`
- `TestLastBlock`
- `testLastBlock`
- `testInsertAfterMerge`
- `TestExtendCanonicalHeaders`
- `TestExtendCanonicalBlocks`
- `testExtendCanonical`
- `TestExtendCanonicalHeadersAfterMerge`
- `TestExtendCanonicalBlocksAfterMerge`
- `testExtendCanonicalAfterMerge`
- `TestShorterForkHeaders`
- `TestShorterForkBlocks`
- `testShorterFork`
- `TestShorterForkHeadersAfterMerge`
- `TestShorterForkBlocksAfterMerge`
- `testShorterForkAfterMerge`
- `TestLongerForkHeaders`
- `TestLongerForkBlocks`
- `testLongerFork`
- `TestLongerForkHeadersAfterMerge`
- `TestLongerForkBlocksAfterMerge`
- `testLongerForkAfterMerge`
- `TestEqualForkHeaders`
- `TestEqualForkBlocks`
- `testEqualFork`
- `TestEqualForkHeadersAfterMerge`
- `TestEqualForkBlocksAfterMerge`
- `testEqualForkAfterMerge`
- `TestBrokenHeaderChain`
- `TestBrokenBlockChain`
- `testBrokenChain`
- `TestReorgLongHeaders`
- `TestReorgLongBlocks`
- `testReorgLong`
- `TestReorgShortHeaders`
- `TestReorgShortBlocks`
- `testReorgShort`
- `testReorg`
- `TestHeadersInsertNonceError`
- `TestBlocksInsertNonceError`
- `testInsertNonceError`
- `TestFastVsFullChains`
- `testFastVsFullChains`
- `TestLightVsFastVsFullChainHeads`
- `testLightVsFastVsFullChainHeads`
- `TestChainTxReorgs`
- `testChainTxReorgs`
- `TestLogReorgs`
- `testLogReorgs`
- `TestLogRebirth`
- `testLogRebirth`
- `TestSideLogRebirth`
- `testSideLogRebirth`
- `checkLogEvents`
- `TestCanonicalBlockRetrieval`
- `testCanonicalBlockRetrieval`
- `TestEIP155Transition`
- `testEIP155Transition`
- `TestEIP161AccountRemoval`
- `testEIP161AccountRemoval`
- `TestBlockchainHeaderchainReorgConsistency`
- `testBlockchainHeaderchainReorgConsistency`
- `TestTrieForkGC`
- `TestLargeReorgTrieGC`
- `testLargeReorgTrieGC`
- `TestBlockchainRecovery`
- `testBlockchainRecovery`
- `TestLowDiffLongChain`
- `testLowDiffLongChain`
- `testSideImport`
- `TestPrunedImportSide`
- `TestPrunedImportSideWithMerging`
- `TestInsertKnownHeaders`
- `TestInsertKnownReceiptChain`
- `TestInsertKnownBlocks`
- `testInsertKnownChainData`
- `TestInsertKnownHeadersWithMerging`
- `TestInsertKnownReceiptChainWithMerging`
- `TestInsertKnownBlocksWithMerging`
- `TestInsertKnownHeadersAfterMerging`
- `TestInsertKnownReceiptChainAfterMerging`
- `TestInsertKnownBlocksAfterMerging`
- `testInsertKnownChainDataWithMerging`
- `getLongAndShortChains`
- `TestReorgToShorterRemovesCanonMapping`
- `testReorgToShorterRemovesCanonMapping`
- `TestReorgToShorterRemovesCanonMappingHeaderChain`
- `testReorgToShorterRemovesCanonMappingHeaderChain`
- `benchmarkLargeNumberOfValueToNonexisting`
- `BenchmarkBlockChain_1x1000ValueTransferToNonexisting`
- `BenchmarkBlockChain_1x1000ValueTransferToExisting`
- `BenchmarkBlockChain_1x1000Executions`
- `TestSideImportPrunedBlocks`
- `testSideImportPrunedBlocks`
- `TestDeleteCreateRevert`
- `testDeleteCreateRevert`
- `TestDeleteRecreateSlots`
- `testDeleteRecreateSlots`
- `TestDeleteRecreateAccount`
- `testDeleteRecreateAccount`
- `TestDeleteRecreateSlotsAcrossManyBlocks`
- `testDeleteRecreateSlotsAcrossManyBlocks`
- `TestInitThenFailCreateContract`
- `testInitThenFailCreateContract`
- `TestEIP2718Transition`
- `testEIP2718Transition`
- `TestEIP1559Transition`
- `testEIP1559Transition`
- `TestSetCanonical`
- `testSetCanonical`
- `TestCanonicalHashMarker`
- `testCanonicalHashMarker`
- `TestCreateThenDeletePreByzantium`
- `TestCreateThenDeletePostByzantium`
- `testCreateThenDelete`
- `TestDeleteThenCreate`
- `TestTransientStorageReset`
- `TestEIP3651`
- `TestPragueRequests`
- `TestEIP7702`
- `TestChainReorgSnapSync`
- `testChainReorgSnapSync`
- `TestInsertChainWithCutoff`
- `testInsertChainWithCutoff`
- `TestGetCanonicalReceipt`
- `TestSetHeadBeyondRootFinalizedBug`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[consensus/beacon/consensus.go.md|consensus/beacon/consensus.go]]
- [[consensus/consensus.go.md|consensus/consensus.go]]
- [[consensus/ethash/ethash.go.md|consensus/ethash/ethash.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/state/access_events.go.md|core/state/access_events.go]]
- [[core/types.go.md|core/types.go]]
- [[core/vm/analysis_legacy.go.md|core/vm/analysis_legacy.go]]
- [[core/vm/program/program.go.md|core/vm/program/program.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[eth/tracers/logger/logger.go.md|eth/tracers/logger/logger.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[ethdb/pebble/pebble.go.md|ethdb/pebble/pebble.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[trie/trie.go.md|trie/trie.go]]

## Imported By (Dependents)
*Not imported by any file*

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

package core

import (
	"bytes"
...
```