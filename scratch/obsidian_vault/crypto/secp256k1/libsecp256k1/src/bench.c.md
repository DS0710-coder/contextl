# bench.c

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/bench.c`
- **Extension:** `.c`
- **Size:** 9987 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 7

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `help`
- `bench_verify`
- `bench_sign_setup`
- `bench_sign_run`
- `bench_keygen_setup`
- `bench_keygen_run`
- `main`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]
- [[crypto/secp256k1/libsecp256k1/src/bench.h.md|crypto/secp256k1/libsecp256k1/src/bench.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/ecdh/bench_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/ecdh/bench_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/ellswift/bench_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/ellswift/bench_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/recovery/bench_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/recovery/bench_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/bench_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/bench_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```c
/***********************************************************************
 * Copyright (c) 2014 Pieter Wuille                                    *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../include/secp256k1.h"
#include "util.h"
#include "bench.h"

static void help(int default_iters) {
    printf("Benchmarks the following algorithms:\n");
    printf("    - ECDSA signing/verification\n");

#ifdef ENABLE_MODULE_ECDH
    printf("    - ECDH key exchange (optional module)\n");
...
```