"""Recreate the Lab 4 demo workspace from the two pinned source revisions."""

import argparse
import subprocess
from pathlib import Path

LAB4_REV = "15e31ff3251622b7655cbc96b351f37523ca50d6"
AIMA_REV = "f104e03fdc1582f014b3a4c93f1a9b7d2da70114"
AIMA_FILES = (
    "aima/mdp.py",
    "gui/grid_mdp.py",
    "gui/vacuum_agent.py",
    "gui/xy_vacuum_environment.py",
)


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("lab4", type=Path, help="Local clone containing the Lab 4 snapshot")
    parser.add_argument("aima", type=Path, help="Local AIMA clone")
    parser.add_argument("output", type=Path, help="New workspace outside the source repositories")
    args = parser.parse_args()
    paths = git(args.lab4, "ls-tree", "-r", "--name-only", LAB4_REV, "--",
                "README.md", "strategy_1", "strategy_4").decode().splitlines()
    files = {name: git(args.lab4, "show", f"{LAB4_REV}:{name}") for name in paths}
    files.update({
        f"aima-python/{name}": git(args.aima, "show", f"{AIMA_REV}:{name}")
        for name in AIMA_FILES
    })
    args.output.mkdir()
    for name, content in files.items():
        path = args.output / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
    print(args.output.resolve())


if __name__ == "__main__":
    main()
