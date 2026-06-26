# curve.go

## Architecture Metrics
- **Path:** `crypto/secp256k1/curve.go`
- **Extension:** `.go`
- **Size:** 9403 bytes
- **Centrality Score:** 0.0005
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BitCurve`
- `Params`
- `IsOnCurve`
- `affineFromJacobian`
- `Add`
- `addJacobian`
- `Double`
- `doubleJacobian`
- `ScalarBaseMult`
- `Marshal`
- `Unmarshal`
- `init`
- `S256`

## Imports (Dependencies)
- [[common/math/big.go.md|common/math/big.go]]

## Imported By (Dependents)
- [[crypto/signature_cgo.go.md|crypto/signature_cgo.go]]
- [[tests/fuzzers/secp256k1/secp_test.go.md|tests/fuzzers/secp256k1/secp_test.go]]

## Source Code Snippet
```go
// Copyright 2010 The Go Authors. All rights reserved.
// Copyright 2011 ThePiachu. All rights reserved.
// Copyright 2015 Jeffrey Wilcke, Felix Lange, Gustav Simonsson. All rights reserved.
//
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are
// met:
//
// * Redistributions of source code must retain the above copyright
//   notice, this list of conditions and the following disclaimer.
// * Redistributions in binary form must reproduce the above
//   copyright notice, this list of conditions and the following disclaimer
//   in the documentation and/or other materials provided with the
//   distribution.
// * Neither the name of Google Inc. nor the names of its
//   contributors may be used to endorse or promote products derived from
//   this software without specific prior written permission.
// * The name of ThePiachu may not be used to endorse or promote products
//   derived from this software without specific prior written permission.
//
...
```