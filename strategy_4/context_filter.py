"""Allowlist-based context filtering for isolated sub-agents."""
from pathlib import Path
from typing import Dict, Iterable, Optional

CONTEXT_DIR = Path(__file__).parent / "context"

AGENT_ALLOWED_CONTEXT = {
    "code_reviewer": ("project_context.md", "code_review_context.md"),
    "researcher": ("project_context.md", "research_context.md"),
}

def load_context(agent_name: str, extra_context: Optional[Dict[str, str]] = None) -> Dict[str, str]:
    """Load only context files explicitly allowed for the named agent."""
    if agent_name not in AGENT_ALLOWED_CONTEXT:
        raise ValueError(f"Unknown agent: {agent_name}")

    selected = {}
    for filename in AGENT_ALLOWED_CONTEXT[agent_name]:
        path = CONTEXT_DIR / filename
        selected[filename] = path.read_text(encoding="utf-8")

    # Extra input is deliberately passed by the orchestrator, not auto-shared.
    if extra_context:
        selected.update(extra_context)
    return selected

def context_summary(context: Dict[str, str]) -> str:
    """Short diagnostic useful for demonstrating what an agent received."""
    return ", ".join(sorted(context.keys()))
