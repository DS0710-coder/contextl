# downloader_test.go

## Architecture Metrics
- **Path:** `eth/downloader/downloader_test.go`
- **Extension:** `.go`
- **Size:** 29542 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 14

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `downloadTester`
- `downloadTesterPeer`
- `newTester`
- `newTesterWithNotification`
- `newTesterWithSnap`
- `terminate`
- `newPeer`
- `dropPeer`
- `unmarshalRlpHeaders`
- `RequestHeadersByHash`
- `RequestHeadersByNumber`
- `RequestBodies`
- `RequestReceipts`
- `ID`
- `RequestAccountRange`
- `RequestStorageRanges`
- `RequestByteCodes`
- `RequestTrieNodes`
- `RequestAccessLists`
- `Log`
- `assertOwnChain`
- `TestCanonicalSynchronisationFull`
- `TestCanonicalSynchronisationSnap`
- `TestCanonicalSynchronisationSnapV2`
- `testCanonSync`
- `TestThrottlingFull`
- `TestThrottlingSnap`
- `testThrottling`
- `TestCancelFull`
- `TestCancelSnap`
- `testCancel`
- `TestEmptyShortCircuitFull`
- `TestEmptyShortCircuitSnap`
- `testEmptyShortCircuit`
- `checkProgress`
- `TestBeaconSyncFull`
- `TestBeaconSyncSnap`
- `testBeaconSync`
- `TestBeaconSyncRepairForkFull`
- `TestBeaconSyncRepairForkSnap`
- `testBeaconSyncRepairFork`
- `TestSyncProgressFull`
- `TestSyncProgressSnap`
- `testSyncProgress`
- `TestInvalidBodyPeerDrop`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[consensus/ethash/ethash.go.md|consensus/ethash/ethash.go]]
- [[core/bal_test.go.md|core/bal_test.go]]
- [[core/rawdb/accessors_chain.go.md|core/rawdb/accessors_chain.go]]
- [[core/types.go.md|core/types.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[eth/ethconfig/config.go.md|eth/ethconfig/config.go]]
- [[eth/protocols/snap/bal_apply.go.md|eth/protocols/snap/bal_apply.go]]
- [[ethdb/batch.go.md|ethdb/batch.go]]
- [[log/format.go.md|log/format.go]]
- [[params/bootnodes.go.md|params/bootnodes.go]]
- [[rlp/decode.go.md|rlp/decode.go]]
- [[trie/trie.go.md|trie/trie.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2015 The go-ethereum Authors
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

package downloader

import (
	"math/big"
...
```