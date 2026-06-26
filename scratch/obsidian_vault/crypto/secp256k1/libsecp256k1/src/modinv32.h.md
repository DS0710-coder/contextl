# modinv32.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modinv32.h`
- **Extension:** `.h`
- **Size:** 1865 bytes
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
- [[crypto/secp256k1/libsecp256k1/src/modinv32_impl.h.md|crypto/secp256k1/libsecp256k1/src/modinv32_impl.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2020 Peter Dettman                                    *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 **********************************************************************/

#ifndef SECP256K1_MODINV32_H
#define SECP256K1_MODINV32_H

#include "util.h"

/* A signed 30-bit limb representation of integers.
 *
 * Its value is sum(v[i] * 2^(30*i), i=0..8). */
typedef struct {
    int32_t v[9];
} secp256k1_modinv32_signed30;

typedef struct {
    /* The modulus in signed30 notation, must be odd and in [3, 2^256]. */
...
```