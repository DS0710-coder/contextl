# bench_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/bench_impl.h`
- **Extension:** `.h`
- **Size:** 3967 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `bench_schnorrsig_sign`
- `bench_schnorrsig_verify`
- `run_schnorrsig_bench`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_schnorrsig.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_schnorrsig.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/bench.c.md|crypto/secp256k1/libsecp256k1/src/bench.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2018-2020 Andrew Poelstra, Jonas Nick                 *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_SCHNORRSIG_BENCH_H
#define SECP256K1_MODULE_SCHNORRSIG_BENCH_H

#include "../../../include/secp256k1_schnorrsig.h"

#define MSGLEN 32

typedef struct {
    secp256k1_context *ctx;
    int n;

    const secp256k1_keypair **keypairs;
    const unsigned char **pk;
    const unsigned char **sigs;
...
```