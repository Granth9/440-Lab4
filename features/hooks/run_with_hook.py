import subprocess
import sys
import shutil
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HOOK = Path(__file__).parent / "on_run.sh"


def find_bash():
    # Check whether Bash is already in PATH
    bash = shutil.which("bash")
    if bash:
        return bash

    # Check common Git Bash installation locations on Windows
    locations = [
        Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "Git/bin/bash.exe",
        Path(os.environ.get("LOCALAPPDATA", "")) / "Programs/Git/bin/bash.exe",
    ]

    for location in locations:
        if location.exists():
            return str(location)

    raise FileNotFoundError(
        "Bash not found. Install Git for Windows (Git Bash) or install Bash."
    )


def main():
    print("=== hook demo ===", flush=True)

    bash = find_bash()

    env = os.environ.copy()

    python_path = Path(sys.executable).as_posix()

    if os.name == "nt":
        python_path = "/" + python_path[0].lower() + python_path[2:]

    env["LAB_PYTHON"] = python_path

    subprocess.run(
        [bash, str(HOOK)],
        cwd=ROOT,
        env=env,
        check=True
    )

    print(flush=True)
    print("=== running rl after hook ===", flush=True)

    subprocess.run([sys.executable, "-m", "rl.main"], cwd=ROOT, check=False)


if __name__ == "__main__":
    main()