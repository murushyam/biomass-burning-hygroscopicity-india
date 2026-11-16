"""Composition closure and consistency checks for kappa_L.

TODO: implement the four checks in Section 9.3: composition closure against
MERRA-2 and CAMS, surface and column anchors, aircraft CCN profile comparison,
and cross-method context.
"""

from __future__ import annotations


def composition_kappa(*args, **kwargs):
    """Placeholder.

    TODO:
        * Build a composition-based kappa from MERRA-2 and CAMS species mass fractions and literature kappa values.
        * Compare boundary-layer results with published surface kappa and growth factors.
        * Compare the sign of the modelled FT-minus-BL activated fraction with SWAAMI-RAWEX activation ratios.
    """

    raise NotImplementedError(
        "composition_kappa is a scaffold only; implementation will follow."
    )
