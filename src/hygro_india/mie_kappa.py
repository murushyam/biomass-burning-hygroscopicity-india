"""Mie look-up and retrieval of the lidar-effective hygroscopicity kappa_L.

TODO: run a forward Mie model (miepython or PyMieScatt) on an AERONET-constrained
lognormal accumulation mode, match the modelled backscatter enhancement, and
return a distribution of kappa_L (Section 8.5).
"""

from __future__ import annotations


def retrieve_kappa_l(*args, **kwargs):
    """Placeholder.

    TODO:
        * Build a Mie look-up over kappa from 0.02 to 0.60 (D).
        * Take median diameter, width and complex refractive index from AERONET inversions, with the fallbacks in Section 8.5.
        * Match the modelled backscatter enhancement to the observed value.
        * Sample size and refractive-index inputs in the same Monte Carlo ensemble as gamma.
    """

    raise NotImplementedError(
        "retrieve_kappa_l is a scaffold only; implementation will follow."
    )
