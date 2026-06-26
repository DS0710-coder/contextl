# types.go

## Architecture Metrics
- **Path:** `signer/core/apitypes/types.go`
- **Extension:** `.go`
- **Size:** 30016 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ValidationInfo`
- `ValidationMessages`
- `SendTxArgs`
- `SigFormat`
- `ValidatorData`
- `TypedData`
- `Type`
- `TypePriority`
- `TypedDataDomain`
- `NameValueType`
- `Crit`
- `Warn`
- `Info`
- `GetWarnings`
- `String`
- `data`
- `ToTransaction`
- `validateTxSidecar`
- `isArray`
- `typeName`
- `TypedDataAndHash`
- `HashStruct`
- `Dependencies`
- `EncodeType`
- `TypeHash`
- `EncodeData`
- `encodeArrayValue`
- `parseBytes`
- `parseInteger`
- `EncodePrimitiveValue`
- `dataMismatchError`
- `convertDataToSlice`
- `validate`
- `Map`
- `Format`
- `formatData`
- `formatPrimitiveValue`
- `validate`
- `init`
- `isPrimitiveTypeValid`
- `validate`
- `Map`
- `Pprint`

## Imports (Dependencies)
- [[accounts/accounts.go.md|accounts/accounts.go]]
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[core/types.go.md|core/types.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]
- [[crypto/kzg4844/kzg4844.go.md|crypto/kzg4844/kzg4844.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
// Copyright 2018 The go-ethereum Authors
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

package apitypes

import (
	"bytes"
...
```