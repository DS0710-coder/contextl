# prque.go

## Architecture Metrics
- **Path:** `common/prque/prque.go`
- **Extension:** `.go`
- **Size:** 2426 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 6
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `Prque`
- `New`
- `Push`
- `Peek`
- `Pop`
- `PopItem`
- `Remove`
- `Empty`
- `Size`
- `Reset`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[core/blockchain.go.md|core/blockchain.go]]
- [[core/rawdb/chain_iterator.go.md|core/rawdb/chain_iterator.go]]
- [[core/txpool/legacypool/legacypool.go.md|core/txpool/legacypool/legacypool.go]]
- [[eth/downloader/fetchers_concurrent.go.md|eth/downloader/fetchers_concurrent.go]]
- [[eth/downloader/queue.go.md|eth/downloader/queue.go]]
- [[trie/sync.go.md|trie/sync.go]]

## Source Code Snippet
```go
// CookieJar - A contestant's algorithm toolbox
// Copyright (c) 2013 Peter Szilagyi. All rights reserved.
//
// CookieJar is dual licensed: use of this source code is governed by a BSD
// license that can be found in the LICENSE file. Alternatively, the CookieJar
// toolbox may be used in accordance with the terms and conditions contained
// in a signed written agreement between you and the author(s).

// This is a duplicated and slightly modified version of "gopkg.in/karalabe/cookiejar.v2/collections/prque".

// Package prque implements a priority queue data structure supporting arbitrary
// value types and int64 priorities.
//
// If you would like to use a min-priority queue, simply negate the priorities.
//
// Internally the queue is based on the standard heap package working on a
// sortable version of the block based stack.
package prque

import (
...
```