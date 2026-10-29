"""Specialized source-review sub-agent (deterministic Python demonstration)."""
from typing import Dict, List


def review(context: Dict[str, str], source_files: Dict[str, str]) -> str:
    """Summarize the supplied source files using simple evidence-based checks."""
    findings: List[str] = []
    if not source_files:
        findings.append("No recognized AIMA vacuum/MDP source files were found.")
    for filename, code in sorted(source_files.items()):
        if filename == "vacuum_agent.py":
            findings.append(
                "vacuum_agent.py contains a two-location GUI environment; its actions include "
                "Left, Right, and Suck, with performance changes for movement and cleaning."
            )
        elif filename == "xy_vacuum_environment.py":
            findings.append(
                "xy_vacuum_environment.py defines a two-dimensional GUI vacuum environment "
                "with Forward, TurnLeft, TurnRight, and Suck actions."
            )
        elif filename == "grid_mdp.py":
            findings.append(
                "grid_mdp.py is a GUI for configuring and displaying grid-based MDP values "
                "and policies; it is a visualization/demo layer."
            )
        elif filename == "mdp.py":
            findings.append(
                "mdp.py defines reusable MDP/GridMDP logic and value/policy iteration; "
                "the file is not a dedicated q_learning.py implementation."
            )
        else:
            findings.append(f"{filename}: {len(code.splitlines())} lines supplied for review.")

    return (
        "CODE REVIEW REPORT\n"
        f"Context received: {', '.join(sorted(context))}\n"
        f"Source files reviewed: {', '.join(sorted(source_files)) or 'none'}\n"
        + "\n".join(f"- {item}" for item in findings)
        + "\n- These are file-level observations from deterministic checks, not a complete correctness proof."
    )
