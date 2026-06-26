# field_10x26_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/field_10x26_impl.h`
- **Extension:** `.h`
- **Size:** 52022 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_fe_impl_verify`
- `secp256k1_fe_impl_get_bounds`
- `secp256k1_fe_impl_normalize`
- `secp256k1_fe_impl_normalize_weak`
- `secp256k1_fe_impl_normalize_var`
- `secp256k1_fe_impl_normalizes_to_zero`
- `secp256k1_fe_impl_normalizes_to_zero_var`
- `secp256k1_fe_impl_set_int`
- `secp256k1_fe_impl_is_zero`
- `secp256k1_fe_impl_is_odd`
- `secp256k1_fe_impl_cmp_var`
- `secp256k1_fe_impl_set_b32_mod`
- `secp256k1_fe_impl_set_b32_limit`
- `secp256k1_fe_impl_get_b32`
- `secp256k1_fe_impl_negate_unchecked`
- `secp256k1_fe_impl_mul_int_unchecked`
- `secp256k1_fe_impl_add`
- `secp256k1_fe_impl_add_int`
- `secp256k1_fe_mul_inner`
- `secp256k1_fe_sqr_inner`
- `secp256k1_fe_impl_mul`
- `secp256k1_fe_impl_sqr`
- `secp256k1_fe_impl_cmov`
- `secp256k1_fe_impl_half`
- `secp256k1_fe_storage_cmov`
- `secp256k1_fe_impl_to_storage`
- `secp256k1_fe_impl_from_storage`
- `secp256k1_fe_from_signed30`
- `secp256k1_fe_to_signed30`
- `secp256k1_fe_impl_inv`
- `secp256k1_fe_impl_inv_var`
- `secp256k1_fe_impl_is_square_var`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/checkmem.h.md|crypto/secp256k1/libsecp256k1/src/checkmem.h]]
- [[crypto/secp256k1/libsecp256k1/src/field.h.md|crypto/secp256k1/libsecp256k1/src/field.h]]
- [[crypto/secp256k1/libsecp256k1/src/modinv32_impl.h.md|crypto/secp256k1/libsecp256k1/src/modinv32_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/field_impl.h.md|crypto/secp256k1/libsecp256k1/src/field_impl.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2013, 2014 Pieter Wuille                              *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_FIELD_REPR_IMPL_H
#define SECP256K1_FIELD_REPR_IMPL_H

#include "checkmem.h"
#include "util.h"
#include "field.h"
#include "modinv32_impl.h"

#ifdef VERIFY
static void secp256k1_fe_impl_verify(const secp256k1_fe *a) {
    const uint32_t *d = a->n;
    int m = a->normalized ? 1 : 2 * a->magnitude;
    VERIFY_CHECK(d[0] <= 0x3FFFFFFUL * m);
    VERIFY_CHECK(d[1] <= 0x3FFFFFFUL * m);
...
```