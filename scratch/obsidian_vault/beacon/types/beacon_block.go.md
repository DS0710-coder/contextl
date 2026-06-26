# beacon_block.go

## Architecture Metrics
- **Path:** `beacon/types/beacon_block.go`
- **Extension:** `.go`
- **Size:** 4886 bytes
- **Centrality Score:** 0.0103
- **In-Degree (Imported By):** 22
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `blockObject`
- `BeaconBlock`
- `BlockFromJSON`
- `NewBeaconBlock`
- `Slot`
- `ExecutionPayload`
- `Header`
- `Root`
- `ExecutionRequestsList`
- `marshalRequests`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[core/types.go.md|core/types.go]]

## Imported By (Dependents)
- [[beacon/blsync/block_sync.go.md|beacon/blsync/block_sync.go]]
- [[beacon/blsync/block_sync_test.go.md|beacon/blsync/block_sync_test.go]]
- [[beacon/blsync/client.go.md|beacon/blsync/client.go]]
- [[beacon/blsync/engineclient.go.md|beacon/blsync/engineclient.go]]
- [[beacon/light/api/api_server.go.md|beacon/light/api/api_server.go]]
- [[beacon/light/api/light_api.go.md|beacon/light/api/light_api.go]]
- [[beacon/light/committee_chain.go.md|beacon/light/committee_chain.go]]
- [[beacon/light/committee_chain_test.go.md|beacon/light/committee_chain_test.go]]
- [[beacon/light/head_tracker.go.md|beacon/light/head_tracker.go]]
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[beacon/light/sync/head_sync_test.go.md|beacon/light/sync/head_sync_test.go]]
- [[beacon/light/sync/test_helpers.go.md|beacon/light/sync/test_helpers.go]]
- [[beacon/light/sync/types.go.md|beacon/light/sync/types.go]]
- [[beacon/light/sync/update_sync.go.md|beacon/light/sync/update_sync.go]]
- [[beacon/light/sync/update_sync_test.go.md|beacon/light/sync/update_sync_test.go]]
- [[beacon/light/test_helpers.go.md|beacon/light/test_helpers.go]]
- [[cmd/devp2p/dns_route53.go.md|cmd/devp2p/dns_route53.go]]
- [[cmd/devp2p/dns_route53_test.go.md|cmd/devp2p/dns_route53_test.go]]
- [[rlp/rlpgen/gen.go.md|rlp/rlpgen/gen.go]]
- [[rlp/rlpgen/gen_test.go.md|rlp/rlpgen/gen_test.go]]
- [[rlp/rlpgen/main.go.md|rlp/rlpgen/main.go]]
- [[rlp/rlpgen/types.go.md|rlp/rlpgen/types.go]]

## Source Code Snippet
```go
// Copyright 2024 The go-ethereum Authors
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

package types

import (
	"bytes"
...
```