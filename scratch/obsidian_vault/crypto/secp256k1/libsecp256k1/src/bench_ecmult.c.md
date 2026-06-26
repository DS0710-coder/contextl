# bench_ecmult.c

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/bench_ecmult.c`
- **Extension:** `.c`
- **Size:** 13752 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `help`
- `hash_into_offset`
- `bench_ecmult_teardown_helper`
- `bench_ecmult_setup`
- `bench_ecmult_gen`
- `bench_ecmult_gen_teardown`
- `bench_ecmult_const`
- `bench_ecmult_const_teardown`
- `bench_ecmult_1p`
- `bench_ecmult_1p_teardown`
- `bench_ecmult_0p_g`
- `bench_ecmult_0p_g_teardown`
- `bench_ecmult_1p_g`
- `bench_ecmult_1p_g_teardown`
- `run_ecmult_bench`
- `bench_ecmult_multi_callback`
- `bench_ecmult_multi`
- `bench_ecmult_multi_setup`
- `bench_ecmult_multi_teardown`
- `generate_scalar`
- `run_ecmult_multi_bench`
- `main`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]
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
 * Copyright (c) 2017 Pieter Wuille                                    *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/
#include <stdio.h>
#include <stdlib.h>

#include "secp256k1.c"
#include "../include/secp256k1.h"

#include "util.h"
#include "hash_impl.h"
#include "field_impl.h"
#include "group_impl.h"
#include "scalar_impl.h"
#include "ecmult_impl.h"
#include "bench.h"

#define POINTS 32768
...
```