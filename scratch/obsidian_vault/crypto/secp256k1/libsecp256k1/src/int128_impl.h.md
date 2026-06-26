# int128_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/int128_impl.h`
- **Extension:** `.h`
- **Size:** 376 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/int128.h.md|crypto/secp256k1/libsecp256k1/src/int128.h]]
- [[crypto/secp256k1/libsecp256k1/src/int128_native_impl.h.md|crypto/secp256k1/libsecp256k1/src/int128_native_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/int128_struct_impl.h.md|crypto/secp256k1/libsecp256k1/src/int128_struct_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/precompute_ecmult.c.md|crypto/secp256k1/libsecp256k1/src/precompute_ecmult.c]]
- [[crypto/secp256k1/libsecp256k1/src/precompute_ecmult_gen.c.md|crypto/secp256k1/libsecp256k1/src/precompute_ecmult_gen.c]]
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]
- [[crypto/secp256k1/libsecp256k1/src/tests.c.md|crypto/secp256k1/libsecp256k1/src/tests.c]]

## Source Code Snippet
```h
#ifndef SECP256K1_INT128_IMPL_H
#define SECP256K1_INT128_IMPL_H

#include "util.h"

#include "int128.h"

#if defined(SECP256K1_WIDEMUL_INT128)
#  if defined(SECP256K1_INT128_NATIVE)
#    include "int128_native_impl.h"
#  elif defined(SECP256K1_INT128_STRUCT)
#    include "int128_struct_impl.h"
#  else
#    error "Please select int128 implementation"
#  endif
#endif

#endif
```