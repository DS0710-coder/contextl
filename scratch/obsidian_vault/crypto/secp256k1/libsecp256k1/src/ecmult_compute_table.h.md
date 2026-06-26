# ecmult_compute_table.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/ecmult_compute_table.h`
- **Extension:** `.h`
- **Size:** 1073 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/ecmult_compute_table_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_compute_table_impl.h]]

## Source Code Snippet
```h
/*****************************************************************************************************
 * Copyright (c) 2013, 2014, 2017, 2021 Pieter Wuille, Andrew Poelstra, Jonas Nick, Russell O'Connor *
 * Distributed under the MIT software license, see the accompanying                                  *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.                              *
 *****************************************************************************************************/

#ifndef SECP256K1_ECMULT_COMPUTE_TABLE_H
#define SECP256K1_ECMULT_COMPUTE_TABLE_H

/* Construct table of all odd multiples of gen in range 1..(2**(window_g-1)-1). */
static void secp256k1_ecmult_compute_table(secp256k1_ge_storage* table, int window_g, const secp256k1_gej* gen);

/* Like secp256k1_ecmult_compute_table, but one for both gen and gen*2^128. */
static void secp256k1_ecmult_compute_two_tables(secp256k1_ge_storage* table, secp256k1_ge_storage* table_128, int window_g, const secp256k1_ge* gen);

#endif /* SECP256K1_ECMULT_COMPUTE_TABLE_H */
```