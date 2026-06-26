# bitarray_test.go

## Architecture Metrics
- **Path:** `trie/bintrie/bitarray_test.go`
- **Extension:** `.go`
- **Size:** 5829 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 0

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `ba`
- `TestNewBitArray`
- `TestSetBytes`
- `TestSetBytesFull`
- `TestMSBs`
- `TestAppendBit`
- `TestSetBit`
- `TestEqual`
- `TestKeyBytesRoundTrip`
- `TestCopyIsIndependent`

## Imports (Dependencies)
*No internal imports*

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package bintrie

import (
	"bytes"
	"testing"
)

// ba builds a BitArray with the given length and leading bytes, for use as an
// expected value. Remaining bytes are zero.
func ba(length uint8, lead ...byte) BitArray {
	var b BitArray
	b.len = length
	copy(b.bytes[:], lead)
	return b
}

func TestNewBitArray(t *testing.T) {
	tests := []struct {
		name   string
		length uint8
...
```