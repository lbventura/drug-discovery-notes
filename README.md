# drug-discovery-notes
A collection of notes on drug discovery online courses.

## Set up a development environment

Install [Micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html), then run from the repository root:

```bash
micromamba create -f environment.yml
micromamba activate drug-discovery-notes
```

To update an existing environment after dependencies change:

```bash
micromamba install -n drug-discovery-notes -f environment.yml
```

## Notebooks

[SMILES with RDKit](notebooks/smiles-with-rdkit.ipynb) introduces molecular line
notation, simple molecules, aromatic rings, and all-trans β-carotene with rendered
structures and executable examples. Open it in a Jupyter-capable editor, select
the Python interpreter from the `drug-discovery-notes` micromamba environment,
and run all cells.
