"""Load the persistent context files used in Strategy 1."""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def load_context() -> str:
    """Return project instructions and project-specific context."""
    files = (BASE_DIR / "CLAUDE.md", BASE_DIR / "project_context.md")
    return "\n\n".join(path.read_text(encoding="utf-8").strip() for path in files)


if __name__ == "__main__":
    print(load_context())
