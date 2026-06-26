# bench_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/ecdh/bench_impl.h`
- **Extension:** `.h`
- **Size:** 1875 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `bench_ecdh_setup`
- `bench_ecdh`
- `run_ecdh_bench`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_ecdh.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_ecdh.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/bench.c.md|crypto/secp256k1/libsecp256k1/src/bench.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2015 Pieter Wuille, Andrew Poelstra                   *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_ECDH_BENCH_H
#define SECP256K1_MODULE_ECDH_BENCH_H

#include "../../../include/secp256k1_ecdh.h"

typedef struct {
    secp256k1_context *ctx;
    secp256k1_pubkey point;
    unsigned char scalar[32];
} bench_ecdh_data;

static void bench_ecdh_setup(void* arg) {
    int i;
    bench_ecdh_data *data = (bench_ecdh_data*)arg;
...
```