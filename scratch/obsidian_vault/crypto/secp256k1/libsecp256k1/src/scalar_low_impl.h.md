# scalar_low_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/scalar_low_impl.h`
- **Extension:** `.h`
- **Size:** 5841 bytes
- **Centrality Score:** 0.0003
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_scalar_is_even`
- `secp256k1_scalar_set_int`
- `secp256k1_scalar_get_bits_limb32`
- `secp256k1_scalar_get_bits_var`
- `secp256k1_scalar_check_overflow`
- `secp256k1_scalar_add`
- `secp256k1_scalar_cadd_bit`
- `secp256k1_scalar_set_b32`
- `secp256k1_scalar_get_b32`
- `secp256k1_scalar_is_zero`
- `secp256k1_scalar_negate`
- `secp256k1_scalar_is_one`
- `secp256k1_scalar_is_high`
- `secp256k1_scalar_cond_negate`
- `secp256k1_scalar_mul`
- `secp256k1_scalar_split_128`
- `secp256k1_scalar_eq`
- `secp256k1_scalar_cmov`
- `secp256k1_scalar_inverse`
- `secp256k1_scalar_inverse_var`
- `secp256k1_scalar_half`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/checkmem.h.md|crypto/secp256k1/libsecp256k1/src/checkmem.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar.h.md|crypto/secp256k1/libsecp256k1/src/scalar.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/scalar_impl.h.md|crypto/secp256k1/libsecp256k1/src/scalar_impl.h]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2015 Andrew Poelstra                                  *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/

#ifndef SECP256K1_SCALAR_REPR_IMPL_H
#define SECP256K1_SCALAR_REPR_IMPL_H

#include "checkmem.h"
#include "scalar.h"
#include "util.h"

#include <string.h>

SECP256K1_INLINE static int secp256k1_scalar_is_even(const secp256k1_scalar *a) {
    SECP256K1_SCALAR_VERIFY(a);

    return !(*a & 1);
}
...
```