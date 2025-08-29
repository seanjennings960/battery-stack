# Battery Stack Monorepo

Components:
- `pkgs/battery-data` — ETL (dbt/dlt/DuckDB/Parquet), schemas, exports (incl. BatteryML-compatible)
- `pkgs/battery-models` — baselines + Neural ODE/UDE, common ModelModule ABI, exporters
- `pkgs/battery-runtime` — minimal fixed-rate loop + adapters (sources/sinks) + node interfaces
- `pkgs/batteryd` — (future) service wrapper; can be Rust or Python
- `pkgs/monitor-ui` — web UI (Svelte/React), dashboards & residuals

Dev:
- One devcontainer w/ Python + Node (and optional Rust)
- Per-package tests + one E2E observer replay
