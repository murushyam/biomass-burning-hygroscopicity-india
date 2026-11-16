"""Layer selection and well-mixed tests.

TODO: apply the Table 2 criteria in configs/qc_thresholds.yaml, without
selecting on the sign or size of gamma (Section 8.2).
"""

from __future__ import annotations


def select_layers(*args, **kwargs):
    """Placeholder.

    TODO:
        * Apply each criterion in configs/qc_thresholds.yaml.
        * Assign layers to the boundary layer or free troposphere using the diurnal maximum of ERA5 boundary-layer height (Section 8.4).
        * Keep intermediate layers for the continuous-altitude model only.
        * Never filter on the sign or size of gamma.
    """

    raise NotImplementedError(
        "select_layers is a scaffold only; implementation will follow."
    )
