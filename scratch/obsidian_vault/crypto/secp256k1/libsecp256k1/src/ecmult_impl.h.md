# ecmult_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/ecmult_impl.h`
- **Extension:** `.h`
- **Size:** 33819 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_strauss_point_state`
- `secp256k1_strauss_state`
- `secp256k1_strauss_point_state`
- `secp256k1_strauss_state`
- `secp256k1_strauss_point_state`
- `secp256k1_strauss_state`
- `secp256k1_strauss_point_state`
- `secp256k1_strauss_state`
- `secp256k1_strauss_point_state`
- `secp256k1_strauss_point_state`
- `secp256k1_pippenger_point_state`
- `secp256k1_pippenger_state`
- `secp256k1_pippenger_point_state`
- `secp256k1_pippenger_state`
- `secp256k1_pippenger_point_state`
- `secp256k1_pippenger_point_state`
- `secp256k1_pippenger_state`
- `secp256k1_pippenger_state`
- `secp256k1_pippenger_state`
- `secp256k1_pippenger_point_state`
- `secp256k1_pippenger_point_state`
- `secp256k1_pippenger_state`
- `secp256k1_ecmult_odd_multiples_table`
- `secp256k1_ecmult_table_verify`
- `secp256k1_ecmult_table_get_ge`
- `secp256k1_ecmult_table_get_ge_lambda`
- `secp256k1_ecmult_table_get_ge_storage`
- `secp256k1_ecmult_wnaf`
- `secp256k1_ecmult_strauss_wnaf`
- `secp256k1_ecmult`
- `secp256k1_strauss_scratch_size`
- `secp256k1_ecmult_strauss_batch`
- `secp256k1_ecmult_strauss_batch_single`
- `secp256k1_strauss_max_points`
- `secp256k1_wnaf_fixed`
- `secp256k1_ecmult_pippenger_wnaf`
- `secp256k1_pippenger_bucket_window`
- `secp256k1_pippenger_bucket_window_inv`
- `secp256k1_ecmult_endo_split`
- `secp256k1_pippenger_scratch_size`
- `secp256k1_ecmult_pippenger_batch`
- `secp256k1_ecmult_pippenger_batch_single`
- `secp256k1_pippenger_max_points`
- `secp256k1_ecmult_multi_simple_var`
- `secp256k1_ecmult_multi_batch_size_helper`
- `secp256k1_ecmult_multi_var`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/ecmult.h.md|crypto/secp256k1/libsecp256k1/src/ecmult.h]]
- [[crypto/secp256k1/libsecp256k1/src/group.h.md|crypto/secp256k1/libsecp256k1/src/group.h]]
- [[crypto/secp256k1/libsecp256k1/src/precomputed_ecmult.h.md|crypto/secp256k1/libsecp256k1/src/precomputed_ecmult.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar.h.md|crypto/secp256k1/libsecp256k1/src/scalar.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/bench_ecmult.c.md|crypto/secp256k1/libsecp256k1/src/bench_ecmult.c]]
- [[crypto/secp256k1/libsecp256k1/src/bench_internal.c.md|crypto/secp256k1/libsecp256k1/src/bench_internal.c]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_const_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_const_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]

## Source Code Snippet
```h
/******************************************************************************
 * Copyright (c) 2013, 2014, 2017 Pieter Wuille, Andrew Poelstra, Jonas Nick  *
 * Distributed under the MIT software license, see the accompanying           *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.       *
 ******************************************************************************/

#ifndef SECP256K1_ECMULT_IMPL_H
#define SECP256K1_ECMULT_IMPL_H

#include <string.h>
#include <stdint.h>

#include "util.h"
#include "group.h"
#include "scalar.h"
#include "ecmult.h"
#include "precomputed_ecmult.h"

#if defined(EXHAUSTIVE_TEST_ORDER)
/* We need to lower these values for exhaustive tests because
...
```