# message.go

## Architecture Metrics
- **Path:** `p2p/message.go`
- **Extension:** `.go`
- **Size:** 9019 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Msg`
- `MsgReader`
- `MsgWriter`
- `MsgReadWriter`
- `eofSignal`
- `MsgPipeRW`
- `msgEventer`
- `Decode`
- `String`
- `Discard`
- `Time`
- `Send`
- `SendItems`
- `Read`
- `MsgPipe`
- `WriteMsg`
- `ReadMsg`
- `Close`
- `ExpectMsg`
- `newMsgEventer`
- `ReadMsg`
- `WriteMsg`
- `Close`

## Imports (Dependencies)
- [[event/event.go.md|event/event.go]]
- [[node/api.go.md|node/api.go]]
- [[rlp/decode.go.md|rlp/decode.go]]

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

package p2p

import (
	"bytes"
...
```