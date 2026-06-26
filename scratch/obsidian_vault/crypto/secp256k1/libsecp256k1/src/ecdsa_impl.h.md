# ecdsa_impl.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/ecdsa_impl.h`
- **Extension:** `.h`
- **Size:** 10462 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 1
- **Out-Degree (Imports):** 6

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_der_read_len`
- `secp256k1_der_parse_integer`
- `secp256k1_ecdsa_sig_parse`
- `secp256k1_ecdsa_sig_serialize`
- `secp256k1_ecdsa_sig_verify`
- `secp256k1_ecdsa_sig_sign`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/src/ecdsa.h.md|crypto/secp256k1/libsecp256k1/src/ecdsa.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult.h.md|crypto/secp256k1/libsecp256k1/src/ecmult.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_gen.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_gen.h]]
- [[crypto/secp256k1/libsecp256k1/src/field.h.md|crypto/secp256k1/libsecp256k1/src/field.h]]
- [[crypto/secp256k1/libsecp256k1/src/group.h.md|crypto/secp256k1/libsecp256k1/src/group.h]]
- [[crypto/secp256k1/libsecp256k1/src/scalar.h.md|crypto/secp256k1/libsecp256k1/src/scalar.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/secp256k1.c.md|crypto/secp256k1/libsecp256k1/src/secp256k1.c]]

## Source Code Snippet
```h
/***********************************************************************
 * Copyright (c) 2013-2015 Pieter Wuille                               *
 * Distributed under the MIT software license, see the accompanying    *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.*
 ***********************************************************************/


#ifndef SECP256K1_ECDSA_IMPL_H
#define SECP256K1_ECDSA_IMPL_H

#include "scalar.h"
#include "field.h"
#include "group.h"
#include "ecmult.h"
#include "ecmult_gen.h"
#include "ecdsa.h"

/** Group order for secp256k1 defined as 'n' in "Standards for Efficient Cryptography" (SEC2) 2.7.1
 *  $ sage -c 'load("secp256k1_params.sage"); print(hex(N))'
 *  0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
...
```