"""Runnable demonstration of persistent context loading."""
from context_loader import load_context


def main() -> None:
    context = load_context()
    print("STRATEGY 1 — PERSISTENT CONTEXT")
    print("===============================")
    print(context)


if __name__ == "__main__":
    main()
