# scalar_8x32_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/scalar_8x32_impl.h`
- **Extension:** `.h`
- **Size:** 29036 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_scalar_set_int`
- `secp256k1_scalar_get_bits_limb32`
- `secp256k1_scalar_get_bits_var`
- `secp256k1_scalar_check_overflow`
- `secp256k1_scalar_reduce`
- `secp256k1_scalar_add`
- `secp256k1_scalar_cadd_bit`
- `secp256k1_scalar_set_b32`
- `secp256k1_scalar_get_b32`
- `secp256k1_scalar_is_zero`
- `secp256k1_scalar_negate`
- `secp256k1_scalar_half`
- `secp256k1_scalar_is_one`
- `secp256k1_scalar_is_high`
- `secp256k1_scalar_cond_negate`
- `secp256k1_scalar_reduce_512`
- `secp256k1_scalar_mul_512`
- `secp256k1_scalar_mul`
- `secp256k1_scalar_split_128`
- `secp256k1_scalar_eq`
- `secp256k1_scalar_mul_shift_var`
- `secp256k1_scalar_cmov`
- `secp256k1_scalar_from_signed30`
- `secp256k1_scalar_to_signed30`
- `secp256k1_scalar_inverse`
- `secp256k1_scalar_inverse_var`
- `secp256k1_scalar_is_even`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/checkmem.h.md|crypto/secp256k1/libsecp256k1/src/checkmem.h]]
- [[crypto/secp256k1/libsecp256k1/src/modinv32_impl.h.md|crypto/secp256k1/libsecp256k1/src/modinv32_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/scalar_impl.h.md|crypto/secp256k1/libsecp256k1/src/scalar_impl.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2014 Pieter Wuille                                    *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_SCALAR_REPR_IMPL_H
#define SECP256K1_SCALAR_REPR_IMPL_H

#include "checkmem.h"
#include "modinv32_impl.h"
#include "util.h"

/* Limbs of the secp256k1 order. */
#define SECP256K1_N_0 ((uint32_t)0xD0364141UL)
#define SECP256K1_N_1 ((uint32_t)0xBFD25E8CUL)
#define SECP256K1_N_2 ((uint32_t)0xAF48A03BUL)
#define SECP256K1_N_3 ((uint32_t)0xBAAEDCE6UL)
#define SECP256K1_N_4 ((uint32_t)0xFFFFFFFEUL)
#define SECP256K1_N_5 ((uint32_t)0xFFFFFFFFUL)
...
```