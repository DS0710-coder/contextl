# int128_native.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/int128_native.h`
- **Extension:** `.h`
- **Size:** 581 bytes
- **Centrality Score:** 0.0007
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/assumptions.h.md|crypto/secp256k1/libsecp256k1/src/assumptions.h]]
- [[crypto/secp256k1/libsecp256k1/src/int128.h.md|crypto/secp256k1/libsecp256k1/src/int128.h]]

## Source Code Snippet
```h
#ifndef SECP256K1_INT128_NATIVE_H
#define SECP256K1_INT128_NATIVE_H

#include <stdint.h>
#include "util.h"

#if !defined(UINT128_MAX) && defined(__SIZEOF_INT128__)
SECP256K1_GNUC_EXT typedef unsigned __int128 uint128_t;
SECP256K1_GNUC_EXT typedef __int128 int128_t;
# define UINT128_MAX ((uint128_t)(-1))
# define INT128_MAX ((int128_t)(UINT128_MAX >> 1))
# define INT128_MIN (-INT128_MAX - 1)
/* No (U)INT128_C macros because compilers providing __int128 do not support 128-bit literals.  */
#endif

typedef uint128_t secp256k1_uint128;
typedef int128_t secp256k1_int128;

#endif
```