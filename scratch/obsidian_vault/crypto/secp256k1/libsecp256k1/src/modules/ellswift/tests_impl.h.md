# tests_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/modules/ellswift/tests_impl.h`
- **Extension:** `.h`
- **Size:** 88309 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ellswift_xswiftec_inv_test`
- `ellswift_decode_test`
- `ellswift_xdh_test`
- `ellswift_xswiftec_inv_test`
- `ellswift_decode_test`
- `ellswift_xdh_test`
- `ellswift_xswiftec_inv_test`
- `ellswift_decode_test`
- `ellswift_xdh_test`
- `ellswift_xdh_hash_x32`
- `run_ellswift_tests`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_ellswift.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_ellswift.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/tests.c.md|crypto/secp256k1/libsecp256k1/src/tests.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_MODULE_ELLSWIFT_TESTS_H
#define SECP256K1_MODULE_ELLSWIFT_TESTS_H

#include "../../../include/secp256k1_ellswift.h"

struct ellswift_xswiftec_inv_test {
    int enc_bitmap;
    secp256k1_fe u;
    secp256k1_fe x;
    secp256k1_fe encs[8];
};

struct ellswift_decode_test {
    unsigned char enc[64];
    secp256k1_fe x;
...
```