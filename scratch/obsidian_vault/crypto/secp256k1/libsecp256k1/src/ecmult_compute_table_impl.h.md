# ecmult_compute_table_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/ecmult_compute_table_impl.h`
- **Extension:** `.h`
- **Size:** 1913 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 5

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_ecmult_compute_table`
- `secp256k1_ecmult_compute_two_tables`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/ecmult.h.md|crypto/secp256k1/libsecp256k1/src/ecmult.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_compute_table.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_compute_table.h]]
- [[crypto/secp256k1/libsecp256k1/src/field_impl.h.md|crypto/secp256k1/libsecp256k1/src/field_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/group_impl.h.md|crypto/secp256k1/libsecp256k1/src/group_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/precompute_ecmult.c.md|crypto/secp256k1/libsecp256k1/src/precompute_ecmult.c]]
- [[crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c.md|crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c]]

## Source Code Snippet
```h
/*****************************************************************************************************
 * Copyright (c) 2013, 2014, 2017, 2021 Pieter Wuille, Andrew Poelstra, Jonas Nick, Russell O'Connor *
 * Distributed under the MIT software license, see the accompanying                                  *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.                              *
 *****************************************************************************************************/

#ifndef SECP256K1_ECMULT_COMPUTE_TABLE_IMPL_H
#define SECP256K1_ECMULT_COMPUTE_TABLE_IMPL_H

#include "ecmult_compute_table.h"
#include "group_impl.h"
#include "field_impl.h"
#include "ecmult.h"
#include "util.h"

static void secp256k1_ecmult_compute_table(secp256k1_ge_storage* table, int window_g, const secp256k1_gej* gen) {
    secp256k1_gej gj;
    secp256k1_ge ge, dgen;
    int j;

...
```