"""Document intended tests for modules that are still stubs."""

import pytest

from hygro_india.humidogram import fit_hanel_gamma
from hygro_india.ccn import critical_dry_diameter
from hygro_india.qc import select_layers


@pytest.mark.skip(reason="Retrieval and quality-control code is not implemented yet.")
def test_hanel_fit_recovers_known_gamma():
    fit_hanel_gamma()


@pytest.mark.skip(reason="CCN code is not implemented yet.")
def test_critical_diameter_scaling():
    critical_dry_diameter()


@pytest.mark.skip(reason="Layer selection is not implemented yet.")
def test_quality_control_does_not_filter_on_gamma():
    select_layers()
