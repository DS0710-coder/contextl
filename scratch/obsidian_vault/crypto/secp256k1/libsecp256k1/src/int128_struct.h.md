# int128_struct.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/int128_struct.h`
- **Extension:** `.h`
- **Size:** 229 bytes
- **Centrality Score:** 0.0005
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/int128.h.md|crypto/secp256k1/libsecp256k1/src/int128.h]]

## Source Code Snippet
```h
#ifndef SECP256K1_INT128_STRUCT_H
#define SECP256K1_INT128_STRUCT_H

#include <stdint.h>
#include "util.h"

typedef struct {
  uint64_t lo;
  uint64_t hi;
} secp256k1_uint128;

typedef secp256k1_uint128 secp256k1_int128;

#endif
```