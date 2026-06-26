# secp256k1_musig.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/include/secp256k1_musig.h`
- **Extension:** `.h`
- **Size:** 28115 bytes
- **Centrality Score:** 0.0005
- **In-Degree (Imported By):** 6
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_musig_keyagg_cache`
- `secp256k1_musig_secnonce`
- `secp256k1_musig_pubnonce`
- `secp256k1_musig_aggnonce`
- `secp256k1_musig_session`
- `secp256k1_musig_partial_sig`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_extrakeys.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_extrakeys.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/examples/musig.c.md|crypto/secp256k1/libsecp256k1/examples/musig.c]]
- [[crypto/secp256k1/libsecp256k1/src/ctime_tests.c.md|crypto/secp256k1/libsecp256k1/src/ctime_tests.c]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/keyagg.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/session.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/session.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/session_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/session_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/tests_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/tests_impl.h]]

## Source Code Snippet
```h
#ifndef SECP256K1_MUSIG_H
#define SECP256K1_MUSIG_H

#include "secp256k1_extrakeys.h"

#ifdef __cplusplus
extern "C" {
#endif

#include <stddef.h>
#include <stdint.h>

/** This module implements BIP 327 "MuSig2 for BIP340-compatible
 *  Multi-Signatures"
 *  (https://github.com/bitcoin/bips/blob/master/bip-0327.mediawiki)
 *  v1.0.0. You can find an example demonstrating the musig module in
 *  examples/musig.c.
 *
 *  The module also supports BIP 341 ("Taproot") public key tweaking.
 *
...
```