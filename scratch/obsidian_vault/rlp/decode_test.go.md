# decode_test.go

## Architecture Metrics
- **Path:** `rlp/decode_test.go`
- **Extension:** `.go`
- **Size:** 37013 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `decodeTest`
- `simplestruct`
- `recstruct`
- `bigIntStruct`
- `invalidNilTag`
- `invalidTail1`
- `invalidTail2`
- `tailRaw`
- `tailUint`
- `tailPrivateFields`
- `nilListUint`
- `nilStringSlice`
- `intField`
- `optionalFields`
- `optionalAndTailField`
- `optionalBigIntField`
- `optionalPtrField`
- `nonOptionalPtrField`
- `multipleOptionalFields`
- `optionalPtrFieldNil`
- `ignoredField`
- `testDecoder`
- `invalid1`
- `invalid2`
- `invalid3`
- `example`
- `TestStreamKind`
- `TestNewListStream`
- `TestStreamErrors`
- `TestStreamList`
- `TestStreamRaw`
- `TestStreamReadBytes`
- `TestDecodeErrors`
- `uintp`
- `runTests`
- `TestDecodeWithByteReader`
- `testDecodeWithEncReader`
- `TestDecodeWithEncReader`
- `newPlainReader`
- `Read`
- `TestDecodeWithNonByteReader`
- `TestDecodeStreamReset`
- `DecodeRLP`
- `TestDecodeDecoder`
- `TestDecodeDecoderNilPointer`
- `DecodeRLP`
- `called`
- `TestDecoderInByteSlice`
- `DecodeRLP`
- `TestDecoderFunc`
- `TestInvalidOptionalField`
- `ExampleDecode`
- `ExampleDecode_structTagNil`
- `ExampleStream`
- `BenchmarkDecodeUints`
- `BenchmarkDecodeUintsReused`
- `BenchmarkDecodeByteArrayStruct`
- `BenchmarkDecodeBigInts`
- `BenchmarkDecodeU256Ints`
- `encodeTestSlice`
- `unhex`

## Imports (Dependencies)
- [[common/math/big.go.md|common/math/big.go]]

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

package rlp

import (
	"bytes"
...
```