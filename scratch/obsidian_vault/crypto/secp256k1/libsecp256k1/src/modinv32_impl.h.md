# modinv32_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modinv32_impl.h`
- **Extension:** `.h`
- **Size:** 33492 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_modinv32_mul_30`
- `secp256k1_modinv32_mul_cmp_30`
- `secp256k1_modinv32_normalize_30`
- `secp256k1_modinv32_divsteps_30`
- `secp256k1_modinv32_divsteps_30_var`
- `secp256k1_modinv32_posdivsteps_30_var`
- `secp256k1_modinv32_update_de_30`
- `secp256k1_modinv32_update_fg_30`
- `secp256k1_modinv32_update_fg_30_var`
- `secp256k1_modinv32`
- `secp256k1_modinv32_var`
- `secp256k1_jacobi32_maybe_var`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/modinv32.h.md|crypto/secp256k1/libsecp256k1/src/modinv32.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/field_10x26_impl.h.md|crypto/secp256k1/libsecp256k1/src/field_10x26_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar_8x32_impl.h.md|crypto/secp256k1/libsecp256k1/src/scalar_8x32_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/tests.c.md|crypto/secp256k1/libsecp256k1/src/tests.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2020 Peter Dettman                                    *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 **********************************************************************/

#ifndef SECP256K1_MODINV32_IMPL_H
#define SECP256K1_MODINV32_IMPL_H

#include "modinv32.h"

#include "util.h"

#include <stdlib.h>

/* This file implements modular inversion based on the paper "Fast constant-time gcd computation and
 * modular inversion" by Daniel J. Bernstein and Bo-Yin Yang.
 *
 * For an explanation of the algorithm, see doc/safegcd_implementation.md. This file contains an
 * implementation for N=30, using 30-bit signed limbs represented as int32_t.
...
```