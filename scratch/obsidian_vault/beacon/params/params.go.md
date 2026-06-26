# params.go

## Architecture Metrics
- **Path:** `beacon/params/params.go`
- **Extension:** `.go`
- **Size:** 2335 bytes
- **Centrality Score:** 0.0007
- **In-Degree (Imported By):** 14
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `StateIndexFinalBlock`
- `StateIndexSyncCommittee`
- `StateIndexNextSyncCommittee`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[beacon/blsync/block_sync.go.md|beacon/blsync/block_sync.go]]
- [[beacon/blsync/client.go.md|beacon/blsync/client.go]]
- [[beacon/blsync/engineclient.go.md|beacon/blsync/engineclient.go]]
- [[beacon/light/api/light_api.go.md|beacon/light/api/light_api.go]]
- [[beacon/light/committee_chain.go.md|beacon/light/committee_chain.go]]
- [[beacon/light/committee_chain_test.go.md|beacon/light/committee_chain_test.go]]
- [[beacon/light/head_tracker.go.md|beacon/light/head_tracker.go]]
- [[beacon/light/sync/update_sync.go.md|beacon/light/sync/update_sync.go]]
- [[beacon/light/test_helpers.go.md|beacon/light/test_helpers.go]]
- [[beacon/types/committee.go.md|beacon/types/committee.go]]
- [[beacon/types/header.go.md|beacon/types/header.go]]
- [[beacon/types/light_sync.go.md|beacon/types/light_sync.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[eth/syncer/syncer.go.md|eth/syncer/syncer.go]]

## Source Code Snippet
```go
// Copyright 2022 The go-ethereum Authors
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

package params

const (
	EpochLength      = 32
...
```