# bench_internal.c

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/bench_internal.c`
- **Extension:** `.c`
- **Size:** 17394 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 10

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `help`
- `bench_setup`
- `bench_scalar_add`
- `bench_scalar_negate`
- `bench_scalar_half`
- `bench_scalar_mul`
- `bench_scalar_split`
- `bench_scalar_inverse`
- `bench_scalar_inverse_var`
- `bench_field_half`
- `bench_field_normalize`
- `bench_field_normalize_weak`
- `bench_field_mul`
- `bench_field_sqr`
- `bench_field_inverse`
- `bench_field_inverse_var`
- `bench_field_sqrt`
- `bench_field_is_square_var`
- `bench_group_double_var`
- `bench_group_add_var`
- `bench_group_add_affine`
- `bench_group_add_affine_var`
- `bench_group_add_zinv_var`
- `bench_group_to_affine_var`
- `bench_ecmult_wnaf`
- `bench_sha256`
- `bench_hmac_sha256`
- `bench_rfc6979_hmac_sha256`
- `bench_context`
- `main`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]
- [[crypto/secp256k1/libsecp256k1/src/assumptions.h.md|crypto/secp256k1/libsecp256k1/src/assumptions.h]]
- [[crypto/secp256k1/libsecp256k1/src/bench.h.md|crypto/secp256k1/libsecp256k1/src/bench.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/field_impl.h.md|crypto/secp256k1/libsecp256k1/src/field_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/group_impl.h.md|crypto/secp256k1/libsecp256k1/src/group_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/hash_impl.h.md|crypto/secp256k1/libsecp256k1/src/hash_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar_impl.h.md|crypto/secp256k1/libsecp256k1/src/scalar_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```c
/***********************************************************************
 * Copyright (c) 2014-2015 Pieter Wuille                               *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/
#include <stdio.h>
#include <stdlib.h>

#include "secp256k1.c"
#include "../include/secp256k1.h"

#include "assumptions.h"
#include "util.h"
#include "hash_impl.h"
#include "field_impl.h"
#include "group_impl.h"
#include "scalar_impl.h"
#include "ecmult_impl.h"
#include "bench.h"

...
```