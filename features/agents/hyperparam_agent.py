from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def run(context):
    hp = (ROOT / "rl" / "hyperparams.py").read_text()
    skill = (ROOT / "features" / "skills" / "rl_hyperparams.md").read_text()
    return (
        "hyperparam agent\n"
        f"context files: {', '.join(context)}\n"
        "selected values from rl/hyperparams.py:\n"
        + hp.strip()
        + "\n\nskill notes:\n"
        + skill.strip()
    )
