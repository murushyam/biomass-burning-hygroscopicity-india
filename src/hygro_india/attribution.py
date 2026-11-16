"""Fire exposure and smoke age from HYSPLIT trajectories and FIRMS detections.

TODO: implement the 120 h back-trajectory exposure index in Section 8.7 and
configs/hysplit.yaml. The smoke-class threshold is set in the pilot.
"""

from __future__ import annotations


def fire_exposure_index(*args, **kwargs):
    """Placeholder.

    TODO:
        * Start 120 h HYSPLIT trajectories at the layer boundaries and centre.
        * Count FIRMS detections within 0.25 deg of the trajectory when it lies below the ERA5 boundary-layer height.
        * Weight fire radiative power by residence time.
        * Estimate smoke age and bin it as below 24 h, 24 to 72 h, or above 72 h.
        * Optionally repeat attribution with FLEXPART 10.4 for a subset of seasons.
    """

    raise NotImplementedError(
        "fire_exposure_index is a scaffold only; implementation will follow."
    )
