# Intake archive

Supplier feed revisions land here each quarter. The loader accepts one marker per line:

```
PART|<sku>|<part name>|<category>|<uom>
```

Notes:

- `feeds/` holds the consolidated warehouse feeds consumed by the purchasing loader.
- `vendor_bundle/` holds third-party reseller dumps. These are duplicated mirrors and are
  not part of our own price agreements.
- `legacy/` holds historical extracts kept for audit only.
- Lines may appear several times, may trail other content, or may be empty (`PART|`).

The `q3-baseline` branch keeps the previous quarter's snapshot unchanged for audit; `main`
carries the current revision.
