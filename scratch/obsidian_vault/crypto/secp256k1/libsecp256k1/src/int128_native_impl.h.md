# int128_native_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/int128_native_impl.h`
- **Extension:** `.h`
- **Size:** 2881 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
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
#ifndef SECP256K1_INT128_NATIVE_IMPL_H
#define SECP256K1_INT128_NATIVE_IMPL_H

#include "int128.h"
#include "util.h"

static SECP256K1_INLINE void secp256k1_u128_load(secp256k1_uint128 *r, uint64_t hi, uint64_t lo) {
    *r = (((uint128_t)hi) << 64) + lo;
}

static SECP256K1_INLINE void secp256k1_u128_mul(secp256k1_uint128 *r, uint64_t a, uint64_t b) {
   *r = (uint128_t)a * b;
}

static SECP256K1_INLINE void secp256k1_u128_accum_mul(secp256k1_uint128 *r, uint64_t a, uint64_t b) {
   *r += (uint128_t)a * b;
}

static SECP256K1_INLINE void secp256k1_u128_accum_u64(secp256k1_uint128 *r, uint64_t a) {
   *r += a;
...
```