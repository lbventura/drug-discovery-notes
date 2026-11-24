"""Clean notebook execution information for Git using only the standard library."""

import argparse
import json
from pathlib import Path
import shlex
import subprocess
import sys
from typing import Any


def clean_notebook(*, notebook: dict[str, Any]) -> None:
    """Clear execution information while preserving sources and output content."""
    for cell in notebook["cells"]:
        for key in ("execution", "ExecuteTime", "trusted"):
            cell["metadata"].pop(key, None)
        if cell["cell_type"] == "code":
            cell["execution_count"] = None
            for output in cell["outputs"]:
                if output["output_type"] == "execute_result":
                    output["execution_count"] = None


def install_filter() -> None:
    """Configure this checkout to run the filter with the current Python."""
    script = Path(__file__).resolve()
    root = script.parent.parent
    command = shlex.join([sys.executable, str(script)])
    for name, value in (
        ("filter.clean-notebooks.clean", command),
        ("filter.clean-notebooks.required", "true"),
    ):
        subprocess.run(
            args=["git", "-C", str(root), "config", "--local", name, value],
            check=True,
        )
    print("Notebook clean filter installed for this checkout.")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--install", action="store_true", help="install the Git filter in this checkout"
    )
    args = parser.parse_args()
    if args.install:
        install_filter()
    else:
        notebook = json.load(fp=sys.stdin)
        clean_notebook(notebook=notebook)
        json.dump(obj=notebook, fp=sys.stdout, ensure_ascii=False, indent=1)
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()
