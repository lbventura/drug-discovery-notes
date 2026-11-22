"""Simulate the fork X <- Z -> Y and plot pooled/conditional associations.

Assumptions: Z ~ Bernoulli(0.5), X = Z + noise_x, Y = Z + noise_y,
where both noises are independent standard normals, independent of Z.
Thus X and Y are independent given Z. Their population correlation is
0.25 / (0.25 + 1) = 0.2 when pooled, and zero within each Z group.
Finite samples will only approximate these correlations.

dag_analysis.py provides linear fits and approximate two-sided 95% confidence
intervals. The normal-model intervals are approximate for the pooled mixture.

Install: python3 -m pip install numpy matplotlib
Run:     python3 amidd-2026/fork_dag.py [--show]
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
    z = rng.integers(0, 2, size=n)
    # Separate draws make the Gaussian noises independent of each other and Z.
    noise_x = rng.normal(loc=0, scale=1, size=n)
    noise_y = rng.normal(loc=0, scale=1, size=n)
    x = z + noise_x
    y = z + noise_y

    plot_dag_analysis(
        x, y, z,
        output_prefix=Path(__file__).resolve().with_suffix(""),
        pooled_title="X and Y share a cause: Z (pooled data)",
        conditioned_title="Condition on Z: fit X and Y separately within each group",
        show=args.show,
    )


if __name__ == "__main__":
    main()
