"""Mixed-effects models, cluster bootstrap, TOST equivalence and FDR control.

TODO: implement the primary model, interaction test, equivalence test and
uncertainty methods in Section 8.8. Do not run confirmatory tests until the
pilot values are frozen in docs/protocol.md.
"""

from __future__ import annotations


def fit_primary_model(*args, **kwargs):
    """Placeholder.

    TODO:
        * Fit the mixed-effects model for gamma (and kappa_L) with random intercepts for sub-region and overpass.
        * Test H1 with the altitude coefficient and a two one-sided equivalence test.
        * Test H2 with a cluster bootstrap of the critical-diameter difference.
        * Test H3 with a likelihood-ratio test of the altitude by season interaction, then regime contrasts under a 5 % false discovery rate.
        * Provide Kruskal-Wallis and Mann-Whitney tests in parallel for comparability with HYGRO19.
    """

    raise NotImplementedError(
        "fit_primary_model is a scaffold only; implementation will follow."
    )
