# Data directory

Raw downloads and derived catalogues are not committed to git. Place files as follows:

```
data/
├── README.md          This file
├── raw/               Git-ignored original products (CALIOP, ERA5, FIRMS, and so on)
└── derived/           Git-ignored layer catalogue and gamma/kappa tables, unless a small file is later archived
```

How to obtain each product, including registration, is listed in [docs/data_sources.md](../docs/data_sources.md). Section 7 of [docs/proposal.md](../docs/proposal.md) is the authoritative catalogue.

Suggested layout under `raw/` (to be followed once download scripts exist):

- `raw/caliop/V5.00/` and `raw/caliop/V4.51/`
- `raw/era5/pressure_levels/`, `raw/era5/single_levels/`, `raw/era5/model_levels/`
- `raw/firms/`
- `raw/aeronet/`
- `raw/merra2/`, `raw/cams/`
- `raw/radiosonde/`, `raw/swaami_rawex/`

Do not store Earthdata, CDS, ADS or FIRMS keys in this repository. Use environment variables or a local, git-ignored file.
