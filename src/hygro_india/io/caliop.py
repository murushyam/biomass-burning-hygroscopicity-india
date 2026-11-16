"""CALIOP level 2 5 km aerosol profile and layer readers.

TODO: read V5.00 (primary) and V4.51 (sensitivity) HDF products, including
backscatter, depolarisation, extinction, CAD, quality flags, MERRA-2
relative humidity, and layer top, base and subtype.
"""

from __future__ import annotations


def read_profile(*args, **kwargs):
    """Placeholder for a CALIOP 5 km aerosol profile reader.

    TODO:
        * Open a V5.00 or V4.51 5 km APro granule.
        * Return the variables listed in docs/data_sources.md.
        * Convert Total_Backscatter_Coefficient_532 from km^-1 sr^-1 to
          Mm^-1 sr^-1.
        * Propagate fill values and quality flags without silently dropping them.
    """

    raise NotImplementedError(
        "read_profile is a scaffold only; implementation will follow."
    )


def read_layer(*args, **kwargs):
    """Placeholder for a CALIOP 5 km aerosol layer reader.

    TODO:
        * Open a V5.00 5 km ALay granule.
        * Return layer top, base, subtype and layer optical depth.
    """

    raise NotImplementedError(
        "read_layer is a scaffold only; implementation will follow."
    )
