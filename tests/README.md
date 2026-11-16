# Tests

Unit tests and synthetic-profile recovery tests will be added as the modules in `src/hygro_india/` are implemented.

Planned coverage:

- readers return the expected variables and handle fill values
- quality-control criteria match `configs/qc_thresholds.yaml`
- Hänel fits recover known gamma on synthetic humidograms
- kappa-Köhler critical diameters match the analytic scaling in Section 8.6
- statistical helpers implement TOST and Benjamini-Hochberg as specified

There are no implemented tests yet. `test_package.py` only checks that the package imports.
