from pathlib import Path

SKILL = Path(__file__).parent / "rl_hyperparams.md"


def load_skill():
    return SKILL.read_text()


if __name__ == "__main__":
    print("=== skill: rl_hyperparams ===")
    print(load_skill())
