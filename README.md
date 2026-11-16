# Does the hygroscopicity of biomass-burning aerosol over India change with altitude?

A constraint from CALIOP and ERA5 humidograms, 2006 to 2023. This repository holds a research proposal prepared for *Atmospheric Chemistry and Physics* (ACP), together with a code scaffold for the planned analysis.

**Author:** Shyam Sunder Murugesan Sellammal, NIT Rourkela
**ORCID:** [https://orcid.org/0000-0002-9964-6199](https://orcid.org/0000-0002-9964-6199)
**Status:** proposal stage; analysis code to follow

## Summary

Aerosol hygroscopicity controls how efficiently particles activate as cloud condensation nuclei (CCN), but its vertical structure over South Asia has not been constrained by observation, and existing CALIOP-based CCN estimates assume a fixed hygroscopicity parameter. This proposal sets out a pre-specified analysis of the final CALIOP version 5.00 level 2 aerosol record (June 2006 to June 2023) over India. Layers are co-located with ERA5 humidity and screened for well-mixed conditions. Smoke is identified by independent fire exposure from active-fire detections and HYSPLIT back trajectories, because the CALIOP elevated-smoke subtype is itself assigned by altitude. The Hänel exponent γ is fitted to the backscatter increase with relative humidity inside each layer, converted to a lidar-effective hygroscopicity κ_L, and propagated to critical dry diameter. Three pre-stated hypotheses are tested with a mixed-effects model, equivalence tests and a power calculation. All inputs are public.

The full text is in [docs/proposal.md](docs/proposal.md).

## Hypotheses

The effect sizes are design choices and will be revisited after a pilot analysis. Full statements, tests and sample-size calculations are in Section 5 of the proposal.

- **H1 (altitude dependence).** After adjustment for smoke age, source region, season and RH range, the Hänel exponent γ differs between the free troposphere and the boundary layer by at least 0.15. An equivalence test against a margin of 0.10 is used so that a null result is informative.
- **H2 (CCN implication).** The critical dry diameter at 0.3 % supersaturation differs by at least 10 % between those layers.
- **H3 (seasonal modulation).** The altitude effect is not the same in every season, and is largest in the post-monsoon regime (October to November).

## Data sources

All inputs listed in the proposal are public. Several archives need a free account, as noted below. Links were checked on 16 November 2026. Details, variables and licences are in [docs/data_sources.md](docs/data_sources.md) and in Section 7 of the proposal.

| Dataset | Access | Registration |
| --- | --- | --- |
| CALIOP L2 5 km Aerosol Profile, V5.00 (primary) | [DOI 10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V5-00](https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V5-00); [Subsetter](https://subset.larc.nasa.gov/calipso/) | Free NASA Earthdata Login |
| CALIOP L2 5 km Aerosol Layer, V5.00 | [DOI 10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmALay-Standard-V5-00](https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmALay-Standard-V5-00) | Free NASA Earthdata Login |
| CALIOP L2 5 km Aerosol Profile, V4.51 (sensitivity) | [DOI 10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V4-51](https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V4-51) | Free NASA Earthdata Login |
| ERA5 hourly, pressure levels | [DOI 10.24381/cds.bd0915c6](https://doi.org/10.24381/cds.bd0915c6) | Free Copernicus CDS account |
| ERA5 hourly, single levels | [DOI 10.24381/cds.adbb2d47](https://doi.org/10.24381/cds.adbb2d47) | Free Copernicus CDS account |
| ERA5 on model levels (refinement) | [CDS page](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-complete) | Free Copernicus CDS account |
| FIRMS active fires (MODIS C6.1, VIIRS 375 m) | [FIRMS download](https://firms.modaps.eosdis.nasa.gov/download/) | Free MAP_KEY for the API |
| AERONET Version 3 | [AERONET](https://aeronet.gsfc.nasa.gov/); [site list](https://aeronet.gsfc.nasa.gov/aeronet_locations_v3.txt) | No registration; citation policy applies |
| HYSPLIT with GDAS1 | [HYSPLIT](https://www.ready.noaa.gov/HYSPLIT.php); [GDAS1](https://www.ready.noaa.gov/gdas1.php) | Public |
| FLEXPART 10.4 (sensitivity) | [Source code](https://github.com/flexpart/flexpart) | Open source; ERA5 input needs a CDS account |
| MERRA-2 aerosol diagnostics | [M2I3NVAER](https://disc.gsfc.nasa.gov/datasets/M2I3NVAER_5.12.4/summary); [M2T1NXAER](https://disc.gsfc.nasa.gov/datasets/M2T1NXAER_5.12.4/summary) | Free Earthdata Login |
| CAMS global reanalysis (EAC4) | [DOI 10.24381/d58bbf47](https://doi.org/10.24381/d58bbf47) | Free Copernicus ADS account |
| Radiosonde profiles for RH checks | [University of Wyoming archive](https://weather.uwyo.edu/upperair/sounding.shtml) | No registration observed; terms of use to be confirmed |
| SWAAMI-RAWEX aircraft CCN and CN profiles | [figshare 10.6084/m9.figshare.14744046](https://doi.org/10.6084/m9.figshare.14744046) | Public (CC BY 4.0 per DataCite) |
| EarthCARE ATLID L2A (extension) | [ESA EarthCARE data](https://earth.esa.int/eogateway/missions/earthcare/data) | Free ESA EO Sign In |

Raw downloads belong in `data/raw/` and are git-ignored. Do not commit NetCDF, HDF or HDF5 files.

## Repository structure

```
├── README.md
├── LICENSE
├── CITATION.cff
├── environment.yml
├── requirements.txt
├── docs/
│   ├── proposal.md           Full ACP research proposal
│   ├── protocol.md           Frozen design choices (to be filled after the pilot)
│   └── data_sources.md       Datasets, versions, access and registration notes
├── configs/
│   ├── qc_thresholds.yaml    Layer selection criteria (Table 2)
│   ├── regions.yaml          Domain, sub-regions and seasons
│   └── hysplit.yaml          Trajectory settings
├── data/                     Download notes; raw and derived data are git-ignored
├── src/hygro_india/          Package stubs (docstrings and TODOs only)
├── workflows/                Pipeline placeholder
├── notebooks/                Pilot and figure notebooks (to follow)
├── tests/                    Unit and synthetic-profile tests (to follow)
└── results/                  Tables and figures produced by the workflow
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Alternatively, create the conda environment in `environment.yml`:

```bash
conda env create -f environment.yml
conda activate hygro-india
```

The `pyhdf` package needs the HDF4 C library. On Debian or Ubuntu, install `libhdf4-dev` first. If that build fails, `h5py` still covers HDF5 products. Install at least one of `miepython` or `PyMieScatt` for the planned Mie lookup; both are listed in `requirements.txt`.

Analysis modules in `src/hygro_india/` are stubs with docstrings and TODO notes. There is no retrieval or statistical code yet.

## Licence and citation

The code in this repository is released under the MIT Licence. Please cite the proposal in [docs/proposal.md](docs/proposal.md). A DOI will be added to [CITATION.cff](CITATION.cff) once the archive is published.
