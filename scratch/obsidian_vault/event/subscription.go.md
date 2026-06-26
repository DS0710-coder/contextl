# subscription.go

## Architecture Metrics
- **Path:** `event/subscription.go`
- **Extension:** `.go`
- **Size:** 8264 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Subscription`
- `funcSub`
- `resubscribeSub`
- `SubscriptionScope`
- `scopeSub`
- `NewSubscription`
- `Unsubscribe`
- `Err`
- `Resubscribe`
- `ResubscribeErr`
- `Unsubscribe`
- `Err`
- `loop`
- `subscribe`
- `waitForError`
- `backoffWait`
- `Track`
- `Close`
- `Count`
- `Unsubscribe`
- `Err`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]
- [[common/mclock/mclock.go.md|common/mclock/mclock.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2016 The go-ethereum Authors
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

package event

import (
	"context"
...
```