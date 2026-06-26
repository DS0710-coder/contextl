# bench_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/ellswift/bench_impl.h`
- **Extension:** `.h`
- **Size:** 4399 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `bench_ellswift_setup`
- `bench_ellswift_encode`
- `bench_ellswift_create`
- `bench_ellswift_decode`
- `bench_ellswift_xdh`
- `run_ellswift_bench`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_ellswift.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_ellswift.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/bench.c.md|crypto/secp256k1/libsecp256k1/src/bench.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_ELLSWIFT_BENCH_H
#define SECP256K1_MODULE_ELLSWIFT_BENCH_H

#include "../../../include/secp256k1_ellswift.h"

typedef struct {
    secp256k1_context *ctx;
    secp256k1_pubkey point[256];
    unsigned char rnd64[64];
} bench_ellswift_data;

static void bench_ellswift_setup(void *arg) {
    int i;
    bench_ellswift_data *data = (bench_ellswift_data*)arg;
    static const unsigned char init[64] = {
...
```