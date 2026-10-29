"""Strategy 4 demo: orchestrator + context filter + isolated sub-agents."""
import argparse
from pathlib import Path
from typing import Dict

from context_filter import load_context, context_summary
from agents.code_reviewer import review
from agents.researcher import research

def read_optional(path: str | None) -> str:
    if not path:
        return ""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Source file not found: {file_path}")
    return file_path.read_text(encoding="utf-8")

def run_method4(env_path: str | None = None,
                agent_path: str | None = None,
                main_path: str | None = None) -> str:
    """Delegate two subtasks with separate context bundles and combine reports."""
    # Only code review receives source code.
    code_context = load_context(
        "code_reviewer",
        extra_context={"task_brief.md": "Review the vacuum robot implementation for correctness and lab-relevant risks."},
    )
    source_files: Dict[str, str] = {
        "vacuum_env.py": read_optional(env_path),
        "q_learning.py": read_optional(agent_path),
        "main.py": read_optional(main_path),
    }

    # Research receives only its allowlisted project/research context; no source code.
    research_context = load_context(
        "researcher",
        extra_context={"task_brief.md": "Explain how this repository demonstrates Strategy 4: isolation via sub-agents."},
    )

    print("ORCHESTRATOR: delegating tasks")
    print(f"  Code reviewer context: {context_summary(code_context)}")
    print(f"  Researcher context:    {context_summary(research_context)}")
    print("  Isolation check: source code is passed only to code_reviewer.\n")

    code_report = review(code_context, source_files)
    research_report = research(research_context)

    # The orchestrator combines final outputs, not the agents' input contexts.
    final_report = (
        "METHOD 4 — ORCHESTRATED SUB-AGENT REPORT\n"
        "========================================\n\n"
        + code_report + "\n\n"
        + research_report + "\n\n"
        + "ORCHESTRATOR SUMMARY\n"
        "- Two specialized agents were invoked for separate subtasks.\n"
        "- Each agent received an allowlisted context bundle.\n"
        "- Source code was isolated to the code-review agent.\n"
        "- Reports were combined after each sub-agent finished.\n"
        "- This is a deterministic demonstration; the agents do not call an LLM.\n"
    )
    return final_report

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Strategy 4 sub-agent isolation demo.")
    parser.add_argument("--env-path", help="Path to vacuum_env.py")
    parser.add_argument("--agent-path", help="Path to q_learning.py")
    parser.add_argument("--main-path", help="Path to main.py")
    args = parser.parse_args()
    print(run_method4(args.env_path, args.agent_path, args.main_path))
