# ecies_test.go

## Architecture Metrics
- **Path:** `crypto/ecies/ecies_test.go`
- **Extension:** `.go`
- **Size:** 11930 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `testCase`
- `TestKDF`
- `cmpParams`
- `TestSharedKey`
- `TestSharedKeyPadding`
- `TestTooBigSharedKey`
- `BenchmarkGenerateKeyP256`
- `BenchmarkGenSharedKeyP256`
- `BenchmarkGenSharedKeyS256`
- `TestEncryptDecrypt`
- `TestDecryptShared2`
- `TestParamSelection`
- `testParamSelection`
- `TestBasicKeyValidation`
- `TestBox`
- `TestSharedKeyStatic`
- `hexKey`
- `decode`

## Imports (Dependencies)
- [[crypto/crypto.go.md|crypto/crypto.go]]

## Imported By (Dependents)
*Not imported by any file*

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