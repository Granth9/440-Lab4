"""Specialized research/architecture sub-agent (rule-based demo)."""
from typing import Dict

def research(context: Dict[str, str]) -> str:
    """Summarize the Strategy 4 design based only on filtered research context."""
    project = context.get("project_context.md", "")
    research_notes = context.get("research_context.md", "")
    findings = [
        "Strategy 4 is demonstrated as an orchestrator delegating to specialized agents.",
        "A context filter should restrict each agent to task-relevant information.",
        "The code-review agent should receive implementation details; the researcher should receive architecture and assignment notes.",
        "The orchestrator should combine concise reports rather than forwarding every agent's full context.",
    ]
    if not project or not research_notes:
        findings.append("Some expected research context was missing.")
    return (
        "RESEARCH REPORT\n"
        f"Context received: {', '.join(sorted(context.keys()))}\n"
        + "\n".join(f"- {item}" for item in findings)
    )
