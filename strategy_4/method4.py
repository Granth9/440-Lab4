"""Strategy 4 demo: orchestrator + filtered context + isolated sub-agents."""
from pathlib import Path
from typing import Dict

from context_filter import context_summary, load_context
from agents.code_reviewer import review
from agents.researcher import research

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_FILES = {
    "vacuum_agent.py": REPO_ROOT / "aima-python" / "gui" / "vacuum_agent.py",
    "xy_vacuum_environment.py": REPO_ROOT / "aima-python" / "gui" / "xy_vacuum_environment.py",
    "grid_mdp.py": REPO_ROOT / "aima-python" / "gui" / "grid_mdp.py",
    "mdp.py": REPO_ROOT / "aima-python" / "aima" / "mdp.py",
}


def read_source_files() -> Dict[str, str]:
    """Read only the known, relevant vacuum/MDP source files that exist."""
    source_files = {}
    for name, path in DEFAULT_SOURCE_FILES.items():
        if path.is_file():
            source_files[name] = path.read_text(encoding="utf-8", errors="replace")
    return source_files


def run_method4() -> str:
    """Delegate code review and architecture research with separate contexts."""
    source_files = read_source_files()
    code_context = load_context(
        "code_reviewer",
        extra_context={
            "task_brief.md": (
                "Review the supplied vacuum/MDP source files. Describe their roles "
                "and identify evidence-based observations; do not assume Q-learning."
            )
        },
    )
    research_context = load_context(
        "researcher",
        extra_context={
            "task_brief.md": (
                "Explain how this repository demonstrates Strategy 4 through "
                "an orchestrator, context filtering, and specialized sub-agents."
            )
        },
    )

    print("ORCHESTRATOR: delegating tasks")
    print(f"  Code reviewer context: {context_summary(code_context)}")
    print(f"  Researcher context:    {context_summary(research_context)}")
    print(f"  Source files supplied only to code reviewer: {', '.join(sorted(source_files)) or 'none'}")
    print("  Isolation check: researcher receives no source code.\n")

    code_report = review(code_context, source_files)
    research_report = research(research_context)

    return (
        "METHOD 4 — ORCHESTRATED SUB-AGENT REPORT\n"
        "========================================\n\n"
        + code_report + "\n\n"
        + research_report + "\n\n"
        + "ORCHESTRATOR SUMMARY\n"
        "- Two specialized functions were invoked for separate subtasks.\n"
        "- Each received an allowlisted context bundle plus its explicit task brief.\n"
        "- Source code was passed only to the code-review function.\n"
        "- The orchestrator combined the reports.\n"
        "- This is a deterministic Python demonstration, not an LLM-powered agent system.\n"
    )


if __name__ == "__main__":
    print(run_method4())
