# schema.go

## Architecture Metrics
- **Path:** `core/rawdb/schema.go`
- **Extension:** `.go`
- **Size:** 19062 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `LegacyTxLookupEntry`
- `encodeBlockNumber`
- `headerKeyPrefix`
- `headerKey`
- `headerHashKey`
- `headerNumberKey`
- `blockBodyKey`
- `blockReceiptsKey`
- `accessListKey`
- `txLookupKey`
- `accountSnapshotKey`
- `storageSnapshotKey`
- `storageSnapshotsKey`
- `skeletonHeaderKey`
- `preimageKey`
- `codeKey`
- `IsCodeKey`
- `configKey`
- `genesisStateSpecKey`
- `stateIDKey`
- `accountTrieNodeKey`
- `storageTrieNodeKey`
- `IsLegacyTrieNode`
- `ResolveAccountTrieNodeKey`
- `IsAccountTrieNode`
- `ResolveStorageTrieNode`
- `IsStorageTrieNode`
- `filterMapRowKey`
- `filterMapLastBlockKey`
- `filterMapBlockLVKey`
- `accountHistoryIndexKey`
- `storageHistoryIndexKey`
- `trienodeHistoryIndexKey`
- `accountHistoryIndexBlockKey`
- `storageHistoryIndexBlockKey`
- `trienodeHistoryIndexBlockKey`
- `transitionStateKey`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2018 The go-ethereum Authors
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

// Package rawdb contains a collection of low level database accessors.
package rawdb

import (
...
```