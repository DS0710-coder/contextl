# field_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/field_impl.h`
- **Extension:** `.h`
- **Size:** 14043 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 6
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_fe_clear`
- `secp256k1_fe_equal`
- `secp256k1_fe_verify`
- `secp256k1_fe_verify_magnitude`
- `secp256k1_fe_verify`
- `secp256k1_fe_verify_magnitude`
- `secp256k1_fe_normalize`
- `secp256k1_fe_normalize_weak`
- `secp256k1_fe_normalize_var`
- `secp256k1_fe_normalizes_to_zero`
- `secp256k1_fe_normalizes_to_zero_var`
- `secp256k1_fe_set_int`
- `secp256k1_fe_add_int`
- `secp256k1_fe_is_zero`
- `secp256k1_fe_is_odd`
- `secp256k1_fe_cmp_var`
- `secp256k1_fe_set_b32_mod`
- `secp256k1_fe_set_b32_limit`
- `secp256k1_fe_get_b32`
- `secp256k1_fe_negate_unchecked`
- `secp256k1_fe_mul_int_unchecked`
- `secp256k1_fe_add`
- `secp256k1_fe_mul`
- `secp256k1_fe_sqr`
- `secp256k1_fe_cmov`
- `secp256k1_fe_to_storage`
- `secp256k1_fe_from_storage`
- `secp256k1_fe_inv`
- `secp256k1_fe_inv_var`
- `secp256k1_fe_is_square_var`
- `secp256k1_fe_get_bounds`
- `secp256k1_fe_half`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/field.h.md|crypto/secp256k1/libsecp256k1/src/field.h]]
- [[crypto/secp256k1/libsecp256k1/src/field_10x26_impl.h.md|crypto/secp256k1/libsecp256k1/src/field_10x26_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/field_5x52_impl.h.md|crypto/secp256k1/libsecp256k1/src/field_5x52_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/bench_ecmult.c.md|crypto/secp256k1/libsecp256k1/src/bench_ecmult.c]]
- [[crypto/secp256k1/libsecp256k1/src/bench_internal.c.md|crypto/secp256k1/libsecp256k1/src/bench_internal.c]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_compute_table_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_compute_table_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_gen_compute_table_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_gen_compute_table_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/precompute_ecmult.c.md|crypto/secp256k1/libsecp256k1/src/precompute_ecmult.c]]
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2013, 2014 Pieter Wuille                              *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_FIELD_IMPL_H
#define SECP256K1_FIELD_IMPL_H

#include "field.h"
#include "util.h"

#if defined(SECP256K1_WIDEMUL_INT128)
#include "field_5x52_impl.h"
#elif defined(SECP256K1_WIDEMUL_INT64)
#include "field_10x26_impl.h"
#else
#error "Please select wide multiplication implementation"
#endif

...
```