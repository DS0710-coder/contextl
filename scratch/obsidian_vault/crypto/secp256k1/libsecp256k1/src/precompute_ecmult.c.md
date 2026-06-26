# precompute_ecmult.c

## Architecture Metrics
- **Path:** `crypto/secp256k1/libsecp256k1/src/precompute_ecmult.c`
- **Extension:** `.c`
- **Size:** 4014 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 8

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `print_table`
- `print_two_tables`
- `main`

## Imports (Dependencies)
- [[crypto/secp256k1/libsecp256k1/include/secp256k1.h.md|crypto/secp256k1/libsecp256k1/include/secp256k1.h]]
- [[crypto/secp256k1/libsecp256k1/src/assumptions.h.md|crypto/secp256k1/libsecp256k1/src/assumptions.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult.h.md|crypto/secp256k1/libsecp256k1/src/ecmult.h]]
- [[crypto/secp256k1/libsecp256k1/src/ecmult_compute_table_impl.h.md|crypto/secp256k1/libsecp256k1/src/ecmult_compute_table_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/field_impl.h.md|crypto/secp256k1/libsecp256k1/src/field_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/group_impl.h.md|crypto/secp256k1/libsecp256k1/src/group_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/int128_impl.h.md|crypto/secp256k1/libsecp256k1/src/int128_impl.h]]
- [[crypto/secp256k1/libsecp256k1/src/util.h.md|crypto/secp256k1/libsecp256k1/src/util.h]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```c
/*****************************************************************************************************
 * Copyright (c) 2013, 2014, 2017, 2021 Pieter Wuille, Andrew Poelstra, Jonas Nick, Russell O'Connor *
 * Distributed under the MIT software license, see the accompanying                                  *
 * file COPYING or https://www.opensource.org/licenses/mit-license.php.                              *
 *****************************************************************************************************/

#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>

#include "../include/secp256k1.h"

#include "assumptions.h"
#include "util.h"

#include "field_impl.h"
#include "group_impl.h"
#include "int128_impl.h"
#include "ecmult.h"
#include "ecmult_compute_table_impl.h"
...
```