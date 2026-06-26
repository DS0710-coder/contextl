# checkmem.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/checkmem.h`
- **Extension:** `.h`
- **Size:** 4640 bytes
- **Centrality Score:** 0.0030
- **In-Degree (Imported By):** 9
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
*No major classes or functions detected.*

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/ctime_tests.c.md|crypto/secp256k1/libsecp256k1/src/ctime_tests.c]]
- [[crypto/secp256k1/libsecp256k1/src/field_10x26_impl.h.md|crypto/secp256k1/libsecp256k1/src/field_10x26_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/field_5x52_impl.h.md|crypto/secp256k1/libsecp256k1/src/field_5x52_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar_4x64_impl.h.md|crypto/secp256k1/libsecp256k1/src/scalar_4x64_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar_8x32_impl.h.md|crypto/secp256k1/libsecp256k1/src/scalar_8x32_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar_low_impl.h.md|crypto/secp256k1/libsecp256k1/src/scalar_low_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]
- [[crypto/secp256k1/libsecp256k1/src/tests.c.md|crypto/secp256k1/libsecp256k1/src/tests.c]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2022 Pieter Wuille                                    *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

/* The code here is inspired by Kris Kwiatkowski's approach in
 * https://github.com/kriskwiatkowski/pqc/blob/main/src/common/ct_check.h
 * to provide a general interface for memory-checking mechanisms, primarily
 * for constant-time checking.
 */

/* These macros are defined by this header file:
 *
 * - SECP256K1_CHECKMEM_ENABLED:
 *   - 1 if memory-checking integration is available, 0 otherwise.
 *     This is just a compile-time macro. Use the next macro to check it is actually
 *     available at runtime.
 * - SECP256K1_CHECKMEM_RUNNING():
 *   - Acts like a function call, returning 1 if memory checking is available
...
```