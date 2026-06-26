# modinv64.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modinv64.h`
- **Extension:** `.h`
- **Size:** 1969 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/modinv64_impl.h.md|crypto/secp256k1/libsecp256k1/src/modinv64_impl.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2020 Peter Dettman                                    *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 **********************************************************************/

#ifndef SECP256K1_MODINV64_H
#define SECP256K1_MODINV64_H

#include "util.h"

#ifndef SECP256K1_WIDEMUL_INT128
#error "modinv64 requires 128-bit wide multiplication support"
#endif

/* A signed 62-bit limb representation of integers.
 *
 * Its value is sum(v[i] * 2^(62*i), i=0..4). */
typedef struct {
    int64_t v[5];
...
```