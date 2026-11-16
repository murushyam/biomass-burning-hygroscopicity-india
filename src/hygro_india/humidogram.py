"""Hänel fit of backscatter against relative humidity, with Monte Carlo errors.

TODO: regress ln beta(z) on -ln[(1 - RH(z)) / (1 - RH_ref)] by weighted least
squares, as in Section 8.5, and return a distribution of gamma for each layer.
"""

from __future__ import annotations


def fit_hanel_gamma(*args, **kwargs):
    """Placeholder.

    TODO:
        * Fit gamma by weighted least squares using CALIOP backscatter uncertainty and the RH error.
        * Draw a Monte Carlo ensemble (1000 draws in the starting config) of backscatter noise and RH error.
        * Return the gamma distribution and fit diagnostics, including the coefficient of determination.
    """

    raise NotImplementedError(
        "fit_hanel_gamma is a scaffold only; implementation will follow."
    )
