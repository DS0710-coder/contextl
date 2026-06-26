# ecies.go

## Architecture Metrics
- **Path:** `crypto/ecies/ecies.go`
- **Extension:** `.go`
- **Size:** 9515 bytes
- **Centrality Score:** 0.0005
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `PublicKey`
- `PrivateKey`
- `ExportECDSA`
- `ImportECDSAPublic`
- `ExportECDSA`
- `ImportECDSA`
- `GenerateKey`
- `MaxSharedKeyLength`
- `GenerateShared`
- `concatKDF`
- `roundup`
- `deriveKeys`
- `messageTag`
- `generateIV`
- `symEncrypt`
- `symDecrypt`
- `Encrypt`
- `Decrypt`

## Imports (Dependencies)
- [[crypto/crypto.go.md|crypto/crypto.go]]

## Imported By (Dependents)
- [[p2p/rlpx/rlpx.go.md|p2p/rlpx/rlpx.go]]
- [[p2p/rlpx/rlpx_oracle_poc_test.go.md|p2p/rlpx/rlpx_oracle_poc_test.go]]
- [[p2p/rlpx/rlpx_test.go.md|p2p/rlpx/rlpx_test.go]]

## Source Code Snippet
```go
// Copyright (c) 2013 Kyle Isom <kyle@tyrfingr.is>
// Copyright (c) 2012 The Go Authors. All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are
// met:
//
//    * Redistributions of source code must retain the above copyright
// notice, this list of conditions and the following disclaimer.
//    * Redistributions in binary form must reproduce the above
// copyright notice, this list of conditions and the following disclaimer
// in the documentation and/or other materials provided with the
// distribution.
//    * Neither the name of Google Inc. nor the names of its
// contributors may be used to endorse or promote products derived from
// this software without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
// "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
// LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
...
```