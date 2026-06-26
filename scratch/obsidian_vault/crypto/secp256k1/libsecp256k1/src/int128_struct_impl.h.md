# int128_struct_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/int128_struct_impl.h`
- **Extension:** `.h`
- **Size:** 7884 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_umul128`
- `secp256k1_mul128`
- `secp256k1_umul128`
- `secp256k1_mul128`
- `secp256k1_u128_load`
- `secp256k1_u128_mul`
- `secp256k1_u128_accum_mul`
- `secp256k1_u128_accum_u64`
- `secp256k1_u128_rshift`
- `secp256k1_u128_to_u64`
- `secp256k1_u128_hi_u64`
- `secp256k1_u128_from_u64`
- `secp256k1_u128_check_bits`
- `secp256k1_i128_load`
- `secp256k1_i128_mul`
- `secp256k1_i128_accum_mul`
- `secp256k1_i128_dissip_mul`
- `secp256k1_i128_det`
- `secp256k1_i128_rshift`
- `secp256k1_i128_to_u64`
- `secp256k1_i128_to_i64`
- `secp256k1_i128_from_i64`
- `secp256k1_i128_eq_var`
- `secp256k1_i128_check_pow2`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/int128.h.md|crypto/secp256k1/libsecp256k1/src/int128.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/int128_impl.h.md|crypto/secp256k1/libsecp256k1/src/int128_impl.h]]

## Source Code Snippet
```h
#ifndef SECP256K1_INT128_STRUCT_IMPL_H
#define SECP256K1_INT128_STRUCT_IMPL_H

#include "int128.h"
#include "util.h"

#if defined(_MSC_VER) && (defined(_M_X64) || defined(_M_ARM64)) /* MSVC */
#    include <intrin.h>
#    if defined(_M_ARM64) || defined(SECP256K1_MSVC_MULH_TEST_OVERRIDE)
/* On ARM64 MSVC, use __(u)mulh for the upper half of 64x64 multiplications.
   (Define SECP256K1_MSVC_MULH_TEST_OVERRIDE to test this code path on X64,
   which supports both __(u)mulh and _umul128.) */
#        if defined(SECP256K1_MSVC_MULH_TEST_OVERRIDE)
#            pragma message(__FILE__ ": SECP256K1_MSVC_MULH_TEST_OVERRIDE is defined, forcing use of __(u)mulh.")
#        endif
static SECP256K1_INLINE uint64_t secp256k1_umul128(uint64_t a, uint64_t b, uint64_t* hi) {
    *hi = __umulh(a, b);
    return a * b;
}

...
```