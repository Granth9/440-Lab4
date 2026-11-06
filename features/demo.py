import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(title, args):
    print(title, flush=True)
    print("-" * len(title), flush=True)
    subprocess.run(args, cwd=ROOT)
    print(flush=True)


def main():
    run("1) skill", [sys.executable, "features/skills/load_skill.py"])
    run("2) hook", [sys.executable, "features/hooks/run_with_hook.py"])
    run("3) sub-agents", [sys.executable, "features/agents/orchestrator.py"])


if __name__ == "__main__":
    main()
