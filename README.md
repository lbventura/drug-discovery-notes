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

[Good and bad controls](notebooks/good-and-bad-controls.ipynb) translates Carlos
Cinelli’s R crash course into Python, with causal diagrams and regression examples
for Models 1–18 plus the variation of Model 11.

### Committing notebooks

Install the notebook Git filter once per clone, from the repository root:

```bash
python3 scripts/clean_notebooks.py --install
```

On `git add`, the filter sets cell and
output execution counts to `null` and removes cell execution timing metadata
(`execution`, `ExecuteTime`) and `trusted` flags. Code, Markdown, diagrams,
regression outputs, cell IDs, and other metadata (including kernel information)
are preserved. Staging does not rewrite your working notebooks.
