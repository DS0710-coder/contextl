# registry_test.go

## Architecture Metrics
- **Path:** `metrics/registry_test.go`
- **Extension:** `.go`
- **Size:** 7521 bytes
- **Centrality Score:** 0.0002
- **In-Degree (Imported By):** 0
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `BenchmarkRegistry`
- `BenchmarkRegistryGetOrRegister`
- `BenchmarkRegistryGetOrRegisterParallel_8`
- `BenchmarkRegistryGetOrRegisterParallel_32`
- `benchmarkRegistryGetOrRegisterParallel`
- `TestRegistry`
- `TestRegistryDuplicate`
- `TestRegistryGet`
- `TestRegistryGetOrRegister`
- `TestRegistryGetOrRegisterWithLazyInstantiation`
- `TestRegistryUnregister`
- `TestPrefixedChildRegistryGetOrRegister`
- `TestPrefixedRegistryGetOrRegister`
- `TestPrefixedRegistryRegister`
- `TestPrefixedRegistryUnregister`
- `TestPrefixedRegistryGet`
- `TestPrefixedChildRegistryGet`
- `TestChildPrefixedRegistryRegister`
- `TestChildPrefixedRegistryOfChildRegister`
- `TestWalkRegistries`

## Imports (Dependencies)
- [[beacon/light/sync/head_sync.go.md|beacon/light/sync/head_sync.go]]

## Imported By (Dependents)
*Not imported by any file*

## Source Code Snippet
```go
package metrics

import (
	"sync"
	"testing"
)

func BenchmarkRegistry(b *testing.B) {
	r := NewRegistry()
	r.Register("foo", NewCounter())
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		r.Each(func(string, interface{}) {})
	}
}

func BenchmarkRegistryGetOrRegister(b *testing.B) {
	sample := func() Sample { return nil }
	tests := []struct {
		name string
...
```