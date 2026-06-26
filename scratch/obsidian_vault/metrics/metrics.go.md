# metrics.go

## Architecture Metrics
- **Path:** `metrics/metrics.go`
- **Extension:** `.go`
- **Size:** 7599 bytes
- **Centrality Score:** 0.0372
- **In-Degree (Imported By):** 61
- **Out-Degree (Imports):** 1

## Explanation
*No explanation provided in source code.*

## Structural Outline
- `runtimeStats`
- `Enabled`
- `Enable`
- `ReadRuntimeStats`
- `readRuntimeStats`
- `CollectProcessMetrics`

## Imports (Dependencies)
- [[metrics/metrics.go.md|metrics/metrics.go]]

## Imported By (Dependents)
- [[cmd/geth/config.go.md|cmd/geth/config.go]]
- [[cmd/utils/flags.go.md|cmd/utils/flags.go]]
- [[core/blockchain.go.md|core/blockchain.go]]
- [[core/filtermaps/filtermaps.go.md|core/filtermaps/filtermaps.go]]
- [[core/jumpdest.go.md|core/jumpdest.go]]
- [[core/rawdb/freezer.go.md|core/rawdb/freezer.go]]
- [[core/rawdb/freezer_table.go.md|core/rawdb/freezer_table.go]]
- [[core/rawdb/freezer_table_test.go.md|core/rawdb/freezer_table_test.go]]
- [[core/rawdb/schema.go.md|core/rawdb/schema.go]]
- [[core/state/metrics.go.md|core/state/metrics.go]]
- [[core/state/snapshot/metrics.go.md|core/state/snapshot/metrics.go]]
- [[core/state/snapshot/snapshot.go.md|core/state/snapshot/snapshot.go]]
- [[core/state/state_sizer.go.md|core/state/state_sizer.go]]
- [[core/state/trie_prefetcher.go.md|core/state/trie_prefetcher.go]]
- [[core/stateless/stats.go.md|core/stateless/stats.go]]
- [[core/txpool/blobpool/blobpool.go.md|core/txpool/blobpool/blobpool.go]]
- [[core/txpool/blobpool/cache.go.md|core/txpool/blobpool/cache.go]]
- [[core/txpool/blobpool/metrics.go.md|core/txpool/blobpool/metrics.go]]
- [[core/txpool/legacypool/legacypool.go.md|core/txpool/legacypool/legacypool.go]]
- [[core/txpool/locals/tx_tracker.go.md|core/txpool/locals/tx_tracker.go]]
- [[core/txpool/reserver.go.md|core/txpool/reserver.go]]
- [[eth/catalyst/metrics.go.md|eth/catalyst/metrics.go]]
- [[eth/downloader/metrics.go.md|eth/downloader/metrics.go]]
- [[eth/downloader/queue.go.md|eth/downloader/queue.go]]
- [[eth/dropper.go.md|eth/dropper.go]]
- [[eth/fetcher/metrics.go.md|eth/fetcher/metrics.go]]
- [[eth/handler.go.md|eth/handler.go]]
- [[eth/protocols/eth/handler.go.md|eth/protocols/eth/handler.go]]
- [[eth/protocols/eth/handshake.go.md|eth/protocols/eth/handshake.go]]
- [[eth/protocols/eth/metrics.go.md|eth/protocols/eth/metrics.go]]
- [[eth/protocols/snap/handler.go.md|eth/protocols/snap/handler.go]]
- [[eth/protocols/snap/metrics.go.md|eth/protocols/snap/metrics.go]]
- [[ethdb/leveldb/leveldb.go.md|ethdb/leveldb/leveldb.go]]
- [[ethdb/pebble/pebble.go.md|ethdb/pebble/pebble.go]]
- [[ethdb/pebble/pebble_v1.go.md|ethdb/pebble/pebble_v1.go]]
- [[internal/debug/flags.go.md|internal/debug/flags.go]]
- [[metrics/exp/exp.go.md|metrics/exp/exp.go]]
- [[metrics/influxdb/influxdb.go.md|metrics/influxdb/influxdb.go]]
- [[metrics/influxdb/influxdb_test.go.md|metrics/influxdb/influxdb_test.go]]
- [[metrics/influxdb/influxdbv1.go.md|metrics/influxdb/influxdbv1.go]]
- [[metrics/influxdb/influxdbv2.go.md|metrics/influxdb/influxdbv2.go]]
- [[metrics/internal/sampledata.go.md|metrics/internal/sampledata.go]]
- [[metrics/internal/sampledata_test.go.md|metrics/internal/sampledata_test.go]]
- [[metrics/metrics.go.md|metrics/metrics.go]]
- [[metrics/prometheus/collector.go.md|metrics/prometheus/collector.go]]
- [[metrics/prometheus/collector_test.go.md|metrics/prometheus/collector_test.go]]
- [[metrics/prometheus/prometheus.go.md|metrics/prometheus/prometheus.go]]
- [[metrics/runtimehistogram.go.md|metrics/runtimehistogram.go]]
- [[metrics/runtimehistogram_test.go.md|metrics/runtimehistogram_test.go]]
- [[p2p/discover/metrics.go.md|p2p/discover/metrics.go]]
- [[p2p/discover/table.go.md|p2p/discover/table.go]]
- [[p2p/metrics.go.md|p2p/metrics.go]]
- [[p2p/peer.go.md|p2p/peer.go]]
- [[p2p/tracker/tracker.go.md|p2p/tracker/tracker.go]]
- [[p2p/tracker/tracker_test.go.md|p2p/tracker/tracker_test.go]]
- [[p2p/transport.go.md|p2p/transport.go]]
- [[rpc/metrics.go.md|rpc/metrics.go]]
- [[trie/sync.go.md|trie/sync.go]]
- [[triedb/hashdb/database.go.md|triedb/hashdb/database.go]]
- [[triedb/pathdb/metrics.go.md|triedb/pathdb/metrics.go]]
- [[triedb/pathdb/states.go.md|triedb/pathdb/states.go]]

## Source Code Snippet
```go
// Go port of Coda Hale's Metrics library
//
// <https://github.com/rcrowley/go-metrics>
//
// Coda Hale's original work: <https://github.com/codahale/metrics>

package metrics

import (
	"runtime/metrics"
	"runtime/pprof"
	"time"
)

var (
	metricsEnabled = false
)

// Enabled is checked by functions that are deemed 'expensive', e.g. if a
// meter-type does locking and/or non-trivial math operations during update.
...
```