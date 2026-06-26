# scalar.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/scalar.h`
- **Extension:** `.h`
- **Size:** 5395 bytes
- **Centrality Score:** 0.0017
- **In-Degree (Imported By):** 16
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/scalar_4x64.h.md|crypto/secp256k1/libsecp256k1/src/scalar_4x64.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar_8x32.h.md|crypto/secp256k1/libsecp256k1/src/scalar_8x32.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar_low.h.md|crypto/secp256k1/libsecp256k1/src/scalar_low.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

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
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/session.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/session.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/session_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/session_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/tests_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/tests_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar_impl.h.md|crypto/secp256k1/libsecp256k1/src/scalar_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar_low_impl.h.md|crypto/secp256k1/libsecp256k1/src/scalar_low_impl.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2014 Pieter Wuille                                    *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_SCALAR_H
#define SECP256K1_SCALAR_H

#include "util.h"

#if defined(EXHAUSTIVE_TEST_ORDER)
#include "scalar_low.h"
#elif defined(SECP256K1_WIDEMUL_INT128)
#include "scalar_4x64.h"
#elif defined(SECP256K1_WIDEMUL_INT64)
#include "scalar_8x32.h"
#else
#error "Please select wide multiplication implementation"
#endif
...
```