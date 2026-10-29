from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def load_context() -> str:
    claude = (BASE_DIR / "CLAUDE.md").read_text(encoding="utf-8")
    project = (BASE_DIR / "project_context.md").read_text(encoding="utf-8")
    return claude + "\n\n" + project


if __name__ == "__main__":
    print(load_context())
