"""Minimal import check for the package scaffold."""

from hygro_india import __version__


def test_package_version():
    assert __version__ == "0.1.0"
