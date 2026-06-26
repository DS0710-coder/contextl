# group.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/group.h`
- **Extension:** `.h`
- **Size:** 11491 bytes
- **Centrality Score:** 0.0021
- **In-Degree (Imported By):** 21
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/field.h.md|crypto/secp256k1/libsecp256k1/src/field.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/ecdsa.h.md|crypto/secp256k1/libsecp256k1/src/ecdsa.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecdsa_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecdsa_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/eckey.h.md|crypto/secp256k1/libsecp256k1/src/eckey.h]]
- [[crypto/secp256k1/libsecp256k1/src/eckey_impl.h.md|crypto/secp256k1/libsecp256k1/src/eckey_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult.h.md|crypto/secp256k1/libsecp256k1/src/ecmult.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_const.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_const.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_const_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_const_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_gen.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_gen.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_gen_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_gen_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/group_impl.h.md|crypto/secp256k1/libsecp256k1/src/group_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/tests_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/tests_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/precompute_ecmult_gen.c.md|crypto/secp256k1/libsecp256k1/src/precompute_ecmult_gen.c]]
- [[crypto/secp256k1/libsecp256k1/src/precomputed_ecmult.c.md|crypto/secp256k1/libsecp256k1/src/precomputed_ecmult.c]]
- [[crypto/secp256k1/libsecp256k1/src/precomputed_ecmult.h.md|crypto/secp256k1/libsecp256k1/src/precomputed_ecmult.h]]
- [[crypto/secp256k1/libsecp256k1/src/precomputed_ecmult_gen.c.md|crypto/secp256k1/libsecp256k1/src/precomputed_ecmult_gen.c]]
- [[crypto/secp256k1/libsecp256k1/src/precomputed_ecmult_gen.h.md|crypto/secp256k1/libsecp256k1/src/precomputed_ecmult_gen.h]]
- [[crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c.md|crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c]]
- [[crypto/secp256k1/libsecp256k1/src/testutil.h.md|crypto/secp256k1/libsecp256k1/src/testutil.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2013, 2014 Pieter Wuille                              *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_GROUP_H
#define SECP256K1_GROUP_H

#include "field.h"

/** A group element in affine coordinates on the secp256k1 curve,
 *  or occasionally on an isomorphic curve of the form y^2 = x^3 + 7*t^6.
 *  Note: For exhaustive test mode, secp256k1 is replaced by a small subgroup of a different curve.
 */
typedef struct {
    secp256k1_fe x;
    secp256k1_fe y;
    int infinity; /* whether this represents the point at infinity */
} secp256k1_ge;
...
```