# bench_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/recovery/bench_impl.h`
- **Extension:** `.h`
- **Size:** 2320 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `bench_recover`
- `bench_recover_setup`
- `run_recovery_bench`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_recovery.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_recovery.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/dummy.go.md|crypto/secp256k1/dummy.go]]
- [[crypto/secp256k1/libsecp256k1/src/bench.c.md|crypto/secp256k1/libsecp256k1/src/bench.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2014-2015 Pieter Wuille                               *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_RECOVERY_BENCH_H
#define SECP256K1_MODULE_RECOVERY_BENCH_H

#include "../../../include/secp256k1_recovery.h"

typedef struct {
    secp256k1_context *ctx;
    unsigned char msg[32];
    unsigned char sig[64];
} bench_recover_data;

static void bench_recover(void* arg, int iters) {
    int i;
    bench_recover_data *data = (bench_recover_data*)arg;
...
```