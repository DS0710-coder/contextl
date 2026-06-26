# ellswift.c

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/examples/ellswift.c`
- **Extension:** `.c`
- **Size:** 5494 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 3

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `main`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/examples/examples_util.h.md|crypto/secp256k1/libsecp256k1/examples/examples_util.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]
- [[crypto/secp256k1/libsecp256k1/include/secp256k1_ellswift.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1_ellswift.h]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```c
/*************************************************************************
 * Written in 2024 by Sebastian Falbesoner                               *
 * To the extent possible under law, the author(s) have dedicated all    *
 * copyright and related and neighboring rights to the software in this  *
 * file to the public domain worldwide. This software is distributed     *
 * without any warranty. For the CC0 Public Domain Dedication, see       *
 * EXAMPLES_COPYING or https://creativecommons.org/publicdomain/zero/1.0 *
 *************************************************************************/

/** This file demonstrates how to use the ElligatorSwift module to perform
 *  a key exchange according to BIP 324. Additionally, see the documentation
 *  in include/secp256k1_ellswift.h and doc/ellswift.md.
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

#include <secp256k1.h>
...
```