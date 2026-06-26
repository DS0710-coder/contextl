# ecmult.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/ecmult.h`
- **Extension:** `.h`
- **Size:** 2679 bytes
- **Centrality Score:** 0.0008
- **In-Degree (Imported By):** 9
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/group.h.md|crypto/secp256k1/libsecp256k1/src/group.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar.h.md|crypto/secp256k1/libsecp256k1/src/scalar.h]]
- [[crypto/secp256k1/libsecp256k1/src/scratch.h.md|crypto/secp256k1/libsecp256k1/src/scratch.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/ecdsa.h.md|crypto/secp256k1/libsecp256k1/src/ecdsa.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecdsa_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecdsa_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/eckey.h.md|crypto/secp256k1/libsecp256k1/src/eckey.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_compute_table_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_compute_table_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/precompute_ecmult.c.md|crypto/secp256k1/libsecp256k1/src/precompute_ecmult.c]]
- [[crypto/secp256k1/libsecp256k1/src/precomputed_ecmult.c.md|crypto/secp256k1/libsecp256k1/src/precomputed_ecmult.c]]
- [[crypto/secp256k1/libsecp256k1/src/precomputed_ecmult.h.md|crypto/secp256k1/libsecp256k1/src/precomputed_ecmult.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2013, 2014, 2017 Pieter Wuille, Andrew Poelstra       *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_ECMULT_H
#define SECP256K1_ECMULT_H

#include "group.h"
#include "scalar.h"
#include "scratch.h"

#ifndef ECMULT_WINDOW_SIZE
#  define ECMULT_WINDOW_SIZE 15
#  ifdef DEBUG_CONFIG
#     pragma message DEBUG_CONFIG_MSG("ECMULT_WINDOW_SIZE undefined, assuming default value")
#  endif
#endif

...
```