# peer.go

## Architecture Metrics
- **Path:** `eth/downloader/peer.go`
- **Extension:** `.go`
- **Size:** 8789 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `peerConnection`
- `Peer`
- `peeringEvent`
- `peerSet`
- `peerCapacitySort`
- `newPeerConnection`
- `Reset`
- `UpdateHeaderRate`
- `UpdateBodyRate`
- `UpdateReceiptRate`
- `HeaderCapacity`
- `BodyCapacity`
- `ReceiptCapacity`
- `MarkLacking`
- `Lacks`
- `newPeerSet`
- `SubscribeEvents`
- `Reset`
- `Register`
- `Unregister`
- `Peer`
- `Len`
- `AllPeers`
- `Len`
- `Less`
- `Swap`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/big.go.md|common/big.go]]
- [[eth/api_admin.go.md|eth/api_admin.go]]
- [[event/event.go.md|event/event.go]]
- [[log/format.go.md|log/format.go]]
- [[p2p/msgrate/msgrate.go.md|p2p/msgrate/msgrate.go]]

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

// Contains the active peer-set of the downloader, maintaining both failures
// as well as reputation metrics to prioritize the block retrievals.

package downloader
...
```