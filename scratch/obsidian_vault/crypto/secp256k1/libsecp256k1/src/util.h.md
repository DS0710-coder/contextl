# util.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/util.h`
- **Extension:** `.h`
- **Size:** 15011 bytes
- **Centrality Score:** 0.0057
- **In-Degree (Imported By):** 42
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `print_buf_plain`
- `secp256k1_callback_call`
- `secp256k1_default_illegal_callback_fn`
- `secp256k1_default_error_callback_fn`
- ``
- `secp256k1_memczero`
- `secp256k1_memclear`
- `secp256k1_memcmp_var`
- `secp256k1_is_zero_array`
- `secp256k1_int_cmov`
- `secp256k1_ctz32_var_debruijn`
- `secp256k1_ctz64_var_debruijn`
- `secp256k1_ctz32_var`
- `secp256k1_ctz64_var`
- `secp256k1_read_be32`
- `secp256k1_write_be32`
- `secp256k1_read_be64`
- `secp256k1_write_be64`
- `secp256k1_rotr32`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]
- [[crypto/secp256k1/libsecp256k1/src/checkmem.h.md|crypto/secp256k1/libsecp256k1/src/checkmem.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/assumptions.h.md|crypto/secp256k1/libsecp256k1/src/assumptions.h]]
- [[crypto/secp256k1/libsecp256k1/src/bench.c.md|crypto/secp256k1/libsecp256k1/src/bench.c]]
- [[crypto/secp256k1/libsecp256k1/src/bench_ecmult.c.md|crypto/secp256k1/libsecp256k1/src/bench_ecmult.c]]
- [[crypto/secp256k1/libsecp256k1/src/bench_internal.c.md|crypto/secp256k1/libsecp256k1/src/bench_internal.c]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_compute_table_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_compute_table_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_gen_compute_table_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_gen_compute_table_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_gen_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_gen_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/field.h.md|crypto/secp256k1/libsecp256k1/src/field.h]]
- [[crypto/secp256k1/libsecp256k1/src/field_10x26_impl.h.md|crypto/secp256k1/libsecp256k1/src/field_10x26_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/field_5x52_impl.h.md|crypto/secp256k1/libsecp256k1/src/field_5x52_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/field_5x52_int128_impl.h.md|crypto/secp256k1/libsecp256k1/src/field_5x52_int128_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/field_impl.h.md|crypto/secp256k1/libsecp256k1/src/field_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/group_impl.h.md|crypto/secp256k1/libsecp256k1/src/group_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/hash_impl.h.md|crypto/secp256k1/libsecp256k1/src/hash_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/int128.h.md|crypto/secp256k1/libsecp256k1/src/int128.h]]
- [[crypto/secp256k1/libsecp256k1/src/int128_impl.h.md|crypto/secp256k1/libsecp256k1/src/int128_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/int128_native.h.md|crypto/secp256k1/libsecp256k1/src/int128_native.h]]
- [[crypto/secp256k1/libsecp256k1/src/int128_native_impl.h.md|crypto/secp256k1/libsecp256k1/src/int128_native_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/int128_struct.h.md|crypto/secp256k1/libsecp256k1/src/int128_struct.h]]
- [[crypto/secp256k1/libsecp256k1/src/int128_struct_impl.h.md|crypto/secp256k1/libsecp256k1/src/int128_struct_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modinv32.h.md|crypto/secp256k1/libsecp256k1/src/modinv32.h]]
- [[crypto/secp256k1/libsecp256k1/src/modinv32_impl.h.md|crypto/secp256k1/libsecp256k1/src/modinv32_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modinv64.h.md|crypto/secp256k1/libsecp256k1/src/modinv64.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/extrakeys/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/extrakeys/main_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/session_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/session_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/tests_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/tests_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/precompute_ecmult.c.md|crypto/secp256k1/libsecp256k1/src/precompute_ecmult.c]]
- [[crypto/secp256k1/libsecp256k1/src/precompute_ecmult_gen.c.md|crypto/secp256k1/libsecp256k1/src/precompute_ecmult_gen.c]]
- [[crypto/secp256k1/libsecp256k1/src/scalar.h.md|crypto/secp256k1/libsecp256k1/src/scalar.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar_4x64_impl.h.md|crypto/secp256k1/libsecp256k1/src/scalar_4x64_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar_8x32_impl.h.md|crypto/secp256k1/libsecp256k1/src/scalar_8x32_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar_impl.h.md|crypto/secp256k1/libsecp256k1/src/scalar_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar_low_impl.h.md|crypto/secp256k1/libsecp256k1/src/scalar_low_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/scratch_impl.h.md|crypto/secp256k1/libsecp256k1/src/scratch_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]
- [[crypto/secp256k1/libsecp256k1/src/testrand.h.md|crypto/secp256k1/libsecp256k1/src/testrand.h]]
- [[crypto/secp256k1/libsecp256k1/src/testrand_impl.h.md|crypto/secp256k1/libsecp256k1/src/testrand_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/tests.c.md|crypto/secp256k1/libsecp256k1/src/tests.c]]
- [[crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c.md|crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c]]
- [[crypto/secp256k1/libsecp256k1/src/testutil.h.md|crypto/secp256k1/libsecp256k1/src/testutil.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2013, 2014 Pieter Wuille                              *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_UTIL_H
#define SECP256K1_UTIL_H

#include "../include/secp256k1.h"
#include "checkmem.h"

#include <string.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <limits.h>
#if defined(_MSC_VER)
/* For SecureZeroMemory */
#include <Windows.h>
...
```