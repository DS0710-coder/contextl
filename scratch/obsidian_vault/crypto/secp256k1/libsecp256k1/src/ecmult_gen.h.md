# ecmult_gen.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/ecmult_gen.h`
- **Extension:** `.h`
- **Size:** 5368 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 9
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/group.h.md|crypto/secp256k1/libsecp256k1/src/group.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar.h.md|crypto/secp256k1/libsecp256k1/src/scalar.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/ecdsa_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecdsa_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/eckey.h.md|crypto/secp256k1/libsecp256k1/src/eckey.h]]
- [[crypto/secp256k1/libsecp256k1/src/eckey_impl.h.md|crypto/secp256k1/libsecp256k1/src/eckey_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_gen_compute_table.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_gen_compute_table.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_gen_compute_table_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_gen_compute_table_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_gen_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_gen_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/precompute_ecmult_gen.c.md|crypto/secp256k1/libsecp256k1/src/precompute_ecmult_gen.c]]
- [[crypto/secp256k1/libsecp256k1/src/precomputed_ecmult_gen.c.md|crypto/secp256k1/libsecp256k1/src/precomputed_ecmult_gen.c]]
- [[crypto/secp256k1/libsecp256k1/src/precomputed_ecmult_gen.h.md|crypto/secp256k1/libsecp256k1/src/precomputed_ecmult_gen.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) Pieter Wuille, Peter Dettman                          *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_ECMULT_GEN_H
#define SECP256K1_ECMULT_GEN_H

#include "scalar.h"
#include "group.h"


/* Configuration parameters for the signed-digit multi-comb algorithm:
 *
 * - COMB_BLOCKS is the number of blocks the input is split into. Each
 *   has a corresponding table.
 * - COMB_TEETH is the number of bits simultaneously covered by one table.
 * - COMB_RANGE is the number of bits in supported scalars. For production
 *   purposes, only 256 is reasonable, but smaller numbers are supported for
...
```