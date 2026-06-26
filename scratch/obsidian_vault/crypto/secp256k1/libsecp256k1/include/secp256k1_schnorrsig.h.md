# secp256k1_schnorrsig.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/include/secp256k1_schnorrsig.h`
- **Extension:** `.h`
- **Size:** 8177 bytes
- **Centrality Score:** 0.0010
- **In-Degree (Imported By):** 7
- **Out-Degree (Imports):** 2

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_schnorrsig_extraparams`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_extrakeys.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_extrakeys.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/examples/musig.c.md|crypto/secp256k1/libsecp256k1/examples/musig.c]]
- [[crypto/secp256k1/libsecp256k1/examples/schnorr.c.md|crypto/secp256k1/libsecp256k1/examples/schnorr.c]]
- [[crypto/secp256k1/libsecp256k1/src/ctime_tests.c.md|crypto/secp256k1/libsecp256k1/src/ctime_tests.c]]
- [[crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/bench_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/bench_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/main_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/tests_exhaustive_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/tests_exhaustive_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/tests_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/schnorrsig/tests_impl.h]]

## Source Code Snippet
```h
#ifndef SECP256K1_SCHNORRSIG_H
#define SECP256K1_SCHNORRSIG_H

#include "secp256k1.h"
#include "secp256k1_extrakeys.h"

#ifdef __cplusplus
extern "C" {
#endif

/** This module implements a variant of Schnorr signatures compliant with
 *  Bitcoin Improvement Proposal 340 "Schnorr Signatures for secp256k1"
 *  (https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki).
 */

/** A pointer to a function to deterministically generate a nonce.
 *
 *  Same as secp256k1_nonce function with the exception of accepting an
 *  additional pubkey argument and not requiring an attempt argument. The pubkey
 *  argument can protect signature schemes with key-prefixed challenge hash
...
```