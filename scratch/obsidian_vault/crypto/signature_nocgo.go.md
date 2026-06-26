# signature_nocgo.go

## Architecture Metrics
- **Path:** `crypto/signature_nocgo.go`
- **Extension:** `.go`
- **Size:** 6619 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `btCurve`
- `Ecrecover`
- `sigToPub`
- `SigToPub`
- `Sign`
- `VerifySignature`
- `DecompressPubkey`
- `CompressPubkey`
- `S256`
- `IsOnCurve`
- `Marshal`
- `Unmarshal`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2017 The go-ethereum Authors
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

//go:build nacl || js || wasip1 || !cgo || gofuzz || tinygo
// +build nacl js wasip1 !cgo gofuzz tinygo

package crypto
...
```