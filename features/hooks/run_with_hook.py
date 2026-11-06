import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HOOK = Path(__file__).parent / "on_run.sh"


def main():
    print("=== hook demo ===", flush=True)
    subprocess.run(["bash", str(HOOK)], cwd=ROOT, check=False)
    print(flush=True)
    print("=== running rl after hook ===", flush=True)
    subprocess.run([sys.executable, "-m", "rl.main"], cwd=ROOT, check=False)


if __name__ == "__main__":
    main()
