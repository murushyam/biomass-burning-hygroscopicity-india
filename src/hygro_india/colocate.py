"""Time and space interpolation of ERA5 (and MERRA-2 RH) onto CALIOP bins.

TODO: interpolate linearly in time to the overpass, bilinearly in the
horizontal to the profile location, and in log-pressure to the CALIOP bins,
as described in Section 8.3.
"""

from __future__ import annotations


def colocate_era5(*args, **kwargs):
    """Placeholder.

    TODO:
        * Interpolate ERA5 to each CALIOP profile time and location.
        * Interpolate in log-pressure to the 60 m CALIOP bins.
        * Attach the MERRA-2 Relative_Humidity field already in the CALIOP files as a second humidity source.
        * Optionally repeat the interpolation on ERA5 model levels.
    """

    raise NotImplementedError(
        "colocate_era5 is a scaffold only; implementation will follow."
    )
