"""Simulate the collider X -> Z <- Y and plot pooled/conditional associations.

X and Y are independent standard normals. Z = 1 when X + Y > 0 and
Z = -1 when X + Y <= 0. Pooled population correlation is zero, but
conditioning on either value of Z induces a negative correlation:
corr(X, Y | Z) = -1 / (pi - 1), approximately -0.467.
Finite samples will only approximate these correlations.

dag_analysis.py provides linear fits and approximate two-sided 95% confidence
intervals. Conditioning truncates the Gaussian distribution, so the usual
normal-model interval assumptions need not hold within each Z group.

Install: python3 -m pip install numpy matplotlib
Run:     python3 amidd-2026/collider_dag.py [--show]
The two PNG plots are saved beside this script; --show also opens them.
"""

import argparse
from pathlib import Path

import numpy as np

from dag_analysis import plot_dag_analysis


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--show", action="store_true", help="also display the plots")
    args = parser.parse_args()

    rng = np.random.default_rng(42)
    n = 1000
    # Draw X and Y independently before computing their shared effect Z.
    x = rng.normal(loc=0, scale=1, size=n)
    y = rng.normal(loc=0, scale=1, size=n)
    z = np.where(x + y > 0, 1, -1)

    plot_dag_analysis(
        x, y, z,
        output_prefix=Path(__file__).resolve().with_suffix(""),
        pooled_title="Collider X -> Z <- Y: pooled data",
        conditioned_title="Condition on Z: X and Y become negatively correlated",
        show=args.show,
    )


if __name__ == "__main__":
    main()
