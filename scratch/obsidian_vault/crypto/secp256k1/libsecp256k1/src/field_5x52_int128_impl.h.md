# field_5x52_int128_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/field_5x52_int128_impl.h`
- **Extension:** `.h`
- **Size:** 11341 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_fe_mul_inner`
- `secp256k1_fe_sqr_inner`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/int128.h.md|crypto/secp256k1/libsecp256k1/src/int128.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/field_5x52_impl.h.md|crypto/secp256k1/libsecp256k1/src/field_5x52_impl.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2013, 2014 Pieter Wuille                              *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_FIELD_INNER5X52_IMPL_H
#define SECP256K1_FIELD_INNER5X52_IMPL_H

#include <stdint.h>

#include "int128.h"
#include "util.h"

#define VERIFY_BITS(x, n) VERIFY_CHECK(((x) >> (n)) == 0)
#define VERIFY_BITS_128(x, n) VERIFY_CHECK(secp256k1_u128_check_bits((x), (n)))

SECP256K1_INLINE static void secp256k1_fe_mul_inner(uint64_t *r, const uint64_t *a, const uint64_t * SECP256K1_RESTRICT b) {
    secp256k1_uint128 c, d;
    uint64_t t3, t4, tx, u0;
...
```