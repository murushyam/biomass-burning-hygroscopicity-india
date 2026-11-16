"""ERA5 humidity, wind and boundary-layer height readers.

TODO: read hourly pressure-level, single-level and (for refinement) model-level
fields listed in docs/data_sources.md.
"""

from __future__ import annotations


def read_pressure_levels(*args, **kwargs):
    """Placeholder for ERA5 pressure-level fields.

    TODO:
        * Load temperature, specific and relative humidity, geopotential and winds.
        * Keep native 0.25 deg, hourly, 37-level resolution until co-location.
    """

    raise NotImplementedError(
        "read_pressure_levels is a scaffold only; implementation will follow."
    )


def read_boundary_layer_height(*args, **kwargs):
    """Placeholder for ERA5 single-level boundary-layer height."""

    raise NotImplementedError(
        "read_boundary_layer_height is a scaffold only; implementation will follow."
    )
