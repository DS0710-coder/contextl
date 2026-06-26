# secp256k1_extrakeys.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/include/secp256k1_extrakeys.h`
- **Extension:** `.h`
- **Size:** 10986 bytes
- **Centrality Score:** 0.0016
- **In-Degree (Imported By):** 10
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_xonly_pubkey`
- `secp256k1_keypair`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/examples/musig.c.md|crypto/secp256k1/libsecp256k1/examples/musig.c]]
- [[crypto/secp256k1/libsecp256k1/examples/schnorr.c.md|crypto/secp256k1/libsecp256k1/examples/schnorr.c]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_musig.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_musig.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_schnorrsig.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_schnorrsig.h]]
- [[crypto/secp256k1/libsecp256k1/src/ctime_tests.c.md|crypto/secp256k1/libsecp256k1/src/ctime_tests.c]]
- [[crypto/secp256k1/libsecp256k1/src/modules/extrakeys/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/extrakeys/main_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/extrakeys/tests_exhaustive_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/extrakeys/tests_exhaustive_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/extrakeys/tests_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/extrakeys/tests_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/session_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/session_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/musig/tests_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/musig/tests_impl.h]]

## Source Code Snippet
```h
#ifndef SECP256K1_EXTRAKEYS_H
#define SECP256K1_EXTRAKEYS_H

#include "secp256k1.h"

#ifdef __cplusplus
extern "C" {
#endif

/** Opaque data structure that holds a parsed and valid "x-only" public key.
 *  An x-only pubkey encodes a point whose Y coordinate is even. It is
 *  serialized using only its X coordinate (32 bytes). See BIP-340 for more
 *  information about x-only pubkeys.
 *
 *  The exact representation of data inside is implementation defined and not
 *  guaranteed to be portable between different platforms or versions. It is
 *  however guaranteed to be 64 bytes in size, and can be safely copied/moved.
 *  If you need to convert to a format suitable for storage, transmission, use
 *  use secp256k1_xonly_pubkey_serialize and secp256k1_xonly_pubkey_parse. To
 *  compare keys, use secp256k1_xonly_pubkey_cmp.
...
```