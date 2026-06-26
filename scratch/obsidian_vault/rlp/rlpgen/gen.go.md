# gen.go

## Architecture Metrics
- **Path:** `rlp/rlpgen/gen.go`
- **Extension:** `.go`
- **Size:** 23870 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `buildContext`
- `genContext`
- `genImportPackage`
- `op`
- `basicOp`
- `byteArrayOp`
- `bigIntOp`
- `uint256Op`
- `encoderDecoderOp`
- `ptrOp`
- `structOp`
- `structField`
- `sliceOp`
- `newBuildContext`
- `isEncoder`
- `isDecoder`
- `typeToStructType`
- `newGenContext`
- `temp`
- `resetTemp`
- `addImportPath`
- `addImport`
- `hasAlias`
- `loadPackage`
- `qualify`
- `importsList`
- `makeBasicOp`
- `makeByteSliceOp`
- `makeRawValueOp`
- `writeNeedsConversion`
- `decodeNeedsConversion`
- `genWrite`
- `genDecode`
- `makeByteArrayOp`
- `genWrite`
- `genDecode`
- `genWrite`
- `genDecode`
- `genWrite`
- `genDecode`
- `genWrite`
- `genDecode`
- `makePtrOp`
- `genWrite`
- `genDecode`
- `makeStructOp`
- `checkUnsupportedTags`
- `genWrite`
- `writeOptionalFields`
- `genDecode`
- `decodeOptionalFields`
- `makeSliceOp`
- `genWrite`
- `genDecode`
- `makeOp`
- `generateDecoder`
- `generateEncoder`
- `generate`

## Imports (Dependencies)
- [[beacon/types/beacon_block.go.md|beacon/types/beacon_block.go]]
- [[rlp/internal/rlpstruct/rlpstruct.go.md|rlp/internal/rlpstruct/rlpstruct.go]]

## Imported By (Dependents)
*Not imported by any file*

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

package main

import (
	"bytes"
...
```