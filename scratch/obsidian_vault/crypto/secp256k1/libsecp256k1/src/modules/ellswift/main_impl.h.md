# main_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/ellswift/main_impl.h`
- **Extension:** `.h`
- **Size:** 26374 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 2
- **Out-Degree (Imports):** 4

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_ellswift_xswiftec_frac_var`
- `secp256k1_ellswift_xswiftec_var`
- `secp256k1_ellswift_swiftec_var`
- `secp256k1_ellswift_xswiftec_inv_var`
- `secp256k1_ellswift_prng`
- `secp256k1_ellswift_xelligatorswift_var`
- `secp256k1_ellswift_elligatorswift_var`
- `secp256k1_ellswift_sha256_init_encode`
- `secp256k1_ellswift_encode`
- `secp256k1_ellswift_sha256_init_create`
- `secp256k1_ellswift_create`
- `secp256k1_ellswift_decode`
- `ellswift_xdh_hash_function_prefix`
- `secp256k1_ellswift_sha256_init_bip324`
- `ellswift_xdh_hash_function_bip324`
- `secp256k1_ellswift_xdh`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_ellswift.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_ellswift.h]]
- [[crypto/secp256k1/libsecp256k1/src/eckey.h.md|crypto/secp256k1/libsecp256k1/src/eckey.h]]
- [[crypto/secp256k1/libsecp256k1/src/hash.h.md|crypto/secp256k1/libsecp256k1/src/hash.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/modules/ellswift/tests_exhaustive_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/ellswift/tests_exhaustive_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_ELLSWIFT_MAIN_H
#define SECP256K1_MODULE_ELLSWIFT_MAIN_H

#include "../../../include/secp256k1.h"
#include "../../../include/secp256k1_ellswift.h"
#include "../../eckey.h"
#include "../../hash.h"

/** c1 = (sqrt(-3)-1)/2 */
static const secp256k1_fe secp256k1_ellswift_c1 = SECP256K1_FE_CONST(0x851695d4, 0x9a83f8ef, 0x919bb861, 0x53cbcb16, 0x630fb68a, 0xed0a766a, 0x3ec693d6, 0x8e6afa40);
/** c2 = (-sqrt(-3)-1)/2 = -(c1+1) */
static const secp256k1_fe secp256k1_ellswift_c2 = SECP256K1_FE_CONST(0x7ae96a2b, 0x657c0710, 0x6e64479e, 0xac3434e9, 0x9cf04975, 0x12f58995, 0xc1396c28, 0x719501ee);
/** c3 = (-sqrt(-3)+1)/2 = -c1 = c2+1 */
static const secp256k1_fe secp256k1_ellswift_c3 = SECP256K1_FE_CONST(0x7ae96a2b, 0x657c0710, 0x6e64479e, 0xac3434e9, 0x9cf04975, 0x12f58995, 0xc1396c28, 0x719501ef);
/** c4 = (sqrt(-3)+1)/2 = -c2 = c1+1 */
...
```