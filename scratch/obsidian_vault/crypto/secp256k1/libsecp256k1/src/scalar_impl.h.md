# scalar_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/scalar_impl.h`
- **Extension:** `.h`
- **Size:** 12104 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_scalar_clear`
- `secp256k1_scalar_set_b32_seckey`
- `secp256k1_scalar_verify`
- `secp256k1_scalar_split_lambda_verify`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/scalar.h.md|crypto/secp256k1/libsecp256k1/src/scalar.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar_4x64_impl.h.md|crypto/secp256k1/libsecp256k1/src/scalar_4x64_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar_8x32_impl.h.md|crypto/secp256k1/libsecp256k1/src/scalar_8x32_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar_low_impl.h.md|crypto/secp256k1/libsecp256k1/src/scalar_low_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/bench_ecmult.c.md|crypto/secp256k1/libsecp256k1/src/bench_ecmult.c]]
- [[crypto/secp256k1/libsecp256k1/src/bench_internal.c.md|crypto/secp256k1/libsecp256k1/src/bench_internal.c]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_gen_compute_table_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_gen_compute_table_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2014 Pieter Wuille                                    *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_SCALAR_IMPL_H
#define SECP256K1_SCALAR_IMPL_H

#ifdef VERIFY
#include <string.h>
#endif

#include "scalar.h"
#include "util.h"

#if defined(EXHAUSTIVE_TEST_ORDER)
#include "scalar_low_impl.h"
#elif defined(SECP256K1_WIDEMUL_INT128)
#include "scalar_4x64_impl.h"
...
```