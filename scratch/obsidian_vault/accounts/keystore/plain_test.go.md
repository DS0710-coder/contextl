# plain_test.go

## Architecture Metrics
- **Path:** `accounts/keystore/plain_test.go`
- **Extension:** `.go`
- **Size:** 7666 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `KeyStoreTestV3`
- `KeyStoreTestV1`
- `tmpKeyStoreIface`
- `TestKeyStorePlain`
- `TestKeyStorePassphrase`
- `TestKeyStorePassphraseDecryptionFail`
- `TestImportPreSaleKey`
- `TestV3_PBKDF2_1`
- `skipIfSubmoduleMissing`
- `TestV3_PBKDF2_2`
- `TestV3_PBKDF2_3`
- `TestV3_PBKDF2_4`
- `TestV3_Scrypt_1`
- `TestV3_Scrypt_2`
- `TestV1_1`
- `TestV1_2`
- `testDecryptV3`
- `testDecryptV1`
- `loadKeyStoreTestV3`
- `loadKeyStoreTestV1`
- `TestKeyForDirectICAP`
- `TestV3_31_Byte_Key`
- `TestV3_30_Byte_Key`

## Imports (Dependencies)
- [[common/big.go.md|common/big.go]]
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

package keystore

import (
	"crypto/rand"
...
```