# modinv64_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modinv64_impl.h`
- **Extension:** `.h`
- **Size:** 37653 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_modinv64_abs`
- `secp256k1_modinv64_mul_62`
- `secp256k1_modinv64_mul_cmp_62`
- `secp256k1_modinv64_det_check_pow2`
- `secp256k1_modinv64_normalize_62`
- `secp256k1_modinv64_divsteps_59`
- `secp256k1_modinv64_divsteps_62_var`
- `secp256k1_modinv64_posdivsteps_62_var`
- `secp256k1_modinv64_update_de_62`
- `secp256k1_modinv64_update_fg_62`
- `secp256k1_modinv64_update_fg_62_var`
- `secp256k1_modinv64`
- `secp256k1_modinv64_var`
- `secp256k1_jacobi64_maybe_var`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/int128.h.md|crypto/secp256k1/libsecp256k1/src/int128.h]]
- [[crypto/secp256k1/libsecp256k1/src/modinv64.h.md|crypto/secp256k1/libsecp256k1/src/modinv64.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/field_5x52_impl.h.md|crypto/secp256k1/libsecp256k1/src/field_5x52_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar_4x64_impl.h.md|crypto/secp256k1/libsecp256k1/src/scalar_4x64_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/tests.c.md|crypto/secp256k1/libsecp256k1/src/tests.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2020 Peter Dettman                                    *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 **********************************************************************/

#ifndef SECP256K1_MODINV64_IMPL_H
#define SECP256K1_MODINV64_IMPL_H

#include "int128.h"
#include "modinv64.h"

/* This file implements modular inversion based on the paper "Fast constant-time gcd computation and
 * modular inversion" by Daniel J. Bernstein and Bo-Yin Yang.
 *
 * For an explanation of the algorithm, see doc/safegcd_implementation.md. This file contains an
 * implementation for N=62, using 62-bit signed limbs represented as int64_t.
 */

/* Data type for transition matrices (see section 3 of explanation).
...
```