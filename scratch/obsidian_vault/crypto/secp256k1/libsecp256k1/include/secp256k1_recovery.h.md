# secp256k1_recovery.h

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/include/secp256k1_recovery.h`
- **Extension:** `.h`
- **Size:** 4672 bytes
- **Centrality Score:** 0.0009
- **In-Degree (Imported By):** 4
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `secp256k1_ecdsa_recoverable_signature`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]

## Imported By (Dependents)
- [[crypto/secp256k1/libsecp256k1/src/ctime_tests.c.md|crypto/secp256k1/libsecp256k1/src/ctime_tests.c]]
- [[crypto/secp256k1/libsecp256k1/src/modules/recovery/bench_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/recovery/bench_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/recovery/main_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/recovery/main_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/modules/recovery/tests_exhaustive_impl.h.md|crypto/secp256k1/libsecp256k1/src/modules/recovery/tests_exhaustive_impl.h]]

## Source Code Snippet
```h
#ifndef SECP256K1_RECOVERY_H
#define SECP256K1_RECOVERY_H

#include "secp256k1.h"

#ifdef __cplusplus
extern "C" {
#endif

/** Opaque data structure that holds a parsed ECDSA signature,
 *  supporting pubkey recovery.
 *
 *  The exact representation of data inside is implementation defined and not
 *  guaranteed to be portable between different platforms or versions. It is
 *  however guaranteed to be 65 bytes in size, and can be safely copied/moved.
 *  If you need to convert to a format suitable for storage or transmission, use
 *  the secp256k1_ecdsa_signature_serialize_* and
 *  secp256k1_ecdsa_signature_parse_* functions.
 *
 *  Furthermore, it is guaranteed that identical signatures (including their
...
```