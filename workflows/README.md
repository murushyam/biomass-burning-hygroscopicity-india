# Workflows

A Snakemake or Makefile pipeline from download to figures will be added here once the readers and retrieval modules exist. The intended steps follow Sections 8 and 9 of `docs/proposal.md`:

1. Download or subset the public products listed in `docs/data_sources.md`.
2. Co-locate ERA5 with CALIOP profiles.
3. Apply layer selection and well-mixed tests.
4. Fit gamma, retrieve kappa_L, and compute critical diameters.
5. Attribute fire exposure and smoke age.
6. Run the pilot, freeze design choices in `docs/protocol.md`, then run the main analysis and consistency checks.

The Makefile in this folder is a placeholder and does not run any analysis.

A GitHub Actions workflow that compiles the package and runs the import check is prepared locally as `.github/workflows/ci.yml`. It was not included in the initial push because the GitHub token used to create the repository does not include the `workflow` scope. The file can be added later once that scope is granted.
