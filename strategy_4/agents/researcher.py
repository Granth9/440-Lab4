"""Specialized architecture-research sub-agent (deterministic demonstration)."""
from typing import Dict


def research(context: Dict[str, str]) -> str:
    """Explain the Strategy 4 architecture using only the research context."""
    project = context.get("project_context.md", "")
    research_notes = context.get("research_context.md", "")
    findings = [
        "The orchestrator delegates separate code-review and architecture-research tasks.",
        "The context filter uses an allowlist to choose context files for each role.",
        "Only the code-review function receives the source-code dictionary.",
        "The researcher receives project and strategy notes, but no source code.",
        "The orchestrator combines both reports after the subtasks return.",
    ]
    if not project or not research_notes:
        findings.append("Some expected research context was missing.")
    return (
        "RESEARCH REPORT\n"
        f"Context received: {', '.join(sorted(context))}\n"
        + "\n".join(f"- {item}" for item in findings)
    )
