# bench.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/bench.h`
- **Extension:** `.h`
- **Size:** 5088 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 3
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `timespec`
- `timeval`
- `gettime_i64`
- `print_number`
- `run_benchmark`
- `have_flag`
- `have_invalid_args`
- `get_iters`
- `print_output_table_header_row`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/bench.c.md|crypto/secp256k1/libsecp256k1/src/bench.c]]
- [[crypto/secp256k1/libsecp256k1/src/bench_ecmult.c.md|crypto/secp256k1/libsecp256k1/src/bench_ecmult.c]]
- [[crypto/secp256k1/libsecp256k1/src/bench_internal.c.md|crypto/secp256k1/libsecp256k1/src/bench_internal.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2014 Pieter Wuille                                    *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_BENCH_H
#define SECP256K1_BENCH_H

#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include <string.h>

#if (defined(_MSC_VER) && _MSC_VER >= 1900)
#  include <time.h>
#else
#  include <sys/time.h>
#endif

...
```