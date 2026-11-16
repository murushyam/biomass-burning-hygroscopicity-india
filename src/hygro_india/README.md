# `hygro_india`

Python package scaffold for the CALIOP-ERA5 hygroscopicity analysis described in `docs/proposal.md`.

| Module | Role |
| --- | --- |
| `io/` | CALIOP, ERA5, FIRMS and AERONET readers (TODO) |
| `colocate.py` | Time and space interpolation (TODO) |
| `qc.py` | Layer selection and well-mixed tests (TODO) |
| `dust_fraction.py` | Two-component depolarisation separation (TODO) |
| `humidogram.py` | Hänel fit with Monte Carlo errors (TODO) |
| `mie_kappa.py` | Mie look-up and kappa_L retrieval (TODO) |
| `ccn.py` | Critical diameter and activated fraction (TODO) |
| `attribution.py` | Fire exposure and smoke age (TODO) |
| `closure.py` | Composition closure and aircraft-profile checks (TODO) |
| `stats.py` | Mixed models, bootstrap, TOST, FDR (TODO) |

There is no retrieval, attribution or statistical implementation in this directory yet.
