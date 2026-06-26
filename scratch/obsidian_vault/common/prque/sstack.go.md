# sstack.go

## Architecture Metrics
- **Path:** `common/prque/sstack.go`
- **Extension:** `.go`
- **Size:** 3394 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `item`
- `sstack`
- `newSstack`
- `Push`
- `Pop`
- `Len`
- `Less`
- `Swap`
- `Reset`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

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

package prque

import "cmp"

// The size of a block of data
const blockSize = 4096

// A prioritized item in the sorted stack.
type item[P cmp.Ordered, V any] struct {
	value    V
...
```