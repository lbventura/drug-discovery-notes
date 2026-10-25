"""Shared linear fits, approximate confidence intervals, and plots for DAG demos.

Pearson r uses Fisher's transformation. Slope and intercept use normal
intervals with ordinary least-squares standard errors (constant residual
variance). All intervals are approximate; Gaussian mixtures and conditioning
on a collider need not satisfy the normal-model assumptions.
"""

from pathlib import Path
from statistics import NormalDist

import matplotlib.pyplot as plt
import numpy as np


def linear_regression_statistics(x, y):
    """Fit Y = intercept + slope * X and estimate coefficient standard errors.

    Uses ordinary least squares with constant residual variance. The simulated
    groups have more than three observations and nonzero variance in X and Y.
    """
    sample_count = len(x)
    mean_x, mean_y = np.mean(x), np.mean(y)
    centered_x, centered_y = x - mean_x, y - mean_y
    sum_squared_x = np.sum(centered_x**2)
    sum_squared_y = np.sum(centered_y**2)
    cross_product = np.sum(centered_x * centered_y)

    slope = cross_product / sum_squared_x
    intercept = mean_y - slope * mean_x
    correlation = cross_product / np.sqrt(sum_squared_x * sum_squared_y)

    residuals = y - (intercept + slope * x)
    # Subtract two degrees of freedom because we estimated slope and intercept.
    residual_variance = np.sum(residuals**2) / (sample_count - 2)
    slope_standard_error = np.sqrt(residual_variance / sum_squared_x)
    intercept_standard_error = np.sqrt(
        residual_variance * (1 / sample_count + mean_x**2 / sum_squared_x)
    )
    return slope, intercept, correlation, slope_standard_error, intercept_standard_error


def plot_dag_analysis(x, y, z, output_prefix, pooled_title, conditioned_title,
                      show=False):
    """Save pooled and stratified plots for a binary Z, optionally displaying them.

    output_prefix is a path without an extension; filenames append
    _pooled.png and _conditioned.png. Brackets show approximate two-sided
    95% confidence intervals, with 2.5% probability in each tail.
    """
    confidence_level = 0.95
    tail_probability = (1 - confidence_level) / 2
    critical_value = NormalDist().inv_cdf(1 - tail_probability)

    output_prefix = Path(output_prefix)
    x_grid = np.linspace(x.min(), x.max(), 200)
    limits = (min(x.min(), y.min()) - 0.2, max(x.max(), y.max()) + 0.2)

    def add_group(ax, group_x, group_y, color, label):
        slope, intercept, correlation, slope_se, intercept_se = (
            linear_regression_statistics(group_x, group_y)
        )

        # Fisher's transform is approximately normal, with SE = 1 / sqrt(n - 3).
        fisher_r = np.arctanh(correlation)
        fisher_margin = critical_value / np.sqrt(len(group_x) - 3)
        correlation_low, correlation_high = np.tanh(
            [fisher_r - fisher_margin, fisher_r + fisher_margin]
        )

        # Two-sided coefficient intervals: estimate +/- critical value * SE.
        slope_margin = critical_value * slope_se
        intercept_margin = critical_value * intercept_se
        summary = (
            f"{label}: r = {correlation:.3f} "
            f"[{correlation_low:.3f}, {correlation_high:.3f}]\n"
            f"slope = {slope:.3f} "
            f"[{slope - slope_margin:.3f}, {slope + slope_margin:.3f}]\n"
            f"intercept = {intercept:.3f} "
            f"[{intercept - intercept_margin:.3f}, "
            f"{intercept + intercept_margin:.3f}]"
        )
        ax.scatter(group_x, group_y, s=5, alpha=0.12, color=color)
        ax.plot(x_grid, slope * x_grid + intercept, color=color,
                linewidth=2, label=summary)
        print(f"{summary}\nBrackets show approximate 95% confidence intervals.\n")

    def save_plot(fig, ax, suffix, title):
        ax.set(xlabel="X", ylabel="Y", title=title, xlim=limits, ylim=limits)
        ax.set_aspect("equal", adjustable="box")
        ax.grid(alpha=0.2)
        ax.legend(loc="upper left", fontsize=9, title="Estimates [approx. 95% CI]")
        fig.tight_layout()
        path = output_prefix.with_name(f"{output_prefix.name}_{suffix}.png")
        fig.savefig(path, dpi=160)
        print(f"Saved {path}")

    fig, ax = plt.subplots(figsize=(7, 6))
    add_group(ax, x, y, "tab:blue", "Pooled")
    save_plot(fig, ax, "pooled", pooled_title)

    fig, ax = plt.subplots(figsize=(7, 6))
    for value, color in zip(np.unique(z), ["tab:orange", "tab:purple"]):
        mask = z == value
        add_group(ax, x[mask], y[mask], color, f"Z = {value}")
    save_plot(fig, ax, "conditioned", conditioned_title)

    if show:
        plt.show()
    plt.close("all")
