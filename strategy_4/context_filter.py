"""Allowlist-based context filtering for isolated sub-agents."""
from pathlib import Path
from typing import Dict, Optional

CONTEXT_DIR = Path(__file__).resolve().parent / "context"

AGENT_ALLOWED_CONTEXT = {
    "code_reviewer": ("project_context.md", "code_review_context.md"),
    "researcher": ("project_context.md", "research_context.md"),
}


def load_context(agent_name: str, extra_context: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    """Load only the context files allowlisted for the requested agent."""
    if agent_name not in AGENT_ALLOWED_CONTEXT:
        raise ValueError(f"Unknown agent: {agent_name}")

    selected = {}
    for filename in AGENT_ALLOWED_CONTEXT[agent_name]:
        selected[filename] = (CONTEXT_DIR / filename).read_text(encoding="utf-8")

    # Explicitly supplied task input is added by the orchestrator.
    if extra_context:
        selected.update(extra_context)
    return selected


def context_summary(context: Dict[str, str]) -> str:
    """Return a concise list of context filenames for the demo output."""
    return ", ".join(sorted(context))
