# ctime_tests.c

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/ctime_tests.c`
- **Extension:** `.c`
- **Size:** 9631 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 9

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `main`
- `run_tests`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_ecdh.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_ecdh.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_ellswift.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_ellswift.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_extrakeys.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_extrakeys.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_musig.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_musig.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_recovery.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_recovery.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_schnorrsig.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_schnorrsig.h]]
- [[crypto/secp256k1/libsecp256k1/src/assumptions.h.md|crypto/secp256k1/libsecp256k1/src/assumptions.h]]
- [[crypto/secp256k1/libsecp256k1/src/checkmem.h.md|crypto/secp256k1/libsecp256k1/src/checkmem.h]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```c
/***********************************************************************
 * Copyright (c) 2020 Gregory Maxwell                                  *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../include/secp256k1.h"
#include "assumptions.h"
#include "checkmem.h"

#if !SECP256K1_CHECKMEM_ENABLED
#  error "This tool cannot be compiled without memory-checking interface (valgrind or msan)"
#endif

#ifdef ENABLE_MODULE_ECDH
# include "../include/secp256k1_ecdh.h"
...
```