# ecmult_const_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/ecmult_const_impl.h`
- **Extension:** `.h`
- **Size:** 19496 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_ecmult_const_odd_multiples_table_globalz`
- `secp256k1_ecmult_const`
- `secp256k1_ecmult_const_xonly`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/ecmult_const.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_const.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/group.h.md|crypto/secp256k1/libsecp256k1/src/group.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar.h.md|crypto/secp256k1/libsecp256k1/src/scalar.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/modules/ecdh/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/ecdh/main_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2015, 2022 Pieter Wuille, Andrew Poelstra             *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_ECMULT_CONST_IMPL_H
#define SECP256K1_ECMULT_CONST_IMPL_H

#include "scalar.h"
#include "group.h"
#include "ecmult_const.h"
#include "ecmult_impl.h"

#if defined(EXHAUSTIVE_TEST_ORDER)
/* We need 2^ECMULT_CONST_GROUP_SIZE - 1 to be less than EXHAUSTIVE_TEST_ORDER, because
 * the tables cannot have infinities in them (this breaks the effective-affine technique's
 * z-ratio tracking) */
#  if EXHAUSTIVE_TEST_ORDER == 199
#    define ECMULT_CONST_GROUP_SIZE 4
...
```