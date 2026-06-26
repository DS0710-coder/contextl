# signed_data_internal_test.go

## Architecture Metrics
- **Path:** `signer/core/apitypes/signed_data_internal_test.go`
- **Extension:** `.go`
- **Size:** 8608 bytes
- **Centrality Score:** 0.0006
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `testDataInput`
- `TestBytesPadding`
- `TestParseAddress`
- `TestParseBytes`
- `TestParseInteger`
- `TestConvertStringDataToSlice`
- `TestConvertUint256DataToSlice`
- `TestConvertAddressDataToSlice`
- `TestTypedDataArrayValidate`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
- [[common/hexutil/hexutil.go.md|common/hexutil/hexutil.go]]
- [[common/math/big.go.md|common/math/big.go]]
- [[crypto/crypto.go.md|crypto/crypto.go]]

## Imported By (Dependents)
- [[accounts/external/backend.go.md|accounts/external/backend.go]]
- [[cmd/abidump/main.go.md|cmd/abidump/main.go]]
- [[signer/fourbyte/validation.go.md|signer/fourbyte/validation.go]]
- [[signer/fourbyte/validation_test.go.md|signer/fourbyte/validation_test.go]]

## Source Code Snippet
```go
// Copyright 2019 The go-ethereum Authors
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