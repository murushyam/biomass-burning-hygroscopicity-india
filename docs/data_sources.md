# Data sources

All inputs used by this proposal are public. Several archives require a free account, which is stated below. Links were opened on 16 November 2026 and returned an accessible page unless noted. No restricted data are required for any primary result. This page follows Section 7 of [proposal.md](proposal.md).

Download instructions for local use are in [data/README.md](../data/README.md). Raw files are not committed to this repository.

## Catalogue

| Dataset | Variables used | Resolution and period | Access | Licence and registration |
| --- | --- | --- | --- | --- |
| CALIOP L2 5 km Aerosol Profile, **V5.00 (primary)** | `Total_Backscatter_Coefficient_532` and its uncertainty, `Particulate_Depolarization_Ratio_Profile_532`, `Extinction_Coefficient_532`, `Extinction_QC_Flag_532`, `CAD_Score`, `Atmospheric_Volume_Description`, `Relative_Humidity` (MERRA-2), `Temperature`, `Pressure`, `DEM_Surface_Elevation`, `Day_Night_Flag`, `Minimum_Laser_Energy_532`, `Low_Energy_Mitigation_Column_QC_Flag` | 5 km along track, 60 m vertical, June 2006 to June 2023 | [DOI 10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V5-00](https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V5-00); [Subsetter](https://subset.larc.nasa.gov/calipso/) | NASA open data. Free NASA Earthdata Login for download |
| CALIOP L2 5 km Aerosol Layer, V5.00 | Layer top and base, subtype, layer optical depth | As above | [DOI 10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmALay-Standard-V5-00](https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmALay-Standard-V5-00) | As above |
| CALIOP L2 5 km Aerosol Profile, V4.51 (sensitivity) | Same variables | As above | [DOI 10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V4-51](https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V4-51) | As above |
| ERA5 hourly, pressure levels | Temperature, specific and relative humidity, geopotential, winds | 0.25°, hourly, 37 levels | [DOI 10.24381/cds.bd0915c6](https://doi.org/10.24381/cds.bd0915c6) | CC-BY. Free CDS account |
| ERA5 hourly, single levels | Boundary-layer height | 0.25°, hourly | [DOI 10.24381/cds.adbb2d47](https://doi.org/10.24381/cds.adbb2d47) | CC-BY. Free CDS account |
| ERA5 on model levels (refinement) | Humidity and temperature | 0.25°, hourly, 137 levels | [CDS page](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-complete) | Free CDS account, request limits apply |
| FIRMS active fires (MODIS C6.1, VIIRS 375 m) | Location, time, confidence, fire radiative power | 1 km and 375 m | [FIRMS download](https://firms.modaps.eosdis.nasa.gov/download/) | NASA open data. Free MAP_KEY for the API |
| AERONET Version 3, Level 2.0 (Level 1.5 as fallback) | AOD, Ångström exponent, inversion size distribution, refractive index, SSA | Kanpur and Gandhi_College have Level 2.0 AOD in every year 2006 to 2023. Jaipur has 2009 to 2018 and 2020 to 2023 (none in 2019) | [AERONET](https://aeronet.gsfc.nasa.gov/); [site list](https://aeronet.gsfc.nasa.gov/aeronet_locations_v3.txt); [usage policy](https://aeronet.gsfc.nasa.gov/new_web/data_usage.html) | No registration. Citation policy applies |
| HYSPLIT with GDAS1 | 120 h back trajectories | 3-hourly, 0.5° or 1° | [HYSPLIT](https://www.ready.noaa.gov/HYSPLIT.php); [GDAS1](https://www.ready.noaa.gov/gdas1.php) | Public |
| FLEXPART 10.4 (sensitivity) | Source-receptor footprints | User-defined | [Source code](https://github.com/flexpart/flexpart) | Open source. ERA5 input needs the CDS account |
| MERRA-2 aerosol diagnostics | Organic and black carbon, sulphate, dust, sea salt | 0.5° × 0.625°, 3-hourly | [M2I3NVAER](https://disc.gsfc.nasa.gov/datasets/M2I3NVAER_5.12.4/summary); [M2T1NXAER](https://disc.gsfc.nasa.gov/datasets/M2T1NXAER_5.12.4/summary) | Free Earthdata Login |
| CAMS global reanalysis (EAC4) | Organic matter, black carbon, sulphate, dust, sea salt | 0.75°, 3-hourly | [DOI 10.24381/d58bbf47](https://doi.org/10.24381/d58bbf47) | CC-BY. Free ADS account |
| Radiosonde profiles for RH checks | Temperature, humidity | Station launches | [University of Wyoming archive](https://weather.uwyo.edu/upperair/sounding.shtml) | No registration observed. Terms of use to be confirmed |
| SWAAMI-RAWEX aircraft CCN and CN profiles | CCN, CN, activation ratio, 2016 | Flights over the IGP | Manoj et al. (2021) data on [figshare](https://doi.org/10.6084/m9.figshare.14744046) (CC BY 4.0 per DataCite) | Public. The Jayachandran et al. (2020a) data are available only on request to the authors |
| EarthCARE ATLID L2A (extension) | `ATL_EBD_2A`, `ATL_AER_2A` | 2024 onwards | [ESA EarthCARE data](https://earth.esa.int/eogateway/missions/earthcare/data) | Open. Free ESA EO Sign In. Launch 28 May 2024 |

## Access notes

NASA ASDC is the primary route to CALIOP data. The ICARE centre in Lille also distributes CALIPSO products and has a login and registration system, but its web authentication was announced as unavailable on 16 November 2026 because of a security problem, so ICARE is not relied on.

The CAIPEEX ground and aircraft data are held by the Indian Institute of Tropical Meteorology and are obtained through a registration form (Jayachandran et al., 2020b). The form page returned an HTTP 500 error on 16 November 2026, so these data are listed as available on request and are not required for any primary result.

The Delhi hygroscopicity data of Arub et al. (2020) are stated in that paper to be available as a spreadsheet on the authors' institute web server. The file link returned an HTTP 500 error on 16 November 2026, and the data are used only for context.

The aircraft CCN data of Jayachandran et al. (2020a) are available only on request, and no result depends on them.

## Accounts

| Archive | Account | Used for |
| --- | --- | --- |
| NASA Earthdata Login | Free | CALIOP, MERRA-2, FIRMS API (`MAP_KEY`) |
| Copernicus CDS | Free | ERA5 |
| Copernicus ADS | Free | CAMS EAC4 |
| ESA EO Sign In | Free | EarthCARE ATLID (extension only) |

Dataset and software versions used in a given run will be recorded in this repository when the analysis begins.
