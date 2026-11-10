# Meridian BioLabs — supplier procurement workspace

This repository keeps the approved-parts watchlist and the NorthPeak Supply intake
archive for Meridian BioLabs' consumables purchasing team.

- `watchlist/approved-parts.csv` — the curated list of parts Meridian has approved for
  procurement. Each row keeps the last agreed unit price in USD and the date it was
  reviewed. The list is under change control and only reflects parts we actually source.
- `intake/` — NorthPeak Supply feed revisions. `main` carries the current quarter
  (Q4 2026) revision. Branch `q3-baseline` preserves the previous quarter (Q3 2026)
  snapshot for audit.
- `CHANGELOG.md` — notes from earlier quarterly reviews.

The supplier feeds are raw dumps. They list far more parts than Meridian actually
sources, including third-party reseller bundles and historical ledger extracts. Only
parts on the approved watchlist are contracted.
