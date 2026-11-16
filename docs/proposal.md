# Does the hygroscopicity of biomass-burning aerosol over India change with altitude? A constraint from CALIOP and ERA5 humidograms, 2006 to 2023

**Author:** Shyam Sunder Murugesan Sellammal, National Institute of Technology Rourkela, India (ORCID [0000-0002-9964-6199](https://orcid.org/0000-0002-9964-6199))

**Target journal:** *Atmospheric Chemistry and Physics* (ACP), research article

**Document status:** research proposal and analysis plan, version 2.0, 16 November 2026. No results are reported. Every numerical threshold is labelled either as taken from a cited source (P) or as a design choice (D) that a pilot phase will test and freeze before the main analysis.

---

## Abstract

Aerosol hygroscopicity controls how efficiently particles activate as cloud condensation nuclei (CCN), but its vertical structure over South Asia has not been constrained by observation, and existing CALIOP-based CCN estimates assume a fixed hygroscopicity parameter. This proposal sets out a pre-specified analysis of the final CALIOP version 5.00 level 2 aerosol record (June 2006 to June 2023) over India. Layers are co-located with ERA5 humidity and screened for well-mixed conditions with published criteria. Smoke is identified by independent fire exposure from active-fire detections and HYSPLIT back trajectories, because the CALIOP elevated-smoke subtype is itself assigned by altitude. The Hänel exponent γ is fitted to the backscatter increase with relative humidity inside each layer, converted to a lidar-effective hygroscopicity κ_L with a Mie model constrained by AERONET inversions, and propagated to critical dry diameter. A mixed-effects model tests three hypotheses: γ differs between the boundary layer and the free troposphere by at least 0.15; this shifts the critical diameter at 0.3 % supersaturation by at least 10 %; and the difference varies among post-monsoon, pre-monsoon and winter regimes. Equivalence tests and power calculations make a null result informative. Because no direct measurement of smoke hygroscopicity aloft over India was found, free-tropospheric values are treated as constrained inferences and checked against reanalysis composition, surface κ and aircraft CCN profiles. All inputs are public, and code and catalogues will be archived with a DOI.

**Keywords:** aerosol hygroscopicity, biomass burning, CALIOP, ERA5, κ-Köhler theory, cloud condensation nuclei, India

---

## 1 Introduction

Water uptake changes the size, refractive index and scattering efficiency of ambient particles, and it sets the supersaturation at which a particle activates into a cloud droplet. The κ-Köhler framework condenses these properties into a single hygroscopicity parameter κ, which lies near zero for insoluble material and can exceed 1 for inorganic salts (Petters and Kreidenweis, 2007). Fresh biomass-burning organic aerosol sits at the low end of this range. Laboratory and field studies indicate that atmospheric ageing raises κ as the organic fraction oxidises (Petters et al., 2009; Engelhart et al., 2012; Jimenez et al., 2009).

South Asia is one of the largest regional sources of smoke. Post-monsoon burning of rice residue in north-western India fills the Indo-Gangetic Plain (IGP) with plumes every October and November (Jethva et al., 2018, 2019; Singh et al., 2018), and forest and agricultural fires follow in the pre-monsoon months. Surface studies report κ of about 0.3 in New Delhi for all sampled air masses (Arub et al., 2020), seasonal means between 0.11 and 0.24 at Kanpur (Bhattu and Tripathi, 2014), and wintertime growth factors at 85 % relative humidity (RH) of 1.27 ± 0.06 for 100 nm particles at Kanpur (Mandariya et al., 2020). These values describe air near the ground. They do not say whether smoke lofted above the boundary layer, where it meets clouds, has the same hygroscopicity.

Active remote sensing can address the vertical dimension. In well-mixed layers the increase of lidar backscatter with RH yields a hygroscopic growth parameter (Feingold and Morley, 2003; Granados-Muñoz et al., 2015; Navas-Guzmán et al., 2019; Sicard et al., 2022). The HYGRO19 campaign at Payerne, Switzerland (June to December 2019) analysed 227 layers and found no dependence of γ on altitude (Kruskal-Wallis p = 0.98), with γ_β at 355 nm of 0.70 ± 0.16 below and 0.72 ± 0.20 above 1.5 km above ground level (Díaz-Zurita et al., 2026). A Raman lidar study of anthropogenic aerosol over Wuhan reported 0.63 ± 0.25 in the boundary layer and 0.60 ± 0.24 in the free troposphere (Jing et al., 2026). Smoke has received much less attention. A single smoke layer observed with a Mie-Raman-fluorescence lidar gave γ = 0.5 ± 0.3 at 532 nm (Miri et al., 2024), whereas aged Canadian wildfire smoke showed almost no backscatter growth at RH between 90 % and 100 % (Hu et al., 2026). These results differ, so the hygroscopicity of smoke cannot simply be assumed.

Spaceborne lidar is the only instrument that samples smoke layers across the whole Indian domain over many years. It has already been used to estimate CCN concentrations, but with a prescribed κ (Georgoulias et al., 2020; Choudhury and Tesche, 2022). The present proposal asks whether the humidity response contained in the same CALIOP profiles can instead be used to constrain κ and its altitude dependence.

## 2 Knowledge gap and closest prior work

The studies most relevant to this proposal are summarised in Table 1. They were identified by searching Crossref and the open web on 16 November 2026 for combinations of lidar, CALIOP, humidity, hygroscopic growth, smoke, CCN and India. A search of Web of Science and Scopus will be added before submission, and the search terms will be listed in the supplement.

**Table 1.** Closest prior work and what it leaves open.

| Study | Platform and region | What was done | What it does not do |
|---|---|---|---|
| Choudhury and Tesche (2022) | CALIOP V4.20 profiles with MERRA-2 RH | CCN estimated from backscatter with assumed κ of 0.3 (continental) and 0.7 (marine), uncertainty factor of 2 to 3 | Does not retrieve κ from the humidity response of the backscatter |
| Georgoulias et al. (2020) | CALIOP, single case study | First spaceborne CCN case study with the POLIPHON method | No humidogram, κ taken from the method |
| Prasad et al. (2023) | CALIPSO extinction and RH, India | Shows that RH drives aerosol extinction and its vertical distribution over India. The abstract mentions humidity-dependent growth factors | Appears to work with climatological relations by aerosol type, not with individually selected well-mixed layers, and has no fire attribution or κ. The full text was not available to me and must be checked before submission |
| Kallihosur et al. (2024) | MODIS AOD, CALIOP-weighted column RH, MERRA-2 composition, eastern IGP in winter | Column-integrated extinction enhancement (about 1.8) from assumed species growth functions | Growth is assumed from composition, not observed. No altitude resolution |
| Nair et al. (2020) | RegCM4 model, South Asia | Water vapour-aerosol amplification of haze. As summarised by Kallihosur et al. (2024), the hygroscopic effect is weak between 1 and 3 km and negligible above 3 km | Model result, not an observation. Gives a testable expectation for H1 |
| Miri et al. (2024); Hu et al. (2026) | Ground lidar, Lille and the 2023 Canadian smoke | Smoke γ of 0.5 ± 0.3 in one case. Near-absence of growth in aged smoke | Few cases, mid-latitude smoke only |
| Díaz-Zurita et al. (2026); Jing et al. (2026) | Ground Raman lidar, Payerne and Wuhan | Layer-wise γ with no altitude dependence | Not smoke-specific, no India data |

Three deficits follow. First, I found no published retrieval of γ or κ from within-layer CALIOP humidograms of individually selected well-mixed layers, and no test of altitude dependence of smoke hygroscopicity over India. Prasad et al. (2023) may derive growth factors from CALIPSO extinction as a function of RH over India, so this gap is stated for layer-wise retrievals and not for any use of CALIOP humidity dependence. Second, the CALIOP "smoke" label cannot be used to define the sample. In version 4 and version 5, elevated smoke is assigned to non-depolarising layers whose tops lie more than 2.5 km above ground level, while within the boundary layer the same optical signature is called polluted continental/smoke, and both subtypes share a lidar ratio of 70 sr at 532 nm (Kim et al., 2018; NASA/LARC/SD/ASDC, 2026). An altitude analysis based on the label would therefore be circular. Third, the step from a lidar humidity response to a CCN-relevant quantity has not been propagated with uncertainty for Indian smoke.

## 3 Novelty and contribution

**What is not new.** The Hänel parameterisation and its use with Raman lidar are established (Hänel, 1976; Feingold and Morley, 2003; Navas-Guzmán et al., 2019). The coupling of CALIOP backscatter or extinction with reanalysis RH has been done regionally, including over India (He et al., 2025; Prasad et al., 2023; Kallihosur et al., 2024), and CCN estimation from CALIOP exists (Georgoulias et al., 2020; Choudhury and Tesche, 2022). This proposal does not claim any of these.

**What is new, to my knowledge and after the search described in Section 2.** The analysis would be the first to do the following together:

1. retrieve γ and a lidar-effective κ_L from within-layer CALIOP humidograms of individually selected, well-mixed layers, instead of using climatological extinction-RH relations or an assumed κ;
2. apply this to smoke over India, with smoke defined by independent fire exposure and not by the altitude-dependent CALIOP subtype;
3. test altitude dependence with pre-stated hypotheses, an equivalence margin and a power calculation, so that agreement with HYGRO19 or with Nair et al. (2020) can be reported as a result;
4. propagate backscatter noise, reanalysis RH error, size distribution and refractive-index uncertainty to critical dry diameter and activated fraction.

**Intended contribution.** The outcome is an open, versioned workflow and a quantitative test of whether altitude must be treated as a control on smoke hygroscopicity in models of aerosol-cloud interaction over South Asia. The result would also test the fixed-κ assumption used in current CALIOP CCN products.

## 4 Objectives and research questions

**Primary question.** Do Indian biomass-burning smoke layers show altitude-dependent hygroscopicity, and does any such dependence change CCN activation potential between the boundary layer (BL) and the free troposphere (FT)?

- **O1.** Build a quality-controlled catalogue of well-mixed, non-dust CALIOP aerosol layers over India with co-located ERA5 humidity.
- **O2.** Retrieve γ and κ_L for each layer with propagated uncertainty.
- **O3.** Quantify the dependence of γ and κ_L on altitude after controlling for smoke age, source region, season and RH range.
- **O4.** Convert κ_L to critical dry diameter and activated fraction at supersaturations of 0.1 % to 0.5 % and compare BL with FT.
- **O5.** Evaluate the retrievals against independent information, which is limited in the FT and is described as a constrained inference in Section 9.

## 5 Hypotheses

The effect sizes below are design choices anchored on the spreads reported by HYGRO19 (γ_β of 0.70 ± 0.18, where "±" is half the interquartile range) and by the Wuhan study (0.62 ± 0.24, standard deviation). They size the tests and will be revisited after the pilot. Both come from other regions and wavelengths.

| ID | Null hypothesis (H0) | Alternative (H1) | Test |
|---|---|---|---|
| **H1** Altitude dependence | Δγ = γ_FT − γ_BL = 0 | \|Δγ\| ≥ 0.15 after adjustment for smoke age, source region, season and RH range (D) | Altitude coefficient in a mixed-effects model, two-sided, α = 0.05. Equivalence by two one-sided tests (TOST) against a ±0.10 margin (D) |
| **H2** CCN implication | Critical dry diameter D_c at 0.3 % supersaturation is unchanged: \|ΔD_c / D_c\| < 5 % | \|ΔD_c / D_c\| ≥ 10 % (D), equal to a κ_L ratio FT/BL of at least 1.37 or at most 0.75, because D_c scales as κ^(−1/3) | Bootstrapped D_c difference with a shared size distribution, repeated at 0.1, 0.2, 0.4 and 0.5 % |
| **H3** Seasonal modulation | Altitude × season interaction is zero | Interaction is non-zero, largest in the post-monsoon regime (October to November) | Likelihood-ratio test of the interaction, then regime contrasts under a 5 % false discovery rate (Benjamini and Hochberg, 1995) |

The 10 % margin in H2 is a design choice. The pilot will replace it with the smallest D_c shift that changes the activated fraction by more than the propagated size-distribution uncertainty. The model result of Nair et al. (2020), a weaker hygroscopic effect aloft, gives H1 a predicted sign (γ_FT < γ_BL), whereas the ageing argument of Section 1 predicts the opposite. The regression residual after the smoke-age term is the quantity of interest.

**Falsification logic.** H1 is not supported if the 95 % cluster-bootstrap interval of Δγ lies inside the equivalence margin. A supported H1 combined with an unsupported H2 would mean the altitude effect is real but too small to matter for activation. H3 cannot be supported unless H1 or its regime-specific contrasts are.

**Power and sample size.** The HYGRO19 half-interquartile ranges of 0.16 to 0.20 correspond to standard deviations of about 0.24 to 0.30 if the distribution is close to normal. The calculation uses the larger value, σ = 0.30. For a two-sided test with α = 0.05 and power 0.80, n = 2(z_α/2 + z_β)² σ² / Δ² gives 63 independent layers per group for Δ = 0.15. A design effect of 2 for clustering within overpasses raises this to about 125 per group. The minimum detectable difference is 2.80 σ √(2/n), which is 0.15 for 60 layers per group and 0.11 for 120. An equivalence test with a ±0.10 margin needs about 154 independent layers per group, or about 310 with the design effect. If the pilot finds fewer, the margin will be widened to ±0.15, which needs about 70 and 140 respectively. The margin and its reason will be written into the frozen protocol.

## 6 Study domain and period

The domain spans 5°N to 37°N and 67°E to 98°E, restricted to land and coastal cells over India. Four sub-regions are analysed separately:

- the north-western IGP (Punjab, Haryana and western Uttar Pradesh), the post-monsoon crop-residue source and its downwind plume;
- the central and eastern IGP (eastern Uttar Pradesh and Bihar), where the AERONET sites Kanpur and Gandhi_College are located;
- central and north-east India, the pre-monsoon forest-fire region;
- peninsular India, a contrast region with fewer smoke events.

The CALIOP version 5.00 record, the final release, covers mid-June 2006 to 30 June 2023 (NASA/LARC/SD/ASDC, 2026). NASA announced the official end of the science mission as 1 August 2023 (NASA Earthdata, 2023), whereas the mission final report states that the science phase ended in June 2023 (Trepte, 2026). The analysis uses the data period of the product, which ends on 30 June 2023.

The satellite flew in the A-Train afternoon orbit, with nominal local overpass times near 13:30 on the ascending node and near 01:30 on the descending node (Winker et al., 2009). In September 2018 the orbit was lowered from 705 to 688 km to join the C-Train, and after the manoeuvre the local crossing time drifted towards later hours because propellant was depleted (Trepte, 2026). Local solar time is therefore read from the metadata of each granule and is never assumed. Three regimes are defined: post-monsoon (October to November), pre-monsoon (March to May) and winter (December to February). The monsoon (June to September) is excluded from the main analysis because of frequent cloud, and it is examined as a sensitivity case.

## 7 Data

All inputs are public. Several archives require a free account, which is stated in the table. Links were opened on 16 November 2026 and returned an accessible page unless noted. No restricted data are used.

| Dataset | Variables used | Resolution and period | Access | Licence and registration |
|---|---|---|---|---|
| CALIOP L2 5 km Aerosol Profile, **V5.00 (primary)** | `Total_Backscatter_Coefficient_532` and its uncertainty, `Particulate_Depolarization_Ratio_Profile_532`, `Extinction_Coefficient_532`, `Extinction_QC_Flag_532`, `CAD_Score`, `Atmospheric_Volume_Description`, `Relative_Humidity` (MERRA-2), `Temperature`, `Pressure`, `DEM_Surface_Elevation`, `Day_Night_Flag`, `Minimum_Laser_Energy_532`, `Low_Energy_Mitigation_Column_QC_Flag` | 5 km along track, 60 m vertical, June 2006 to June 2023 | [DOI 10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V5-00](https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V5-00); [Subsetter](https://subset.larc.nasa.gov/calipso/) | NASA open data. **Free NASA Earthdata Login** for download |
| CALIOP L2 5 km Aerosol Layer, V5.00 | Layer top and base, subtype, layer optical depth | As above | [DOI 10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmALay-Standard-V5-00](https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmALay-Standard-V5-00) | As above |
| CALIOP L2 5 km Aerosol Profile, V4.51 (sensitivity) | Same variables | As above | [DOI 10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V4-51](https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V4-51) | As above |
| ERA5 hourly, pressure levels | Temperature, specific and relative humidity, geopotential, winds | 0.25°, hourly, 37 levels | [DOI 10.24381/cds.bd0915c6](https://doi.org/10.24381/cds.bd0915c6) | CC-BY. **Free CDS account** |
| ERA5 hourly, single levels | Boundary-layer height | 0.25°, hourly | [DOI 10.24381/cds.adbb2d47](https://doi.org/10.24381/cds.adbb2d47) | CC-BY. **Free CDS account** |
| ERA5 on model levels (refinement) | Humidity and temperature | 0.25°, hourly, 137 levels | [CDS page](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-complete) | **Free CDS account**, request limits apply |
| FIRMS active fires (MODIS C6.1, VIIRS 375 m) | Location, time, confidence, fire radiative power | 1 km and 375 m | [FIRMS download](https://firms.modaps.eosdis.nasa.gov/download/) | NASA open data. **Free MAP_KEY** for the API |
| AERONET Version 3, Level 2.0 (Level 1.5 as fallback) | AOD, Ångström exponent, inversion size distribution, refractive index, SSA | Kanpur and Gandhi_College have Level 2.0 AOD in every year 2006 to 2023. Jaipur has 2009 to 2018 and 2020 to 2023 (none in 2019) | [AERONET](https://aeronet.gsfc.nasa.gov/); [site list](https://aeronet.gsfc.nasa.gov/aeronet_locations_v3.txt); [usage policy](https://aeronet.gsfc.nasa.gov/new_web/data_usage.html) | No registration. Citation policy applies |
| HYSPLIT with GDAS1 | 120 h back trajectories | 3-hourly, 0.5° or 1° | [HYSPLIT](https://www.ready.noaa.gov/HYSPLIT.php); [GDAS1](https://www.ready.noaa.gov/gdas1.php) | Public |
| FLEXPART 10.4 (sensitivity) | Source-receptor footprints | User-defined | [Source code](https://github.com/flexpart/flexpart) | Open source. ERA5 input needs the CDS account |
| MERRA-2 aerosol diagnostics | Organic and black carbon, sulphate, dust, sea salt | 0.5° × 0.625°, 3-hourly | [M2I3NVAER](https://disc.gsfc.nasa.gov/datasets/M2I3NVAER_5.12.4/summary); [M2T1NXAER](https://disc.gsfc.nasa.gov/datasets/M2T1NXAER_5.12.4/summary) | **Free Earthdata Login** |
| CAMS global reanalysis (EAC4) | Organic matter, black carbon, sulphate, dust, sea salt | 0.75°, 3-hourly | [DOI 10.24381/d58bbf47](https://doi.org/10.24381/d58bbf47) | CC-BY. **Free ADS account** |
| Radiosonde profiles for RH checks | Temperature, humidity | Station launches | [University of Wyoming archive](https://weather.uwyo.edu/upperair/sounding.shtml) | No registration observed. Terms of use to be confirmed |
| SWAAMI-RAWEX aircraft CCN and CN profiles | CCN, CN, activation ratio, 2016 | Flights over the IGP | Manoj et al. (2021) data on [figshare](https://doi.org/10.6084/m9.figshare.14744046) (CC BY 4.0 per DataCite) | Public. The Jayachandran et al. (2020a) data are available only on request to the authors |
| EarthCARE ATLID L2A (extension) | `ATL_EBD_2A`, `ATL_AER_2A` | 2024 onwards | [ESA EarthCARE data](https://earth.esa.int/eogateway/missions/earthcare/data) | Open. **Free ESA EO Sign In**. Launch 28 May 2024 |

**Notes on access.** NASA ASDC is the primary route to CALIOP data. The ICARE centre in Lille also distributes CALIPSO products and has a login and registration system, but its web authentication was announced as unavailable on 16 November 2026 because of a security problem, so ICARE is not relied on. The CAIPEEX ground and aircraft data are held by the Indian Institute of Tropical Meteorology and are obtained through a registration form (Jayachandran et al., 2020b). The form page returned an HTTP 500 error on 16 November 2026, so these data are listed as available on request and are not required for any primary result. The Delhi hygroscopicity data of Arub et al. (2020) are stated in that paper to be available as a spreadsheet on the authors' institute web server. The file link returned an HTTP 500 error on 16 November 2026, and the data are used only for context.

## 8 Methods

### 8.1 Physical basis

For a particle of dry diameter D_d, the κ-Köhler growth factor at relative humidity RH, with the Kelvin term neglected at accumulation-mode sizes, is GF = (1 + κ RH / (1 − RH))^(1/3) (Petters and Kreidenweis, 2007). The 532 nm backscatter coefficient rises with RH because particles grow and their refractive index moves towards that of water. In a well-mixed layer the rise is described by the Hänel relation

β(RH) / β(RH_ref) = [(1 − RH) / (1 − RH_ref)]^(−γ),

where γ is the backscatter hygroscopic growth parameter and RH_ref is the lowest RH within the layer (Hänel, 1976; Navas-Guzmán et al., 2019; Díaz-Zurita et al., 2026). The quantity γ is observable. The conversion to κ_L depends on a model and is reported separately.

Backscatter is the primary variable. The CALIOP variable `Total_Backscatter_Coefficient_532` is the sum of the parallel and perpendicular particulate backscatter coefficients and is given in km⁻¹ sr⁻¹ (NASA/LARC/SD/ASDC, 2026). Values are converted to Mm⁻¹ sr⁻¹ (1 km⁻¹ = 1000 Mm⁻¹) to match the lidar literature. Extinction in the product is derived from backscatter through a subtype-dependent lidar ratio, so it adds no independent humidity information once the subtype is fixed (Young et al., 2018).

### 8.2 Layer selection and quality control

Layers are drawn from the 5 km aerosol profile and layer products (Winker et al., 2009). Table 2 gives every criterion with its basis.

**Table 2.** Selection criteria. P: taken from a cited source. D: design choice, to be tested and frozen by the pilot.

| # | Criterion | Value | Basis |
|---|---|---|---|
| 1 | Cloud-aerosol discrimination | `CAD_Score` between −100 and −20. Stricter range −100 to −70 as sensitivity | P: Tackett et al. (2018), Table 1. Sensitivity is D. CAD algorithm: Liu et al. (2019) |
| 2 | Extinction quality flag | `Extinction_QC_Flag_532` equal to 0 or 1 | P in part: Tackett et al. (2018) also keep 16 and 18. These are opaque-layer values, and the layer base is unconstrained, so they are dropped here (D) |
| 3 | Fill and special values | Extinction uncertainty of 99.9 km⁻¹ rejected. Backscatter flags −111, −333, −444 and fill −9999 rejected | P: Tackett et al. (2018); NASA/LARC/SD/ASDC (2026) |
| 4 | Surface proximity | Samples at or below 60 m above ground rejected | P: Tackett et al. (2018) |
| 5 | Cirrus fringe | Aerosol above 4 km above mean sea level in contact with ice cloud rejected | P: Tackett et al. (2018) |
| 6 | Low laser energy | Columns flagged in `Low_Energy_Mitigation_Column_QC_Flag` rejected | D. Flag semantics to be read from file metadata |
| 7 | Altitude | Layer below 7 km | P: Jing et al. (2026) |
| 8 | Thickness | At least 300 m, which is at least 5 bins | P: Jing et al. (2026) |
| 9 | Minimum backscatter | Non-dust backscatter above 0.5 Mm⁻¹ sr⁻¹ | P for ground lidar: Jing et al. (2026). Transfer to CALIOP noise is D |
| 10 | Bin uncertainty | Relative backscatter uncertainty at most 30 % | D. Bins noisier than this carry little weight in the fit. Pilot decides |
| 11 | Monotonic response | β increases with RH within the layer | P: Jing et al. (2026) |
| 12 | Well-mixed layer | Potential temperature range below 2 K and water vapour mixing ratio range below 2 g kg⁻¹ | P: Granados-Muñoz et al. (2015); Jing et al. (2026); Sicard et al. (2022) |
| 13 | Air-mass homogeneity | Wind speed range below 2 m s⁻¹ and wind direction range below 15° across the layer (ERA5). Back-trajectory origins at layer base and top compared | P: Jing et al. (2026) after Sicard et al. (2022). Trajectories: Díaz-Zurita et al. (2026) |
| 14 | Reference RH | Lowest RH in the layer, at least 40 %. Enhancement reported on a 40 to 85 % range | P for RH_ref definition and range: Díaz-Zurita et al. (2026). The 40 % floor is D |
| 15 | Maximum RH | Below 90 % | D. HYGRO19 reports growth up to 85 %, and reanalysis RH is least reliable near saturation |
| 16 | RH range | x = ln[(1 − RH_min)/(1 − RH_max)] at least 0.4, for example RH from 60 % to 73 % | D. Pilot recovery tests on synthetic profiles set the final value |
| 17 | Dust screening | Dust backscatter fraction f_d from the two-component depolarisation method, with particle depolarisation of 0.31 for dust and 0.05 for non-dust. Layer median f_d at most 0.2, which corresponds to a particle depolarisation near 0.09 | P: Tesche et al. (2009), as used by Choudhury and Tesche (2022). The 0.2 limit is D |
| 18 | Subtypes | Polluted continental/smoke and elevated smoke accepted. Polluted dust only in sensitivity. Marine, dust, dusty marine and clean continental rejected | P: subtype codes from NASA/LARC/SD/ASDC (2026). Use of the label is a filter only |
| 19 | Time of day | Night-time profiles for the primary analysis. Daytime as a separate stratum | D. Daytime solar noise raises CAD rejection (Tackett et al., 2018) and degrades depolarisation in weak layers by a factor of 2 to 4 (NASA/LARC/SD/ASDC, 2026) |
| 20 | Overlying optical depth | Optical depth above the layer base at most 1.0 | D. This keeps two-way transmission above 14 % |
| 21 | Fit quality | Coefficient of determination at least 0.5 | D. Results are also reported without this filter, because it can bias γ upwards |

Selection is never made on the sign or size of γ. Layers with negative or near-zero γ stay in the sample and are reported, as they carry information about aged or weakly hygroscopic smoke.

### 8.3 Co-location with ERA5 and a second humidity source

ERA5 temperature and humidity (Hersbach et al., 2020) are interpolated linearly in time to the overpass, bilinearly in the horizontal to the profile location, and in log-pressure to the CALIOP bins. The 37 pressure levels are coarse (25 hPa, roughly 250 m, in the lower troposphere), and the model-level product tests whether the criteria and γ change at finer vertical resolution. The CALIOP files carry a second humidity source, the MERRA-2 variable `Relative_Humidity`, stored as a fraction between 0 and 1.5 and averaged over 5 km (NASA/LARC/SD/ASDC, 2026). The difference between ERA5 and MERRA-2 RH is used as an empirical estimate of reanalysis uncertainty.

Published error values anchor the perturbation. Lidar RH differs from radiosondes by less than 4 % RH in bias and less than 10 % RH in standard deviation (Navas-Guzmán et al., 2019), and HYGRO19 reports a bias of −1 % RH with a standard deviation of 6 % RH. ERA5 differs from radiosondes by −0.63 % RH on average at Wuhan (He et al., 2026), and a dry bias growing above about 8.5 km has been documented (Alraddawi et al., 2025). The analysis therefore stays below 7 km (Table 2). RH errors are propagated as Gaussian perturbations with a standard deviation of 6 % RH (D, from HYGRO19). The pilot replaces this with an estimate from ERA5 and MERRA-2 comparisons with radiosondes at Indian stations.

### 8.4 Boundary-layer and free-troposphere assignment

Night-time CALIOP profiles sample the residual layer or a shallow nocturnal layer. The BL is therefore defined from the diurnal maximum of ERA5 boundary-layer height on the overpass day, following He et al. (2026). Layers whose centre lies below that height are classed BL. Layers whose base lies at least 300 m above it (D) are classed FT. Intermediate layers are excluded from the BL-FT contrast and kept in the continuous-altitude model. The CALIOP definition of elevated aerosol, a layer top above 2.5 km above ground level (Kim et al., 2018), serves as a sensitivity test. Ground elevation comes from `DEM_Surface_Elevation`.

### 8.5 Retrieval of γ and κ_L

For each layer, ln β(z) is regressed on −ln[(1 − RH(z)) / (1 − RH_ref)] by weighted least squares, with weights from the CALIOP backscatter uncertainty and the RH error. The slope is γ. A Monte Carlo ensemble of 1000 draws samples backscatter noise and RH error to give a distribution of γ for every layer.

The step from γ to κ_L uses a forward Mie model such as PyMieScatt or MOPSMAP. The dry population is a lognormal accumulation mode whose median diameter, width and complex refractive index come from AERONET Version 3 inversions near the layer (Dubovik and King, 2000; Sinyuk et al., 2020). Level 2.0 inversions require an AOD at 440 nm above 0.4, which limits coincident cases to hazy days, so Level 1.5 inversions and a regional seasonal median are used as fallbacks. Growth follows κ-Köhler theory over a grid of κ from 0.02 to 0.60 (D). The modelled backscatter enhancement is matched to the observed value to give κ_L. Size and refractive-index inputs are sampled in the same Monte Carlo ensemble, so κ_L is a distribution and not a point value.

Two caveats are stated with every result. First, κ_L is weighted by the optically dominant accumulation mode at 532 nm, whose size range differs from the sizes that set activation at 0.1 % to 0.5 % supersaturation. Second, hygroscopicity measured below water saturation need not equal that at activation for organic-rich aerosol.

A secondary approach normalises backscatter with CAMS or MERRA-2 smoke mass mixing ratios and fits a composite humidogram per stratum (Gelaro et al., 2017; Inness et al., 2019). It depends on model skill and is a sensitivity test only.

### 8.6 CCN calculation

For each layer and each κ_L draw, the critical dry diameter at supersaturation SS follows from κ-Köhler theory:

D_c = [4A³ / (27 κ ln²(1 + SS/100))]^(1/3), with A = 4σ_w M_w / (R T ρ_w) ≈ 2.1 nm at 298 K,

where σ_w, M_w and ρ_w are the surface tension, molar mass and density of water, R is the gas constant and T is temperature (Petters and Kreidenweis, 2007). The activated fraction is the part of a prescribed number size distribution above D_c. The primary analysis applies the same regional, seasonal AERONET-derived size distribution to BL and FT layers, so any difference arises from κ_L alone. The distribution is then perturbed (median diameter ±20 %, width ±0.1) to show the dependence of the conclusion on it. Supersaturations of 0.1, 0.2, 0.3, 0.4 and 0.5 % are used, and 0.4 % allows comparison with the activation efficiencies measured during SWAAMI-RAWEX (Jayachandran et al., 2020a).

As a scaling check, raising κ_L from 0.15 to 0.30 reduces D_c by a factor of 2^(−1/3) = 0.79, and raising it to 0.20 reduces D_c by a factor of 0.91.

### 8.7 Fire attribution and smoke age

Fire exposure is computed from 120 h HYSPLIT back trajectories started at the layer boundaries and centre, as in HYGRO19 and Navas-Guzmán et al. (2019), with an ensemble of start heights across the layer (Stein et al., 2015). FIRMS detections from MODIS Collection 6.1 and VIIRS 375 m, at nominal and high confidence, are counted within 0.25° of the trajectory when it lies below the ERA5 boundary-layer height (Giglio et al., 2016; Schroeder et al., 2014). The fire exposure index is the fire radiative power weighted by residence time. A layer is classed as smoke when the index exceeds a threshold set in the pilot (D), together with an AERONET Ångström exponent above 1.0 within one day where a site lies within 200 km (D).

Smoke age is the time from the last trajectory contact with an active fire to the overpass. Trajectory error grows with time, so ages are binned (below 24 h, 24 to 72 h, above 72 h) and reported with a range. FLEXPART footprints driven by ERA5 give a second attribution for a subset of seasons (Pisso et al., 2019). The source region is the sub-region of Section 6 with the highest fire exposure.

### 8.8 Statistical design

**Pilot.** Two post-monsoon and two pre-monsoon seasons are processed first. The pilot counts layers that pass each step of Table 2, estimates σ for γ, tests parameter recovery on synthetic profiles with known κ and noise, and fixes every design choice. The values are then recorded, time-stamped, in the repository before the main analysis.

**Primary model.** For layer i in overpass j and sub-region r,

γ_ij = β0 + β_z z_ij + β_a age_ij + β_s season_ij + β_RH ΔRH_ij + β_f FEI_ij + u_r + v_j + ε_ij,

where z is the standardised layer height above ground, ΔRH is the RH range, FEI is the fire exposure index, and u_r and v_j are random intercepts (Bates et al., 2015). The same model is applied to κ_L, and to the BL/FT indicator in place of z. HYGRO19 used Kruskal-Wallis and Mann-Whitney tests, so the same tests are run in parallel for comparability.

**Interaction and equivalence.** H3 is tested by adding the altitude × season term. Equivalence for H1 uses two one-sided tests against the margin set in Section 5 (Lakens, 2017).

**Uncertainty and multiplicity.** Intervals come from a cluster bootstrap by overpass day with 5000 resamples. H1 and H2 are primary and are not adjusted. Regime and sub-region contrasts under H3 use the Benjamini-Hochberg procedure at 5 %. Effect sizes are reported as Δγ and Δκ_L with intervals.

**Sensitivity tests.** The analysis is repeated while varying each design choice in Table 2, the BL definition, the humidity source, the size distribution, the inclusion of daytime layers and the monsoon season, the fire-attribution method and the CALIOP version (V5.00 against V4.51). Heavy-tailed residuals are handled with a Student-t model and quantile regression. Collinearity of altitude and smoke age is checked with variance inflation factors, and a mediation analysis estimates how much of any altitude effect passes through age.

## 9 Validation and constrained inference

**9.1 Retrieval method.** The γ fit is first tested on synthetic profiles with known κ, noise and RH error, which gives its bias and spread. ERA5 and the MERRA-2 field in the CALIOP files are compared with each other and with radiosondes at Indian stations.

**9.2 What cannot be validated directly.** Vertically resolved CCN profiles over the IGP exist from the SWAAMI-RAWEX aircraft campaign in 2016 (Jayachandran et al., 2020a; Manoj et al., 2021). I did not find a vertically resolved measurement of κ or hygroscopic growth for smoke over India, and I found no Indian lidar study of humidograms in the literature checked. The FT value of κ_L is therefore a constrained inference and not a validated measurement. The abstract, results and conclusions will say so.

**9.3 Consistency checks.** The inference is constrained by four independent checks, each with a pass criterion stated before the main analysis:

1. *Composition closure.* A composition-based κ is built for each layer from MERRA-2 and CAMS species mass fractions and literature κ values for each species. Agreement within the combined uncertainty is expected if κ_L is meaningful. A systematic offset that depends on altitude is treated as a retrieval artefact until shown otherwise.
2. *Surface and column anchors.* BL results are compared with surface κ and growth factors at Kanpur (Bhattu and Tripathi, 2014, 2015; Mandariya et al., 2020), Delhi (Arub et al., 2020) and Solapur (Jayachandran et al., 2020b). AERONET inversions supply fine-mode fraction and Ångström exponent for type consistency. They are inputs and type checks, not a validation of κ.
3. *Aircraft CCN profiles.* SWAAMI-RAWEX reported higher activation efficiency above the BL than below it in the pre-monsoon (Jayachandran et al., 2020a), and Manoj et al. (2021) give altitude profiles for the pre-monsoon and monsoon periods. The number of CALIOP overpasses that coincide with flights will be tabulated. The sign of the modelled FT-minus-BL activated fraction is compared with the measured activation ratio, which tests direction and order of magnitude only, because activation efficiency also depends on size.
4. *Cross-method and model context.* The γ values are compared with ground-lidar values for smoke and other aerosol (Miri et al., 2024; Hu et al., 2026; Díaz-Zurita et al., 2026; Jing et al., 2026), and the FT-BL contrast is compared with the model expectation of Nair et al. (2020).

## 10 Expected results and implications

The analysis should yield a catalogue of well-mixed smoke layers with γ and κ_L distributions by season and sub-region, and a quantified altitude effect with an interval. Three outcomes are possible. If the effect is absent within the equivalence margin, the HYGRO19 finding extends to Indian smoke, and an altitude-independent κ could be used in regional models with a stated error. If the FT is more hygroscopic than the BL by more than the pre-stated margin, ageing during lofting matters for CCN, and models using a fixed κ for smoke would underestimate FT activation. If the FT is less hygroscopic, the result would agree with the model expectation of Nair et al. (2020) and would point to less-aged or differently sourced smoke aloft.

The study also gives an uncertainty budget for lidar-derived hygroscopicity from space. This helps to judge whether the EarthCARE ATLID can reduce the main error sources, since it measures at 355 nm with a high-spectral-resolution receiver and gives extinction and backscatter without an assumed lidar ratio (Illingworth et al., 2015; Wehr et al., 2023; Donovan et al., 2024). A feasibility test with ATLID data is proposed as an extension.

## 11 Risks and mitigation

| Risk | Consequence | Mitigation |
|---|---|---|
| Too few layers pass QC, especially in the FT at night. Elevated aerosol layers over India at 4 to 6 km are dominated by dust and polluted dust (Kumar et al., 2023) | Low power for H1 and H3 | Count layers in the pilot. Pool regions. Relax design choices only within pre-set limits. Widen the equivalence margin to ±0.15. Report H3 as exploratory |
| CALIOP backscatter noise at 5 km resolution | Large uncertainty in γ | Monte Carlo propagation. Test 15 km averaging. Prefer night-time |
| Humidity rises with height inside a well-mixed layer, while attenuation lowers the signal-to-noise ratio towards the base | Gradient in γ caused by the fit and not by the aerosol | Check the correlation of γ with layer optical depth. Require homogeneity (criteria 12 and 13). Use synthetic tests |
| Backscatter in the product depends on an assumed lidar ratio, which itself may change with RH | Bias in γ | Use only extinction flags 0 and 1. Compare V5.00 with V4.51 |
| Reanalysis RH error aloft or near saturation | Biased γ | Limit to below 7 km and RH below 90 %. Compare ERA5 with MERRA-2 and radiosondes. Perturbation ensemble |
| Subtype circularity | Altitude confounded with aerosol class | Independent fire attribution. Subtype used as a filter only |
| Dust or cloud contamination, mostly March to June and in the monsoon | False hygroscopic signal | Dust fraction screen, CAD filter, cirrus-fringe filter, monsoon exclusion |
| Smoke-age uncertainty | Weakened covariate | Binned ages, FLEXPART comparison, mediation analysis |
| κ_L differs from the κ that matters for CCN | Biased CCN step | State as an assumption. Size-distribution sensitivity. Compare with surface CCN-derived κ |
| No direct in situ validation aloft | FT result is an inference | Section 9. Explicit statement in all outputs |
| Change in CALIOP version | Results shift | V5.00 is final. Record versions. V4.51 as a sensitivity case |

## 12 Timeline

A 15-month plan is proposed (M is the month from project start).

| Task | M1-3 | M4-6 | M7-9 | M10-12 | M13-15 |
|---|---|---|---|---|---|
| Literature search update and repository set-up | ■ | | | | |
| Data download and ERA5 co-location | ■ | ■ | | | |
| Pilot, feasibility and design-choice freeze | | ■ | | | |
| Layer catalogue and γ retrieval | | ■ | ■ | | |
| Fire attribution (HYSPLIT, FLEXPART) | | ■ | ■ | | |
| Mie look-up, κ_L and CCN step | | | ■ | ■ | |
| Statistical models and sensitivity tests | | | | ■ | ■ |
| Consistency checks (Section 9) | | | | ■ | |
| EarthCARE ATLID feasibility test | | | | | ■ |
| Manuscript, archive and submission | | | | | ■ |

## 13 Data and code availability

All data used are public and are listed in Section 7 with their access routes, licences and registration requirements. CALIOP, MERRA-2, FIRMS and AERONET data are distributed by NASA, ERA5 and CAMS data by Copernicus, and EarthCARE data by ESA. Some archives need a free account. The aircraft CCN data of Jayachandran et al. (2020a) and the CAIPEEX data are available only on request, and no result depends on them. The analysis code, configuration files, the layer catalogue and the derived γ, κ_L and CCN tables will be archived in a public repository with a DOI (Zenodo is planned) and mirrored on GitHub, in line with the data policy of Copernicus Publications (Copernicus Publications, 2026). The data availability statement will be placed as the last paragraph of the article before the acknowledgements, as that policy requires. The version of every dataset and software package is recorded in the repository. The CALIOP data sets are cited as NASA/LARC/SD/ASDC (2025a, 2025b, 2023).

## 14 Author contributions

*Placeholder to be completed with CRediT roles (conceptualisation, methodology, software, formal analysis, writing, supervision). Co-authors and supervisors are to be confirmed by the author.*

**Competing interests:** none declared at this stage.

## 15 Suggested GitHub repository structure

```
hygroscopicity-india-caliop-era5/
├── README.md                 Summary, install, quick start, citation
├── LICENSE                   Code licence (MIT or Apache-2.0, to be chosen)
├── CITATION.cff              Citation metadata, ORCID, archive DOI after release
├── environment.yml           Pinned conda environment (python, xarray, pyhdf, scipy, statsmodels)
├── docs/
│   ├── proposal.md           This document
│   ├── protocol.md           Frozen design choices and analysis plan (time-stamped after pilot)
│   └── data_sources.md       Dataset list, versions, access dates, registration notes
├── configs/
│   ├── qc_thresholds.yaml    Table 2 criteria, each tagged P (published) or D (design)
│   ├── regions.yaml          Sub-region boxes and seasons
│   └── hysplit.yaml          Trajectory settings
├── data/
│   ├── README.md             How to download each dataset (no raw data committed)
│   ├── raw/                  Git-ignored downloads
│   └── derived/              Layer catalogue and gamma/kappa tables (small files or archive)
├── src/hygro_india/
│   ├── io/                   CALIOP, ERA5, FIRMS and AERONET readers
│   ├── colocate.py           Time and space interpolation
│   ├── qc.py                 Layer selection and well-mixed tests
│   ├── dust_fraction.py      Two-component depolarisation separation
│   ├── humidogram.py         Hänel fit with Monte Carlo errors
│   ├── mie_kappa.py          Mie look-up and kappa_L retrieval
│   ├── ccn.py                Critical diameter and activated fraction
│   ├── attribution.py        Fire exposure and smoke age
│   ├── closure.py            Composition closure and aircraft-profile checks
│   └── stats.py              Mixed models, bootstrap, TOST, FDR
├── workflows/                Snakemake or Makefile pipeline from download to figures
├── notebooks/                Pilot, synthetic tests, figure drafts
├── tests/                    Unit tests and synthetic-profile recovery tests
├── results/                  Tables and figures produced by the workflow
└── .github/workflows/ci.yml  Lint and tests on push
```

---

## References

- Alraddawi, D., Keckhut, P., Mandija, F., Sarkissian, A., et al.: Calibration of upper air water vapour profiles using the IPRAL Raman lidar and ERA5 model results and comparison to GRUAN radiosonde observations, Atmosphere, 16, 351, https://doi.org/10.3390/atmos16030351, 2025.
- Arub, Z., Bhandari, S., Gani, S., Apte, J. S., Hildebrandt Ruiz, L., and Habib, G.: Air mass physiochemical characteristics over New Delhi: impacts on aerosol hygroscopicity and cloud condensation nuclei (CCN) formation, Atmos. Chem. Phys., 20, 6953-6971, https://doi.org/10.5194/acp-20-6953-2020, 2020.
- Bates, D., Mächler, M., Bolker, B., and Walker, S.: Fitting linear mixed-effects models using lme4, J. Stat. Softw., 67, https://doi.org/10.18637/jss.v067.i01, 2015.
- Benjamini, Y. and Hochberg, Y.: Controlling the false discovery rate: a practical and powerful approach to multiple testing, J. R. Stat. Soc. B, 57, 289-300, https://doi.org/10.1111/j.2517-6161.1995.tb02031.x, 1995.
- Bhattu, D. and Tripathi, S. N.: Inter-seasonal variability in size-resolved CCN properties at Kanpur, India, Atmos. Environ., 85, 161-168, https://doi.org/10.1016/j.atmosenv.2013.12.016, 2014.
- Bhattu, D. and Tripathi, S. N.: CCN closure study: effects of aerosol chemical composition and mixing state, J. Geophys. Res. Atmos., 120, 766-783, https://doi.org/10.1002/2014JD021978, 2015.
- Choudhury, G. and Tesche, M.: Estimating cloud condensation nuclei concentrations from CALIPSO lidar measurements, Atmos. Meas. Tech., 15, 639-654, https://doi.org/10.5194/amt-15-639-2022, 2022.
- Copernicus Publications: Data policy (Atmospheric Chemistry and Physics), https://www.atmospheric-chemistry-and-physics.net/policies/data_policy.html, last access: 16 November 2026.
- Díaz-Zurita, A., Brunamonti, S., Haefele, A., Collaud Coen, M., Martucci, G., Brem, B. T., Gysel-Beer, M., Lyamani, H., Titos, G., Pérez-Ramírez, D., et al.: Characterisation of hygroscopic aerosol processes using remote sensing and in situ techniques at the MeteoSwiss Payerne station, Atmos. Chem. Phys., 26, 15653-15682, https://doi.org/10.5194/acp-26-15653-2026, 2026.
- Donovan, D. P., van Zadelhoff, G.-J., and Wang, P.: The EarthCARE lidar cloud and aerosol profile processor (A-PRO): the A-AER, A-EBD, A-TC, and A-ICE products, Atmos. Meas. Tech., 17, 5301-5340, https://doi.org/10.5194/amt-17-5301-2024, 2024.
- Dubovik, O. and King, M. D.: A flexible inversion algorithm for retrieval of aerosol optical properties from Sun and sky radiance measurements, J. Geophys. Res., 105, 20673-20696, https://doi.org/10.1029/2000JD900282, 2000.
- Engelhart, G. J., Hennigan, C. J., Miracolo, M. A., Robinson, A. L., and Pandis, S. N.: Cloud condensation nuclei activity of fresh primary and aged biomass burning aerosol, Atmos. Chem. Phys., 12, 7285-7293, https://doi.org/10.5194/acp-12-7285-2012, 2012.
- Feingold, G. and Morley, B.: Aerosol hygroscopic properties as measured by lidar and comparison with in situ measurements, J. Geophys. Res., 108, https://doi.org/10.1029/2002JD002842, 2003.
- Gelaro, R., McCarty, W., Suárez, M. J., Todling, R., et al.: The Modern-Era Retrospective Analysis for Research and Applications, Version 2 (MERRA-2), J. Climate, 30, 5419-5454, https://doi.org/10.1175/JCLI-D-16-0758.1, 2017.
- Georgoulias, A. K., Marinou, E., Tsekeri, A., Proestakis, E., Akritidis, D., Alexandri, G., Zanis, P., Balis, D., Marenco, F., Tesche, M., and Amiridis, V.: A first case study of CCN concentrations from spaceborne lidar observations, Remote Sens., 12, 1557, https://doi.org/10.3390/rs12101557, 2020.
- Giglio, L., Schroeder, W., and Justice, C. O.: The collection 6 MODIS active fire detection algorithm and fire products, Remote Sens. Environ., 178, 31-41, https://doi.org/10.1016/j.rse.2016.02.054, 2016.
- Granados-Muñoz, M. J., Navas-Guzmán, F., Bravo-Aranda, J. A., Guerrero-Rascado, J. L., et al.: Hygroscopic growth of atmospheric aerosol particles based on active remote sensing and radiosounding measurements: selected cases in southeastern Spain, Atmos. Meas. Tech., 8, 705-718, https://doi.org/10.5194/amt-8-705-2015, 2015.
- Hänel, G.: The properties of atmospheric aerosol particles as functions of the relative humidity at thermodynamic equilibrium with the surrounding moist air, Adv. Geophys., 73-188, https://doi.org/10.1016/S0065-2687(08)60142-9, 1976.
- He, J., Li, Z., He, L., and Wang, J.: Long-term spatiotemporal features of aerosol optical characteristics and relative humidity in China's offshore areas, Geo-spatial Inf. Sci., 28, 2431-2448, https://doi.org/10.1080/10095020.2024.2447445, 2025.
- He, Y., Jing, Y., Yin, Z., Müller, D., et al.: Hygroscopic growth obscures actual variation in anthropogenic aerosol optical depth over central China during 2010-2024, Atmos. Chem. Phys., 26, 4937-4951, https://doi.org/10.5194/acp-26-4937-2026, 2026.
- Hersbach, H., Bell, B., Berrisford, P., Hirahara, S., et al.: The ERA5 global reanalysis, Q. J. R. Meteorol. Soc., 146, 1999-2049, https://doi.org/10.1002/qj.3803, 2020.
- Hu, Q., Goloub, P., Veselovskii, I., Podvin, T., Dubois, G., Khaykin, S., Boissière, W., Ducos, F., and Korenskiy, M.: Advanced insights into biomass burning aerosols during the 2023 Canadian wildfires from dual-site Raman and fluorescence lidar observations, Atmos. Chem. Phys., 26, 13027-13053, https://doi.org/10.5194/acp-26-13027-2026, 2026.
- Illingworth, A. J., Barker, H. W., Beljaars, A., Ceccaldi, M., et al.: The EarthCARE satellite: the next step forward in global measurements of clouds, aerosols, precipitation, and radiation, Bull. Am. Meteorol. Soc., 96, 1311-1332, https://doi.org/10.1175/BAMS-D-12-00227.1, 2015.
- Inness, A., Ades, M., Agustí-Panareda, A., Barré, J., et al.: The CAMS reanalysis of atmospheric composition, Atmos. Chem. Phys., 19, 3515-3556, https://doi.org/10.5194/acp-19-3515-2019, 2019.
- Jayachandran, V. N., Suresh Babu, S. N., Vaishya, A., Gogoi, M. M., et al.: Altitude profiles of cloud condensation nuclei characteristics across the Indo-Gangetic Plain prior to the onset of the Indian summer monsoon, Atmos. Chem. Phys., 20, 561-576, https://doi.org/10.5194/acp-20-561-2020, 2020a.
- Jayachandran, V. N., Varghese, M., Murugavel, P., Todekar, K. S., et al.: Cloud condensation nuclei characteristics during the Indian summer monsoon over a rain-shadow region, Atmos. Chem. Phys., 20, 7307-7334, https://doi.org/10.5194/acp-20-7307-2020, 2020b.
- Jethva, H., Chand, D., Torres, O., Gupta, P., et al.: Agricultural burning and air quality over northern India: a synergistic analysis using NASA's A-train satellite data and ground measurements, Aerosol Air Qual. Res., 18, 1756-1773, https://doi.org/10.4209/aaqr.2017.12.0583, 2018.
- Jethva, H., Torres, O., Field, R. D., Lyapustin, A., et al.: Connecting crop productivity, residue fires, and air quality over northern India, Sci. Rep., 9, https://doi.org/10.1038/s41598-019-52799-x, 2019.
- Jimenez, J. L., Canagaratna, M. R., Donahue, N. M., Prevot, A. S. H., et al.: Evolution of organic aerosols in the atmosphere, Science, 326, 1525-1529, https://doi.org/10.1126/science.1180353, 2009.
- Jing, Y., He, Y., Yin, Z., Müller, D., et al.: Hygroscopic growth characteristics of anthropogenic aerosols over central China revealed by lidar observations, Atmos. Meas. Tech., 19, 389-403, https://doi.org/10.5194/amt-19-389-2026, 2026.
- Kallihosur, T., Nair, V. S., and Sinha, P. R.: Winter haze amplification by aerosol hygroscopic growth over eastern Indo-Gangetic Plain, Commun. Earth Environ., 5, 656, https://doi.org/10.1038/s43247-024-01792-y, 2024.
- Kim, M.-H., Omar, A. H., Tackett, J. L., Vaughan, M. A., et al.: The CALIPSO version 4 automated aerosol classification and lidar ratio selection algorithm, Atmos. Meas. Tech., 11, 6107-6135, https://doi.org/10.5194/amt-11-6107-2018, 2018.
- Kumar, G., Madhavan, B. L., Sahu, L. K., Kumar, Y. B., et al.: Multi-year CALIPSO observations of ubiquitous elevated aerosol layer in the free troposphere over South Asia: sources and formation mechanism, J. Geophys. Res. Atmos., 128, e2021JD036277, https://doi.org/10.1029/2021JD036277, 2023.
- Lakens, D.: Equivalence tests: a practical primer for t tests, correlations, and meta-analyses, Soc. Psychol. Personal. Sci., 8, 355-362, https://doi.org/10.1177/1948550617697177, 2017.
- Liu, Z., Kar, J., Zeng, S., Tackett, J., et al.: Discriminating between clouds and aerosols in the CALIOP version 4.1 data products, Atmos. Meas. Tech., 12, 703-734, https://doi.org/10.5194/amt-12-703-2019, 2019.
- Mandariya, A. K., Tripathi, S. N., Gupta, T., and Mishra, G.: Wintertime hygroscopic growth factors (HGFs) of accumulation mode particles and their linkage to chemical composition in a heavily polluted urban atmosphere of Kanpur at the Centre of IGP, India: impact of ambient relative humidity, Sci. Total Environ., 704, 135363, https://doi.org/10.1016/j.scitotenv.2019.135363, 2020.
- Manoj, M. R., Satheesh, S. K., Moorthy, K. K., Trembath, J., and Coe, H.: Measurement report: Altitudinal variation of cloud condensation nuclei activation across the Indo-Gangetic Plain prior to the onset of the Indian summer monsoon, Atmos. Chem. Phys., 21, 8979-8997, https://doi.org/10.5194/acp-21-8979-2021, 2021.
- Miri, R., Pujol, O., Hu, Q., Goloub, P., Veselovskii, I., Podvin, T., and Ducos, F.: Innovative aerosol hygroscopic growth study from Mie-Raman-fluorescence lidar and microwave radiometer synergy, Atmos. Meas. Tech., 17, 3367-3375, https://doi.org/10.5194/amt-17-3367-2024, 2024.
- Nair, V. S., Giorgi, F., and Hasyagar, U. K.: Amplification of South Asian haze by water vapour-aerosol interactions, Atmos. Chem. Phys., 20, 14457-14471, https://doi.org/10.5194/acp-20-14457-2020, 2020.
- NASA Earthdata: Official end of CALIPSO science mission, https://www.earthdata.nasa.gov/news/official-end-calipso-science-mission, 2 August 2023.
- NASA/LARC/SD/ASDC (2023): CALIPSO Lidar Level 2 5 km Aerosol Profile, version 4.51, NASA Langley Atmospheric Science Data Center DAAC, https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V4-51, last access: 16 November 2026.
- NASA/LARC/SD/ASDC (2025a): CALIPSO Lidar Level 2 5 km Aerosol Profile, version 5.00, NASA Langley Atmospheric Science Data Center DAAC, https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmAPro-Standard-V5-00, last access: 16 November 2026.
- NASA/LARC/SD/ASDC (2025b): CALIPSO Lidar Level 2 5 km Aerosol Layer, version 5.00, NASA Langley Atmospheric Science Data Center DAAC, https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L2_05kmALay-Standard-V5-00, last access: 16 November 2026.
- NASA/LARC/SD/ASDC: CALIPSO Lidar Level 2 Profile Data Description Document, Version 5.00 (including the quality summary), https://asdc.larc.nasa.gov/documents/calipso/quality_summaries/cal_lid_l2_pro_v5-00_desc_qs.pdf, 2026.
- Navas-Guzmán, F., Martucci, G., Collaud Coen, M., Granados-Muñoz, M. J., et al.: Characterization of aerosol hygroscopicity using Raman lidar measurements at the EARLINET station of Payerne, Atmos. Chem. Phys., 19, 11651-11668, https://doi.org/10.5194/acp-19-11651-2019, 2019.
- Petters, M. D. and Kreidenweis, S. M.: A single parameter representation of hygroscopic growth and cloud condensation nucleus activity, Atmos. Chem. Phys., 7, 1961-1971, https://doi.org/10.5194/acp-7-1961-2007, 2007.
- Petters, M. D., Carrico, C. M., Kreidenweis, S. M., Prenni, A. J., et al.: Cloud condensation nucleation activity of biomass burning aerosol, J. Geophys. Res., 114, https://doi.org/10.1029/2009JD012353, 2009.
- Pisso, I., Sollum, E., Grythe, H., Kristiansen, N. I., et al.: The Lagrangian particle dispersion model FLEXPART version 10.4, Geosci. Model Dev., 12, 4955-4997, https://doi.org/10.5194/gmd-12-4955-2019, 2019.
- Prasad, P., Basha, G., and Ratnam, M. V.: Impact of relative humidity on the vertical distribution of aerosols over India, Atmos. Res., 281, 106468, https://doi.org/10.1016/j.atmosres.2022.106468, 2023.
- Schroeder, W., Oliva, P., Giglio, L., and Csiszar, I. A.: The new VIIRS 375 m active fire detection data product: algorithm description and initial assessment, Remote Sens. Environ., 143, 85-96, https://doi.org/10.1016/j.rse.2013.12.008, 2014.
- Sicard, M., Fortunato dos Santos Oliveira, D. C., Muñoz-Porcar, C., Gil-Díaz, C., et al.: Measurement report: Spectral and statistical analysis of aerosol hygroscopic growth from multi-wavelength lidar measurements in Barcelona, Spain, Atmos. Chem. Phys., 22, 7681-7697, https://doi.org/10.5194/acp-22-7681-2022, 2022.
- Singh, N., Banerjee, T., Raju, M. P., Deboudt, K., et al.: Aerosol chemistry, transport, and climatic implications during extreme biomass burning emissions over the Indo-Gangetic Plain, Atmos. Chem. Phys., 18, 14197-14215, https://doi.org/10.5194/acp-18-14197-2018, 2018.
- Sinyuk, A., Holben, B. N., Eck, T. F., Giles, D. M., et al.: The AERONET Version 3 aerosol retrieval algorithm, associated uncertainties and comparisons to Version 2, Atmos. Meas. Tech., 13, 3375-3411, https://doi.org/10.5194/amt-13-3375-2020, 2020.
- Stein, A. F., Draxler, R. R., Rolph, G. D., Stunder, B. J. B., et al.: NOAA's HYSPLIT atmospheric transport and dispersion modeling system, Bull. Am. Meteorol. Soc., 96, 2059-2077, https://doi.org/10.1175/BAMS-D-14-00110.1, 2015.
- Tackett, J. L., Winker, D. M., Getzewich, B. J., Vaughan, M. A., et al.: CALIPSO lidar level 3 aerosol profile product: version 3 algorithm design, Atmos. Meas. Tech., 11, 4129-4152, https://doi.org/10.5194/amt-11-4129-2018, 2018.
- Tesche, M., Ansmann, A., Müller, D., Althausen, D., et al.: Vertically resolved separation of dust and smoke over Cape Verde using multiwavelength Raman and polarization lidars during Saharan Mineral Dust Experiment 2008, J. Geophys. Res., 114, https://doi.org/10.1029/2009JD011862, 2009.
- Trepte, C.: CALIPSO final report, NASA Technical Reports Server, 20260000771, https://doi.org/10.64631/LIZS5968, 2026.
- Wehr, T., Kubota, T., Tzeremes, G., Wallace, K., et al.: The EarthCARE mission: science and system overview, Atmos. Meas. Tech., 16, 3581-3608, https://doi.org/10.5194/amt-16-3581-2023, 2023.
- Winker, D. M., Vaughan, M. A., Omar, A., Hu, Y., et al.: Overview of the CALIPSO mission and CALIOP data processing algorithms, J. Atmos. Ocean. Technol., 26, 2310-2323, https://doi.org/10.1175/2009JTECHA1281.1, 2009.
- Young, S. A., Vaughan, M. A., Garnier, A., Tackett, J. L., et al.: Extinction and optical depth retrievals for CALIPSO's Version 4 data release, Atmos. Meas. Tech., 11, 5701-5727, https://doi.org/10.5194/amt-11-5701-2018, 2018.
