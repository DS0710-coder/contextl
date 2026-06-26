# assumptions.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/assumptions.h`
- **Extension:** `.h`
- **Size:** 4667 bytes
- **Centrality Score:** 0.0004
- **In-Degree (Imported By):** 7
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_assumption_checker`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/int128_native.h.md|crypto/secp256k1/libsecp256k1/src/int128_native.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/dummy.go.md|crypto/secp256k1/dummy.go]]
- [[crypto/secp256k1/libsecp256k1/src/bench_internal.c.md|crypto/secp256k1/libsecp256k1/src/bench_internal.c]]
- [[crypto/secp256k1/libsecp256k1/src/ctime_tests.c.md|crypto/secp256k1/libsecp256k1/src/ctime_tests.c]]
- [[crypto/secp256k1/libsecp256k1/src/precompute_ecmult.c.md|crypto/secp256k1/libsecp256k1/src/precompute_ecmult.c]]
- [[crypto/secp256k1/libsecp256k1/src/precompute_ecmult_gen.c.md|crypto/secp256k1/libsecp256k1/src/precompute_ecmult_gen.c]]
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]
- [[crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c.md|crypto/secp256k1/libsecp256k1/src/tests_exhaustive.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2020 Pieter Wuille                                    *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_ASSUMPTIONS_H
#define SECP256K1_ASSUMPTIONS_H

#include <limits.h>

#include "util.h"
#if defined(SECP256K1_INT128_NATIVE)
#include "int128_native.h"
#endif

/* This library, like most software, relies on a number of compiler implementation defined (but not undefined)
   behaviours. Although the behaviours we require are essentially universal we test them specifically here to
   reduce the odds of experiencing an unwelcome surprise.
*/
...
```