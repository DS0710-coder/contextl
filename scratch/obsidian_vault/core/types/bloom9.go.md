# bloom9.go

## Architecture Metrics
- **Path:** `core/types/bloom9.go`
- **Extension:** `.go`
- **Size:** 4884 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `bytesBacked`
- `BytesToBloom`
- `SetBytes`
- `Add`
- `AddWithBuffer`
- `Big`
- `Bytes`
- `Test`
- `MarshalText`
- `UnmarshalText`
- `CreateBloom`
- `MergeBloom`
- `Bloom9`
- `bloomValues`
- `BloomLookup`

## Imports (Dependencies)
- [[common/bitutil/bitutil.go.md|common/bitutil/bitutil.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]

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

package types

import (
	"encoding/binary"
...
```